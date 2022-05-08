<template>
  <div v-html="output">
  </div>
</template>

<script setup lang="ts">
import { pyodide, onPythonReady } from "@/state";
import { onMounted, ref } from "vue";

const lorem = `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor <br /><br /><br />incididunt ut labore et dolore magna aliqua. Eget nunc lobortis mattis aliquam. Nec ultrices dui sapien eget mi proin sed. Mauris nunc congue nisi vitae suscipit. Phasellus vestibulum lorem sed risus. Volutpat lacus laoreet non curabitur gravida arcu ac. Id aliquet risus feugiat in ante metus dictum at tempor. Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Odio aenean sed adipiscing diam donec adipiscing tristique. Id donec ultrices tincidunt arcu non. Praesent tristique magna sit amet purus gravida. Tortor dignissim convallis aenean et tortor at risus viverra adipiscing. Nec sagittis aliquam malesuada bibendum arcu vitae. Etiam sit amet nisl purus in mollis nunc sed. Cursus in hac habitasse platea dictumst quisque sagittis purus. Aliquet porttitor lacus luctus accumsan tortor posuere ac ut. Neque egestas congue quisque egestas diam in arcu. Maecenas pharetra convallis posuere morbi.
<br /><br /><br />
Felis donec et odio pellentesque. Elementum nibh tellus molestie nunc non blandit massa. Feugiat <br /><br /><br />vivamus at augue eget arcu dictum varius duis. Faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper. Id interdum velit laoreet id donec ultrices tincidunt arcu non. Malesuada fames ac turpis egestas sed. Commodo odio aenean sed adipiscing diam. Id nibh tortor id aliquet lectus proin nibh nisl. Fringilla urna porttitor rhoncus dolor purus non enim. Arcu felis bibendum ut tristique et. Ut etiam sit amet nisl purus in. Mauris rhoncus aenean vel elit. Leo urna molestie at elementum eu facilisis. Auctor augue mauris augue neque gravida in fermentum et.
<br /><br /><br />
Viverra ipsum nunc aliquet bibendum enim facilisis gravida. Nunc non blandit massa enim nec dui. <br /><br /><br />Ac orci phasellus egestas tellus. Magna fringilla urna porttitor rhoncus dolor. Non tellus orci ac auctor augue. Aliquet lectus proin nibh nisl condimentum id venenatis. Sed risus pretium quam vulputate dignissim suspendisse. Lobortis elementum nibh tellus molestie nunc non blandit. Consectetur libero id faucibus nisl tincidunt eget. Malesuada fames ac turpis egestas sed tempus urna. Nibh praesent tristique magna sit amet purus gravida quis blandit. A pellentesque sit amet porttitor eget dolor. Praesent elementum facilisis leo vel fringilla est. Neque convallis a cras semper auctor neque vitae. Cursus euismod quis viverra nibh cras pulvinar mattis.
<br /><br /><br />
Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Turpis in eu mi bibendum neque egestas congue. Enim facilisis gravida neque convallis a. Ac turpis egestas sed tempus urna et pharetra pharetra. Orci a scelerisque purus semper eget duis. Netus et malesuada fames ac turpis egestas. Cras ornare arcu dui vivamus. Sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec. Ut etiam sit amet nisl purus in mollis. Id diam maecenas ultricies mi eget mauris pharetra et.
<br /><br /><br />
Convallis aenean et tortor at risus viverra adipiscing at. Adipiscing enim eu turpis egestas <br /><br /><br />pretium aenean. Aenean et tortor at risus viverra adipiscing at. Varius vel pharetra vel turpis nunc eget lorem. Malesuada proin libero nunc consequat. Gravida rutrum quisque non tellus orci. Adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus urna neque. Mi proin sed libero enim. In hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit. Et malesuada fames ac turpis. Facilisis leo vel fringilla est ullamcorper. Pretium quam vulputate dignissim suspendisse in est ante in nibh. Interdum velit laoreet id donec ultrices tincidunt. Sapien pellentesque habitant morbi tristique. Convallis posuere morbi leo urna molestie at elementum eu facilisis. At tellus at urna condimentum mattis pellentesque. Lacinia at quis risus sed vulputate odio ut enim. Sagittis vitae et leo duis. Urna nunc id cursus metus aliquam. Adipiscing tristique risus nec feugiat.`
const output = ref(lorem);

async function runCode() {
  console.log("Waiting for python interpreter")
  await onPythonReady;
  console.log("Running script")
  let run = pyodide.runPython(`
      def create():
        data = {"col1": [1, 2, 3, 4, 5], "col2": [1, 6, 2, 4, 1]}
        df = pd.DataFrame(data)
        ds = dataspace.from_df(df)
        return to_js(ds.df.to_html(justify="center"))
      
      create
  `);
  let ds = run();
  console.log("DS", ds)
  output.value = ds
}

//onMounted(() => runCode())

</script>