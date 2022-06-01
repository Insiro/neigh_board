<template>
  <div>
    <UserViewCard title="id">{{ user.id }}</UserViewCard>
    <UserViewCard title="user name">{{ user.user_name }}</UserViewCard>
    <UserViewCard title="regist date">{{ user.register }}</UserViewCard>
    <UserViewCard v-if="user.call !== ''" title="call">
      {{ user.call }}
    </UserViewCard>
    <UserViewCard title="region">{{ user.region }}</UserViewCard>
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import UserViewCard from "@/components/card/UserViewCard.vue";
import authState from "@/store/auth/state";
import { apiUrl } from "@/utils";
import { UserFull } from "@/store/entity";

@Options({ components: { UserViewCard } })
export default class Component extends Vue {
  route = useRoute();
  router = useRouter();
  private m_user: UserFull = {
    call: "",
    id: "",
    register: "",
    region: "",
    user_name: "",
  };
  async beforeMount() {
    let id = this.route.params.id;
    try {
      let result = await axios.get(apiUrl + "/user/" + id);
      let user = result.data.user;
      this.m_user.call = user.call;
      this.m_user.id = user.id;
      this.m_user.register = user.register;
      this.m_user.region = user.region;
      this.m_user.user_name = user.user_name;
      console.log(this.m_user);
    } catch (error) {
      this.router.push("/404");
    }
  }
  get user(): UserFull {
    return this.m_user;
  }
}
</script>
