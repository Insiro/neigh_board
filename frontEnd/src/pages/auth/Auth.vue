<template>
  <div class="col-xl-6 col-lg-6 signContainer">
    <div class="p-5">
      <div class="text-center">
        <h1 class="h4 text-gray-900 mb-4">Neigh Board</h1>
      </div>
      <form class="user" @submit.prevent="signIn">
        <UserInput
          class="form-group"
          type="text"
          placeholder="Enter ID..."
          :value="id"
          @updates="idChanged"
        />
        <UserInput
          class="form-group"
          type="password"
          placeholder="Password"
          :value="pwd"
          @updates="pwdChanged"
        />
        <!-- remember id-->
        <div class="form-group custom-control custom-checkbox small">
          <input
            v-model="remember"
            type="checkbox"
            class="custom-control-input"
          />
          <label
            class="custom-control-label"
            for="customCheck"
            @click="chkboxUpdate"
            >Remember Me</label
          >
        </div>
        <button class="btn btn-primary btn-user btn-block">Login</button>
      </form>
      <hr />
      <!-- <div class="text-center">
        <a class="small" href="forgot-password.html">Forgot Password?</a>
      </div> -->
      <div class="text-center">
        <router-link to="regist">Create an Account!</router-link>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import UserInput from "@/components/input/UserInput.vue";
import { useRouter } from "vue-router";
import authState from "@/store/auth/state";

@Options({ components: { UserInput } })
export default class Component extends Vue {
  private m_remember: boolean = (localStorage.getItem("remember") ??
    false) as boolean;
  router = useRouter();
  id = "";
  pwd = "";
  async signIn() {
    try {
      const result = await authState.signIn({
        id: this.id,
        password: this.pwd,
      });
      if (result) this.router.push("/");
      else alert("로그인에 실패하였습니다");
    } catch (error) {
      console.log(error);
    }
    //TODO:
  }

  idChanged(data: string) {
    this.id = data;
  }
  pwdChanged(data: string) {
    this.pwd = data;
  }
  get remember() {
    return this.m_remember;
  }
  set remember(value) {
    localStorage.setItem("remember", String(this.remember));
    this.m_remember = value;
  }
  chkboxUpdate() {
    let checked = !this.m_remember;
    localStorage.setItem("remember", String(checked));
    this.m_remember = checked;
  }
}
</script>
<style scoped>
.signContainer {
  margin-top: 2rem;
  border-radius: 10px;
  background-color: whitesmoke;
}
</style>
