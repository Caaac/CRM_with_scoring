import { ref } from 'vue'
import { defineStore } from 'pinia'
/* Other stores */
import { stageStore } from './stage.js'
import { userFieldStore } from './user-field.js'

export const settingsStore = defineStore('settings', () => {

  const stage = () => stageStore();
  const userField = () => userFieldStore();

  return { stage, userField }
})
