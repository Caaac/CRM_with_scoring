<script setup>
import SidebarCardGeneral from '@/components/crm/sidebar-card-tabs/SidebarCardGeneral.vue';
import StageBar from '@/components/crm/additions/StageBar.vue';

import { useRouter, useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'

const store = rootStore()
const router = useRouter()
const route = useRoute()

const visibleDealSidebar = ref(true)
const {dealDetail} = storeToRefs(store.crmStore())

onMounted(() => {
  const refreshId = setInterval(() => {
    if (route.params.idDeal != 0){
      store.crmStore().dealDetail = store.crmStore().findDealById(route.params.idDeal)
      clearInterval(refreshId)
    }
  }, 200);
})


const pushBack = () => {
  router.push({ path: '/crm/' })
  store.settingsStore().isLoading = true
  store.crmStore().getDeal()
    .then(r => {
      store.settingsStore().isLoading = false
    })
}

</script>

<template>
  <div class="crm-crm-sidebar-card">
    <Sidebar
      v-model:visible="visibleDealSidebar"
      @hide="pushBack"
      class="crm-side-bar"
      :header="dealDetail.title"
      position="right"
    >
      <Divider class="sidebar-header-divider" />

      <StageBar />

      {{ dealDetail }}
      <div class="card">
        <TabView class="aaa">
          <TabPanel header="Общее">
            <SidebarCardGeneral />
          </TabPanel>
          <TabPanel header="Анализ">
            <SidebarCardAnalitic />
          </TabPanel>
        </TabView>
      </div>
    </Sidebar>
  </div>
</template>

<style>

</style>