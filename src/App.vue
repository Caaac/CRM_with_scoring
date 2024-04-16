<script setup>
import { RouterView } from 'vue-router'
import MainLeftBar from '@/components/MainLeftBar.vue'
import MainTopBar from '@/components/MainTopBar.vue'
</script>

<template>
  <div class="flex w-full">
    <MainLeftBar />
    <!-- <Sidebar v-model:visible="visibleRight" header="Right Sidebar" position="right">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat.
      </p>
    </Sidebar> -->
    <main>
      <MainTopBar class="top-menubar" />

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
  background-color: #f2f4f6;
}

.v-main {
  flex: 1 1 auto;
  max-width: 100%;
}
</style>
