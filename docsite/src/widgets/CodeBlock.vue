<template>
  <div>
    <code-editor v-model="parsedCode" :languages="lang" :display_language="false" :hide_header="true"
      @keyup.ctrl.enter="runTheCode()" class="pr-20 code-block dark:bg-neutral-700 bg-amber-50 w-max"
      spellcheck="false">
    </code-editor>
    <button class="mt-3 border btn" @click="runTheCode()" :disabled="pyState.isExecuting == true || pyLog.install < 3">
      <i-cil:media-play class="mr-2 txt-success"></i-cil:media-play>Execute
    </button>
    <div class="pt-3 pl-8">
      <pre v-for="log in pyLog.log" v-if="pyLog.install == 3" v-html="log"></pre>
    </div>
    <div class="pt-5 pl-8" v-html="outputHtml"></div>
    <vega-chart id="chart" v-if="hasChart == true" :spec="chartSpec"></vega-chart>
  </div>
</template>

<script lang="js">
import { defineComponent, ref, toRefs, watchEffect } from "vue";
//import hljs from 'highlight.js/lib/core';
import hljs from "highlight.js";
import { runCode } from "@/state";
import { resetLog, pyLog } from "@/pylog";
import { pyState } from "@/state";
import CodeEditor from 'simple-code-editor';
import VegaChart from "@/widgets/VegaChart.vue";

export default defineComponent({
  components: {
    CodeEditor,
    VegaChart,
  },
  props: {
    code: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const { code } = toRefs(props);
    const parsedCode = ref("");
    const lang = [['python', 'Python']];
    const outputHtml = ref("");
    const chartSpec = ref({});
    const hasChart = ref(false);

    async function dispatchRenderer(res) {
      hasChart.value = false;
      await new Promise(resolve => setTimeout(resolve, 1));
      if (res.startsWith('{\n  "$schema"')) {
        console.log("CHART", res);
        chartSpec.value = JSON.parse(res);
        hasChart.value = true;
      } else {
        //console.log("No chart", res)
        outputHtml.value = res;
      }
    }

    async function runTheCode() {
      resetLog();
      pyState.isExecuting = true;
      await new Promise(resolve => setTimeout(resolve, 1));
      console.log("Run", parsedCode.value)
      const res = await runCode(parsedCode.value);
      if (res) {
        //console.log("RES", typeof res, res);
        await dispatchRenderer(res);
      }
      pyState.isExecuting = false;
    }

    watchEffect(() => {
      //console.log("Effect")
      parsedCode.value = code.value;
      hasChart.value = false;
      resetLog();
      outputHtml.value = ""
    })

    return {
      pyLog,
      lang,
      parsedCode,
      outputHtml,
      runTheCode,
      pyState,
      chartSpec,
      hasChart,
    };
  },
});
</script>

<style lang="sass">
.code-block
  min-width: 48rem
.dataframe
  @apply table-auto divide-y divide-gray-200 rounded-t w-max text-center
  & thead
    & th
      @apply lighter px-3
      min-width: 2em
      
.msg
  @apply mb-3
.code_area
  & > textarea
    min-width: 768px
    width: 1200px !important
</style>