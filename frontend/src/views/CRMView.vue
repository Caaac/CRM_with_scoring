<script setup>
import { onActivated, computed, onMounted, ref } from 'vue'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'
import { RouterView, useRouter } from 'vue-router'
import { useToast } from 'primevue/usetoast'

const store = rootStore()
const router = useRouter()
const toast = useToast()

const { stages } = storeToRefs(store.settingsStore())
const { list } = storeToRefs(store.crmStore())
const crmStyles = ref({ width: '' })

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
  const prevSatge = card.stage
  card.stage = stageName

  if (prevSatge == stageName) return false

  if (stageName == 'END') card.date_closed = new Date().format('yyyy-mm-dd')
  else card.date_closed = null

  store.crmStore().updateDeal(card.id, card)
    .then((result) => {
      // Из-за реактивности id удаляется и его нужно восстановить
      card.id = result.data.id
      if (list.value[stageName].some((crd) => crd.id == card.id)) return false
      list.value[prevSatge] = list.value[prevSatge].filter((el) => el.id != card.id)
      if (!list.value[stageName]) list.value[stageName] = []
      list.value[stageName].push(card)
    }).catch((err) => {
      card.stage = prevSatge
      alertOfError('Стадия задачи не изменена', 'Во время изменения стадии произошла ошибка')
    });
}

const cardTitel = (title) => {
  if (title.length > 33)
    return title.slice(0, 30) + '...'
  return title
}

const totalAmount = (stageName) => list.value[stageName]?.reduce((acc, curr) => acc + curr.loan_amount, 0)
const getContact = (card) => {
  // if (card.client) {
  //   const company = store.companyStore().companies.find(c => c.id == card.company)
  //   return 1
  // }
  return 'Ануфриев Алексей' 
  return 'Пользователь не найден'
}
const getCompany = (card) => {
  if (card.company) {
    const company = store.companyStore().companies.find(c => c.id == card.company)
    return company.full_name
  }
  return 'Компания не найдена'
}

const getAvatarLable = (responsible) => {
  const resp = store.userStore().managers.find(mg => mg.id == responsible)
  return resp.name.slice(0, 1) + resp.last_name.slice(0, 1)
}

const alertOfError = (summary = '', detail = '') => {
  toast.add({
    severity: 'error',
    summary: summary,
    detail: detail,
    life: 3000
  })
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
      <div class="crm-crm-stage-title" :style="{ 'background-color': stage.color, color: stage?.textColor }">
        {{ stage.name }}
      </div>
      <div class="crm-crm-total-amount">
        <div class="crm-crm-total-amount-wrapper">
          {{ totalAmount(stage.code) }} ₽
        </div>
      </div>
      <div class="crm-crm-create">
        <div class="crm-crm-create-wrapper">
          <span class="mdi mdi-plus-circle-outline"></span>
        </div>
      </div>
      <div v-if="list" class="crm-crm-cards-block" @drop="onDrop($event, stage.code)" @dragover.prevent
        @dragenter.prevent>
          <div v-for="card in list[stage.code]" :key="card.id" class="crm-crm-card" draggable="true"
            @dragstart="onDragstart($event, card)">
            <div class="crm-crm-card-wrapper">
              <div class="crm-crm-card-title" @click="router.push({ path: `/crm/${card.id}/` })">
                {{ cardTitel(card.title) }}
              </div>
              <div class="crm-crm-card-price">{{ card.loan_amount }} ₽</div>
              <div v-if="card.contant" class="crm-crm-card-client" @click="router.push({ path: `contact/details/${card.contant}/` })">{{ getContact(card) }}</div>
              <div v-else-if="card.company" class="crm-crm-card-client" @click="router.push({ path: `company/details/${card.company}/` })">{{ getCompany(card) }}</div>
              <div class="flex items-center justify-between mt-2">
                <Avatar :label="getAvatarLable(card.responsible)" class="" shape="circle" style="background-color: #ece9fc; color: #2a1261; font-size:14px" />
                <div><Tag :value="card.stage" /></div>
              </div>
            </div>
          </div>
      </div>
    </div>
  </div>
  <!-- <SidebarCard :selectedTask="selectedTask" /> -->
  <RouterView />
</template>

<style>
.crm-crm-main-block {
  overflow-x: auto;
  white-space: nowrap;
  height: 100%;
  min-height: 100%;
  display: flex;
}

.crm-crm-card-wrapper .p-avatar:hover {
  scale: 1.05;
}

.crm-crm-stage-block {
  width: 100%;
  /* min-width: 270px; */
  max-width: 300px;
  height: 100%;
  /* min-height: 100%; */
  /* overflow-y: scroll; */
  border-radius: 0 16px 16px 0;
}

.crm-crm-stage-title {
  border-radius: inherit;
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  white-space: normal;
}

.crm-crm-card {
  width: 250px;
  margin: 5px;
  background-color: white;
}

.crm-crm-card:hover {
  margin-top: 3px;
  margin-bottom: 7px;
}

.crm-crm-card-title {
  cursor: pointer;
  font-size: 15px;
  font-weight: bold;
  color: #3a4963;
  white-space: normal;
}

.crm-crm-card-title:hover {
  color: #1853b9;
}

.crm-crm-card-price {
  font-size: 14px;
  color: #535c6a;
}

.crm-crm-card-client {
  font-size: 14px;
  font-weight: 500;
  color: #4620b0;
  cursor: pointer;
}

.crm-crm-card-client:hover {
  text-decoration: underline;
}

.crm-crm-cards-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 100vh;
  overflow-y: scroll;
  margin-bottom: 10px;
}

.crm-crm-total-amount,
.crm-crm-cards-block,
.crm-crm-create {
  border: 1px dashed rgba(72, 72, 72, 0.581);
  border-top: none;
  border-bottom: none;
  /* border-right: none; */
}

.crm-crm-total-amount {
  width: 100%;
  display: flex;
  justify-content: center;
}

.crm-crm-total-amount-wrapper {
  margin-top: 5px;
  margin-bottom: 7px;
  background-color: rgb(183, 201, 250);
  width: 80%;
  text-align: center;
  border-radius: 16px;
}

.crm-crm-create {
  display: none;
  justify-content: center;
  transition: display .5s;
}

.crm-crm-stage-block:hover + .crm-crm-create,
.crm-crm-total-amount:hover + .crm-crm-create,
.crm-crm-create:hover  {
  display: flex;
}

.crm-crm-create-wrapper {
  width: 80%;
  height: 30px;
  background-color: #c2d2e48e;
  border-radius: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: -10px 0 -10px 0;
}

.crm-crm-create-wrapper span {
  font-size: 25px;
}

.crm-crm-card-wrapper {
  padding: 10px 15px;
  height: 100%;
  width: 100%;
}

.p-card {
  width: 280px;
  margin: 5px;
}

.crm-side-bar {
  width: 80%;
}
</style>