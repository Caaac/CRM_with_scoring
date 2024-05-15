import { ref, inject } from 'vue'
import { defineStore } from 'pinia'

export const useLandingRateStore = defineStore('landingRate', () => {
    const $axios = inject('$axios')
    const landingRateList = ref([])

    const getLandingRate = () => {
        return new Promise((reject, resolve) => {
          $axios
            .get('landing-rate/')
            .then(function (response) {
                landingRateList.value = response.data
              reject(response)
            })
            .catch(function (error) {
              resolve(error)
            })
        })
      }

    return { landingRateList, getLandingRate}
})
