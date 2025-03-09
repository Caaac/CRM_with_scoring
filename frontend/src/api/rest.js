import instance from "@/api/axios";
import axios from 'axios';

class RestService {
  constructor() {
    this.API_BASE_PATH = "/api/v1/";
    this.relation = {
      "crm.status.get": {
        path: this.API_BASE_PATH + "crm/status/",
        method: "GET",
      },
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

  async callMethod(method, params, callBack) {
    if (!this.relation[method]) {
      return new Promise((_, reject) => {
        reject({ error: "method not found", status: 404 });
      });
    }

    return new Promise(async (resolve, reject) => {
      this.runQuery(this.relation[method], params)
        .then((r) => {
          resolve(callBack(r));
        })
        .catch((e) => {
          reject(e);
        });
    });
  }

  async callBatch(commands, callBack) {
    const methods = [];
    const keys = Object.keys(commands);

    keys.forEach((key) => {
      methods.push(this.getInstanse(this.relation[commands[key][0]], commands[key][1]));
    });

    return new Promise(async (resolve, reject) => {
      axios.all(methods)
        .then(axios.spread((...responses) => {
          const result = {};

          responses.forEach((response, index) => {
            result[keys[index]] = response;
          })

          resolve(callBack(result))
        }))
        .catch(e => { reject(e) })
    })
  }

  async runQuery(serverData, params) {
    return await this.getInstanse(serverData, params);
  }

  getInstanse(serverData, params) {
    if (serverData.method == "GET") {
      return instance.get(serverData.path, { params: params });
    } else if (serverData.method == "POST") {
      return instance.post(serverData.path, params);
    } else if (serverData.method == "PUT") {
      return instance.put(serverData.path, params);
    } else if (serverData.method == "DELETE") {
      return instance.delete(serverData.path, params);
    }
  }
}

export { RestService };
