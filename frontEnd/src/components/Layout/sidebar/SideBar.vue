<template>
  <ul
    id="sidebar"
    class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion"
    :class="[isToggled ? toggledCss : blank]"
  >
    <!-- Sidebar - Brand -->
    <router-link
      class="sidebar-brand d-flex align-items-center justify-content-center"
      to="/"
    >
      <div class="sidebar-brand-icon rotate-n-15">
        <i class="fas fa-laugh-wink"></i>
      </div>
      <div class="sidebar-brand-text mx-3">NeigBoard</div>
    </router-link>

    <Divider />

    <!-- Nav Item - Dashboard -->
    <Item to="/">
      <i class="fas fa-fw fa-tachometer-alt"></i>
      <span>Item</span>
    </Item>

    <Divider>Divider</Divider>

    <Fold>
      <template #default>
        <i class="fas fa-fw fa-cog"></i>
        <span>Fold Menu</span>
      </template>
      <template #content>
        <FoldHeader>Fold Items:</FoldHeader>
        <FoldItem>FoldItem</FoldItem>
      </template>
    </Fold>

    <div class="text-center d-none d-md-inline">
      <button class="toggle_btn" @click="sidebarToggle()" />
    </div>
  </ul>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import { ref } from "vue";
import Divider from "./item/Divider.vue";
import Item from "./item/Item.vue";
import Fold, { FoldItem, FoldHeader } from "./item/fold";
@Options({ components: { Item, Divider, Fold, FoldItem, FoldHeader } })
export default class Sidebar extends Vue {
  isToggled = false;
  sidebarToggle(): void {
    this.isToggled = !this.isToggled;
  }

  toggledCss = ref("toggled");
  blank = ref("");
}
</script>
<style scoped>
.toggle_btn {
  border-radius: 50% !important;
  border-width: 0px;
}
@media screen and (max-width: 768px) {
  #sidebar.toggled {
    display: none;
  }
}
</style>
