import Api from "@/api/classes/api";

export default class AuthApi extends Api {
  static _relation = {
    "auth.login": {
      path: "auth/login/",
      method: "POST",
    },
    "auth.refresh": {
      path: "auth/refresh/",
      method: "POST",
    },
    // "auth.logout": {
    //   path: "auth/logout/",
    //   method: "POST",
    // },
  };
}

