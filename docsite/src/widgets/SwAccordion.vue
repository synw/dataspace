<template>
  <div>
    <div v-for="k in Object.keys(state)">
      <button class="btn" @click="swap(k)">
        <i-bi:caret-up v-if="state[k] === false" class="txt-lighter"></i-bi:caret-up>
        <i-bi:caret-down v-else-if="state[k] === true" class="txt-lighter"></i-bi:caret-down>
        {{ k }}
      </button>
      <div :class="{
        'slideup': state[k] === true,
        'slidedown': state[k] === false
      }" class=" slide-y">

        <div class="flex flex-col pb-3 pl-5 space-y-1" v-if="!hasTitles">
          <div v-for="val in props.data[k]" class="p-1 cursor-pointer" @click="emit('onclick', val)">
            {{ val }}
          </div>
        </div>
        <div class="flex flex-col pb-3 pl-5 space-y-1" v-else>
          <div v-for="entry in props.data[k]" class="p-1 cursor-pointer" @click="emit('onclick', entry.value)">
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

const state = reactive(assign({}, props.data))

function swap(key: string) {
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