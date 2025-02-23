import { defineStore } from 'pinia'
import { ref } from 'vue'
/* Other stores */
import {settingsStore} from '@/stores/settings'
import { crmStore } from '@/stores/modules/crm/index'

export const rootStore = defineStore('root', () => {

  const crm = () => crmStore();
  const settings = () => settingsStore();

  return {crm, settings}
})
