<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
import { ref } from 'vue'
import SidebarCardGeneral from '@/components/crm/sidebar-card-tabs/SidebarCardGeneral.vue';

const visibleDealSidebar = ref(true)

const pushBack = () => {
  router.push({ path: '/crm/' })
}
</script>

<template>
  <div class="crm-crm-sidebar-card">
    <Sidebar
      v-model:visible="visibleDealSidebar"
      @hide="pushBack"
      class="crm-side-bar"
      :header="'dede'"
      position="right"
    >
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