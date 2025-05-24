import Api from "@/api/classes/api";

export default class StatusApi extends Api {
  static _relation = {
    "crm.status.get": {
      path: this.API_BASE_PATH + "crm/status/",
      method: "GET",
    }
  };
}

