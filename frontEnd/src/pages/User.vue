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
  async mounted() {
    let id = this.route.params.id;
    if (id === undefined) {
      this.update_self();
      return;
    }
    try {
      let result = await axios.get(apiUrl + "/user/" + id);
      let user: UserFull = result.data.user;
      this.m_user = user;
    } catch (error) {
      this.router.push("/404");
    }
  }
  get user(): UserFull {
    return this.m_user;
  }
  update_self() {
    let id = authState.data.id;
    try {
      this.router.push("/user/" + id);
    } catch (error) {
      this.router.push("/404");
    }
  }
}
</script>
