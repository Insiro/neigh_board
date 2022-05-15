<template>
  <hr class="sidebar-divider" />
  <div class="sidebar-heading"><slot /></div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class Divider extends Vue {}
</script>
