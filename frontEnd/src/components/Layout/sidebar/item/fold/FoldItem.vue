<template>
  <router-link class="collapse-item" :to="to">slot</router-link>
</template>
<script lang="ts">
import { Vue, prop } from "vue-class-component";
class Props {
  to = prop<string>({ default: "" });
}
export default class FoldItem extends Vue.with(Props) {}
</script>
