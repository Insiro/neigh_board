<template>
  <div>
    <!--eslint-disable-next-line vue/no-v-html-->
    <div id="marked" class="marked mt-5" v-html="license"></div>
  </div>
</template>
<script lang="ts">
import axios from "axios";
import { Vue } from "vue-class-component";
import {marked} from "marked";
export default class Component extends Vue {
  license = "";
  async created() {
    try {
      const rawMark = await axios.get("/notice.md");
      this.license = marked(rawMark.data);
    } catch (error) {
      this.license = "";
    }
  }
}
</script>
