<template>
  <Card header="head">
    <Table>
      <template #header>
        <tr>
          <th scope="row">#</th>
          <th scope="row">title</th>
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
        </tr>
      </template>
    </Table>
  </Card>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import Card from "../components/Card.vue";
import Table from "../components/Table.vue";
import axios from "axios";
import { useRouter } from "vue-router";
interface page {
  id: string;
  title: string;
}
@Options({ components: { Table, Card } })
export default class Board extends Vue {
  pages: Array<page> = [];
  router = useRouter();
  beforeMount() {
    this.pages.push({ id: "id", title: "title" });
    this.pages.push({ id: "id2", title: "title2" });
  }
  moveSub(id: string) {
    this.router.push("/post/" + id);
  }
}
</script>
