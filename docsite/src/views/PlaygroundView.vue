<template>
  <div class="container">
    <div class="text-xl">Playground</div>
    <div class="mt-5">
      <div v-for="child in children" :key="child.id">
        <component :is="child.component" :id="child.id"></component>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineAsyncComponent, markRaw, reactive } from 'vue';



const codeBlock = defineAsyncComponent(() => import("@/widgets/DsCodeBlock.vue"))
const children = reactive([
  { id: "1", component: markRaw(codeBlock) },
  { id: "2", component: markRaw(codeBlock) },
])


</script>