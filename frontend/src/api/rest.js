import axios from "axios";

import { rootStore } from "@/stores";

import { instance } from "@/api/axios";

import AuthApi from "@/api/classes/auth";
import DealApi from "@/api/classes/deal";
import StatusApi from "@/api/classes/status";
import SettingsApi from "@/api/classes/settings";


class RestService {
  constructor() {
    this.relation = {
      ...AuthApi.relation,
      ...DealApi.relation,
      ...StatusApi.relation,
      ...SettingsApi.relation,
    };
  }

  async callMethod(method, params, callBack) {
    if (!this.relation[method]) {
      return new Promise((_, reject) => {
        reject(callBack({ error: "method not found", status: 404 }));
      });
    }

    return new Promise(async (resolve, reject) => {
      this.runQuery(this.relation[method], params, this.getHeaders(method))
        .then((r) => {
          resolve(callBack(r));
        })
        .catch((e) => {
          if (e.status == 401) {
            this.disableAuthorization();
          }
          reject(callBack(e));
        });
    });
  }

  async callBatch(commands, callBack) {
    const methods = [];
    const keys = Object.keys(commands);

    keys.forEach((key) => {
      methods.push(
        this.getInstanse(
          this.relation[commands[key][0]],
          commands[key][1],
          this.getHeaders(commands[key][0])
        )
      );
    });

    return new Promise(async (resolve, reject) => {
      axios
        .all(methods)
        .then(
          axios.spread((...responses) => {
            const result = {};

            responses.forEach((response, index) => {
              result[keys[index]] = response;
            });

            resolve(callBack(result));
          })
        )
        .catch((e) => {
          if (e.status == 401) {
            this.disableAuthorization();
          }
          reject(callBack(e));
        });
    });
  }

  async runQuery(serverData, params, headers = {}) {
    

    return await this.getInstanse(serverData, params, headers);
  }

  getInstanse(serverData, params, headers = {}) {
    if (serverData.method == "GET") {
      return instance.get(serverData.path, { params: params, headers: { ...headers } });
    } else if (serverData.method == "POST") {
      return instance.post(serverData.path, params, { headers: { ...headers } });
    } else if (serverData.method == "PUT") {
      return instance.put(serverData.path, params, { headers: { ...headers } });
    } else if (serverData.method == "DELETE") {
      return instance.delete(serverData.path, { data: params, headers: { ...headers } });
    }
  }

  getHeaders(method) {
    switch (method) {
      case "auth.login":
        console.log('!111');
        
        return {}
      default:
        console.log('!222');
        return {
          'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
        };
    }
  }

  disableAuthorization() {
    try {
      const store = rootStore()
      store.auth().isAuth = false
    } catch (error) {
      console.log('_ERROR', error);
    }
  }
}

export { RestService };
