import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import './assets/index.css';
import './assets/solarized-light.css'
import "vuepython/style.css";
import "highlight.js/styles/stackoverflow-light.css"

createApp(App).use(router).mount('#app')
