<template>
  <li class="nav-item">
    <a
      class="nav-link collapsed"
      href="#"
      data-toggle="collapse"
      data-target="#collapseTwo"
      aria-expanded="true"
      aria-controls="collapseTwo"
      @click="toggle()"
    >
      <slot name="default" />
    </a>
    <div
      id="collapseTwo"
      class="collapse"
      aria-labelledby="headingTwo"
      data-parent="#accordionSidebar"
      :class="[ShowMenu ? show : blank]"
    >
      <div class="bg-white py-2 collapse-inner rounded">
        <slot name="content" />
      </div>
    </div>
  </li>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
import { ref } from "vue";
export default class Component extends Vue {
  ShowMenu = false;
  show = ref("show");
  blank = ref("");
  toggle() {
    this.ShowMenu = !this.ShowMenu;
  }
}
</script>
