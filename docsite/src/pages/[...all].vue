<template>
  <dispatch-route :hljs="hljs" :nav="nav" :url="$route.path" :on-open="$router.push" :base-title="libTitle">
    <template #docstring="slotProps">
      <render-docstring lang="python" :hljs="hljs" v-if="slotProps.data.hasDocstring === true" class="w-full"
        :docstring="slotProps.data.docstring" :title="slotProps.data.name">
        <template v-if="slotProps.data.docstring.extra_md?.header">
          <render-md :hljs="hljs" :source="slotProps.data.docstring.extra_md.header"
            :class="slotProps.data.hasDocstring ? 'mb-3' : ''"></render-md>
        </template>
      </render-docstring>
    </template>
  </dispatch-route>
</template>

<script setup lang="ts">
import { DispatchRoute, RenderDocstring, RenderMd } from '@docdundee/vue';
import { nav } from '@/state';
import { hljs, libTitle } from "@/conf";
</script>