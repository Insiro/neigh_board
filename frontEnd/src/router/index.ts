import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Main from "../pages/Main.vue";
import Auth from "@/pages/auth/Auth.vue";
import Register from "@/pages/auth/Register.vue";
import Board from "@/pages/Board.vue";
import NewPost from "@/pages/NewPost.vue";
import Post from "@/pages/Post.vue";

const authRoutes: Array<RouteRecordRaw> = [
  { path: "/", component: Main },
  {
    path: "/auth",
    component: Auth,
    meta: { noLayout: true },
  },
  {
    path: "/regist",
    component: Register,
    meta: { noLayout: true },
  },
  {
    path: "/post",
    component: Board,
  },
  {
    path: "/newPost",
    component: NewPost,
  },
  {
    path: "/post/:id",
    component: Post,
  },
];

const routes: Array<RouteRecordRaw> = [...authRoutes];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
