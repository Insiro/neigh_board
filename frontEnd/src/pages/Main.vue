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
          v-for="(item, index) in posts"
          :key="item.id"
          @click="movePost(item.id)"
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
import { useRouter } from "vue-router";
import Card from "../components/card/Card.vue";
import Table from "../components/Table.vue";
@Options({ components: { Table, Card } })
export default class Main extends Vue {
  posts = [{ id: "id", title: "title" }];
  router = useRouter();
  movePost(id: string) {
    this.router.push("/post/" + id);
  }
}
</script>
