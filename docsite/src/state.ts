import { User } from "@snowind/state";
import { initPyRuntime } from "@/py"
import { PyodideInterface } from "./global";
import { reactive } from "vue";

const user = new User();
let pyodide: PyodideInterface;

let setPythonReady: (value: unknown) => void;
const onPythonReady = new Promise((resolve) => setPythonReady = resolve);
const pyState = reactive({
  isReady: false,
  isExecuting: false,
});

async function initState() {
  pyodide = await initPyRuntime();
  setPythonReady(true);
  pyState.isReady = true;
}

async function runCode(code: string): Promise<any> {
  console.log("Waiting for python interpreter")
  await onPythonReady;
  const _code = `
def runcode():
  ${code.replace('\n', '\n  ')}
runcode
    `
  console.log("Running script", _code)
  //let run = pyodide.runPython(_code);
  //let ds = run();
  let ds = pyodide.runPython(code)
  return ds
}

export { user, initState, onPythonReady, pyodide, runCode, pyState }