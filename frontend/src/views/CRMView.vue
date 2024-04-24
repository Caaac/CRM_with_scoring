<script setup>
import { onActivated, onMounted, ref } from 'vue'
import { rootStore } from '@/stores'; const store = rootStore()
import { storeToRefs } from 'pinia';
import SidebarCard from '@/components/crm/SidebarCard.vue'

const { stages, list, visibleTaskSidebar } = storeToRefs(store.crmStore())
const crmStyles = ref({ width: '' })
const selectedTask = ref({})

const selecteTask = (task) => {
  visibleTaskSidebar.value = true
  selectedTask.value = task
}

onMounted(() => {
  if (window.innerWidth == 1920 || window.innerWidth == 1872) {
    crmStyles.value.width = '1580px'
  } else if (window.innerWidth == 1536) {
    crmStyles.value.width = '1200px'
  } else if (window.innerWidth == 1318) {
    crmStyles.value.width = '1000px'
  }
  console.log(window.innerWidth)
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
          <div class="crm-crm-card-wrapper">
            <div class="crm-crm-card-title" @click="selecteTask(card)">{{ card.TITLE }}</div>
            <div class="mt-2"><Tag :value="card.STAGE" /></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <SidebarCard :selectedTask="selectedTask" />
</template>

<style>
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

.crm-crm-card-title {
  cursor: pointer;
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

.crm-crm-card-wrapper {
  padding: 10px 15px;
}

.p-card {
  width: 280px;
  margin: 5px;
}

.crm-side-bar {
  width: 80%;
}
</style>