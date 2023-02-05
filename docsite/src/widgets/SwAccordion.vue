<template>
  <div>
    <div v-for="k in Object.keys(state)">
      <button class="flex items-center btn" @click="swap(k)">
        <div class="text-neutral-300 dark:text-neutral-500">
          <i-ph:caret-right-bold v-if="state[k] === true"></i-ph:caret-right-bold>
          <i-ph:caret-down-bold v-else-if="state[k] === false"></i-ph:caret-down-bold>
        </div>
        <div class="ml-2">{{ k }}</div>
      </button>
      <div :class="{
        'slideup': state[k] === true,
        'slidedown': state[k] === false
      }" class=" slide-y">

        <div class="flex flex-col pb-3 pl-8 space-y-1" v-if="!hasTitles">
          <div v-for="val in props.data[k]" class="p-1 cursor-pointer" @click="open(val)">
            {{ val }}
          </div>
        </div>
        <div class="flex flex-col pb-3 pl-8 space-y-1" v-else>
          <div v-for="entry in props.data[k]" class="p-1 cursor-pointer" @click="open(entry)">
            {{ entry.title }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';

const props = defineProps({
  data: {
    type: Object as () => Record<string, Array<any>>,
    required: true
  },
  hasTitles: {
    type: Boolean,
    default: false,
  }
});

const emit = defineEmits(["onclick"])

function assign(object, source) {
  Object.keys(source).forEach(function (key) {
    object[key] = true;
  });
  return object
}

function open(entry) {
  let url = "/method/"
  if (entry?.source) {
    url = "/" + entry.source + url
  }
  emit("onclick", url + entry.value)
}

const state = reactive(assign({}, props.data))

function swap(key: string) {
  state[key] = !state[key];
  return
  for (const k of Object.keys(state)) {
    if (key != k) {
      state[k] = true
    } else {
      state[k] = !state[k]
    }
  }
}
</script>

<style scoped lang="sass">
.slidedown 
  max-height: 10000px
</style>