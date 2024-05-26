<script setup>
import { RouterView } from 'vue-router'
import { onMounted, ref } from 'vue';
import { rootStore } from '@/stores'

import MainLeftBar from '@/components/MainLeftBar.vue'
import MainTopBar from '@/components/MainTopBar.vue'
import Toast from 'primevue/toast'

const store = rootStore()

const mode = ref('auth')
const enterData = ref({
  login: '',
  password: ''
})

onMounted(() => {
  Promise.all([
    store.settingsStore().getStages(),
    store.settingsStore().getSource(),
    store.userStore().getManagers(),
  ])
    .then(_ => Promise.all([
      store.companyStore().getCompany(),
      store.landingRateStore().getLandingRate(),
      store.crmStore().getDeal(),
    ])
    )
    .then(r => {
      store.settingsStore().isLoading = false
      store.settingsStore().isAuth = true
    })

})

</script>

<template>
  <div v-if="store.settingsStore().isAuth" class="flex w-full">
    <MainLeftBar />
    <main>
      <MainTopBar class="top-menubar" />
      <Divider class="mb-5" />
      <ProgressBar v-if="store.settingsStore().isLoading" mode="indeterminate" style="height: 6px"></ProgressBar>
      <div v-else class="v-main">
        <KeepAliveProps>
          <RouterView />
        </KeepAliveProps>
      </div>
    </main>
    <Toast />
  </div>

  <div v-else class="crm-auth">
    <div v-if="mode == 'auth'" class="crm-auth-form">
      <Image src="/src/assets/GSlogoHC.png" alt="Image" imageClass="crm-logo mx-auto pt-6 pb-6"
      />
      <div class="crm-input">
        <label>Логин</label>
        <InputText type="text" v-model="enterData.login" />
      </div>
      <div class="crm-input">
        <label>Пароль</label>
        <Password v-model="enterData.password" :feedback="false"  />
      </div>
      <Button>Войти</Button>
    </div>
    <div v-else-if="mode == 'reg'" class="crm-auth-form">
      <Image src="/src/assets/GSlogoHC.png" alt="Image" imageClass="crm-logo mx-auto pt-6 pb-6"
      />
    </div>
  </div>
</template>

<style>
main {
  width: 100%;
  padding: 0 40px 0 30px;
  background-color: #f2f4f6;
}

.v-main {
  flex: 1 1 auto;
  max-width: 100%;
}

.crm-auth {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background-color: rgb(35, 169, 231);
  display: flex;
  justify-content: center;
  align-items: center;
}

.crm-auth-form {
  width: 600px;
  height: 350px;
  background-color: white;
  border-radius: 16px;
  margin-bottom: 200px;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
}

.crm-auth-form .crm-logo {
  width: 25%;
}

.crm-input {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

.crm-input label {
  padding-left: 10px;
  color: #b4b4b4;
  font-size: 14px;
}
</style>
