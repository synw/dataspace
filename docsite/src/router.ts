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
    path: "/playground",
    component: () => import("./views/PlaygroundView.vue"),
    meta: {
      title: "Playground"
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
  },
  {
    path: "/examples/charts/simple_scatter",
    component: () => import("./views/examples/charts/SimpleScatter.vue"),
    meta: {
      title: "Scatter plot with tooltips"
    }
  },
  {
    path: "/examples/charts/stacked_area",
    component: () => import("./views/examples/charts/SimpleStackedArea.vue"),
    meta: {
      title: "Simple stacked area chart"
    }
  },
  {
    path: "/examples/charts/multiline",
    component: () => import("./views/examples/charts/MultilineChart.vue"),
    meta: {
      title: "Multi series line chart"
    }
  },
  {
    path: "/examples/charts/groupedbar",
    component: () => import("./views/examples/charts/GroupedBarChart.vue"),
    meta: {
      title: "Grouped bar chart"
    }
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.afterEach((to, from) => { // eslint-disable-line
  document.title = `${baseTitle} - ${to.meta?.title}`
});

export default router
