<template>
  <div v-if="isNavReady">
    <default-sidebar v-if="sidebar == 'default'"></default-sidebar>
    <api-sidebar v-else-if="sidebar == 'api'"></api-sidebar>
  </div>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import { useRoute } from 'vue-router';
import { isNavReady } from "@/state";
import DefaultSidebar from "@/components/sidebars/DefaultSidebar.vue";
import ApiSidebar from './sidebars/ApiSidebar.vue';

const route = useRoute();
const sidebar = ref<"default" | "api">("default");

watchEffect(() => {
  if (route.path.startsWith('/api')) {
    sidebar.value = "api";
  } else {
    sidebar.value = "default";
  }
})
</script>