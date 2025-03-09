<script setup>
import { RouterLink, RouterView } from 'vue-router'
/* Custom components */
import Header from '@/components/Header.vue'
import MainTopBar from '@/components/MainTopBar.vue';
/* Store */
import { rootStore } from './stores';

const store = rootStore()

</script>

<template>
  <div id="pl-window" :class="{'left-manu-collapsed': store.settings().menuCollapsed}">
    <Header />
    <div id="pl-container">
      <MainTopBar />
      <RouterView />
    </div>
  </div>
</template>

<style lang="scss">
#app {
  width: 100%;
  height: 100%;
}

#pl-window {
  display: inline-flex;
  width: 100%;
  height: 100%;
}

#pl-container {
  width: calc(100% - var(--header-width));
  // height: 200vh;
  height: 100%;
  padding: 10px 30px 0 20px
}

#pl-window.left-manu-collapsed #pl-container {
  width: calc(100% - var(--header-width-collapsed));
}

#pl-window.left-manu-collapsed header {
  width: var(--header-width-collapsed);
}

</style>
