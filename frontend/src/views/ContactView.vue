<script setup>
import { RouterView, useRouter } from 'vue-router'; const router = useRouter()
import { storeToRefs } from 'pinia';
import { rootStore } from '@/stores'

const store = rootStore()

const { isLoading } = storeToRefs(store.settingsStore())
const { contacts } = storeToRefs(store.contactStore())

const userSelect = (event) => {
  // router.push({ name: 'contact', params: { idContact: event.data.id } })
  router.push({ path: `/contact/details/${event.data.id}/` })
}

const userCreate = (event) => {
  router.push({ path: `/contact/details/0/` })
}

</script>

<template>
  <div class="card">
    <Button @click="userCreate" class="mb-5"> Создать </Button>

    <DataTable :value="contacts" @rowSelect="userSelect" :loading="isLoading" selectionMode="single" dataKey="id"
      :metaKeySelection="false" paginator stripedRows removableSort :rows="10" :rowsPerPageOptions="[10, 20, 50, 100]"
      tableStyle="width: 100%">
      <Column field="id" header="ID" style="width: 5%" sortable></Column>
      <Column field="name" header="Название орагнизации" style="width: 13.6%" sortable></Column>
      <Column field="industry" header="Отрасль" style="width: 13.6%" sortable></Column>
      <Column field="revenue" header="Оборот" style="width: 13.6%" sortable></Column>
      <Column field="representative_name" header="Имя представлителя" style="width: 13.6%" sortable></Column>
      <Column field="representative_last_name" header="Фамилия представлителя" style="width: 13.6%" sortable></Column>
      <Column field="phone" header="Телефон" style="width: 13.6%" sortable></Column>
      <Column field="email" header="Почта" style="width: 13.6%" sortable></Column>
    </DataTable>

    <RouterView />
  </div>
</template>

<style scoped></style>
