<template>
  <div>
    <div class="p-3 text-xl">Data IO</div>
    <sw-accordion :data="docmap['Data IO']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Info</div>
    <sw-accordion :data="docmap['Info']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Select</div>
    <sw-accordion :data="docmap['Select']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Clean</div>
    <sw-accordion :data="docmap['Clean']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Transform</div>
    <sw-accordion :data="docmap['Transform']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    <div class="p-3 text-xl">Charts</div>
    <sw-accordion :data="docmap['Charts']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
  </div>
</template>

<script setup lang="ts">
import SwAccordion from "@/widgets/SwAccordion.vue";
import docmap from "@/docmap.json";
</script>



