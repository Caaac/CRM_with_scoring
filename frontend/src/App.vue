<script setup>
/* PrimeVue components */
import Toast from "primevue/toast";
/* Custom components */
import Header from '@/components/MainLeftBar.vue'
import MainTopBar from '@/components/MainTopBar.vue';
import Login from '@/components/auth/Login.vue';
/* Store */
import { rootStore } from './stores';
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'

const store = rootStore()

</script>

<template>
  <div v-if="store.auth().isAuth" id="pl-window" :class="{ 'left-manu-collapsed': store.menuCollapsed }">
    <Header />
    <div id="pl-container">
      <MainTopBar />
      <RouterView />
    </div>
  </div>
  <Login v-else />
  <Toast />
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
  padding: 10px 30px 0 20px;
  // transition: width 0.5s cubic-bezier(0, 0.42, 0, 0);
}

#pl-window.left-manu-collapsed #pl-container {
  width: calc(100% - var(--header-width-collapsed));
}

#pl-window.left-manu-collapsed header {
  width: var(--header-width-collapsed);
}
</style>
