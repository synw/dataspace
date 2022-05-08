<template>
  <div :id="id"></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Config, TopLevelSpec, compile } from "vega-lite";
import embed from "vega-embed";

export default defineComponent({
  props: {
    id: {
      type: String,
      required: true,
    },
    spec: {
      type: Object,
      required: true,
    },
    config: {
      type: Object,
      default: () => { }, // eslint-disable-line
    },
  },
  methods: {
    async draw() {
      const config: Config = this.config;
      const spec = this.spec as TopLevelSpec;
      //spec.$schema = "https://vega.github.io/schema/vega-lite/v5.json";
      const vegaSpec = compile(spec, { config }).spec;
      await embed(`#${this.id}`, vegaSpec, { actions: false });
      console.log("Chart ok")
      var objDiv = document.getElementById("main");
      if (!objDiv) {
        throw new Error("No #main")
      }
      objDiv.scrollTop = objDiv.scrollHeight;
    },
  },
  mounted() {
    this.draw();

  },
});
</script>

<style>
canvas.marks {
  max-width: 100% !important;
  height: auto !important;
}
</style>