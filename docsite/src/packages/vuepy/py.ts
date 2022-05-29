import { unref, Ref } from "@vue/reactivity";
import { pyInstallLog, pyStderr, pyStdout, pyException, isPyExecuting } from "./logs";
import worker from "./webworker?url";
const pyodideWorker = new Worker(worker);

let callback: (value: {
  results: any;
  error: any;
} | PromiseLike<{
  results: any;
  error: any;
}>) => void = (v) => null;
let _execId = "";

function dispatchEvent(id: string, data: Record<string, any>) {
  switch (data.type) {
    case "end":
      callback({ results: data.res, error: null })
      callback = (v) => null
      isPyExecuting.value = false;
      break;
    case "err":
      callback = (v) => null
      isPyExecuting.value = false;
      pyException[_execId] = data.msg;
      break;
    case "installlog":
      pyInstallLog.stage = data.msg.stage;
      pyInstallLog.msg = data.msg.msg;
      break;
    case "stderr":
      console.log("STDERR:", data.msg)
      pyStderr[_execId].push(data.msg)
      break;
    case "stdout":
      //console.log("STDOUT:", _execId, data.msg)
      pyStdout[_execId].push(data.msg)
      break;
    default:
      isPyExecuting.value = false;
      throw new Error(`Unknown event type ${data.type}`)
  }
}

function processTransformCode(code: string): string {
  if (code.startsWith('\n')) {
    code.replace('\n', '')
  }
  const li = code.split("\n");
  const buf = new Array<string>();
  li.forEach((el) => {
    buf.push('  ' + el)
  });
  return buf.join("\n")
}

pyodideWorker.onmessage = (event) => {
  const { id, ...data } = event.data;
  console.log("=> msg in:", id, ":", data);
  dispatchEvent(id ?? "", data)
};

async function loadPython(pyoPackages: Array<string> = [], packages: Array<string> = [], initCode = "", transformCode = ""): Promise<{ results: any, error: any }> {
  let res;
  try {
    res = await runPython("_pyinstaller", "", {
      pyoPackages: pyoPackages,
      packages: packages,
      initCode: initCode,
      transformCode: processTransformCode(transformCode)
    });
  } catch (e) {
    throw new Error(
      // @ts-ignore
      `Error in pyodideWorker at ${e.filename}, Line: ${e.lineno}, ${e.message}`
    );
  }
  return res
}

async function runPython(id: string, script: string | Ref<string>, context: Record<string, any> = {}): Promise<{ results: any, error: any }> {
  if (isPyExecuting.value == true) {
    throw new Error("Only one python script can run at the time")
  }
  isPyExecuting.value = true;
  _execId = id;
  // create logger
  pyStdout[id] = [];
  pyStderr[id] = [];
  pyException[id] = "";
  // exec
  return new Promise((onSuccess) => {
    callback = onSuccess;
    pyodideWorker.postMessage({
      ...context,
      python: unref(script),
      id: id,
    });
  });
}

export { runPython, loadPython };