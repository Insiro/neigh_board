<template>
  <li class="nav-item">
    <router-link class="nav-link" :to="to">
      <slot />
    </router-link>
  </li>
</template>
<script lang="ts">
import { prop, Vue } from "vue-class-component";
class Props {
  to = prop<string>({
    default: "",
  });
}
export default class NavItem extends Vue.with(Props) {}
</script>
