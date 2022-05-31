<template>
  <Card header="head">
    <Table>
      <template #header>
        <tr>
          <th scope="row">#</th>
          <th scope="row">title</th>
          <th scope="row">author</th>
          <th scope="row">date</th>
        </tr>
      </template>
      <template #content>
        <tr
          v-for="(item, index) in pages"
          :key="item.id"
          @click="moveSub(item.id)"
        >
          <th scope="column">{{ index }}</th>
          <td>{{ item.title }}</td>
          <td>{{ item.author }}</td>
          <td>{{ item.date }}</td>
        </tr>
      </template>
    </Table>
  </Card>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import Card from "../components/card/Card.vue";
import Table from "../components/Table.vue";
import axios from "axios";
import { Post } from "@/store/entity";
import { useRouter } from "vue-router";
@Options({ components: { Table, Card } })
export default class Board extends Vue {
  pages: Array<Post> = [];
  router = useRouter();
  async beforeMount() {
    try {
      let response = await axios.get("/api/post");
      let posts: Array<Post> = response.data.posts;
      posts.forEach((post) => {
        this.pages.push(post);
      });
      console.log(response.data);
    } catch (error) {}
  }
  moveSub(id: string) {
    this.router.push("/post/" + id);
  }
}
</script>
