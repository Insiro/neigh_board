<template>
  <div class="col-xl-6 col-lg-6 registerContainer">
    <div class="p-5">
      <div class="text-center">
        <h1 class="h4 text-gray-900 mb-4">Register</h1>
      </div>
      <form class="user">
        <UserInput
          class="form-group"
          type="text"
          placeholder="Enter ID..."
          :value="id_str"
          @updates="idChanged"
        />
        <UserInput
          class="form-group"
          type="password"
          placeholder="password"
          :value="pass_str"
          @updates="pass_strChanged"
        />
        <UserInput
          class="form-group"
          type="password"
          placeholder="check password"
          :value="pass_strChk"
          @updates="pass_strChkChanged"
        />
        <UserInput
          class="form-group"
          type="tell"
          placeholder="phone Number"
          :value="call"
          @updates="callChanged"
        />
        <UserInput
          class="form-group"
          type="text"
          placeholder="Region"
          :value="region"
          @updates="regionChanged"
        />
        <hr />
        <button class="btn btn-primary btn-user btn-block" @click="regist()">
          Regist
        </button>
      </form>
    </div>
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import UserInput from "@/components/input/UserInput.vue";
@Options({ components: { UserInput } })
export default class Component extends Vue {
  id_str = "";
  pass_str = "";
  pass_strChk = "";
  call = "";
  region = "";
  regist() {
    //TODO: send Request for regist
  }
  idChanged(data: string) {
    this.id_str = data;
  }
  pass_strChanged(data: string) {
    this.pass_str = data;
  }
  pass_strChkChanged(data: string) {
    this.pass_strChk = data;
  }
  callChanged(data: string) {
    this.call = data;
  }
  regionChanged(data: string) {
    this.region = data;
  }
}
</script>
<style scoped>
.registerContainer {
  margin-top: 2rem;
  border-radius: 10px;
  background-color: whitesmoke;
}
</style>
