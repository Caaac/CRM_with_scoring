<script setup>
import { RouterView } from 'vue-router'
import MainLeftBar from '@/components/MainLeftBar.vue'
import MainTopBar from '@/components/MainTopBar.vue'
import Toast from 'primevue/toast';

</script>

<template>
  <div class="flex w-full">
    <MainLeftBar />

    <main>
      <MainTopBar class="top-menubar" />
      <Divider class="mb-5" />
      <div class="v-main">
        <keep-alive>
          <RouterView />
        </keep-alive>
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
