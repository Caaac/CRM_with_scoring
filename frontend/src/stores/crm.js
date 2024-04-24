import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCrmStore = defineStore('crm', () => {
  const visibleTaskSidebar = ref(false)
  
  const stages = ref([
    { name: 'Новая', color: 'red' },
    { name: 'В согласовании', color: 'yellow' },
    { name: 'В очереди', color: 'green' },
    { name: 'В работе', color: 'blue' },
    { name: 'На проверке', color: 'gray' },
    { name: 'Ожидание', color: 'purple' },
    { name: 'Завершена', color: 'red' }
  ])

  const list = ref({
    Новая: [
      { id: 1, TITLE: 'First task', STAGE:'На проверке', COMMENT: ''},
      { id: 2, TITLE: 'Sec task', STAGE:'Новая', COMMENT: '' }
    ],
    'В согласовании': [],
    'В очереди': [{ id: 3, TITLE: 'Fird task', STAGE:'В работе', COMMENT: '' }]
  })

  return {stages, list, visibleTaskSidebar }
})
