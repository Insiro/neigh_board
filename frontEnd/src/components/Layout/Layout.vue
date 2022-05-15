<template>
  <div>
    <div id="wrapper">
      <SideBar />
      <div id="content-wrapper" class="d-flex flex-column">
        <div id="content-fluid" class="d-flex flex-column flex-grow-1">
          <NavBar />
          <div class="container-fluid flex-grow-1">
            <slot />
          </div>
        </div>
        <Footer />
      </div>
    </div>
    <!-- Logout Modal-->
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import SideBar from "./sidebar";
import Footer from "./Footer.vue";
import NavBar from "./navbar/NavBar.vue";
@Options({ components: { SideBar, Footer, NavBar } })
export default class Layout extends Vue {}
</script>
