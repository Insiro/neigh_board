<template>
  <input
    v-model="value"
    class="form-control form-control-user"
    :type="type"
    :placeholder="placeholder"
    @change="onInputChanged"
  />
</template>
<script lang="ts">
import { prop, Vue } from "vue-class-component";
class Prop {
  type = prop<
    | "text"
    | "date"
    | "datetime-local"
    | "email"
    | "month"
    | "password"
    | "number"
    | "url"
    | "tel"
    | "time"
    | "week"
  >({ default: "text" });
  placeholder = prop<string>({ default: null });
  value = prop<string | null>({ default: null });
}
export default class Component extends Vue.with(Prop) {
  onInputChanged(e: Event): void {
    this.$emit("updates", (e.target as HTMLInputElement).value);
  }
}
</script>
