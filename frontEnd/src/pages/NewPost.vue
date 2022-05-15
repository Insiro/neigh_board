<template>
  <div class="d-flex flex-row h-full">
    <div :class="BoxStyle" />
    <div class="flex flex-col h-full postItem flex-grow">
      <div class="flex mt-3 postItem flex-row">
        <UserInput
          placeholder="제목"
          class="flex-grow"
          :value="title"
          @updates="onTitleChanged"
        />
      </div>

      <WideFrame class="flex-grow postItem">
        <textarea
          v-model="content"
          class="h-full w-full"
          placeholder="게시글을 입력하세요"
        ></textarea>
      </WideFrame>
      <Button class="flex-grow-0 mt-5 postItem" @Click="submitPost"
        >게시</Button
      >
    </div>
    <div :class="BoxStyle" />
  </div>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import { ref } from "vue";
import UserInput from "@/components/input/UserInput.vue";
@Options({ components: { UserInput } })
export default class NewPost extends Vue {
  title = "";
  content = "";
  BoxStyle = ref("flex-grow BOX");
  onTitleChanged(title: string) {
    this.title = title;
  }
  submitPost() {
    //TODO
  }
}
</script>
