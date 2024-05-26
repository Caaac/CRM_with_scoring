<script setup>
import SidebarCompanyAbout from '@/components/company/sidebar-company-info/SidebarCompanyAbout.vue'
import SidebarCompanyCreate from '@/components/company/sidebar-company-info/SidebarCompanyCreate.vue'

import { onMounted, ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'

const store = rootStore()
const router = useRouter()
const route = useRoute()

const visibleCompanySidebar = ref(true)
const { companyDetail } = storeToRefs(store.companyStore())

onMounted(() => {
  // TODO За исключением ситуации, когда создается компания
  if (route.params.idCompany != 0)
    store.companyStore().companyDetail = store.companyStore().findCompanyById(route.params.idCompany)
})


const isCreate = computed(() => {
  return route.params.idCompany === '0'
})

const pushBack = () => {
  if (
    route.path.includes('/crm/company/details/') &&
    route.path.indexOf('/crm/company/details/') === 0
  )
    router.push({ path: '/crm/' })
  else if (route.path.includes('/company/') && route.path.indexOf('/company/') === 0)
    router.push({ path: '/company/' })

  store.companyStore().companyDetail = {}
}

watch(route, (to, from) => {
  if (to.params.idCompany > 0) {
    store.companyStore().getCompany()
      .then(r => {
        store.companyStore().companyDetail = store.companyStore().findCompanyById(route.params.idCompany)
      })
  }
})
</script>

<template>
  <div>
    <Sidebar v-model:visible="visibleCompanySidebar" @hide="pushBack" class="crm-side-bar"
      :header="companyDetail?.full_name || 'Создание новой компании'" position="right">
      <Divider class="sidebar-header-divider" />
      <div class="crm-sidebar-about-main">
        <SidebarCompanyCreate v-if="isCreate" />
        <SidebarCompanyAbout v-else />
      </div>
    </Sidebar>
  </div>
</template>

<style></style>