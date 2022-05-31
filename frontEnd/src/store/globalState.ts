import {
  Module,
  VuexModule,
  Mutation,
  getModule,
} from "vuex-module-decorators";
import store from ".";
@Module({ namespaced: true, store, name: "GlobalModule", dynamic: true })
export class GlobalModule extends VuexModule implements GlobalInterface {
  SideBarOpen: boolean = false;
  PageName: string = "";
  UserId: string = "";
  UserName: string = "";
  @Mutation setSideBar(state: boolean): void {
    this.SideBarOpen = state;
  }
  get isSideBarOpend(): boolean {
    return this.SideBarOpen;
  }
  @Mutation setPageName(name: string): void {
    this.PageName = name;
  }
  get pageName(): string {
    return this.PageName;
  }
  set pageName(data: string) {
    this.PageName = data;
  }
}
export const globalState = getModule(GlobalModule);
export interface GlobalInterface {
  SideBarOpen: boolean;
  PageName: string;
  UserName: string;
  UserId: string;
}
export default globalState;
