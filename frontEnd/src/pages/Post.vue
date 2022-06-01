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
    <CardB v-for="com in comments" :key="com.id">
      작성자 : {{ com.author }} <br />
      {{ com.comment }}
    </CardB>
  </div>
</template>
<script lang="ts">
import axios, { AxiosError } from "axios";
import { marked } from "marked";
import { Options, Vue } from "vue-class-component";
import { useRouter, useRoute } from "vue-router";
import { Post, Comment } from "@/store/entity";
import CardB from "@/components/card/CardB.vue";
import { apiUrl } from "@/utils";
@Options({
  components: { CardB },
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
  router = useRouter();
  valid = false;
  comments: Comment[] = [];
  get post(): Post {
    return this.m_post;
  }
  async mounted() {
    let id = useRoute().params.id.toString();
    try {
      let result = await axios.get(apiUrl + "/post/" + id);
      this.m_post = result.data.post as Post;
      this.m_post.id = id;
      if (id === "" || result.status > 399) throw new Error();
      try {
        let comm_result = await axios.get(apiUrl + "/post/" + id + "/comment");
        this.comments = comm_result.data.comments as Comment[];
      } catch (_) {}
    } catch (error) {
      if (!this.valid) this.router.push("/404");
    }
  }
  get postText(): string {
    return marked(this.m_post.content ?? "");
  }
}
</script>
