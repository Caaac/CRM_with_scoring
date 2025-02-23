<script setup>
import Image from "primevue/image";
import { useRouter } from "vue-router";
import { rootStore } from '@/stores/index'

const router = useRouter();
const store = rootStore();
</script>

<template>
  <header>
    <div class="logo-container">
      <Image
        v-if="!store.settings().menuCollapsed"
        src="/src/assets/images/HeaderLogo.PNG"
        alt="Image"
        imageClass="logo"
        @click="router.push({ path: '/crm/' })"
      />
    </div>
  </header>
</template>

<style lang="scss">
header {
  position: sticky;
  top: 0px;
  height: 100vh;
  width: var(--header-width);
  background: var(--theme-c-white-bg-frame);
  border-radius: 0 35px 35px 0;
  padding: 10px 10px 20px 10px;
  transition: width .5s ease-in-out;
  overflow: hidden;

  .logo {
    cursor: pointer;
    width: 150px;
    height: auto;
  }
}

.logo-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

</style>
