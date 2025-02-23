import instance from "@/api/axios"

class RestService {
  constructor() {
    this.API_BASE_PATH = '/api/v1/'
    this.relation = {
      'crm.status.get': {
        path: this.API_BASE_PATH + 'crm/status',
        method: 'GET'
      }
    }
  }
  async callMethod(method, params, callBack) {
    return await this.runQuery()
  }

  async runQuery(serverData, params) {
    return await new Promise((rs, rj) => {
      instance.get('/api/v1/crm/status/')
        .then(r => {rs(r)})
        .catch(e => {rj(e)}) 
    })
  }
}

export {RestService}