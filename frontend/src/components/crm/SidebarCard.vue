<script setup>
// import Sidebar from "primevue/sidebar"
import { rootStore } from '@/stores'; const store = rootStore()
import { storeToRefs } from 'pinia';

const { visibleTaskSidebar } = storeToRefs(store.crmStore())

const props = defineProps(['selectedTask'])

</script>

<template>
  <div>
    <Sidebar
      v-model:visible="visibleTaskSidebar"
      class="crm-side-bar"
      :header="selectedTask.TITLE"
      position="right"
    >
      {{ selectedTask }}
    </Sidebar>
  </div>
</template>

<style></style>