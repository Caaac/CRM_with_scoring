import Api from "@/api/classes/api";

export default class DealApi extends Api {
  static _relation = {
    "crm.deal.get": {
      path: this.API_BASE_PATH + "crm/deal/",
      method: "GET",
    },
    "crm.deal.update": {
      path: this.API_BASE_PATH + "crm/deal/",
      method: "PUT",
    },
    "crm.deal.detail.get": {
      path: this.API_BASE_PATH + "crm/detail/deal/",
      method: "GET",
    },
    "crm.deal.detail.update": {
      path: this.API_BASE_PATH + "crm/detail/deal/",
      method: "PUT",
    },
    "crm.deal.init.kanban": {
      path: this.API_BASE_PATH + "crm/deal/kanban/",
      method: "GET",
    },
    "crm.deal.init.list": {
      path: this.API_BASE_PATH + "crm/deal/list/",
      method: "GET",
    },
  };
}

