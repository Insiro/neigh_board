import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Main from "../pages/Main.vue";
// import Admin from "../views/Admin.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: Main,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
