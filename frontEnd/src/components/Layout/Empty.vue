<template>
  <div class="container">
    <div class="row justify-content-center">
      <slot />
    </div>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
export default class EmptyLayout extends Vue {}
</script>
