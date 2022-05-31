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
          <label class="custom-control-label" for="customCheck"
            >Remember Me</label
          >
        </div>
        <button class="btn btn-primary btn-user btn-block" @click="signIn">
          Login
        </button>
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
  remember: boolean = false;
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
}
</script>
<style scoped>
.signContainer {
  margin-top: 2rem;
  border-radius: 10px;
  background-color: whitesmoke;
}
</style>
