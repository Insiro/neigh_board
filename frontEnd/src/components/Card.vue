<template>
  <div class="card shadow mb-4">
    <div v-if="header !== null" class="card-header py-3">
      <h6 class="m-0 font-weight-bold text-primary">{{ header }}</h6>
    </div>
    <div class="card-body">
      <slot />
    </div>
  </div>
</template>
<script lang="ts">
import { Vue, prop } from "vue-class-component";
class Prop {
  header = prop<string | null>({ default: null });
}
export default class Card extends Vue.with(Prop) {}
</script>
