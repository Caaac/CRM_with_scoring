import { defineStore } from 'pinia'
/* Other stores */
import { dealStore } from '@/stores/modules/crm/deal'

export const crmStore = defineStore('crm', () => {

  const deal = () => dealStore()

  return {deal}
})
