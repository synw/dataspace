<template>
  <div>
    <div class="m-1 text-xl border rounded-sm cursor-pointer bord-light lighter">
      <button class="flex items-center w-full pl-0 btn" @click="isOpened = !isOpened">
        <div class="text-neutral-300 dark:text-neutral-500">
          <i-ph:caret-right-bold v-if="isOpened === false"></i-ph:caret-right-bold>
          <i-ph:caret-down-bold v-else-if="isOpened === true"></i-ph:caret-down-bold>
        </div>
        <div class="ml-2">{{ name }}</div>
      </button>
    </div>
    <div :class="{
      'slideup': isOpened === false,
      'slidedown': isOpened === true
    }" class=" slide-y">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

defineProps({
  name: {
    type: String,
    required: true
  }
});

const isOpened = ref(true)
</script>