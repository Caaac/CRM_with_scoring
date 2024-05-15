import { ref, computed, inject } from 'vue'
import { defineStore } from 'pinia'
import { rootStore } from '@/stores'

export const useCrmStore = defineStore('crm', () => {
  const $axios = inject('$axios')
  const store = rootStore()

  const list = ref({})
  const dealDetail = ref({})

  const getDeal = () => {
    return new Promise((reject, resolve) => {
      $axios
        .get('crm-deal/')
        .then(function (response) {
          const resp = response.data
          const listOfStage = store.settingsStore().stages.map(stage => stage.code)
          const req = {}

          listOfStage.forEach(stage => {
            req[stage] = []
          })

          resp.forEach(deal => {
            req[deal.stage].push(deal)
          })
          list.value = req

          reject(response)
        })
        .catch(function (error) {
          resolve(error)
        })
    })
  }

  const updateDeal = async(id, dealData = {}) => {
    if (!dealData) dealData = findDealById(id)
    Reflect.deleteProperty(dealData, 'id')
    console.log(dealData);
    return new Promise((reject, resolve) => {
      $axios
        .put(`crm-deal/${id}`, dealData)
        .then(function (response) {
          console.log('yes');
          reject(response)
        })
        .catch(function (error) {
          console.log('no');
          resolve(error)
        })
    })
  }

  const findDealById = (id) => {
    let req = {}
    Object.keys(list.value).forEach((key) => {
      const res = list.value[key].find(deal => deal.id == id)
      if (res) req = res
    })
    return req
  }

  return { list, getDeal, updateDeal, dealDetail, findDealById }
})
