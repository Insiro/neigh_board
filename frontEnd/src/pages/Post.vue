<template>
  <div>
    <div>{{ title }}</div>
    <!--eslint-disable-next-line vue/no-v-html-->
    <div id="marked" class="marked mt-5" v-html="postText"></div>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
import { useRoute } from "vue-router";
export default class Component extends Vue {
  id: string = "ids";
  title = "";
  beforeMount() {
    //
    this.id = useRoute().params.id.toString();
    this.title = this.id;
  }
  get postText(): string {
    return "";
  }
}
</script>
