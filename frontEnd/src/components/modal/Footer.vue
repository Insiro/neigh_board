<template>
  <div class="modal-footer">
    <button
      class="btn btn-secondary"
      type="button"
      data-dismiss="modal"
      @click="closeModal()"
    >
      Cancel
    </button>
    <slot name="footer"> </slot>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
export default class Footer extends Vue {
  closeModal() {
    this.$emit("on-close-click");
  }
}
</script>
