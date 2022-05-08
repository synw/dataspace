<template>
  <div class="flex flex-col pt-3 pb-5 pl-5 pr-3 space-y-1">
    <div v-for="line in content.lines" class="cursor-pointer" @click="$router.push('/method/' + line)">
      {{ line }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { onBeforeMount, reactive } from "vue";
import docref from "@/autodoc/docref.json";

const content = reactive({ "lines": new Array<string>() });

function parseDocref() {
  let buf = new Array<string>();
  Object.keys(docref).sort().forEach((k) => {
    buf.push(k)
  });
  content.lines = buf
}

onBeforeMount(() => parseDocref())
</script>



