<template>
  <div class="d-flex flex-row w-100">
    <div class="flex-grow-1" />
    <div class="postItem contentWrapper">
      <div class="flex mt-3 postItem flex-row">
        <UserInput
          placeholder="제목"
          class="flex-grow"
          :value="title"
          @updates="onTitleChanged"
        />
      </div>

      <div class="postItem mt-5 w-100 contentWrapper">
        <textarea
          v-model="content"
          class="h-100 w-100"
          placeholder="게시글을 입력하세요"
        />
      </div>
      <Button class="mt-5 postItem" @click="submitPost"> 게시 </Button>
    </div>
    <div class="flex-grow-1" />
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import UserInput from "@/components/input/UserInput.vue";
@Options({ components: { UserInput } })
export default class NewPost extends Vue {
  title = "";
  content = "";
  onTitleChanged(title: string) {
    this.title = title;
  }
  submitPost() {
    //TODO
  }
}
</script>
<style scopped>
.postItem {
  max-width: 750px;
}
.contentWrapper {
  min-width: 80%;
}
textarea {
  min-height: 40vh;
}
</style>
