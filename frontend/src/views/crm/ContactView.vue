<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

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
  <div>
    Contact

    <pre>{{ menuItems }}</pre>

    ///

    <pre>{{ router.options.routes }}</pre>

    <RouterView />
  </div>
</template>

<style lang="scss">

</style>