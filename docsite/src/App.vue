<template>
  <div :class="{ dark: user.isDarkMode.value == true }" class="w-screen h-screen">
    <the-header class="fixed w-full h-16 primary"></the-header>
    <the-sidebar id="sidebar" class="fixed w-64 pb-5 mt-16 overflow-y-auto secondary"></the-sidebar>
    <div id="main" class="fixed w-full p-3 pb-12 overflow-auto background top-16 left-64 bg-slate-400">
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup lang="ts">
import TheHeader from "@/components/TheHeader.vue";
import TheSidebar from "./components/TheSidebar.vue";
import { initState, user } from "@/state";
import { onMounted } from "vue";

onMounted(() => initState())
</script>

<style lang="sass">
#main, #sidebar
  height: calc(100% - 4rem)
#main
  width: calc(100% - 16rem)

</style>




