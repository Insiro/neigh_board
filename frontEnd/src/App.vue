<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import { useRoute } from "vue-router";
import { Layout, EmptyLayout } from "./components/Layout";
import authState from "./store/auth/state";
@Options({ components: { Layout, EmptyLayout } })
export default class App extends Vue {
  created() {
    authState.refreshSession();
  }
  get layout(): string {
    return useRoute().meta.noLayout === true ? "EmptyLayout" : "Layout";
  }
}
</script>
