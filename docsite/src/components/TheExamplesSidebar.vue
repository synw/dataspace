<template>
  <div>
    <div class="p-3 text-xl">Examples</div>
    <div v-for="line in content.lines" class="">
      {{ line }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { onBeforeMount, reactive } from "vue";
import docref from "@/autodoc/docref.json";

const content = reactive({ "lines": new Array<string>() });

</script>



