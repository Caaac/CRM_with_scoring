<script setup>
/* PrimeVue components */
import Button from "primevue/button";
/* Icons */
import MenuOpen from "@/assets/icons/MenuOpen.vue";
import MenuClose from "@/assets/icons/MenuClose.vue";
import { rootStore } from "@/stores/index";

const store = rootStore()

</script>

<template>
  <div class="pl-top-container">
    <div class="pl-top-container-wrapper pl-top-container-wrapper-1">
      <Button @click="store.settings().menuCollapsed = !store.settings().menuCollapsed" severity="secondary" variant="text" rounded aria-label="Bookmark">
        <template #icon>
          <MenuOpen class="pl-icon" />
        </template>
      </Button>

      <div class="pl-breadcrumbs">CRM</div>
    </div>
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
