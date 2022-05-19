<template>
  <div>
    <div class="p-3 text-xl">Data IO</div>
    <sw-accordion :data="docDataio" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Info</div>
    <sw-accordion :data="infoData" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Select</div>
    <sw-accordion :data="selectData" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Clean</div>
    <sw-accordion :data="cleanData" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Transform</div>
    <sw-accordion :data="transformData" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Charts</div>
    <sw-accordion :data="chartsData" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Api ref</div>
    <sw-accordion :data="apirefData" @onclick="$router.push($event)"></sw-accordion>

  </div>
</template>

<script setup lang="ts">
import { onBeforeMount, reactive } from "vue";
import SwAccordion from "@/widgets/SwAccordion.vue";
import docref from "@/autodoc/docref.json";

const content = reactive({ "lines": new Array<string>() });
const apirefData = { "DataSpace": content.lines }
const docDataio = {
  "Load": [
    { title: "From a dataframe", value: "from_df" },
    { title: "From a csv file", value: "from_csv" },
    { title: "From a django orm query", value: "from_django" },
  ],
  "Export": [
    { title: "To a csv file", value: "export_csv" }
  ]
}
const infoData = {
  "View data": [
    { title: "Show the dataframe", value: "show" },
    { title: "Show columns types", value: "cols_" },

  ],
  "Count data": [
    { title: "Count nulls", value: "count_null_" },
    { title: "Count empty", value: "count_empty_" },
    { title: "Count zero", value: "count_zero_" },
    { title: "Count unique", value: "count_unique_" },
    { title: "Weight unique values", value: "wunique_" }
  ]
}
const selectData = {
  "Select data": [
    { title: "Limit", value: "limit" },
    { title: "Unique", value: "unique_" },
  ]
}
const cleanData = {
  "Nulls": [
    { title: "Drop NaN", value: "drop_nan" },
    { title: "Fill NaN", value: "fill_nan" },
    { title: "Fill nulls", value: "fill_nulls" },
  ],
  "Dates": [
    { title: "To date", value: "to_date" },
    { title: "Format date", value: "fdate" },
    { title: "Timestamps", value: "timestamps" },
  ],
  "Convert types": [
    { title: "To integer", value: "to_int" },
    { title: "To float", value: "to_float" },
    { title: "To type", value: "to_type" },
  ],
  "Clean values": [
    { title: "Strip", value: "strip" },
    { title: "Strip column names", value: "strip_cols" },
    { title: "Round floats", value: "roundvals" },
    { title: "Replace values", value: "replace" },
  ],
  "Index": [
    { title: "Add an index from a column", value: "index" },
    { title: "Add a date index from a column", value: "dateindex" },
  ]
}
const transformData = {
  "Dataframe": [
    { title: "Split", value: "split_" },
    { title: "Indexcol", value: "indexcol" },
    { title: "Drop", value: "drop" },
    { title: "Add", value: "add" },
    { title: "Rename", value: "rename" },
    { title: "Keep", value: "keep" },
    { title: "Copycol", value: "copycol" },
  ],
  "Values": [
    { title: "Sort", value: "sort" },
    { title: "Exclude", value: "exclude" },
    { title: "Drop rows", value: "dropr" },
    { title: "Append rows", value: "append" },
    { title: "Reverse", value: "reverse" },
    { title: "Apply", value: "apply" },
  ],
  "Resample timeseries": [
    { title: "Rsum", value: "rsum" },
    { title: "Rmean", value: "rmean" },
  ]
}
const chartsData = {
  "Options": [
    { title: "Inititialize the x and y axis", value: "axis" },
    { title: "Select the chart engine", value: "bokeh" },
  ],
  "Draw chart": [
    { title: "Line", value: "line_" },
    { title: "Bar", value: "bar_" },
    { title: "Point", value: "point_" },
    { title: "Area", value: "area_" },
    { title: "HLine", value: "hline_" },
  ],
  "Inline api": [
    { title: "Width", value: "w", source: "chart" },
    { title: "Height", value: "h", source: "chart" },
    { title: "Width and height", value: "wh", source: "chart" },
    { title: "Mark width", value: "mw", source: "chart" },
    { title: "Point width", value: "pw", source: "chart" },
    { title: "Color", value: "color", source: "chart" },
    { title: "Opacity", value: "opacity", source: "chart" },
    { title: "Tooltips", value: "tooltip", source: "chart" },
    { title: "X axis label rotation", value: "rx", source: "chart" },
    { title: "Remove X axis labels", value: "nox", source: "chart" },
    { title: "Remove Y axis labels", value: "noy", source: "chart" },
    { title: "Title", value: "title", source: "chart" },
    { title: "Values colormap", value: "colormap", source: "chart" },
    { title: "Quantiles colormap", value: "qcolormap", source: "chart" },
  ]
}

function parseDocref() {
  let buf = new Array<string>();
  Object.keys(docref).sort().forEach((k) => {
    buf.push(k)
  });
  content.lines = buf
  apirefData["DataSpace"] = content.lines
}

onBeforeMount(() => parseDocref())
</script>



