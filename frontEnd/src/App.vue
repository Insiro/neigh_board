<template>
  <Layout>
    <router-view />
  </Layout>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import Layout from "./components/Layout";
@Options({ components: { Layout } })
export default class App extends Vue {}
</script>
