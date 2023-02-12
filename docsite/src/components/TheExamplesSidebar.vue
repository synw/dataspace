<template>
  <div>
    <div class="p-3 text-xl">Charts</div>
    <div class="pb-3 pl-5 cursor-pointer" @click="$router.push('/examples/charts/simple_scatter')">
      Scatter plot with tooltips
    </div>
    <div class="pb-3 pl-5 cursor-pointer" @click="$router.push('/examples/charts/stacked_area')">
      Simple stacked area chart
    </div>
    <div class="pb-3 pl-5 cursor-pointer" @click="$router.push('/examples/charts/multiline')">
      Multi series line chart
    </div>
    <!-- div class="pb-3 pl-5 cursor-pointer" @click="$router.push('/examples/charts/groupedbar')">
      Grouped bar chart
    </div -->
  </div>
</template>

<script setup lang="ts">
</script>



