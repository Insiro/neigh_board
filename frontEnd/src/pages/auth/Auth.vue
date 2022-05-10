<template>
  <div class="col-xl-6 col-lg-6 signContainer">
    <div class="p-5">
      <div class="text-center">
        <h1 class="h4 text-gray-900 mb-4">Neigh Board</h1>
      </div>
      <form class="user">
        <UserInput
          class="form-group"
          type="email"
          placeholder="Enter Email Address..."
        />
        <UserInput class="form-group" type="password" placeholder="Password" />
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
        <button
          href="index.html"
          class="btn btn-primary btn-user btn-block"
          @click="singIn()"
        >
          Login
        </button>
      </form>
      <hr />
      <!-- <div class="text-center">
        <a class="small" href="forgot-password.html">Forgot Password?</a>
      </div> -->
      <div class="text-center">
        <router-link to="register">Create an Account!</router-link>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import UserInput from "@/components/input/UserInput.vue";
@Options({ components: { UserInput } })
export default class Component extends Vue {
  remember: boolean = false;
  singIn() {
    //TODO
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
