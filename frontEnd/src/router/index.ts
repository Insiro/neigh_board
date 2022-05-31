import {
  createRouter,
  createWebHistory,
  RouteLocationNormalized,
  RouteRecordRaw,
} from "vue-router";
import Main from "../pages/Main.vue";
import Auth from "@/pages/auth/Auth.vue";
import Register from "@/pages/auth/Register.vue";
import Board from "@/pages/Board.vue";
import NewPost from "@/pages/NewPost.vue";
import Post from "@/pages/Post.vue";
import User from "@/pages/User.vue";
import NotFound from "@/pages/NotFound.vue";
import authState from "@/store/auth/state";
import License from "@/pages/License.vue";
const authRoutes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: Main,
    meta: {
      auth_require: true,
    },
  },
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
    meta: {
      auth_require: true,
    },
  },
  {
    path: "/newPost",
    component: NewPost,
    meta: {
      auth_require: true,
    },
  },
  {
    path: "/post/:id",
    component: Post,
  },
  {
    path: "/user",
    component: User,
    meta: {
      auth_require: true,
    },
  },
  {
    path: "/license",
    component: License,
  },
  { path: "/404", component: NotFound },
];

const routes: Array<RouteRecordRaw> = [...authRoutes];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
router.beforeEach(
  async (
    to: RouteLocationNormalized,
    _from: RouteLocationNormalized,
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    next: any
  ) => {
    if (authState.isSigned === undefined) await authState.refreshSession();
    if (to.meta === undefined || to.meta === null || !to.meta.auth_require)
      next();
    else if (authState.isSigned) next();
    else {
      next("/auth");
    }
  }
);
export default router;
