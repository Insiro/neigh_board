<template>
  <li class="nav-item dropdown no-arrow mx-1">
    <a
      class="nav-link dropdown-toggle"
      href="#"
      role="button"
      data-toggle="dropdown"
      aria-haspopup="true"
      aria-expanded="false"
      @click="toggle()"
    >
      <slot />
      <span class="badge badge-danger badge-counter">{{ counter }}</span>
    </a>
    <div
      class="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in"
      :class="[ShowMenu ? show : blank]"
    >
      <slot name="content" />
    </div>
  </li>
</template>
<script lang="ts">
import { Vue, prop } from "vue-class-component";
import { ref } from "vue";
class Prop {
  counter = prop<string>({ default: "" });
  title = prop<string | false>({ default: false });
}

export default class DropDown extends Vue.with(Prop) {
  ShowMenu = false;
  show = ref("show");
  blank = ref("");
  toggle() {
    this.ShowMenu = !this.ShowMenu;
  }
}
</script>
