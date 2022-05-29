<template>
  <div class="w-full p-3">
    <py-code-block id="simple_scatter1" :code="code" :theme="user.isDarkMode.value == true ? 'dark' : 'light'"
      :dispatch="dispatch" width="52rem" @run="onRun()">
    </py-code-block>
    <vega-chart id="chart1" v-if="hasChart == true" :spec="chartSpec"></vega-chart>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import VegaChart from "@/widgets/VegaChart.vue";
import { user } from '@/state';
import PyCodeBlock from '@/packages/vuepy/components/PyCodeBlock.vue';

defineProps({
  "id": {
    type: String,
    required: true
  },
  "code": {
    type: String,
    default: ""
  },
});

const chartSpec = ref({});
const hasChart = ref(false);

function onRun() {
  hasChart.value = false;
  chartSpec.value = {};
}

async function dispatch(res: any): Promise<any> {
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
</script>

