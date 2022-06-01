<template>
  <div class="col-xl-6 col-md-8 mb-6 cardContainer">
    <div class="card border-left-primary shadow h-100 py-2">
      <div class="card-body">
        <slot />
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
export default class CardBB extends Vue {}
</script>

<style scoped>
.cardContainer {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
