<script setup>
/* PrimeVue components */
import Tab from 'primevue/tab';
import Tabs from 'primevue/tabs';
import Button from 'primevue/button';
import Sidebar from "primevue/sidebar";
import TabList from 'primevue/tablist';
import Message from 'primevue/message';
import Skeleton from "primevue/skeleton";
import TabPanel from 'primevue/tabpanel';
import TabPanels from 'primevue/tabpanels';
/* Custom components */
import FieldsCard from "@/components/global-components/sidebar/FieldsCard.vue";
import EnumField from "@/components/global-components/sidebar/fields/EnumField.vue";
import StringField from "@/components/global-components/sidebar/fields/StringField.vue";
import NumberField from "@/components/global-components/sidebar/fields/NumberField.vue";
import BoolenField from "@/components/global-components/sidebar/fields/BoolenField.vue";
import CalendarField from "@/components/global-components/sidebar/fields/CalendarField.vue";
/* Vue v3 */
import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
/* Stores */
import { storeToRefs } from "pinia";
import { rootStore } from "@/stores";

const route = useRoute();
const router = useRouter();
const store = rootStore();
const { params, loading, deal_detail, statusType } = storeToRefs(store.crm().deal());

const visiblee = ref(true);


onMounted(async () => {
  await store.crm().deal().getDealDetail(route.params.idDeal);
  deal_detail.value.title = 'Новая сделка'
});


const isNew = computed(() => route.params.idDeal == 0)

/**
 * @returns 0..n - index of status
 * @returns -1 - sysStatus
 * @returns -2 - undefined
 */
const stageId = computed(() => {
  let result = -2;
  if (Object.keys(deal_detail.value).length) {
    statusType.value["userStatus"].forEach((element, index) => {
      if (element.status_data.status_id == deal_detail.value.stage_id) {
        result = index;
      }
    });
    statusType.value["sysStatus"].forEach((element, index) => {
      if (element.status_data.status_id == deal_detail.value.stage_id) {
        result = -1;
      }
    });
  }
  return result;
});

const finalStageStyle = computed(() => {
  const result = {
    background: "",
    width: `${100 / (statusType.value["userStatus"]?.length + 1)}%`,
  };

  if (stageId == -1 && deal_detail.value.stage_id == "WON") {
    result.background = "green"; // TODO : change color
  } else if (stageId == -1 && ["LOSE", "APOLOGY"].includes(deal_detail.value.stage_id)) {
    result.background = "red"; // TODO : change color
  }

  return result;
});


const saveDeal = () => {
  store.helper().infoToast('Обновлен результат рассмотреня заявки "Новая сделка"');
  // TODO: check mandatory fields
  store.crm().deal().updateDealDetail(deal_detail.value.id, deal_detail.value, false, true)
}

const createDeal = async () => {
  // TODO: check mandatory fields
  deal_detail.value.assigned_by_id = store.user().params.account.id
  deal_detail.value.created_by_id = store.user().params.account.id

  const newDealData = await store.crm().deal().createDeal(deal_detail.value, false, true)
  console.log('newDealData', newDealData);
  router.push({ path: `/crm/deal/details/${newDealData.data.id}/` })
}

const updateUF = (value, field) => {
  console.log(value, field);
}


/**
 * For testing
 */
const selCon = ref(1)
const conList = ref([
  {
    id: 1,
    value: 'Михайлов Олег Валентинович'
  },
  {
    id: 2,
    value: 'Зайцев Константин Николаевич'
  },
  {
    id: 3,
    value: 'test3'
  }
])


</script>

<template>
  <Sidebar v-model:visible="visiblee" @hide="router.push({ path: '/crm/deal/kanban/' }); store.crm().deal().init()"
    id="deal-detail-sidebar" class="propel-sidebar" position="right">
    <template #header>
      <Skeleton v-if="loading.deal_detail" class="sidebar-skeleton-header"></Skeleton>
      <span class="sidebar-header"> {{ deal_detail.title }} </span>
    </template>

    <div class="deal-stage">
      <div v-for="(status, index) in statusType['userStatus']" :key="status.status_data.id" class="stage-item" @click="
        store
          .crm()
          .deal()
          .updateDeal(
            deal_detail.id,
            { stage_id: status.status_data.status_id },
            false,
            true
          )
        " :style="{
          background: index <= stageId || stageId == -1 ? status.status_data.color : '',
          width: `${100 / (statusType['userStatus'].length + 1)}%`,
        }">
        <div class="item-title">{{ status.status_data.title }}</div>
      </div>
      <div class="stage-item" :style="finalStageStyle">
        <div class="item-title">Завершить сделку</div>
      </div>
    </div>

    <div class="container">
      <Tabs id="deal-detail-main-tabs" value="0">
        <TabList>
          <Tab value="0">Общее</Tab>
          <Tab value="1">Анализ</Tab>
        </TabList>
        <TabPanels :class="{ '__new-mode': isNew }">
          <TabPanel value="0" class="d-flex">
            <div class="deal-field">
              <FieldsCard @save="saveDeal" class="mb-1" :hide-mode-btn="isNew" :change-mode="isNew">
                <template #header>Общая</template>
                <template #default="{ changeMode }">
                  <div class="field-wrapper">
                    <StringField v-model="deal_detail.title" v-if="changeMode" :fieldTitle="'Наименование сделки'"
                      :changeMode="changeMode" />
                    <NumberField v-model="deal_detail.opportunity" :fieldTitle="'Сумма'" :changeMode="changeMode"
                      :useGrouping="true" :suffix="' ₽'" :mandatory="true">
                      <template #display="{ model }">
                        <span style="font-size: 20px; font-weight: 300">{{ model ? model.toMonetarily() : "" }}</span>
                      </template>
                    </NumberField>
                    <BoolenField v-model="deal_detail.is_new" :fieldTitle="'Новая сделка'" :changeMode="changeMode"
                      :binary="true" :trueValue="1" :falseValue="0" />
                    <CalendarField v-model="deal_detail.date_create" :fieldTitle="'Дата создания'" :changeMode="false"
                      :dateFormat="'dd.mm.yy'" :showTime="true" />
                    <CalendarField v-model="deal_detail.date_modify" :fieldTitle="'Дата изменения'" :changeMode="false"
                      :dateFormat="'dd.mm.yy'" :showTime="true" />

                    <EnumField v-model="selCon" :fieldTitle="'Контакт'" :changeMode="changeMode"
                      :validItems="conList" :data-field-name="'Контакт'"
                      @update:modelValue="(value) => { updateUF(value, field) }" :mandatory="true">
                      <template #test>Михайлов Олег Валентинович</template>
                    </EnumField>
                  </div>
                </template>
              </FieldsCard>

              <FieldsCard @save="saveDeal" :hide-mode-btn="isNew" :change-mode="isNew">
                <template #header>Пользовательские поля</template>
                <template #default="{ changeMode }">
                  <div class="field-wrapper">
                    <template v-for="field in deal_detail.uf_list">
                      <template v-if="field.user_type_id == 'string'">
                        <StringField v-model="field.values[0].value" :fieldTitle="field.title" :changeMode="changeMode"
                          :key="field.id" :data-field-name="field.field_name" :mandatory="field.mandatory" />
                      </template>

                      <template v-if="field.user_type_id == 'boolean'">
                        <BoolenField v-model="field.values[0].value_int" :fieldTitle="field.title"
                          :changeMode="changeMode" :key="field.id" :binary="true" :trueValue="1" :falseValue="0"
                          :data-field-name="field.field_name" :mandatory="field.mandatory" />
                      </template>

                      <template v-if="field.user_type_id == 'number'">
                        <NumberField v-model="field.values[0].value_double" :fieldTitle="field.title"
                          :changeMode="changeMode" :key="field.id" :maxFractionDigits="2"
                          :data-field-name="field.field_name" :mandatory="field.mandatory">
                          <template #display="{ model }">
                            {{ model }}
                          </template>
                        </NumberField>
                      </template>

                      <template v-if="field.user_type_id == 'integer'">
                        <NumberField v-model="field.values[0].value_int" :fieldTitle="field.title"
                          :changeMode="changeMode" :key="field.id" :maxFractionDigits="0"
                          :data-field-name="field.field_name" :mandatory="field.mandatory">
                          <template #display="{ model }">
                            {{ model }}
                          </template>
                        </NumberField>
                      </template>

                      <template v-if="field.user_type_id == 'date'">
                        <CalendarField v-model="field.values[0].value_datetime" :fieldTitle="field.title"
                          :changeMode="changeMode" :key="field.id" dateFormat="dd.mm.yy" :manualInput="false"
                          :selectionMode="'single'" :data-field-name="field.field_name"
                          :options="{ day: '2-digit', month: '2-digit', year: 'numeric', hour12: false }"
                          :mandatory="field.mandatory">
                          <template #display="{ model }">
                            {{ model }}
                          </template>
                        </CalendarField>
                      </template>

                      <template v-if="field.user_type_id == 'datetime'">
                        <CalendarField v-model="field.values[0].value_datetime" :fieldTitle="field.title"
                          :changeMode="changeMode" :key="field.id" dateFormat="dd.mm.yy" :manualInput="false"
                          :selectionMode="'single'" :showTime="true" :data-field-name="field.field_name"
                          :mandatory="field.mandatory">
                          <template #display="{ model }">
                            {{ model }}
                          </template>
                        </CalendarField>
                      </template>

                      <template v-if="field.user_type_id == 'enumirate'">
                        <EnumField v-model="field.values" :fieldTitle="field.title" :changeMode="changeMode"
                          :key="field.id" :validItems="field.user_field" :template="field.value_tmpl"
                          :data-field-name="field.field_name" @update:modelValue="(value) => { updateUF(value, field) }"
                          :mandatory="field.mandatory" />
                      </template>

                      <!-- TODO Добавить оставшиеся поля + файлы -->
                    </template>
                  </div>
                </template>
              </FieldsCard>
            </div>

            <div class="deal-timeline"></div>
          </TabPanel>
          <TabPanel value="1">
            <Button>Отправить заявку на рассмотрение</Button>

            <Message severity="success" style="margin-top: 20px;"></Message>
          </TabPanel>
        </TabPanels>
      </Tabs>

      <div v-if="isNew" class="pl-save-panel">
        <Button @click="createDeal">Сохранить</Button>
        <Button @click="router.push({ path: '/crm/deal/kanban/' })" severity="secondary">Отменить</Button>
      </div>
    </div>

    <!-- <pre>{{ deal_detail }}</pre> -->
  </Sidebar>
</template>

<style lang="scss">
#deal-detail-sidebar {
  --sizebar-width: 1200px;
  width: var(--sizebar-width);

  .deal-stage {
    display: flex;
    flex-direction: row;
    margin-bottom: 15px;

    .stage-item {
      height: auto;
      width: auto;
      border: 1px solid rgb(214, 214, 214);
      border-radius: 2px 26px 26px 2px;
      cursor: pointer;

      .item-title {
        padding: 5px 20px 5px 10px;
        font-size: 15px;
        line-height: 17px;
        font-weight: 500;
        text-align: center;
      }
    }
  }

  .container {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 93%; // TODO сделать вычисленипе js
    // position: relative;

    .deal-field {
      width: 40%;
      height: 100%;
      display: flex;
      flex-direction: column;

      .field-wrapper {
        display: flex;
        flex-direction: column;
      }
    }

    .deal-timeline {
      width: 60%;
      height: 100%;
    }

    .pl-save-panel {
      position: absolute;
      bottom: 0px;
      left: 0px;
      width: 100%;
      background: white;
      height: 60px;
      display: flex;
      justify-content: center;
      align-items: center;

      button {
        margin-right: 10px;
      }
    }
  }
}

#deal-detail-main-tabs {
  width: 100%;

  .d-flex {
    display: flex
  }

  .p-tabpanels,
  .p-tablist-tab-list {
    background: none;
  }

  .p-tabpanels {
    height: 100%;
  }

  .p-tabpanel {
    height: 100%;
    overflow-y: auto;
  }

  .p-tabpanels.__new-mode .p-tabpanel {
    height: calc(100% - 45px);
  }

  .p-tablist-tab-list {
    button {
      background: white;
      border-radius: 10px 10px 0 0;
      margin-right: 1px;
    }
  }
}
</style>
