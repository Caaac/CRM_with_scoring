import { defineStore } from 'pinia'
import { useCrmStore } from '@/stores/crm'
import { useUserStore } from '@/stores/user'
import { useContactStore } from '@/stores/contact'
import { useCompanyStore } from '@/stores/company'
import { useSettingsStore } from '@/stores/settings'
import { useLandingRateStore } from '@/stores/landingRate'

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

  const companyStore = () => {
    return useCompanyStore()
  }

  const landingRateStore = () => {
    return useLandingRateStore()
  }

  return { crmStore, userStore, contactStore, settingsStore, companyStore, landingRateStore }
})
