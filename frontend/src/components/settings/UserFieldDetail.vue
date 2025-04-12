<script setup>
/* PrimeVue components */
import Select from "primevue/select";
import Button from "primevue/button";
import Checkbox from "primevue/checkbox";
import InputText from "primevue/inputtext";
import ConfirmDialog from "primevue/confirmdialog";
/* PrimeVue utils */
import { useConfirm } from "primevue/useconfirm";
/* Store */
import { storeToRefs } from "pinia";
import { rootStore } from "@/stores";
/* Vue */
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const store = rootStore();
const confirm = useConfirm();

const { params, validTypes } = storeToRefs(store.settings().userField());

onMounted(() => {
  console.log({ field_name: route.params.field_name });

  store.setPageName("Пользовательские поля");

  init()

});

onUnmounted(() => {
  store.settings().userField().resetDetail();
});

const addMode = computed(() => route.params.field_name == 0);
const entityId = computed(() => route.params.entity.toUpperCase());
const typeFieldName = computed(() => validTypes.value.find((t) => t.type == params.value.detailData.user_type_id)?.options?.title)

const disabledSave = computed(() => {
  const checkField = ["title", "entity_id", "user_type_id", "sort"]
  return Object.keys(params.value?.detailData || []).some((key) => checkField.includes(key) && !params.value.detailData[key])
})


const init = () => {
  params.value.detailData = {
    id: 0,
    user_field: [],
    title: "",
    entity_id: route.params.entity.toLocaleUpperCase(),
    field_name: "",
    user_type_id: "",
    xml_id: null,
    sort: 100,
    multiple: 0,
    mandatory: 0,
    show_filter: 0,
    show_in_list: 0,
    edit_in_list: 0,
    is_searchable: 0,
  };

  if (!addMode.value) {
    store.settings().userField().initDetail({
      field_name: route.params.field_name,
    });
  }
}

const save = () => {
  if (addMode.value) {
    store.settings().userField().addUserField();
  } else {
    store.settings().userField().updateUserField()
      .then((r) => {
        console.log(r);

        router.push({ name: "uf-deal-detail", params: { field_name: route.params.field_name } });
      })
      .catch((e) => {
        console.log(e);
      })
  }
};

const confirm2 = () => {
  confirm.require({
    message: "Вы действительно хотите удалить поле?",
    header: "Удаление поля",
    icon: "pi pi-info-circle",
    rejectLabel: "Отменить",
    acceptLabel: "Удалить",
    rejectClass: "p-button-secondary p-button-outlined",
    acceptClass: "p-button-danger",
    accept: () => { store.settings().userField().deleteUserField() },
    reject: () => { },
  });
};

watch(
  () => route.params.field_name,
  (_n, _o) => { init() }
)

watch(
  () => params.value.detailData,
  (_n, _o) => {
    if (Object.keys(_o).length == 0 || _n.field_name == _o.field_name) return;
    router.push({ name: "uf-deal-detail", params: { 'field_name': _n.field_name } })
  }
)

</script>

<template>
  <div id="user-fields-detail">
    <div class="user-fields-detail-container">
      <div class="user-fields-detail-table-wrapper">
        <table class="user-fields-detail-table">
          <tr>
            <td>ID</td>
            <td>{{ params.detailData.id }}</td>
          </tr>
          <tr>
            <td class="required-field">Название поля</td>
            <td>
              <InputText type="text" v-model="params.detailData.title" style="width: 300px" />
            </td>
          </tr>
          <tr>
            <td>Имя поля</td>
            <td>
              {{ params.detailData.field_name }}
            </td>
          </tr>
          <tr>
            <td class="required-field">Тип поля</td>
            <td v-if="addMode">
              <Select v-model="params.detailData.user_type_id" :options="validTypes" optionValue="type"
                optionLabel="options.title" placeholder="Выберите тип поля" style="width: 300px" />
            </td>
            <td v-else>
              {{ typeFieldName }}
            </td>
          </tr>
          <tr>
            <td>XML_ID</td>
            <InputText type="text" v-model="params.detailData.xml_id" style="width: 300px" />
          </tr>
          <tr>
            <td class="required-field">Индекс сортировки</td>
            <InputText type="text" v-model="params.detailData.sort" style="width: 300px" />
          </tr>
          <tr>
            <td>Множественное</td>
            <td v-if="!addMode">{{ params.detailData.multiple ? "Да" : "Нет" }}</td>
            <td v-else>
              <Checkbox v-model="params.detailData.multiple" :binary="true" :true-value="1" :false-value="0" />
            </td>
          </tr>
          <tr>
            <td>Обязательное</td>
            <td v-if="!addMode">{{ params.detailData.mandatory ? "Да" : "Нет" }}</td>
            <td v-else>
              <Checkbox v-model="params.detailData.mandatory" :binary="true" :true-value="1" :false-value="0" />
            </td>
          </tr>
          <tr>
            <td>Отображать в фильтре</td>
            <td>
              <Checkbox v-model="params.detailData.show_filter" :binary="true" :true-value="1" :false-value="0" />
            </td>
            <!-- <td v-if="!addMode">{{ params.detailData.show_filter ? 'Да' : 'Нет' }}</td>
            <td v-else><Checkbox v-model="params.detailData.show_filter" :binary="true" :true-value="1" :false-value="0"/></td> -->
          </tr>
          <tr>
            <td>Отображать в списке</td>
            <td>
              <Checkbox v-model="params.detailData.show_in_list" :binary="true" :true-value="1" :false-value="0" />
            </td>
            <!-- <td v-if="!addMode">{{ params.detailData.show_in_list ? 'Да' : 'Нет' }}</td>
            <td v-else><Checkbox v-model="params.detailData.show_in_list" :binary="true" :true-value="1" :false-value="0"/></td> -->
          </tr>
          <tr>
            <td>Редактирование в списке</td>
            <td v-if="!addMode">{{ params.detailData.edit_in_list ? "Да" : "Нет" }}</td>
            <td v-else>
              <Checkbox v-model="params.detailData.edit_in_list" :binary="true" :true-value="1" :false-value="0" />
            </td>
          </tr>
        </table>

        <div class="btn-container">
          <Button :label="addMode ? 'Добавить' : 'Сохранить'" :disabled="disabledSave" @click="save" />
          <Button v-if="!addMode" label="Удалить поле" severity="danger" @click="confirm2" />
        </div>
      </div>

      <pre>{{ params }}</pre>
      <pre>
        {{ route }}
      </pre>
    </div>
    <ConfirmDialog></ConfirmDialog>
  </div>
</template>

<style lang="scss" scope>
#user-fields-detail {
  background: var(--color-background-frame);
  border-radius: 16px;
  overflow: hidden;

  .user-fields-detail-container {
    height: 100%;
    width: 100%;
    padding: 30px 40px;

    .user-fields-detail-table-wrapper {
      width: 100%;
      height: auto;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;

      margin-bottom: 30px;

      .btn-container {
        display: flex;
        flex-direction: row;
        margin-top: 20px;

        .p-button {
          margin-right: 15px;
        }

        .p-button:last-child {
          margin-right: 0px;
        }
      }
    }

    .user-fields-detail-table {
      // width: 100%;
      // height: 100%;
    }
  }
}
</style>
