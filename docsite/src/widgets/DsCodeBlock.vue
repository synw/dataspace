<template>
  <div class="w-full p-3">
    <py-code-block :controls="true" :id="id" :py="py" :code="code"
      :theme="user.isDarkMode.value == true ? 'dark' : 'light'" :dispatch="dispatch" width="52rem" @run="onRun()">
    </py-code-block>
    <vega-chart :id="id" v-if="hasChart" :spec="chartSpec"></vega-chart>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue';
import VegaChart from "@/widgets/VegaChart.vue";
import { user } from '@/state';
import { PyCodeBlock } from 'vuepython';
import { onBeforeRouteUpdate } from 'vue-router';
import { py } from "@/py";

defineProps({
  id: {
    type: String,
    required: true
  },
  code: {
    type: String,
    required: true,
  },
});

const chartSpec = ref({});
const hasChart = ref(false);

function onRun() {
  hasChart.value = false;
  chartSpec.value = {};
}

async function dispatch(res: any): Promise<any> {
  //console.log("Dispatch", res)
  onRun();
  await nextTick();
  let endres = res;
  if (typeof res == 'string') {
    if (res.startsWith('{\n  "$schema"')) {
      chartSpec.value = JSON.parse(res);
      hasChart.value = true;
      endres = null;
    } else {
      endres = res;
    }
  }
  return endres
}

onBeforeRouteUpdate(() => onRun())
</script>

