import { defineStore } from 'pinia'
import { ref } from 'vue'
/* Other stores */
import { helperStore } from '@/stores/helper'
import { crmStore } from '@/stores/modules/crm/index'
import { settingsStore } from '@/stores/settings/index'

export const rootStore = defineStore('root', () => {

  const pageName = ref('');
  const menuCollapsed = ref(false);

  const setPageName = (name) => { pageName.value = name }

  const crm = () => crmStore();
  const settings = () => settingsStore();
  const helper = () => helperStore();

  return {menuCollapsed, crm, settings, helper, pageName, setPageName}
})
