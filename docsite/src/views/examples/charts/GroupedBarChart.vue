<template>
  <div class="text-xl">
    Grouped bar chart
  </div>
  <p class="mt-3">This example is from the <a href="https://altair-viz.github.io/gallery/grouped_bar_chart.html">Grouped
      Bar Chart</a> example
    from Altair's examples.</p>
  <div class="w-full p-3">
    <ds-code-block id="chart1" :code="code1">
    </ds-code-block>
    <p class="mt-5">Draw the chart:</p>
    <ds-code-block id="chart2" class="mt-3" :code="code2">
    </ds-code-block>
  </div>
</template>

<script setup lang="ts">
import DsCodeBlock from '@/widgets/DsCodeBlock.vue';

const code1 = `ds = await load_dataset('barley')
ds.show()`;

const code2 = `ds.bar_('year:O','sum(yield):Q').encode(
    color='year:N',
    column='site:N'
)`;
</script>

