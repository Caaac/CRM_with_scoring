import { defineStore } from "pinia";
import { ref, inject } from "vue";

export const dealStore = defineStore("deal", () => {
  const $axios = inject('$axios')

  const params = ref({
    selected_deal: {},
    deals: [],
    status: [],
  })

  const getStatus = async () => {
    const res = await Rest.callMethod(123)
    
    console.log(res);

    // return new Promise((reject, resolve) => {
    //   $axios
    //     .get("api/v1/crm/status/")
    //     .then(function (response) {

    //       console.log(response);

    //       reject(response);
    //     })
    //     .catch(function (error) {
    //       resolve(error);
    //     });
    // });
  };

  return { params, getStatus };
});
