<template>
  <div class="text-xl">
    Method {{ method.name }}
  </div>
  <div class="mt-5">
    <method-doc :method="method"></method-doc>
  </div>
  <div v-if="code.length > 0">
    <div class="p-5 pl-8 text-lg italic">Example</div>
    <div class="w-full p-3">
      <code-block :code="code"></code-block>
    </div>
  </div>
</template>

<script setup lang="ts">
import router from '@/router';
import { ref, watchEffect } from 'vue';
import MethodDoc from '@/widgets/MethodDoc.vue';
import CodeBlock from '@/widgets/CodeBlock.vue';
import docref from "@/autodoc/docref.json";
import chartsref from "@/autodoc/chartsref.json";
import exampleref from "@/autodoc/exref.json";

const method = ref({ name: "", docstring: {} })
const code = ref("");

function load() {
  const methodName = router.currentRoute.value.params?.name.toString();
  const source = router.currentRoute.value.meta?.source;
  let docstring: string;
  if (source == "chart") {
    docstring = chartsref[methodName]
  } else {
    docstring = docref[methodName]
  }
  const m = {
    "name": methodName,
    "docstring": docstring
  }
  method.value = m;
  if (m.docstring["example"]) {
    code.value = m.docstring["example"]
  } else {
    code.value = exampleref[methodName] ?? "";
  }
}

watchEffect(() => load())
</script>