<template>
  <button class="btn btn-primary btn-user btn-block">
    <slot />
  </button>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
export default class StyledButton extends Vue {}
</script>
