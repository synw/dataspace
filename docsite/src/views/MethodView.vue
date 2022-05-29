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
      <ds-code-block :id="method.name" :code="code">
      </ds-code-block>
    </div>
  </div>
</template>

<script setup lang="ts">
import router from '@/router';
import { onBeforeUnmount, ref, watchEffect } from 'vue';
import MethodDoc from '@/widgets/MethodDoc.vue';
import DsCodeBlock from '@/widgets/DsCodeBlock.vue';
import docref from "@/autodoc/docref.json";
import chartsref from "@/autodoc/chartsref.json";
import funcsref from "@/autodoc/funcsref.json";
import exampleref from "@/autodoc/exref.json";

const method = ref({ name: "", docstring: {} })
const code = ref("");
const chartSpec = ref({});
const hasChart = ref(false);

function load() {
  const _methodName = router.currentRoute.value.params?.name;
  hasChart.value = false;
  chartSpec.value = {};
  let methodName: string
  if (!_methodName) { return } else { methodName = _methodName.toString() }
  const source = router.currentRoute.value.meta?.source;
  let docstring: string;
  if (source == "chart") {
    docstring = chartsref[methodName]
  } else if (source == "toplevel") {
    docstring = funcsref[methodName]
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

const stop = watchEffect(() => load());

onBeforeUnmount(() => stop())
</script>
