import { defineStore } from 'pinia'
import { useCrmStore } from '@/stores/crm'

export const rootStore = defineStore('root', () => {
  const crmStore = () => {
    return useCrmStore()
  }

  return { crmStore }
})
