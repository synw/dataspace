<template>
  <auto-nav-node :node="nav.findNode('api')" class="space-y-1 nav-panel" :on-open="$router.push"></auto-nav-node>
</template>

<script setup lang="ts">
import { nav } from "@/state";
import { AutoNavNode } from "@docdundee/vue";
</script>