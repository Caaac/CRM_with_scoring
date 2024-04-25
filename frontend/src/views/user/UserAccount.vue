<script setup>
import { rootStore } from '@/stores'
const store = rootStore()
import { storeToRefs } from 'pinia'
import { ref, watch, computed } from 'vue'

import { useToast } from 'primevue/usetoast'
const toast = useToast()
import FloatLabel from 'primevue/floatlabel'

const editStatus = ref(false)
const changePassword = ref(false)
const { curUser } = storeToRefs(store.userStore())
const newPassword = ref({new: '', repete: ''})

const saveNewPassword = () => {
    if (newPassword.value.new != newPassword.value.repete) {
        alertOfError('Пароли не совпадают')  
        return false
    }

    alertOfSuccess('Пароль изменен')
    changePassword.value = false
    return true
}

const avatarLable = computed(() => {
    return curUser.value.NAME.slice(0, 1) + curUser.value.LAST_NAME.slice(0, 1)
})

watch(editStatus, (n, o) => {
  if (!n) {
    alertOfSuccess('Внесения сохранены')
  }
})

const alertOfError = (summary = '', detail = '') => {
  toast.add({
    severity: 'error',
    summary: summary,
    detail: detail,
    life: 3000
  })
}

const alertOfSuccess = (summary = '', detail = '') => {
  toast.add({
    severity: 'success',
    summary: summary,
    detail: detail,
    life: 3000
  })
}
</script>

<template>
  <div class="crm-user">
    <div class="crm-user-avatar">
      <Avatar :label="avatarLable" class="mr-2" size="xlarge" shape="circle" />
      <Button
        @click="editStatus = !editStatus"
        :label="!editStatus ? 'Редактировать' : 'Сохранить изменения'"
        :icon="!editStatus ? 'mdi mdi-account-box-edit-outline' : 'mdi mdi-content-save-outline'"
      />
      <Button label="Сменить пароль" @click="changePassword = true" />
    </div>

    <div class="crm-user-fields">
      <FloatLabel>
        <InputText id="name" :disabled="!editStatus" v-model="curUser.NAME" />
        <label for="name">Имя</label>
      </FloatLabel>

      <FloatLabel>
        <InputText id="last-name" :disabled="!editStatus" v-model="curUser.LAST_NAME" />
        <label for="last-name">Фамилия</label>
      </FloatLabel>

      <FloatLabel>
        <InputText id="email" :disabled="!editStatus" v-model="curUser.EMAIL" />
        <label for="email">Почта</label>
      </FloatLabel>
    </div>

    <Dialog v-model:visible="changePassword" modal header="Смена пароля" :style="{ width: '25rem' }">
      <span class="p-text-secondary block mb-5">Введите ваш новый пароль</span>
      <div class="flex align-items-center gap-3 mb-3">
        <label for="new-password" class="font-semibold w-6rem">Новый пароль</label>
        <Password id="new-password" class="flex-auto" autocomplete="off" v-model="newPassword.new" />
      </div>
      <div class="flex align-items-center gap-3 mb-5">
        <label for="repete-password" class="font-semibold w-6rem">Повторите пароль</label>
        <Password id="repete-password" class="flex-auto" autocomplete="off" v-model="newPassword.repete" :feedback="false" />
      </div>
      <div class="flex justify-content-end gap-2">
        <Button type="button" label="Cancel" severity="secondary" @click="changePassword = false"></Button>
        <Button type="button" label="Save" @click="saveNewPassword"></Button>
      </div>
    </Dialog>
  </div>
</template>

<style>
.crm-user {
  display: inline-flex;
  justify-content: center;
}

.crm-user .p-avatar.p-avatar-xl {
  width: 7rem;
  height: 7rem;
  font-size: 3rem;
}

.crm-user-fields,
.crm-user-avatar {
  display: flex;
  flex-direction: column;
}

.crm-user-avatar {
  align-items: center;
  width: 300px;
}

.crm-user-fields {
  margin-left: 50px;
}

.crm-user-fields input {
  margin-bottom: 25px;
}

.crm-user-avatar button {
  margin-top: 20px;
}
</style>