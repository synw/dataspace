<template>
  <div class="flex flex-row items-center pl-5">
    <div class="flex-grow text-xl cursor-pointer text-foreground-dark" @click="$router.push('/')">Dataspace
      documentation</div>
    <div class="mr-5 cursor-pointer" @click="emit('navigate', 'doc')">Doc</div>
    <div class="mr-8 cursor-pointer" @click="emit('navigate', 'apiref')">Api ref</div>
    <!-- div class="mr-8 cursor-pointer" @click="emit('navigate', 'examples')">Examples</div -->
    <div class="pr-5 text-lg cursor-pointer txt-light dark:txt-light" @click="user.toggleDarkMode()">
      <i-fa-solid:moon v-if="!user.isDarkMode.value"></i-fa-solid:moon>
      <i-fa-solid:sun v-else></i-fa-solid:sun>
    </div>
    <div v-if="pyLog.install < 2">
      <span v-if="pyLog.install == 0">Loading Python interpreter</span>
      <span v-else>Loading Python packages</span>
      <i-file-icons:config-python class="ml-2 mr-5 text-2xl"></i-file-icons:config-python>
    </div>
    <div v-else-if="pyLog.install == 2">
      <span>Installing Python libraries</span>
      <i-file-icons:test-python class="ml-2 mr-5 text-2xl"></i-file-icons:test-python>
    </div>
    <div v-else>
      <i-mdi:language-python class="mr-5 text-2xl" :class="pyState.isExecuting == false ? '' : 'txt-danger'">
      </i-mdi:language-python>
      <!-- i-vscode-icons:file-type-python v-else class="mr-5 text-2xl "></i-vscode-icons:file-type-python -->
    </div>
  </div>
</template>

<script setup lang="ts">
import { pyLog } from '@/pylog';
import { pyState } from "@/state";
import { user } from '@/state';

const emit = defineEmits(['navigate'])
</script>