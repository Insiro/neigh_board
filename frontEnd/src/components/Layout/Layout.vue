<template>
  <div>
    <div id="wrapper">
      <SideBar />
    </div>
    <!-- Logout Modal-->
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import SideBar from "./sidebar";
import Footer from "./Footer.vue";

@Options({ components: { SideBar, Footer } })
export default class Layout extends Vue {}
</script>
