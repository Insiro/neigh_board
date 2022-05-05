<template>
  <Layout @on-close-req="closeReq()">
    <template #header>{{ title }}</template>
    <template #body><slot /></template>
    <template #footer>
      <div class="btn btn-primary" @click="okClicked()">Ok</div>
    </template>
  </Layout>
</template>
<script lang="ts">
import { Vue, prop } from "vue-class-component";
class Props {
  title = prop<string>({ default: "" });
}
export default class LogOut extends Vue.with(Props) {
  okClicked() {
    this.$emit("on-ok-click");
  }
  closeReq() {
    this.$emit("on-close-req");
  }
}
</script>
