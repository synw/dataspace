<template>
  <div class="container">
    <div class="text-xl">Dataspace interactive documentation</div>
    <div class="mt-3">The documentation contains executable python examples. The
      pandas and numpy libraries are imported by default in the examples in addition
      to the dataspace library. Some convenience methods are available in the examples
      like <code>load_dataset</code>.
    </div>
    <div class="flex flex-wrap mt-5">
      <div class="m-3 border shadow rounded-xl dark:rounded-none" v-for="section in Object.keys(docmap)">
        <div class="p-3 text-xl secondary dark:primary">{{ section }}</div>
        <div class="pb-8 pr-8">
          <div v-for="part in Object.keys(docmap[section])" class="mt-1 ml-3 ">
            <div class="text-lg txt-primary dark:txt-light">{{ part }}</div>
            <div class="ml-3 cursor-pointer" v-for="entry in docmap[section][part]" @click="open(entry)">
              {{ entry.title }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import docmap from "@/docmap.json";
import router from "@/router";

function open(entry) {
  let url = "/method"
  if (entry?.source) {
    url = "/" + entry.source + url
  }
  router.push(url + '/' + entry.value)
}
</script>