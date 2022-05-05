<template>
  <div>
    <Layout> neigh baord </Layout>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import Layout from "./components/Layout";
@Options({ components: { Layout } })
export default class App extends Vue {}
</script>
