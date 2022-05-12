import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Main from "../pages/Main.vue";
import Auth from "@/pages/auth/Auth.vue";
import Register from "@/pages/auth/Register.vue";
// import Admin from "../views/Admin.vue";

const authRoutes: Array<RouteRecordRaw> = [
  {
    path: "/auth",
    component: Auth,
    meta: {
      noLayout: true,
    },
  },
  {
    path: "/regist",
    component: Register,
    meta: {
      noLayout: true,
    },
  },
];

const routes: Array<RouteRecordRaw> = [
  { path: "/", component: Main, meta: { noLayout: false } },
  ...authRoutes,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
