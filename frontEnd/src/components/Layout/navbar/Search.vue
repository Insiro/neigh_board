<template>
  <div class="input-group">
    <input
      type="text"
      class="form-control bg-light border-0 small"
      placeholder="Search for..."
      aria-label="Search"
      aria-describedby="basic-addon2"
    />
    <div class="input-group-append">
      <button class="btn btn-primary" type="button">
        <i class="fas fa-search fa-sm"></i>
      </button>
    </div>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
export default class Search extends Vue {}
</script>
