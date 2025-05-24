<script setup>
/* PrimeVue components */
import Button from "primevue/button";
import Column from "primevue/column";
import DataTable from "primevue/datatable";

import { rootStore } from "@/stores";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { storeToRefs } from "pinia";

const route = useRoute();
const router = useRouter();
const store = rootStore();

const selectedField = ref(null);

const { params } = storeToRefs(store.settings().userField());

onMounted(() => {
  store.setPageName('Пользовательские поля');
  store.settings().userField().init();
});

const onRowSelect = (event) => {
  console.log(event.data);
  selectedField.value = null;
  router.push({ path: route.path + event.data.field_name + "/" });
};
</script>

<template>
  <div id="user-fields">
    <div class="user-fields-container">
      <DataTable v-model:selection="selectedField" :value="params.fields" selectionMode="single" dataKey="id"
        :metaKeySelection="false" @rowSelect="onRowSelect">
        <template #header>
          <div class="table-header">
            <Button @click="router.push({ path: route.path + '0/' })">Добавить</Button>
          </div>
        </template>
        <Column field="title" header="Поле"></Column>
        <Column field="field_name" header="Код поля"></Column>
      </DataTable>
    </div>
  </div>
</template>

<style lang="scss">
#user-fields {
  background: var(--color-background-frame);
  border-radius: 16px;
  overflow: hidden;

  .user-fields-container {
    height: 100%;
    width: 100%;
    padding: 30px 40px;
  }

  .table-header {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
  }
}
</style>
