import { ref, inject } from 'vue'
import { defineStore } from 'pinia'
import { data } from 'autoprefixer'

export const useSettingsStore = defineStore('settings', () => {
  const $axios = inject('$axios')

  const isLoading = ref(true)

  // CRM
  const stages = ref([])
  const source = ref([])

  const getStages = () => {
    return new Promise((reject, resolve) => {
      $axios
        .get('settings/stages/')
        .then(function (response) {
          stages.value = response.data
          reject(response)
        })
        .catch(function (error) {
          resolve(error)
        })
    })
  }

  const getSource = () => {
    return new Promise((reject, resolve) => {
      $axios
        .get('settings/source/')
        .then(function (response) {
          source.value = response.data
          reject(response)
        })
        .catch(function (error) {
          resolve(error)
        })
    })
  }

  return { isLoading, stages, getStages, source, getSource }
})
