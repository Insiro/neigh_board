<template>
  <div>
    <UserViewCard title="id">{{ id }}</UserViewCard>
    <UserViewCard title="regist date">{{ regist }}</UserViewCard>
    <UserViewCard title="call">{{ call }}</UserViewCard>
    <UserViewCard title="region">{{ region }}</UserViewCard>
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import UserViewCard from "@/components/card/UserViewCard.vue";

@Options({ components: { UserViewCard } })
export default class Component extends Vue {
  id = "";
  regist = "";
  call = "";
  region = "";
}
</script>
