<template>
  <ul
    id="sidebar"
    class="navbar-nav sidebar sidebar-dark accordion"
    :style="{ backgroundColor: bgColor }"
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
    <div style="height: 2rem"></div>
    <Divider />
    <Item to="/post">
      <i class="fas fa-fw fa-notebook"></i>
      <span>게시판</span>
    </Item>
    <Item to="/newPost">
      <i class="fas fa-fw fa-pen"></i>
      <span>새글 쓰기</span>
    </Item>
    <Item to="/license">
      <i class="fas fa-fw fa-pen"></i>
      <span>오픈소스 라이센스</span>
    </Item>
    <div style="flex-grow: 1"></div>
    <Item>
      <button class="toggle_btn" @click="sidebarToggle()" />
    </Item>
    <div style="height: 20%"></div>
  </ul>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import { ref } from "vue";
import Divider from "./item/Divider.vue";
import Item from "./item/Item.vue";
import Fold, { FoldItem, FoldHeader } from "./item/fold";
import { primaryColor } from "@/utils";
@Options({ components: { Item, Divider, Fold, FoldItem, FoldHeader } })
export default class Sidebar extends Vue {
  bgColor = primaryColor;
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
  border-radius: 15px !important;
  border-width: 0px;
  height: 1rem;
  width: 100%;
  display: flex;
}
@media screen and (max-width: 768px) {
  #sidebar.toggled {
    display: none;
  }
}
</style>
