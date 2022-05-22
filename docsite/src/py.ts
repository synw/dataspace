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
  await micropip.install('dataspace')
  
  print("Python interpreter loaded, loading libraries")
`);
  installLog(2);
  let baseUri = ""
  if (import.meta.env.MODE == "production") {
    baseUri = "/dataspace"
  }
  await pyodide.runPythonAsync(`from io import BytesIO
import pandas as pd
import numpy as np
import dataspace
from pyodide import to_js
from pyodide.http import pyfetch
print("Libraries loaded, the Python interpreter is ready")
async def load_dataset(name):
  url = ""
  if name == "timeserie":
    url = "${baseUri}/small_timeserie.csv"
  elif name == "bitcoin":
    url = "${baseUri}/BTC-USDT-1min.csv"
  else:
    url = f"https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/{name}.csv"
    #raise AttributeError()
  ds = dataspace.from_df(pd.DataFrame({"A": [1]}))
  response = await pyfetch(url)
  if response.status == 200:
      with open("<output_file>", "wb") as f:
          df = pd.read_csv(BytesIO(await response.bytes()))
          ds = dataspace.from_df(df)        
  else:
      print("Wrong status code", response.status)
  return ds
  `);
  console.log("Libraries loaded")
  resetLog();
  installLog(3);
  return pyodide
}

export { initPyRuntime }