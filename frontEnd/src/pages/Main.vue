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
        <tr>
          <th scope="column">1</th>
          <td>title-1</td>
        </tr>
      </template>
    </Table>
  </Card>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import Card from "../components/Card.vue";
import Table from "../components/Table.vue";
@Options({ components: { Table, Card } })
export default class Main extends Vue {}
</script>
