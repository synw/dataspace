import { reactive, ref } from "vue"

const pyLog = reactive({
  install: 0,
  log: new Array<string>(),
  err: new Array<string | Error>(),
});

let printBuffer = new Array<string>();
let bufferIsFilling = false;

function mainLog(msg: string): void {
  console.log("[PYLOGBUFFER]", msg);
  pyLog.log.push(msg);
  return
  console.log("[PYLOGBUFFER]", msg);
  if (msg == '#!S#') {
    bufferIsFilling = true
    return
  }
  else if (msg == '#!E#') {
    bufferIsFilling = false
  }
  if (bufferIsFilling) {
    printBuffer.push(msg)
  } else {
    console.log("END BUFFER", printBuffer)
    pyLog.log.push(printBuffer.join("\n"));
    printBuffer = new Array<string>();
  }
}

function errLog(msg: any): void {
  console.log("[PYERR]", msg)
  pyLog.err.push(msg)
}

function installLog(msg: number): void {
  console.log("[PYINSTALLLOG]", msg)
  pyLog.install = msg
}

function resetLog() {
  pyLog.log = [];
  pyLog.err = [];
}

export { pyLog, mainLog, errLog, installLog, resetLog }
