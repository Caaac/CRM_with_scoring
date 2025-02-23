import { defineStore } from 'pinia'
import { ref } from 'vue'

export const settingsStore = defineStore('settings', () => {

  const menuCollapsed = ref(false);

  return {menuCollapsed}
})
