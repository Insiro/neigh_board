<template>
  <div>
    {{ id }}
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
import { useRoute } from "vue-router";
export default class Component extends Vue {
  id: string = "ids";
  beforeMount() {
    //
    this.id = useRoute().params.id.toString();
  }
}
</script>
