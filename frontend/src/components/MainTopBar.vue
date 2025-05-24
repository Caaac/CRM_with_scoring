<script setup>
/* PrimeVue components */
import Button from "primevue/button";
import Popover from 'primevue/popover';
import TieredMenu from 'primevue/tieredmenu';
/* Icons */
import MenuOpen from "@/assets/icons/MenuOpen.vue";
import MenuClose from "@/assets/icons/MenuClose.vue";
/* Vue */
import { ref } from "vue";
/* Vue Router */
import { useRouter } from "vue-router";
/* Store */
import { rootStore } from "@/stores/index";

const store = rootStore();
const router = useRouter();

const menuPopover = ref(null)

const menuItems = ref([
  {
    label: 'Настройка модуля',
    icon: 'pi pi-file',
    items: [
      {
        label: 'CRM',
        icon: 'pi pi-plus',
        items: [
          {
            label: 'Пользовательские поля',
            icon: 'pi pi-plus',
            command: () => {
              router.push({ path: '/settings/user-field/deal/' })
            }
          },
          {
            label: 'Стадии',
            icon: 'pi pi-plus',
            command: () => {
              router.push({ path: '/settings/kanban/stages/' })
            }
          }
        ]
      }
    ]
  },
  {
    separator: true
  },
  {
    label: 'Sync',
    icon: 'pi pi-cloud',
  }
]);

</script>

<template>
  <div class="pl-top-container">
    <div class="pl-top-container-wrapper">
      <Button @click="store.menuCollapsed = !store.menuCollapsed" severity="secondary" variant="text" rounded
        aria-label="Bookmark">
        <template #icon>
          <MenuOpen class="pl-icon" />
        </template>
      </Button>
      <div class="pl-breadcrumbs">CRM</div>
    </div>
    <div class="pl-top-container-wrapper">
      <Button @click="(event) => { menuPopover.toggle(event) }" severity="secondary" variant="text" rounded
        aria-label="Bookmark" aria-controls="overlay_tmenu">
        <template #icon>
          <!-- <MenuOpen class="pl-icon" /> -->
          <span class="pi pi-cog"></span>
        </template>
      </Button>
    </div>
    <TieredMenu :model="menuItems" ref="menuPopover" id="overlay_tmenu" popup />
  </div>
</template>

<style scoped lang="scss">
.pl-icon {
  width: var(--icon-size-3);
  height: var(--icon-size-3);
  transition: rotate .8s;
}

#pl-window.left-manu-collapsed .pl-icon {
  rotate: calc(180deg + 360deg);
}

.pl-top-container {
  width: 100%;
  height: 40px;
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;

  .pl-top-container-wrapper {
    display: flex;
    background: var(--theme-c-white-bg-frame);
    border-radius: 20px;
  }

  .pl-breadcrumbs {
    margin-left: 10px;
    padding-right: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
