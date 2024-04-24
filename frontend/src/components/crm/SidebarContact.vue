<script setup>
import { onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()
const route = useRoute()

console.log('router', router);
console.log('route', route);
const visibleTaskSidebar = ref(true)

const pushBack = () => {
  router.push({ path: '/contact/' })
}

onMounted(() => {

})

</script>

<template>
  <div>
    <Sidebar v-model:visible="visibleTaskSidebar" @hide="pushBack" class="crm-side-bar" header="wedwed"
      position="right">
      eded
    </Sidebar>
  </div>
</template>

<style></style>