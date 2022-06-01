<template>
  <div>
    <h1>{{ post.title ?? "" }}</h1>
    <div>
      작성자 : {{ post.author }}<br />
      작성일 : {{ post.date }}<br />
    </div>
    <hr />
    <!--eslint-disable-next-line vue/no-v-html-->
    <div id="marked" class="marked mt-5" v-html="postText"></div>
    <hr />
    <CardB>
      <UserInput
        v-if="isSigned"
        :value="newComment"
        class="editComment"
        @updates="newCommentChanged"
      />
      <StyledButton id="com_regist" @click="sendNewComm">
        댓글 등록하기
      </StyledButton>
    </CardB>
    <hr />
    <CardB v-for="com in comments" :key="com.id">
      작성자 : {{ com.author }} <br />
      {{ com.comment }}
    </CardB>
  </div>
</template>
<script lang="ts">
import axios from "axios";
import { marked } from "marked";
import { Options, Vue } from "vue-class-component";
import { useRouter, useRoute } from "vue-router";
import { Post, Comment } from "@/store/entity";
import CardB from "@/components/card/CardB.vue";
import StyledButton from "@/components/StyledButton.vue";
import UserInput from "@/components/input/UserInput.vue";
import { apiUrl } from "@/utils";
import authState from "@/store/auth/state";
@Options({
  components: { CardB, UserInput, StyledButton },
})
export default class Component extends Vue {
  m_post: Post = {
    author: "",
    title: "",
    content: "",
    likes: 0,
    region: "",
    date: "",
    id: "",
  };
  newComment = "";
  router = useRouter();
  valid = true;
  comments: Comment[] = [];
  get post(): Post {
    return this.m_post;
  }
  async loadComment() {
    try {
      let comm_result = await axios.get(
        apiUrl + "/post/" + this.m_post.id + "/comment"
      );
      this.comments = comm_result.data.comments as Comment[];
    } catch (_) {}
  }
  async mounted() {
    let id = useRoute().params.id.toString();
    if (!this.valid) return;
    this.valid = false;
    try {
      let result = await axios.get(apiUrl + "/post/" + id);
      this.m_post = result.data.post as Post;
      this.m_post.id = id;
      if (id === "" || result.status > 399) throw new Error();
      this.loadComment();
    } catch (error) {
      if (!this.valid) this.router.push("/404");
    }
    this.valid = true;
  }
  async sendNewComm() {
    if (this.newComment === "") return;
    try {
      await axios.post(apiUrl + "/post/" + this.m_post.id + "/comment", {
        comment: this.newComment,
      });
      alert("댓글 등록에 성공하였습니다");
      this.newComment = "";
      this.loadComment();
    } catch (error) {}
  }
  newCommentChanged(comm: string) {
    this.newComment = comm;
  }
  get isSigned(): boolean {
    return authState.isSigned === true;
  }
  get postText(): string {
    return marked(this.m_post.content ?? "");
  }
}
</script>
<style scoped>
#com_regist {
  margin-top: 1rem;
}
</style>
