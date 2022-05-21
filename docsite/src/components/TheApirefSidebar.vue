<template>
  <div>
    <div class="p-3 text-xl">Api ref</div>
    <div v-for="line in content.lines" class="flex flex-col pb-3 pl-5 space-y-1 cursor-pointer"
      @click="$router.push('/method/' + line)">
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



