import { ref, inject } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const $axios = inject('$axios')

  const curUser = ref({
    ID: 1,
    NAME: "Alexandr",
    LAST_NAME: "Vedyaev",
    EMAIL: "vedyaev03@mail.ru"
  })

  const managers = ref([])

  const getManagers = () => {
    return new Promise((reject, resolve) => {
      $axios
        .get('managers/')
        .then(function (response) {
          managers.value = response.data
          reject(response)
        })
        .catch(function (error) {
          resolve(error)
        })
    })
  }

  return { curUser, getManagers, managers }
})
