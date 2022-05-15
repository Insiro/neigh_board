<template>
  <div id="logoutModal" class="modal fade" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <Header><slot name="header" @on-close-click="closeModal()" /></Header>
        <div class="modal-body">
          <slot name="body" />
        </div>
        <Footer><slot name="footer" @on-close-click="closeModal()" /></Footer>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Vue, Options, prop } from "vue-class-component";
import Header from "./Header.vue";
import Footer from "./Footer.vue";

class Prop {
  display = prop<boolean>({ default: false });
}
@Options({ components: { Header, Footer } })
export default class ModalLayout extends Vue.with(Prop) {
  closeModal() {
    this.$emit("on-close-req");
  }
}
</script>
