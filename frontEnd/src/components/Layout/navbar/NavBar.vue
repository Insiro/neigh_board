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
    <form
      class="d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search"
    >
      <Search />
    </form>

    <!-- Topbar Navbar -->
    <ul class="navbar-nav ml-auto">
      <!-- Nav Item - Search Dropdown (Visible Only XS) -->
      <DropDown class="searchItem">
        <template #default>
          <i class="fas fa-search fa-fw"></i>
        </template>
        <template #content>
          <form class="form-inline mr-auto w-100 navbar-search">
            <Search />
          </form>
        </template>
      </DropDown>

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
          <span class="mr-2 d-none d-lg-inline text-gray-600 small"
            >User Name</span
          >
          <img class="img-profile rounded-circle" src="/user.svg" />
        </template>
        <template #content>
          <DropDownItem>
            <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
            DropDown
          </DropDownItem>
          <DropDownItem @click="signOut()">
            <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400" />
            Logout
          </DropDownItem>
        </template>
      </DropDown>
    </ul>
  </nav>
</template>
<script lang="ts">
import { Vue, Options } from "vue-class-component";
import globalState from "@/store/globalState";
import Divider from "./Divider.vue";
import Search from "./Search.vue";
import DropDown, {
  DropDownItem,
  DropDownContent,
  DropDownHeader,
} from "./dropDown";
import { useRouter } from "vue-router";

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
  signOut() {
    globalState.setUser("", "");
    this.router.push("/auth");
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
