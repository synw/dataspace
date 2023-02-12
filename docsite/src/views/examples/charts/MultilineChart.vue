<template>
  <div class="text-xl">
    Multi series line chart
  </div>
  <p class="mt-3">This example is from the <a href="https://altair-viz.github.io/gallery/multi_series_line.html">Multi
      series line chart</a> example
    from Altair's examples.</p>
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

const code1 = `ds = await load_dataset('iowa_electricity')
ds.show()`;

const code2 = `ds.area_('year:T','net_generation:Q').encode(
    color='source:N'
)`;
</script>

