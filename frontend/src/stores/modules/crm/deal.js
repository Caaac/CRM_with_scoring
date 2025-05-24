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
    // const cmd = {};
    // cmd['status'] = ['crm.status.get', {}];
    // cmd['deals'] = ['crm.deal.get', {}];

    // Rest.callBatch(cmd, (response) => {
    //   console.log(response);
    //   Object.keys(response).forEach(key => {
    //     params.value[key] = response[key].data
    //   })
    // })

    Rest.callMethod('crm.deal.init.kanban', {}, (response) => {
      params.value = response.data
    })
  }

  const getDealDetail = (id, load = true) => {
    loading.value.deal_detail = load
    Rest.callMethod('crm.deal.detail.get', {id: id}, (response) => {
      deal_detail.value = response.data
      console.log(response);
      loading.value.deal_detail = false
    })
  }

  const updateDeal = (id, data, updateDeals = false, updateDetail = false) => {
    Rest.callMethod('crm.deal.update', {id: id, data: data}, (response) => {
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
    console.log('pre crm.deal.detail.update', {id: id, data: data});
    
    Rest.callMethod('crm.deal.detail.update', {id: id, data: data}, (response) => {
      console.log('crm.deal.detail.update', response);
      if (updateDeals) {
        init()
      }
      if (updateDetail) {
        getDealDetail(id, false)
      }
    })
  }

  return { params, deal_detail, deal_fields, init, getDealDetail, loading, statusType, updateDeal, updateDealDetail};
});
