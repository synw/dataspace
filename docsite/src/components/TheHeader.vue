<template>
  <div class="flex flex-row items-center pl-5 txt-lighter">
    <div class="flex-grow text-xl text-foreground-dark">Dataspace documentation</div>
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
</script>