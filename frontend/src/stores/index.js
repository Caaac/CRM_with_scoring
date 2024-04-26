import { defineStore } from 'pinia'
import { useCrmStore } from '@/stores/crm'
import { useUserStore } from '@/stores/user'
import { useContactStore } from '@/stores/contact'
import { useSettingsStore } from '@/stores/settings'

export const rootStore = defineStore('root', () => {
  const crmStore = () => {
    return useCrmStore()
  }

  const userStore = () => {
    return useUserStore()
  }

  const contactStore = () => {
    return useContactStore()
  }

  const settingsStore = () => {
    return useSettingsStore()
  }

  return { crmStore, userStore, contactStore, settingsStore }
})
