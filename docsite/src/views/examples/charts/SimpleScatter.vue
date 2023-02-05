<template>
  <div class="text-xl">
    Scatter plot with tooltip
  </div>
  <p class="mt-3">This example is from the <a href="https://altair-viz.github.io/gallery/scatter_tooltips.html">Simple
      scatter plot with tooltips</a> example from Altair's examples. First load the dataset</p>
  <div class="w-full p-3">
    <ds-code-block id="simple_scatter1" :code="code1">
    </ds-code-block>
    <p class="mt-5">Draw the chart:</p>
    <ds-code-block id="simple_scatter2" class="mt-3" :code="code2">
    </ds-code-block>
  </div>
</template>

<script setup lang="ts">
import DsCodeBlock from '@/widgets/DsCodeBlock.vue';

const code1 = `ds = await load_dataset('cars')
ds.show()`;

const code2 = `ds.point_('Horsepower:Q','Miles_per_Gallon:Q').pw(60).encode(
    color='Origin:N'
).tooltip(
    ['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()`;
</script>

