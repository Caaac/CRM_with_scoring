import { defineStore } from 'pinia'
import { ref } from 'vue'
import { userFieldStore } from './user-field.js'

export const settingsStore = defineStore('settings', () => {

  const userField = () => userFieldStore();

  return {userField}
})
