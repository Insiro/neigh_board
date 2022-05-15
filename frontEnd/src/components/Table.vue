<template>
  <div class="table-responsive">
    <table
      id="dataTable"
      class="table table-bordered table-hover"
      width="100%"
      cellspacing="0"
    >
      <thead>
        <slot name="header" />
      </thead>
      <tbody>
        <slot name="content" />
      </tbody>
    </table>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";

export default class Table extends Vue {}
</script>
