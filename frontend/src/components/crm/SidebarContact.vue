<script setup>
import { onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()
const route = useRoute()

console.log('router', router);
console.log('route', route);
const visibleContactSidebar = ref(true)

console.log(route.path.indexOf('/contact/'));
// /crm/contact/
const pushBack = () => {
  if (route.path.includes('/crm/contact/') && route.path.indexOf('/crm/contact/') === 0)
    router.push({ path: '/crm/' })
  else if (route.path.includes('/contact/') && route.path.indexOf('/contact/') === 0) 
    router.push({ path: '/contact/' })
}

onMounted(() => {

})

</script>

<template>
  <div>
    <Sidebar v-model:visible="visibleContactSidebar" @hide="pushBack" class="crm-side-bar" header="wedwed"
      position="right">
      {{ route }}
    </Sidebar>
  </div>
</template>

<style></style>