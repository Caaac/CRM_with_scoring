import { defineStore } from "pinia";
import { ref, computed, inject } from "vue";

export const dealStore = defineStore("deal", () => {
  // const $axios = inject('$axios')

  const deal_fields = ref([])
  const deal_detail = ref({})
  const params = ref({})
  const loading = ref({
    deal_detail: false,
  })

  const statusType = computed(() => {
    const userStatus = []
    const sysStatus = []

    Object.entries(params.value?.stage_data || {}).forEach(([stageKey, stageData]) => {
      if (stageData.status_data.system_status == 1 && stageData.status_data.sort == 0) {
        sysStatus.push(stageData)
      } else {
        userStatus.push(stageData)
      }
    });

    return {
      userStatus,
      sysStatus
    }
  })

  const init = (displayMode = '') => {
    Rest.callMethod('crm.deal.init.kanban', {}, (response) => {
      params.value = response.data
    })
  }

  const getDealDetail = async (id, load = true) => {
    loading.value.deal_detail = load
    return new Promise((resolve, reject) => {
      Rest.callMethod('crm.deal.detail.get', { id: id }, (response) => {
        if (response.data.result == false) reject(response.data)
        deal_detail.value = response.data
        loading.value.deal_detail = false
        resolve(response.data)
      })
    })
  }

  const updateDeal = (id, data, updateDeals = false, updateDetail = false) => {
    Rest.callMethod('crm.deal.update', { id: id, data: data }, (response) => {
      console.log('crm.deal.update', response);

      if (updateDeals) {
        init()
      }
      if (updateDetail) {
        getDealDetail(id, false)
      }
    })
  }

  const updateDealDetail = (id, data, updateDeals = false, updateDetail = false) => {
    Rest.callMethod('crm.deal.detail.update', { id: id, data: data }, (response) => {
      console.log('crm.deal.detail.update', response);

      if (updateDeals) init()
      if (updateDetail) getDealDetail(id, false)

    })
  }

  const createDeal = async (data, updateDeals = false, updateDetail = false) => {
    return new Promise((resolve, reject) => {
      Rest.callMethod('crm.deal.detail.add', { data: data }, (response) => {
        console.log(response.data);
        
        if (response.status == 'error') reject(response.data)

        if (updateDeals) init()
        if (updateDetail) getDealDetail(response.data.data.id, false)

        resolve(response.data)
      })
    })
  }

  return { params, deal_detail, deal_fields, init, getDealDetail, loading, statusType, updateDeal, updateDealDetail, createDeal };
});
