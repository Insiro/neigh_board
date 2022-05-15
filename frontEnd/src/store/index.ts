import { Store } from "vuex";
import { GlobalInterface } from "./globalState";

interface RootState {
  global: GlobalInterface;
}

const store = new Store<RootState>({
  state: {
    global: {
      SideBarOpen: false,
      PageName: "",
      UserId: "",
      UserName: "",
    },
  },
});
export default store;
