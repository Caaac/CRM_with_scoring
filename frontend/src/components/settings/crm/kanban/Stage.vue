<script setup>
/* PrimeVue components */
import Button from "primevue/button";
import Column from "primevue/column";
import InputText from 'primevue/inputtext';
import DataTable from "primevue/datatable";
import ColorPicker from 'primevue/colorpicker';
import InputNumber from 'primevue/inputnumber';
/* Store */
import { rootStore } from "@/stores";
/* Vue */
import { ref, onMounted, computed } from "vue";
import { storeToRefs } from "pinia";

const store = rootStore();
const { params } = storeToRefs(store.settings().stage());

const editingRows = ref([]);

onMounted(async () => {
  await store.settings().stage().init();
});

const stages = computed(() => {
  return params.value.stages.filter((s) => s.system_status != 1 || s.status_id == 'NEW');
})

const onRowEditSave = async (event) => {
  let { newData, index } = event;

  if (!(newData.color || '').includes('#')) {
    newData.color = '#' + newData.color;
  }

  if (newData.id <= 0) {
    await store.settings().stage().add(newData);
  } else {
    await store.settings().stage().updateStage(newData.id, newData);
  }

  await store.settings().stage().init();
}

const addStage = async () => {
  await store.settings().stage().addStage();
  await store.settings().stage().init();
}

const deleteStage = async (id) => {
  await store.settings().stage().deleteStage(id);
  await store.settings().stage().init();
}

</script>

<template>
  <div id="stage-settings">
    <div class="stage-settings-container">
      <DataTable v-model:editingRows="editingRows" :value="stages" editMode="row" dataKey="id"
        @row-edit-save="onRowEditSave">
        <template #header>
          <div class="table-header">
            <Button @click="addStage">Добавить стадию</Button>
          </div>
        </template>
        <Column field="id" header="ID" style="width: 20%"></Column>
        <Column field="title" header="Название" style="width: 20%">
          <template #editor="{ data, field }">
            <InputText v-model="data[field]" fluid />
          </template>
        </Column>
        <Column field="color" header="Цвет" style="width: 20%">
          <template #editor="{ data, field }">
            <ColorPicker v-model="data[field]" />
          </template>
          <template #body="slotProps">
            <ColorPicker v-model="slotProps.data['color']" disabled />
          </template>
        </Column>
        <Column field="sort" header="Сортировка" style="width: 20%">
          <template #editor="{ data, field }">
            <InputNumber v-model="data[field]" fluid />
          </template>
        </Column>

        <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center"></Column>
        <Column style="width: 10%; min-width: 8rem" bodyStyle="text-align:center">
          <template #body="{ data }">
            <Button @click="deleteStage(data.id)" icon="pi pi-trash" severity="danger" rounded variant="outlined"
              aria-label="Cancel" />
          </template>
        </Column>
      </DataTable>

    </div>
  </div>
</template>

<style lang="scss" scoped>
#stage-settings {
  background: var(--color-background-frame);
  border-radius: 16px;
  overflow: hidden;

  .stage-settings-container {
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
