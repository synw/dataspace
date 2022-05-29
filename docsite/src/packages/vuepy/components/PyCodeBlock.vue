<template>
  <div>
    <code-editor v-model="parsedCode" :languages="lang" :display_language="false" :hide_header="true"
      @keyup.ctrl.enter="runTheCode()" :theme="theme" :width="width" spellcheck="false">
    </code-editor>
    <button class="mt-3 border btn" :class="canRun ? 'cursor-pointer' : 'cursor-wait'" @click="runTheCode()"
      :disabled="canRun == false">
      <i-cil:media-play class="mr-2 " :class="!canRun ? 'txt-light' : 'txt-success'"></i-cil:media-play>
      Execute
    </button>
    <div class="pt-3 pl-8" v-if="pyStdout[id]">
      <div class="pt-3 pl-8" v-if="pyStdout[id].length > 0">
        <pre v-for="log in pyStdout[id]" v-html="log"></pre>
      </div>
    </div>
    <div class="pt-3 pl-8" v-if="pyException[id]">
      <div v-html="pyException[id]" v-if="pyException[id].length > 0"></div>
    </div>
    <div class="pt-3 pl-8" v-html="outputHtml"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, unref, toRefs, watchEffect, toRaw, computed } from "vue";
import hljs from "highlight.js";
import CodeEditor from 'simple-code-editor';
import { runPython } from "../py";
import { isPyLoaded, pyStdout, pyException, isPyExecuting } from "../logs";

export default defineComponent({
  components: {
    CodeEditor,
  },
  props: {
    id: {
      type: String,
      required: true
    },
    code: {
      type: String,
      default: ""
    },
    dispatch: {
      type: Function
    },
    theme: {
      type: String,
      default: "light"
    },
    width: {
      type: String,
      default: "540px",
    },
  },
  emits: ["run"],
  setup(props, { emit }) {
    const { id, code, dispatch } = toRefs(props);
    const parsedCode = ref(code.value);
    const lang = [['python', 'Python']];
    const outputHtml = ref("");

    const canRun = computed<Boolean>(() => {
      return isPyLoaded.value == true && isPyExecuting.value == false
    });

    async function runTheCode() {
      outputHtml.value = "";
      if (!canRun) {
        return
      }
      emit("run");
      //await new Promise(resolve => setTimeout(resolve, 1));
      console.log("Run", typeof (parsedCode.value), unref(parsedCode.value))
      const { results, error } = await runPython(id.value, parsedCode.value);
      console.log("PYRES", results)
      console.log("PYERR", error)
      if (results) {
        console.log("RES TYPE", typeof results);
        if (dispatch.value) {
          const res = await dispatch.value(results);
          if (res != null) {
            outputHtml.value = res
          }
        } else {
          outputHtml.value = results
        }
      }
    }

    watchEffect(() => {
      parsedCode.value = code.value;
      outputHtml.value = ""
    })

    return {
      toRaw,
      lang,
      parsedCode,
      outputHtml,
      runTheCode,
      isPyExecuting,
      isPyLoaded,
      pyStdout,
      pyException,
      canRun,
    };
  },
});
</script>