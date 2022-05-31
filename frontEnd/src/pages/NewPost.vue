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
      <button class="mt-5 postItem" @click="submitPost">게시</button>
    </div>
    <div class="flex-grow-1" />
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import UserInput from "@/components/input/UserInput.vue";
import axios from "axios";
import { apiUrl } from "@/utils";
@Options({ components: { UserInput } })
export default class NewPost extends Vue {
  title = "";
  content = "";
  onTitleChanged(title: string) {
    this.title = title;
  }
  async submitPost() {
    if (this.title === this.content && this.content === "") return;
    let data = {
      title: this.title,
      conent: this.content,
    };
    try {
      await axios.post(apiUrl + "/post", data);
      this.title = "";
      this.content = "";
      alert("계시글 등록이 완료되었습니다");
    } catch (error) {}
    alert("계시글 등록에 실패하였습니다");
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
