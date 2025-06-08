import Api from "@/api/classes/api";

export default class StatusApi extends Api {
  static _relation = {
    "crm.status.list": {
      path: this.API_BASE_PATH + "crm/stage/",
      method: "GET",
    },
    "crm.status.update": {
      path: this.API_BASE_PATH + "crm/stage/",
      method: "PUT",
    },
    "crm.status.add": {
      path: this.API_BASE_PATH + "crm/stage/",
      method: "POST",
    },
    "crm.status.delete": {
      path: this.API_BASE_PATH + "crm/stage/",
      method: "DELETE",
    }
  };
}

