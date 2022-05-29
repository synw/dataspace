import { computed, reactive, ref } from "@vue/reactivity";

const pyInstallLog = reactive({
  stage: 0,
  msg: ""
});

const pyStdout = reactive<Record<string, any>>({});
const pyStderr = reactive<Record<string, any>>({});
const pyException = reactive<Record<string, any>>({});

const isPyLoaded = computed(() => pyInstallLog.stage == 5);
const isPyExecuting = ref(false);

export { pyInstallLog, isPyLoaded, pyStdout, pyStderr, pyException, isPyExecuting }