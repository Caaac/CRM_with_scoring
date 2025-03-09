<script setup>
/* Router */
import { useRoute, useRouter } from "vue-router";

const props = defineProps(["items"]);

const route = useRoute();
const router = useRouter();
</script>

<template>
  <div id="module-menu">
    <div class="module-menu-container">
      <div
        v-for="item in props.items"
        :key="item"
        @click="router.push({ path: item.path })"
        :class="{ active: route.path.includes(item.name) }"
        class="menu-item"
      >
        {{ item.title }}
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#module-menu {
  width: 100%;
  height: var(--module-menu-height);
  margin-bottom: var(--margine-bottom-1);
  background: var(--theme-c-white-bg-frame);
  border-radius: calc(var(--module-menu-height) / 2);

  .module-menu-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    height: 100%;
    border-radius: inherit;
    padding: 5px;

    .menu-item {
      width: auto;
      min-width: var(--header-item-min-width);
      height: 100%;
      display: flex;
      font-weight: 600;
      justify-content: center;
      align-items: center;
      color: var(--header-title-color);
      border-right: 1px solid rgb(240, 240, 240);
    }

    .menu-item:hover {
      cursor: pointer;
      background: var(--header-item-bg-hover);
      color: var(--header-title-color-hover);
      border-right: 1px solid rgb(240, 240, 240);
    }

    .menu-item:first-child:hover {
      border-top-left-radius: calc(var(--module-menu-height) / 2) !important;
      border-bottom-left-radius: calc(var(--module-menu-height) / 2) !important;
      border-top-right-radius: 0px;
      border-bottom-right-radius: 0px;
    }

    .menu-item:last-child:hover {
      border-top-left-radius: 0px;
      border-bottom-left-radius: 0px;
    }

    .menu-item.active {
      color: #395a80; // TODO
    }
  }
}
</style>
