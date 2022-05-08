<template>
  <div class="text-xl">
    Method {{ method.name }}
  </div>
  <div class="mt-5">
    <method-doc :method="method"></method-doc>
  </div>
  <div class="p-5 pl-8 text-lg italic">Example</div>
  <div class="p-3">
    <code-block :code="code"></code-block>
  </div>
</template>

<script setup lang="ts">
import router from '@/router';
import { ref, watchEffect } from 'vue';
import MethodDoc from '@/widgets/MethodDoc.vue';
import CodeBlock from '@/widgets/CodeBlock.vue';
import docref from "@/autodoc/docref.json";
import exampleref from "@/autodoc/exref.json";

const method = ref({ name: "", docstring: {} })
const code = ref("");

function load() {
  const name = router.currentRoute.value.params?.name.toString();
  console.log("Load", name)
  const methodName = name;
  //console.log("M", methodName);
  code.value = exampleref[name] ?? "";
  console.log("Code", code.value)
  const m = {
    "name": methodName,
    "docstring": docref[methodName]
  }
  method.value = m;
}

watchEffect(() => load())
</script>