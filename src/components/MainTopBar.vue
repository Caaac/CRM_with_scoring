<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const pageTitle = () => {
  const route = useRoute()
  return route.meta?.title || '&'
}

const gg = () => {
  console.log('1')
}

const menu = ref()
const toggle = (event) => {
  menu.value.toggle(event)
}

const items = ref([
  {
    label: 'Options',
    items: [
      {
        label: 'Refresh',
        icon: 'mdi mdi-arrow-left',
        command: () => {
          console.log('222')
        }
      },
      {
        label: 'Export',
        icon: 'mdi mdi-arrow-left'
      }
    ]
  }
])

const items2 = ref([
  {
    label: 'Options',
    items: [
      {
        label: 'Refresh',
        icon: 'mdi mdi-arrow-left',
        command: () => {
          console.log('222')
        }
      },
      {
        label: 'Export',
        icon: 'mdi mdi-arrow-left'
      }
    ]
  }
])
</script>

<template>
  <Menubar>
    <template #start>
      <div class="flex items-center">
        <Button
          icon="mdi mdi-blur-linear crm-menubar-btn"
          @click="gg"
          rounded
          outlined
          aria-label="Filter"
        />
        <p class="ml-5 opacity-80">{{ pageTitle() }}</p>
      </div>
    </template>
    <template #end>
      <div class="flex align-items-center gap-2">
        <Button
          @click="toggle"
          icon="mdi mdi-cog-outline crm-menubar-btn"
          text
          rounded
          aria-label="Filter"
          aria-haspopup="true"
          aria-controls="crm-profile-menu"
        >
          <Avatar
            image="https://primefaces.org/cdn/primevue/images/avatar/asiyajavayant.png"
            shape="circle"
          />
        </Button>
        <Menu ref="menu" id="crm-profile-menu" :model="items2" :popup="true" />

        <Button
          @click="toggle"
          icon="mdi mdi-cog-outline crm-menubar-btn"
          text
          rounded
          aria-label="Filter"
          aria-haspopup="true"
          aria-controls="crm-settings-menu"
        />
        <Menu ref="menu" id="crm-settings-menu" :model="items" :popup="true" />

        <Button
          icon="mdi mdi-arrow-left crm-menubar-btn"
          @click="gg"
          text
          rounded
          aria-label="Filter"
        />
      </div>
    </template>
  </Menubar>
</template>

<style scoped>
</style>