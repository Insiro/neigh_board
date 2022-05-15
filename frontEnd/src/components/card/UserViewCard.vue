<template>
  <Card>
    <div class="col no-gutters align-items-center">
      <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
        {{ title }}
      </div>
      <div class="h5 mb-0 font-weight-bold text-gray-800"><slot /></div>
    </div>
  </Card>
</template>
<script lang="ts">
import { Vue, prop, Options } from "vue-class-component";
import Card from "./Card.vue";
class Prop {
  title = prop<string>({ default: "" });
}
@Options({ components: { Card } })
export default class Component extends Vue.with(Prop) {}
</script>
