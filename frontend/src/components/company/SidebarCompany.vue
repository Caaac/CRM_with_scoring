<script setup>
import { onMounted, ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'

const store = rootStore()
const router = useRouter()
const route = useRoute()

const contactDetail = ref()

console.log('router', router)
console.log('route', route)

const visibleContactSidebar = ref(true)
const isCreate = computed(() => {
  return route.params.idContact === '0'
})

const pushBack = () => {
  if (
    route.path.includes('/crm/contact/details/') &&
    route.path.indexOf('/crm/contact/details/') === 0
  )
    router.push({ path: '/crm/' })
  else if (route.path.includes('/contact/') && route.path.indexOf('/contact/') === 0)
    router.push({ path: '/contact/' })
}

onMounted(() => {
  console.log(route.params.idContact)
  console.log(store.contactStore().findContactById(route.params.idContact))
  contactDetail.value = store.contactStore().findContactById(route.params.idContact)
})
</script>

<template>
  <div>
    <Sidebar
      v-model:visible="visibleContactSidebar"
      @hide="pushBack"
      class="crm-side-bar"
      header="wedwed"
      position="right"
    >
      <div class="crm-contact-about-deal-main">
        <div class="crm-contact-about-deal">
          <div class="crm-contact-about-deal-wrapper">
            {{ contactDetail }}
          </div>
        </div>
      </div>

      <p>{{ isCreate ? 'Новый контакт' : 'Эх нет' }}</p>
      {{ route }}
    </Sidebar>
  </div>
</template>

<style>
.crm-contact-about-deal {
  background: white;
}

.crm-contact-about-deal {
  width: 41%;
  border-radius: 16px;
}

.crm-contact-about-deal-wrapper {
  padding: 10px;
}
</style>