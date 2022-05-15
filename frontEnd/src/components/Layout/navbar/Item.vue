<template>
  <li class="nav-item no-arrow">
    <slot />
  </li>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";

export default class Item extends Vue {}
</script>
