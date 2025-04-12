<script setup>
/* PrimeVue components */
import { rootStore } from "@/stores";
import Sidebar from "primevue/sidebar";
import Skeleton from "primevue/skeleton";
/* Custom components */
import FieldsCard from "@/components/global-components/sidebar/FieldsCard.vue";
import StringField from "@/components/global-components/sidebar/fields/StringField.vue";
import NumberField from "@/components/global-components/sidebar/fields/NumberField.vue";
import BoolenField from "@/components/global-components/sidebar/fields/BoolenField.vue";
import CalendarField from "@/components/global-components/sidebar/fields/CalendarField.vue";
/* Vue v3 */
import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
/* Stores */
import { storeToRefs } from "pinia";

const route = useRoute();
const router = useRouter();
const store = rootStore();
const { params, loading, deal_detail, statusType } = storeToRefs(store.crm().deal());

const visiblee = ref(true);

onMounted(() => {
  store.crm().deal().getDealDetail(route.params.idDeal);
});

/**
 * @returns 0..n - index of status
 * @returns -1 - sysStatus
 * @returns -2 - undefined
 */
const stageId = computed(() => {
  let result = -2;
  if (Object.keys(deal_detail.value).length) {
    statusType.value["userStatus"].forEach((element, index) => {
      console.log(
        element.status_data.status_id,
        deal_detail.value.stage_id,
        element.status_data.status_id == deal_detail.value.stage_id
      );

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
  // TODO: check mandatory fields
  store.crm().deal().updateDealDetail(deal_detail.value.id, deal_detail.value , false, true)
}
</script>

<template>
  <Sidebar v-model:visible="visiblee" @hide="router.go(-1); store.crm().deal().init();" id="deal-detail-sidebar"
    class="propel-sidebar" position="right">
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
      <div class="deal-field">
        <FieldsCard @save="saveDeal" class="mb-1">
          <template #header>Общая</template>
          <template #default="{ changeMode }">
            <div class="field-wrapper">
              <StringField v-model="deal_detail.title" v-if="changeMode" :fieldTitle="'Наименование сделки'"
                :changeMode="changeMode" />
              <NumberField v-model="deal_detail.opportunity" :fieldTitle="'Сумма'" :changeMode="changeMode"
                :useGrouping="true" :suffix="' ₽'">
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
            </div>
          </template>
        </FieldsCard>

        <FieldsCard @save="saveDeal">
          <template #header>Пользовательские поля</template>
          <template #default="{ changeMode }">
            <div class="field-wrapper">
              <template v-for="field in deal_detail.uf_list">
                <template v-if="field.user_type_id == 'string'">
                  <!-- {{ field.values }} -->
                  <StringField v-model="field.values[0].value" :fieldTitle="field.title" :changeMode="changeMode"
                    :key="field.id" :data-field-name="field.field_name" />
                </template>
              </template>
            </div>
          </template>
        </FieldsCard>
      </div>
      <div class="deal-timeline"></div>
    </div>

    <pre>{{ deal_detail }}</pre>
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
    height: 100%;

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
  }
}
</style>
