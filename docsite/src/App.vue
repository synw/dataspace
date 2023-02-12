<template>
  <div :class="{ dark: user.isDarkMode.value == true }" class="w-screen h-screen">
    <the-header class="fixed w-full h-16 primary" @navigate="navigate($event)"></the-header>
    <the-sidebar v-if="sidebar == 'doc'" class="fixed w-64 pb-5 mt-16 overflow-y-auto sidebar secondary"></the-sidebar>
    <the-apiref-sidebar v-else-if="sidebar == 'apiref'" class="fixed w-64 pb-5 mt-16 overflow-y-auto sidebar secondary">
    </the-apiref-sidebar>
    <the-examples-sidebar v-else-if="sidebar == 'examples'"
      class="fixed w-64 pb-5 mt-16 overflow-y-auto sidebar secondary"></the-examples-sidebar>
    <div id="main" class="fixed w-full p-3 pb-12 overflow-auto background top-16 left-64 bg-slate-400">
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup lang="ts">
import TheHeader from "@/components/TheHeader.vue";
import TheSidebar from "./components/TheSidebar.vue";
import TheApirefSidebar from "./components/TheApirefSidebar.vue";
import TheExamplesSidebar from "./components/TheExamplesSidebar.vue";
import { user } from "@/state";
import { onBeforeMount, ref } from "vue";
import { initPy } from "./py";

const sidebar = ref<"doc" | "apiref" | "examples">("doc");

function navigate(section: "doc" | "apiref" | "examples") {
  //console.log("Nav", section)
  sidebar.value = section
}

onBeforeMount(() => initPy())
</script>

<style lang="sass">
a, a:visited
  @apply txt-primary
#main, .sidebar
  height: calc(100% - 4rem)
#main
  width: calc(100% - 16rem)
.dataframe
  @apply table-auto divide-y divide-gray-200 rounded-t w-max mt-3
  & thead
    & th
      @apply lighter px-3 text-center
      min-width: 2em
  & tbody
    & td
      @apply px-2 py-1
</style>




