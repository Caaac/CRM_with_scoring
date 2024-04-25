import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCrmStore = defineStore('crm', () => {
  const stages = ref([
    { name: 'Новая', color: '#3ff26b' },
    { name: 'В согласовании', color: '#12c317', textColor: 'white' },
    { name: 'В очереди', color: '#8ad79f' },
    { name: 'В работе', color: '#ace9fb' },
    { name: 'На проверке', color: '#8c3f87', textColor: 'white' },
    { name: 'Завершена', color: '#5e36a0', textColor: 'white' },
  ])

  const list = ref({
    Новая: [
      { id: 1, TITLE: 'First task', STAGE:'На проверке', COMMENT: ''},
      { id: 2, TITLE: 'Sec task', STAGE:'Новая', COMMENT: '' }
    ],
    'В согласовании': [],
    'В очереди': [{ id: 3, TITLE: 'Fird task', STAGE:'В работе', COMMENT: '' }]
  })

  return {stages, list }
})
