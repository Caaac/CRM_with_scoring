import Api from "@/api/classes/api";

export default class SettingsApi extends Api {
  static _relation = {
    "crm.userField.list": {
      path: this.API_BASE_PATH + "crm/user-field/",
      method: "GET",
    },
    "crm.userField.get": {
      path: this.API_BASE_PATH + "crm/user-field-detail/",
      method: "GET",
    },
    "crm.userField.update": {
      path: this.API_BASE_PATH + "crm/user-field-detail/",
      method: "PUT",
    },
    "crm.userField.add": {
      path: this.API_BASE_PATH + "crm/user-field-detail/",
      method: "POST",
    },
    "crm.userField.delete": {
      path: this.API_BASE_PATH + "crm/user-field-detail/",
      method: "DELETE",
    },
  };
}

