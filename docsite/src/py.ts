import { PyodideInterface } from "./global";
import { mainLog, errLog, installLog, resetLog } from "./pylog";

async function _loadInterpreter(): Promise<PyodideInterface> {
  console.log('creating pyodide runtime');
  // @ts-ignore
  const pyodide = await loadPyodide({
    stdout: mainLog,
    stderr: errLog,
  });
  console.log('loading micropip');
  await pyodide.loadPackage('micropip');
  console.log('done setting up environment');
  return pyodide;
};

async function initPyRuntime(): Promise<PyodideInterface> {
  installLog(0);
  const pyodide = await _loadInterpreter();
  installLog(1);
  console.log("Loading libraries")
  await pyodide.runPythonAsync(`
  import micropip
  await micropip.install('http://localhost:3000/dataspace-0.0.5-py3-none-any.whl')
  
  print("Python interpreter loaded, loading libraries")
`);
  installLog(2);
  await pyodide.runPythonAsync(`import builtins
import pandas as pd
import dataspace
from pyodide import to_js
print("Libraries loaded, the Python interpreter is ready")
def print(*args, **kwargs):
  builtins.print('#!S#')
  builtins.print(*args, **kwargs)
  builtins.print('#!E#')
  `);
  console.log("Libraries loaded")
  resetLog();
  installLog(3);
  return pyodide
}

export { initPyRuntime }