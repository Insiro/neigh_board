import {
  Module,
  VuexModule,
  Mutation,
  getModule,
  Action,
} from "vuex-module-decorators";
import axios from "axios";
import store from "..";
import { AuthData, AuthInterface } from "./interface";
import { apiUrl } from "@/utils";
import { User } from "../entity";
@Module({ namespaced: true, store, name: "authModule", dynamic: true })
export class AuthState extends VuexModule implements AuthInterface {
  data = new AuthData();

  @Mutation setSign(value: boolean): void {
    this.data.bSigned = value;
  }
  @Mutation setID(id: string): void {
    this.data.id = id;
  }
  @Mutation setUserName(name: string): void {
    this.data.name = name;
  }
  @Action async signIn(info: {
    id: string;
    password: string;
  }): Promise<boolean> {
    try {
      const form = new FormData();
      form.append("id", info.id);
      form.append("pwd", info.password);
      const result = await axios.post(apiUrl + "/auth", form);
      const data = result.data.user;
      this.setUserName(data.name);
      this.setID(data.id);
      this.setSign(true);
      return true;
    } catch (err: unknown) {
      console.warn("ERROR!!!!! : ", err);
      this.setSign(false);
      return false;
    }
  }
  @Action async signOut() {
    this.setSign(false);
    axios.delete(apiUrl + "/auth");
  }
  @Action async refreshSession(): Promise<void> {
    const result = await axios.get(apiUrl + "/auth");
    const data = result.data;
    if (data.isSigned === false) {
      this.setSign(false);
      return;
    }
    this.setUserName(data.user.name);
    this.setID(data.user.id);
    this.setSign(true);
  }
  get isSigned() {
    return this.data.bSigned;
  }
  get user(): User {
    console.log(this.data);
    return {
      id: this.data.id,
      name: this.data.name,
    };
  }
}
export const authState = getModule(AuthState);

export default authState;
