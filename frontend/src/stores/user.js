import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const curUser = ref({
    ID: 1,
    NAME: "Alexandr",
    LAST_NAME: "Vedyaev",
    EMAIL: "vedyaev03@mail.ru"
  })


  return { curUser }
})
