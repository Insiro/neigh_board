<template>
  <nav
    class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow"
  >
    <!-- Sidebar Toggle (Topbar) -->
    <button
      id="sidebarToggleTop"
      class="btn btn-link d-md-none rounded-circle mr-3"
    >
      <i class="fa fa-bars"></i>
    </button>

    <!-- Topbar Search -->
    

    <!-- Topbar Navbar -->
    <ul class="navbar-nav ml-auto">
      <!-- Nav Item - Search Dropdown (Visible Only XS) -->
      

      <DropDown counter="3">
        <template #default>
          <i class="fas fa-bell fa-fw"></i>
        </template>
        <template #content>
          <DropDownHeader>header</DropDownHeader>
          <div>dropDown</div>
          <DropDownContent />
          <DropDownItem />
        </template>
      </DropDown>

      <Divider />

      <!-- Nav Item - User Information -->
      <DropDown>
        <template #default>
          <span class="mr-2 d-none d-lg-inline text-gray-600 small">
            {{ user.name }}
          </span>
          <img class="img-profile rounded-circle" src="/user.svg" />
        </template>
        <template #content>
          <DropDownItem
            v-if="user.id !== '' && user.id !== undefined"
            @click="moveUserInfo"
          >
            <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
            User Info
          </DropDownItem>
          <DropDownItem
            v-if="user.id !== '' && user.id !== undefined"
            @click="sign()"
          >
            <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400" />
            {{
              user.id !== "" && user.id !== undefined ? "sign out" : "sign in"
            }}
          </DropDownItem>
        </template>
      </DropDown>
    </ul>
  </nav>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import Divider from "./Divider.vue";
import Search from "./Search.vue";
import DropDown, {
  DropDownItem,
  DropDownContent,
  DropDownHeader,
} from "./dropDown";
import { useRouter } from "vue-router";
import { User } from "@/store/entity";
import authState from "@/store/auth/state";

@Options({
  components: {
    Search,
    Divider,
    DropDown,
    DropDownContent,
    DropDownItem,
    DropDownHeader,
  },
})
export default class NavBar extends Vue {
  router = useRouter();
  sign() {
    authState.signOut();
    this.router.push("/auth");
  }
  get user(): User {
    return authState.user;
  }
  moveUserInfo() {
    this.router.push("/user/" + authState.user.id);
  }
}
</script>
<style scoped>
.searchItem {
  display: none;
}
@media screen and (max-width: 575px) {
  .searchItem {
    display: block;
  }
}
</style>
