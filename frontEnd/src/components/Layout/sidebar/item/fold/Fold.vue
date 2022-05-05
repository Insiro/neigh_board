<template>
  <li class="nav-item">
    <a
      class="nav-link collapsed"
      href="#"
      data-toggle="collapse"
      data-target="#collapseTwo"
      aria-expanded="true"
      aria-controls="collapseTwo"
    >
      <slot />
    </a>
    <div
      id="collapseTwo"
      class="collapse"
      aria-labelledby="headingTwo"
      data-parent="#accordionSidebar"
    >
      <div class="bg-white py-2 collapse-inner rounded">
        <slot name="content" />
      </div>
    </div>
  </li>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
export default class Component extends Vue {}
</script>
