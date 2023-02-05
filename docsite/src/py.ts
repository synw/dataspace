import { usePython } from "usepython";

const py = usePython();

let baseUri = window.location.protocol + "//" + window.location.host
if (import.meta.env.MODE == "production") {
  baseUri = baseUri + import.meta.env.BASE_URL
} else {
  baseUri = baseUri + "/"
}
const initCode = `from io import BytesIO
import pandas as pd
import numpy as np
import altair as alt
import dataspace
from pyodide.http import pyfetch
from vega_datasets import data as _vdata
async def load_dataset(_dsname):
  url = ""
  if _dsname == "timeserie":
    url = "${baseUri}small_timeserie.csv"
  elif _dsname == "bitcoin":
    url = "${baseUri}BTC-USDT-1min.csv"
  elif _dsname == "sp500":
    url = f"https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/{_dsname}.csv"
  else:
    source = _vdata(_dsname)
    ds = dataspace.from_df(source)
    return ds
  ds = dataspace.from_df(pd.DataFrame({"A": [1]}))
  # print("Fetching", url)
  response = await pyfetch(url)
  if response.status == 200:
      with open("<output_file>", "wb") as f:
          df = pd.read_csv(BytesIO(await response.bytes()))
          ds = dataspace.from_df(df)        
  else:
      print("Wrong status code", response.status)
  return ds
`;

const transformCode = `
result_type = str(type(result)).replace("<class '", "").replace("'>", "")
# print("T", result_type)
if (result_type in ['dataspace.charts.altair.charts.AltairChart', 'altair.vegalite.v4.api.Chart', 'altair.vegalite.v4.api.LayerChart']):
  return result.to_json()
`

async function initPy() {
  // const wheel = "/dataspace-0.0.8-py3-none-any.whl";
  await py.load(['pandas', 'numpy', 'bokeh'], ['altair', "dataspace", 'vega_datasets'], initCode, transformCode)
}

export { py, initPy }