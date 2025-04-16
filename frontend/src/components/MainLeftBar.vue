<script setup>
/* PrimeVue components */
import Image from "primevue/image";
/* Vue */
import { useRouter } from "vue-router";
import { computed } from "vue";
/* Store */
import { rootStore } from '@/stores/index'

const router = useRouter();
const store = rootStore();

const menuItems = computed(() => {
  const findItem = (routes) => {
    const items = [];

    routes.forEach(element => {
      if (element.meta && element.meta.display) {
        items.push({...element.meta, name: element.name});
      }

      if (element.children) {
        items.push(...findItem(element.children))
      }
    });

    items.sort((a, b) => a.sort - b.sort);

    return items.deepCopy();
  }

  return findItem(router.options.routes);
})

</script>

<template>
  <header>
    <div class="logo-container">
      <Image v-if="!store.menuCollapsed" src="/src/assets/images/HeaderLogo.PNG" alt="Image" imageClass="logo"
        @click="router.push({ path: '/crm/' })" />
    </div>

    <div class="menu-items">
      <div v-for="item in menuItems" :key="item" class="menu-item">
        <!-- <span class="mdi mdi-application-edit-outline"></span> -->
        <span @click="router.push({ name: item.name })" class="menu-item-title">{{ item.title }}</span>
      </div>
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

  .logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
  }

  .menu-items {
    display: flex;
    flex-direction: column;
    margin-top: 60px;

    .menu-item {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      margin-bottom: 10px;
      color: var(--color-text);

      .menu-item-title {
        font-size: 16px;
        font-weight: 500;
      }
    }

    .menu-item:hover {
      cursor: pointer;
      color: var(--theme-c-indigo);
    }
  }
}
</style>
