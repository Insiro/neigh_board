import { User } from "../entity";
export class AuthData implements User {
  id: string = "";
  name: string = "";
  bSigned?: boolean = undefined;
}
export interface AuthInterface {
  data: AuthData;
}
