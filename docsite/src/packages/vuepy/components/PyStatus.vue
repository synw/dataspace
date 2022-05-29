<template>
  <div v-if="pyInstallLog.stage == 0">
    <i-mdi:language-python class="ml-2 mr-5 text-2xl txt-neutral"></i-mdi:language-python>
  </div>
  <div v-else-if="[1, 2].includes(pyInstallLog.stage)">
    <span>{{ pyInstallLog.msg }}</span>
    <i-file-icons:config-python class="ml-2 mr-5 text-2xl"></i-file-icons:config-python>
  </div>
  <div v-else-if="[3, 4].includes(pyInstallLog.stage)">
    <span>{{ pyInstallLog.msg }}</span>
    <i-file-icons:test-python class="ml-2 mr-5 text-2xl"></i-file-icons:test-python>
  </div>
  <div v-else-if="pyInstallLog.stage == 5">
    <i-mdi:language-python class="mr-5 text-2xl" :class="isPyExecuting == false ? '' : 'txt-danger'">
    </i-mdi:language-python>
    <!-- i-vscode-icons:file-type-python class="mr-5 border"></i-vscode-icons:file-type-python -->
  </div>
</template>

<script setup lang="ts">
import { isPyExecuting, pyInstallLog } from '@/packages/vuepy/logs';
</script>