import { defineStore } from 'pinia'
import { useCrmStore } from '@/stores/crm'
import { useUserStore } from '@/stores/user'

export const rootStore = defineStore('root', () => {
  const crmStore = () => {
    return useCrmStore()
  }

  const userStore = () => {
    return useUserStore()
  }

  return { crmStore, userStore }
})
