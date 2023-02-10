<template>
  <div>
    <sidebar-block name="Data IO">
      <sw-accordion :data="docmap['Data IO']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    </sidebar-block>
    <sidebar-block name="Info">
      <sw-accordion :data="docmap['Info']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    </sidebar-block>
    <sidebar-block name="Select">
      <sw-accordion :data="docmap['Select']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    </sidebar-block>
    <sidebar-block name="Clean">
      <sw-accordion :data="docmap['Clean']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    </sidebar-block>
    <sidebar-block name="Transform">
      <sw-accordion :data="docmap['Transform']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    </sidebar-block>
    <sidebar-block name="Charts">
      <sw-accordion :data="docmap['Charts']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    </sidebar-block>
    <sidebar-block name="Reporting">
      <sw-accordion :data="docmap['Reporting']" :has-titles="true" @onclick="$router.push($event)"></sw-accordion>
    </sidebar-block>
  </div>
</template>

<script setup lang="ts">
import SidebarBlock from "@/widgets/SidebarBlock.vue";
import SwAccordion from "@/widgets/SwAccordion.vue";
import docmap from "@/docmap.json";
</script>



