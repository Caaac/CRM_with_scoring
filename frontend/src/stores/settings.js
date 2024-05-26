import { ref, inject } from 'vue'
import { defineStore } from 'pinia'
import { data } from 'autoprefixer'

export const useSettingsStore = defineStore('settings', () => {
  const $axios = inject('$axios')

  const isLoading = ref(true)
  const isAuth = ref(false)

  // CRM
  const stages = ref([])
  const source = ref([])
  const loan_duration = ref([
    { name: '6 месяцев', month: 6 },
    { name: '1 год', month: 12 },
    { name: '1.5 года', month: 18 },
    { name: '2 года', month: 24 },
    { name: '2.5 года', month: 30 },
    { name: '3 года', month: 36 },
    { name: '3.5 года', month: 42 },
    { name: '4 года', month: 48 },
    { name: '4.5 года', month: 54 },
    { name: '5 лет', month: 60 },
  ])

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

  return { isLoading, stages, getStages, source, getSource, loan_duration, isAuth }
})
