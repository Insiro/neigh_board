<template>
  <div class="col-xl-6 col-lg-6 registerContainer">
    <div class="p-5">
      <div class="text-center">
        <h1 class="h4 text-gray-900 mb-4">Register</h1>
      </div>
      <form class="user" @submit.prevent="regist">
        <UserInput
          class="form-group"
          type="text"
          placeholder="Enter name..."
          :value="name"
          @updates="nameChanged"
        />
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
        <div id="correctPwd">
          <span v-if="pass_strChk != '' && pass_str !== pass_strChk">
            비밀번호가 일치하지 않습니다
          </span>
        </div>
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
        <button class="btn btn-primary btn-user btn-block" @click="">
          Regist
        </button>
      </form>
    </div>
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import UserInput from "@/components/input/UserInput.vue";
import axios, { AxiosError } from "axios";
import { useRouter } from "vue-router";
import { apiUrl } from "@/utils";
import authState from "@/store/auth/state";

@Options({ components: { UserInput } })
export default class Component extends Vue {
  id_str = "";
  pass_str = "";
  pass_strChk = "";
  name = "";
  call = "";
  region = "";
  router = useRouter();
  async regist() {
    if (this.pass_str !== this.pass_strChk) return;
    if (
      (this.id_str.length &&
        this.pass_str.length &&
        this.call.length &&
        this.region.length &&
        this.name.length) === 0
    )
      return;
    let data = new FormData();
    data.append("id", this.id_str);
    data.append("pwd", this.pass_str);
    data.append("phone", this.call);
    data.append("region", this.region);
    data.append("user_name", this.name);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    try {
      await axios.post(apiUrl + "/register", data);
      alert("회원가입에 성공하였습니다");
      this.router.push("/auth");
    } catch (error) {
      if (error instanceof AxiosError) {
        if (error.response?.status === 409) {
          alert("이미 사용중인 아이디 입니다");
          return;
        }
      }
      alert("회원가입에 실패하였습니다");
    }
  }
  mounted() {
    if (authState.isSigned === true) useRouter().push("/");
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
  nameChanged(data: string) {
    this.name = data;
  }
}
</script>
<style scoped>
.registerContainer {
  margin-top: 2rem;
  border-radius: 10px;
  background-color: whitesmoke;
}
#correctPwd {
  height: 2rem;
  width: 100%;
  text-align: center;
  color: red;
}
</style>
