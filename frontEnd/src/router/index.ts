import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Main from "../pages/Main.vue";
import Auth from "@/pages/auth/Auth.vue";
// import Admin from "../views/Admin.vue";

const routes: Array<RouteRecordRaw> = [
  { path: "/", component: Main },
  {
    path: "/auth",
    component: Auth,
    meta: {
      noLayout: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
