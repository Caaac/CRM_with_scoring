<script setup>
import { RouterView } from 'vue-router'
import MainLeftBar from '@/components/MainLeftBar.vue'
import MainTopBar from '@/components/MainTopBar.vue'
</script>

<template>
  <div class="flex w-full">
    <MainLeftBar />

    <main class="mt-2">
      <MainTopBar />

      <Divider class="mb-5" />

      <div class="v-main">
        <keep-alive>
          <RouterView />
        </keep-alive>
      </div>
    </main>
  </div>
</template>

<style scoped>
main {
  width: 100%;
  padding: 0 40px 0 30px;
}
.v-main {
  flex: 1 1 auto;
  max-width: 100%;
}

.p-menu,
.p-menubar {
  border: none !important;
}

.p-menubar {
  justify-content: space-between;
}
</style>
