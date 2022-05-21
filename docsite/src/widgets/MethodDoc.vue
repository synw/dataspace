<template>
  <div class="p-3">
    <pre
      class="px-5 py-2 code-block dark:bg-neutral-700 bg-amber-50 w-max"><code v-html="parsedCode" style="white-space: pre"></code></pre>
    <div class="pl-5 mt-5">
      <div v-html="method.docstring.description"> </div>
      <div class="mt-3" v-if="method.docstring.long_description" v-html="method.docstring.long_description"> </div>
      <div class="mt-5" v-if="Object.keys(method.docstring.params).length > 0">
        <div class="text-lg italic">Parameters</div>
        <ul class="pl-5 mt-3 space-y-2">
          <li v-for="param in Object.keys(method.docstring.params)">
            <span class="font-bold" v-html="param"></span>: <span class="hljs-built_in"
              v-html="method.docstring.params[param].type"></span>:
            <span v-html="method.docstring.params[param].description"></span>
          </li>
        </ul>
      </div>
      <div class="mt-5" v-if="method.docstring.return.type != null">
        <div class="text-lg italic">Return</div>
        <div class="mt-3">
          <span class="hljs-built_in" v-html="method.docstring.return.type"></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import hljs from 'highlight.js/lib/core';
import python from 'highlight.js/lib/languages/python';
import { ref, watchEffect } from 'vue';

const props = defineProps({
  method: {
    type: Object,
    required: true
  }
});

hljs.registerLanguage('python', python);
const parsedCode = ref("");

function load() {
  parsedCode.value = hljs.highlight(props.method.docstring["funcdef"], { language: "python" }).value;
  //console.log(JSON.stringify(props.method.docstring, null, "  "))
}

watchEffect(() => load())
</script>