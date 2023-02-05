<template>
  <div class="flex flex-row items-center pl-5">
    <div class="flex-grow text-xl cursor-pointer text-foreground-dark" @click="$router.push('/')">Dataspace
      documentation</div>
    <div class="mr-8 cursor-pointer" @click="emit('navigate', 'doc')">Doc</div>
    <div class="mr-8 cursor-pointer" @click="emit('navigate', 'apiref')">Api ref</div>
    <div class="mr-12 cursor-pointer" @click="emit('navigate', 'examples')">Examples</div>
    <div class="mr-12 cursor-pointer" @click="openLink('https://github.com/synw/dataspace')">
      <i-fa-brands:github class="text-xl txt-lighter"></i-fa-brands:github>&nbsp;Source
    </div>
    <div class="pr-5 text-lg cursor-pointer txt-light dark:txt-light" @click="user.toggleDarkMode()">
      <i-fa-solid:moon v-if="!user.isDarkMode.value"></i-fa-solid:moon>
      <i-fa-solid:sun v-else></i-fa-solid:sun>
    </div>
    <py-status :py="py" class="mr-5"></py-status>
  </div>
</template>

<script setup lang="ts">
import { user } from '@/state';
import { PyStatus } from 'vuepython';
import { py } from "@/py";

function openLink(url: string) {
  window.location.href = url;
}

const emit = defineEmits(['navigate'])
</script>