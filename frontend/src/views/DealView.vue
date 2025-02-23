<script setup>
/* Stores */
import { rootStore } from '@/stores';
import { onMounted } from 'vue';

const store = rootStore()

onMounted(() => {
  store.crm().deal().getStatus()
})

</script>

<template>
  <div>
    {{ store.crm().deal().test }}
  </div>
</template>

<style lang="scss">

</style>