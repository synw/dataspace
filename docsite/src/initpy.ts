import { loadPython } from "@/packages/vuepy/py";

let baseUri = ""
if (import.meta.env.MODE == "production") {
  baseUri = "/dataspace"
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
    url = "${baseUri}/small_timeserie.csv"
  elif _dsname == "bitcoin":
    url = "${baseUri}/BTC-USDT-1min.csv"
  elif _dsname == "sp500":
    url = f"https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/{_dsname}.csv"
  else:
    source = _vdata(_dsname)
    ds = dataspace.from_df(source)
    return ds
  ds = dataspace.from_df(pd.DataFrame({"A": [1]}))
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
if (result_type in ['dataspace.charts.altair.Chart', 'altair.vegalite.v4.api.Chart', 'altair.vegalite.v4.api.LayerChart']):
  return result.to_json()
`

export default async function initPy() {
  await loadPython(['pandas', 'numpy', 'bokeh'], ['altair', 'dataspace', 'vega_datasets'], initCode, transformCode)
}