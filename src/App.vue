<script setup>
import { RouterView } from 'vue-router'
import MainLeftBar from '@/components/MainLeftBar.vue'
</script>

<template>
  <div class="flex w-full">
    <MainLeftBar />

    <main>
      <keep-alive>
        <RouterView />
      </keep-alive>
    </main>
  </div>

</template>

<style scoped>
main {
  width: 100%;
  padding: 0 40px 0 30px;
}
</style>
