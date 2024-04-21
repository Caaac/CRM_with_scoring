import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCrmStore = defineStore('crm', () => {
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
      { id: 1, name: 'First task' },
      { id: 2, name: 'Sec task' }
    ],
    'В согласовании': [],
    'В очереди': [{ id: 3, name: 'Fird task' }]
  })

  return {stages, list}
})
