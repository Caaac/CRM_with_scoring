<script setup>
import { RouterView } from 'vue-router'
import { onMounted } from 'vue';
import { rootStore } from '@/stores'

import MainLeftBar from '@/components/MainLeftBar.vue'
import MainTopBar from '@/components/MainTopBar.vue'
import Toast from 'primevue/toast'

const store = rootStore()

onMounted(() => {
  Promise.all([
    store.settingsStore().getStages(),
    store.settingsStore().getSource(),
  ])
    .then(_ => Promise.all([
      store.companyStore().getCompany(),
      store.landingRateStore().getLandingRate(),
      store.crmStore().getDeal(),
    ])
    )
    .then(r => {
      store.settingsStore().isLoading = false
    })

})

</script>

<template>
  <div class="flex w-full">
    <MainLeftBar />

    <main>
      <MainTopBar class="top-menubar" />
      <Divider class="mb-5" />
      
      <ProgressBar v-if="store.settingsStore().isLoading" mode="indeterminate" style="height: 6px"></ProgressBar>
      <div v-else class="v-main">
        <KeepAliveProps>
          <RouterView />
        </KeepAliveProps>
      </div>
    </main>

    <Toast />
  </div>
</template>

<style scoped>
main {
  width: 100%;
  padding: 0 40px 0 30px;
  background-color: #f2f4f6;
}

.v-main {
  flex: 1 1 auto;
  max-width: 100%;
}
</style>
