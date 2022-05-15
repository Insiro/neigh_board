<template>
  <div class="dropdown-item">
    <slot />
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
export default class DropDownItem extends Vue {}
</script>
