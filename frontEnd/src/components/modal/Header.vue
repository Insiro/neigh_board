<template>
  <div class="modal-header">
    <h5 class="modal-title"><slot /></h5>
    <button type="button" @click="closeModal()">
      <span aria-hidden="true">×</span>
    </button>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";

export default class Header extends Vue {
  closeModal() {
    this.$emit("on-close-click");
  }
}
</script>
