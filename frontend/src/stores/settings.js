import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useSettingsStore = defineStore('settings', () => {
  // const isLoading = ref(true) // TODO
  const isLoading = ref(false)

  return { isLoading }
})
