import { Store } from "vuex";
import { GlobalInterface } from "./globalState";
import { AuthData, AuthInterface } from "./auth/interface";
interface RootState {
  global: GlobalInterface;
  auth: AuthInterface;
}

const store = new Store<RootState>({
  state: {
    global: {
      SideBarOpen: false,
      PageName: "",
      UserId: "",
      UserName: "",
    },
    auth: { data: new AuthData() },
  },
});
export default store;
