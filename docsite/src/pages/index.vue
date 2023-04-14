<template>
  <div id="home">
    <div class="flex flex-wrap" v-if="isNavReady">
      <div v-for="node in nav.findNode('doc').children">
        <auto-nav-node :node="node" class="space-y-1" :on-open="$router.push" start-state="all"></auto-nav-node>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { nav, isNavReady } from "@/state";
import { libTitle } from "@/conf";
import { AutoNavNode } from "@docdundee/vue";
</script>

<style lang="sass">
#home
  & .autonav
    flex-direction: "row" !important
    & .navnode
      @apply inline-block
      & .navnode-0
        & .navnode-header
          @apply secondary
</style>