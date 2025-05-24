/* Vue */
import { ref } from 'vue'
/* Pinia */
import { defineStore } from 'pinia'
/* Other stores */
import { authStore } from '@/stores/auth'
import { helperStore } from '@/stores/helper'
import { crmStore } from '@/stores/modules/crm/index'
import { settingsStore } from '@/stores/settings/index'

export const rootStore = defineStore('root', () => {

  const pageName = ref('');
  const menuCollapsed = ref(false);

  const setPageName = (name) => { pageName.value = name }

  const crm = () => crmStore();
  const auth = () => authStore();
  const helper = () => helperStore();
  const settings = () => settingsStore();

  return {
    /* Store vars */
    pageName, 
    menuCollapsed,
    /* Store methods */
    setPageName,
    /* Ref to another store */
    crm,
    auth, 
    helper, 
    settings, 
  }
})
