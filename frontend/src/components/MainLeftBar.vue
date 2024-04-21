<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const routeNav = () =>
  router.options.routes.reduce((acc, route) => {
    const title = route.meta?.title
    if (title) {
      acc.push({
        path: route.path,
        icon: route.meta?.icon ?? 'mdi mdi-atom',
        title
      })
    }
    return acc
  }, [])
</script>

<template>
  <header>
    <div class="crm-header-wrapper">
      <Image
        src="/src/assets/GSlogoHC.png"
        alt="Image"
        imageClass="crm-logo w-full mx-auto mt-6 mb-6"
      />

      <Menu :model="routeNav()" class="w-full">
        <template #submenuheader="{ item }">
          <span class="text-primary font-bold">{{ item.title }}</span>
        </template>
        <template #item="{ item, props }">
          <div
            v-ripple
            class="crm-nav-link ml-6"
            @click.prevent="router.push(item)"
            v-bind="props.action"
          >
            <span class="mdi" :class="item.icon" />
            <span class="ml-2">{{ item.title }}</span>
            <!-- <Badge v-if="item.badge" class="ml-auto" :value="item.badge" /> -->
          </div>
        </template>
        <template #end>
          <button
            v-ripple
            class="relative overflow-hidden w-full p-link flex align-items-center p-2 pl-3 text-color hover:surface-200 border-noround"
          >
            <Avatar
              image="https://primefaces.org/cdn/primevue/images/avatar/asiyajavayant.png"
              class="mr-2"
              shape="circle"
            />
            <span class="inline-flex flex-column">
              <span class="font-bold">Amy Elsner</span>
              <span class="text-sm">Admin</span>
            </span>
          </button>
        </template>
      </Menu>
    </div>
  </header>
</template>

<style scoped>
header {
  box-shadow: 0 0 20px 5px rgba(194, 194, 194, 0.2);
}

.crm-header-wrapper {
  width: 250px;
  position: sticky;
  top: 0;
  height: 100vh;
  z-index: 10000;
}

.crm-nav-link {
  font-size: var(--fs-header-desctop);
  color: #293241cc !important;
  /* #293241cc */
}

.crm-nav-link span.mdi {
  margin-right: 3px;
  font-size: 20px;
}

@media (max-width: 1536px) {
  .crm-nav-link {
    font-size: var(--fs-header-laptop);
  }
}
</style>
