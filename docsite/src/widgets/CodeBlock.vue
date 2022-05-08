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
      <div v-for="log in pyLog.log" v-if="pyLog.install == 3" v-html="log"></div>
    </div>
    <div class="pt-5 pl-8" v-html="outputHtml"></div>
  </div>
</template>

<script lang="js">
import { defineComponent, ref, toRefs } from "vue";
import hljs from 'highlight.js/lib/core';
import CodeEditor from 'simple-code-editor';
import { runCode } from "@/state";
import { resetLog, pyLog } from "@/pylog";
import { pyState } from "@/state";

export default defineComponent({
  components: {
    CodeEditor,
  },
  props: {
    code: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const { code } = toRefs(props);
    const parsedCode = ref(code.value);
    const lang = [['python', 'Python']]
    const outputHtml = ref("");

    async function runTheCode() {
      resetLog();
      pyState.isExecuting = true;
      await new Promise(resolve => setTimeout(resolve, 1));
      console.log("Run", parsedCode.value)
      const res = await runCode(parsedCode.value);
      if (res) {
        console.log("RES", res)
        outputHtml.value = res;
      }
      pyState.isExecuting = false;
    }

    return {
      pyLog,
      lang,
      parsedCode,
      outputHtml,
      runTheCode,
      pyState,
    };
  },
});
</script>

<style lang="sass" scoped>
.code-block
  min-width: 48rem
</style>