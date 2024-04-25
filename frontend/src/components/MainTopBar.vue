<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()


const pageTitle = () => {
  return route.meta?.title || '&'
}

const gg = () => {
  console.log('1')
}

const profileMenu = ref()
const toggleProfileMenu = (event) => {
  profileMenu.value.toggle(event)
}

const settingsMenu = ref()
const toggleSettingsMenu = (event) => {
  settingsMenu.value.toggle(event)
}

const accountMenu = ref([
  {
    label: 'Персональный раздел',
    items: [
      {
        label: 'Личный кабинет',
        icon: 'mdi mdi-account',
        command: () => {
          router.push({ path: '/user/account/' })
        }
      },
      {
        label: 'Выйти',
        icon: 'mdi mdi-exit-to-app'
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
  <Menubar class="mt-2">
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
          @click="toggleProfileMenu"
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
        <Menu ref="profileMenu" id="crm-profile-menu" :model="accountMenu" :popup="true" />

        <Button
          @click="toggleSettingsMenu"
          icon="mdi mdi-cog-outline crm-menubar-btn"
          text
          rounded
          aria-label="Filter"
          aria-haspopup="true"
          aria-controls="crm-settings-menu"
        />
        <Menu ref="settingsMenu" id="crm-settings-menu" :model="items2" :popup="true" />

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
.p-menubar {
  background-color: inherit;
}
</style>