<script setup>
import { onActivated, onMounted, ref } from 'vue'

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

let crmStyles = ref({ width: '' })

onMounted(() => {
  if (window.innerWidth == 1920) {
    crmStyles.value.width = '1580px'
  } else if (window.innerWidth == 1536) {
    crmStyles.value.width = '1200px'
  }
})

const onDragstart = (e, card) => {
  e.dataTransfer.dropEffect = 'move'
  e.dataTransfer.effectAllowed = 'move'
  e.dataTransfer.setData('card', JSON.stringify(card))
}

const onDrop = (e, stageName) => {
  const card = JSON.parse(e.dataTransfer.getData('card'))

  if (list.value[stageName].some((crd) => crd.id == card.id)) return false

  Object.keys(list.value).forEach((key) => {
    list.value[key] = list.value[key].filter((el) => el.id != card.id)
  })

  if (!list.value[stageName]) list.value[stageName] = []

  list.value[stageName].push(card)
}

// Попытки автоматизировать расширение
// const mainBlock = ref(null)

// const onResizeLister = () => {
//   crmStyles.value.width = mainBlock.value.offsetWidth + 'px'
//   console.log('resize', crmStyles.value)
// }

// onActivated(() => {
//   onResizeLister()
//   console.log('onActivated')
// })
</script>

<template>
  <div class="crm-crm-main-block" ref="mainBlock" :style="crmStyles">
    <div v-for="stage in stages" :key="stage.name" class="crm-crm-stage-block">
      <div class="crm-crm-stage-title" :style="{ 'background-color': stage.color }">
        {{ stage.name }}
      </div>
      <div
        class="crm-crm-cards-block"
        @drop="onDrop($event, stage.name)"
        @dragover.prevent
        @dragenter.prevent
      >
        <div
          v-for="card in list[stage.name]"
          :key="card.id"
          class="crm-crm-card"
          draggable="true"
          @dragstart="onDragstart($event, card)"
        >
          <div class="crm-crm-card-title">{{ card.name }}</div>
          <br /><br /><br />
          <Button>Press</Button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.crm-crm-main-block {
  overflow-x: auto;
  white-space: nowrap;
  height: 100%;
  min-height: 100%;
  display: flex;
}

.crm-crm-stage-block {
  min-width: 300px;
  width: 100%;
  height: 100%;
  min-height: 100%;
  border-radius: 0 16px 16px 0;
}

.crm-crm-stage-title {
  border-radius: inherit;
  text-align: center;
  font-size: 16px;
  font-weight: 600;
}

.crm-crm-cards-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  min-height: 100vh;
  border: 1px dashed rgba(72, 72, 72, 0.581);
  border-top: none;
  border-bottom: none;
  border-right: none;
}

.p-card {
  width: 280px;
  margin: 5px;
}
</style>