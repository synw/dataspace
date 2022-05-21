import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router"
import HomeView from "./views/HomeView.vue"
import hljs from 'highlight.js/lib/core';
const baseTitle = "Dataspace doc"

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: HomeView,
    meta: {
      title: "Home"
    }
  },
  {
    path: "/settings",
    component: () => import("./views/SettingsView.vue"),
    meta: {
      title: "Settings"
    }
  },
  {
    path: "/method/:name",
    component: () => import("./views/MethodView.vue"),
    meta: {
      title: "Method"
    }
  },
  {
    path: "/chart/method/:name",
    component: () => import("./views/MethodView.vue"),
    meta: {
      title: "Chart method",
      source: "chart"
    }
  },
  {
    path: "/toplevel/method/:name",
    component: () => import("./views/MethodView.vue"),
    meta: {
      title: "Toplevel method",
      source: "toplevel"
    }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.afterEach((to, from) => { // eslint-disable-line
  document.title = `${baseTitle} - ${to.meta?.title}`
});

export default router
