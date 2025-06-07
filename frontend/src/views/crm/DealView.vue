<script setup>
/* PrimeVue components */
import Avatar from 'primevue/avatar';
/* Custom components */
import Kanban from '@/components/global-components/Kanban.vue';
import KanbanCard from '@/components/global-components/KanbanCard.vue';
import ModuleMenu from '@/components/global-components/ModuleMenu.vue';
/* Vue v3 */
import { computed, onMounted, ref } from 'vue';
/* Stores */
import { rootStore } from '@/stores';
import { storeToRefs } from 'pinia';
/* Router */
import { useRoute, useRouter } from 'vue-router';

const store = rootStore()

const { params, statusType} = storeToRefs(store.crm().deal())

const route = useRoute();
const router = useRouter();

const kanbanStyle = ref({})

onMounted(() => {
  /* Init kanabn style */
  const kanbanFrame = document.getElementById('crm-entity-list').getBoundingClientRect();
  const windowInnerHeight = document.documentElement.clientHeight
  kanbanStyle.value.height = windowInnerHeight - kanbanFrame.top - 20 + 'px'

  store.crm().deal().init()
})

// TODO: Auto create
const menuItems = computed(() => {
  return [
    {
      path: '/crm/lead/',
      name: 'lead',
      title: 'Лиды'
    },
    {
      path: '/crm/deal/',
      match: '/crm/deal/',
      name: 'deal',
      title: 'Сделки'
    },
  ]
})

</script>

<template>

  <div id="deal-view">
    <ModuleMenu :items="menuItems" />

    <Kanban id="crm-entity-list" :style="kanbanStyle" :userStages="statusType['userStatus']"
      :systemStages="statusType['sysStatus']">
      <template #card="slotProps">
        <KanbanCard>
          <div class="card-container">
            <div class="card-main">
              <div class="card-main-body">
                <div @click="router.push({ path: `/crm/deal/details/${slotProps.item.id}/`})" class="card-title">{{ slotProps.item.title }}</div>
                <div class="card-price">{{ (slotProps.item?.opportunity || 0).toMonetarily() }}</div>
                <div class="card-entity-date-created">{{ (slotProps.item.date_create).toHumanDate() }}</div>
              </div>
              <div class="card-main-footer">
              </div>
            </div>
            <div class="card-menu">
              <Avatar label="U" class="mr-2" style="background-color: #dee9fc; color: #1a2551" shape="circle" />
            </div>
          </div>
        </KanbanCard>
      </template>
      <template #opportunity="slotProps">
        {{ (slotProps.opportunity || 0).toMonetarily() }}
      </template>
    </Kanban>

    <RouterView />
  </div>

</template>

<style scoped lang="scss">
#deal-view {
  display: flex;
  flex-direction: column;
}

#crm-entity-list {
  .card-title {
    font-weight: 600;
    font-size: 13px;
    color: var(--card-title-color);
    cursor: pointer;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .card-container {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    min-height: 100px;

    .card-main {
      width: 100%
    }

    .card-menu {
      width: 40px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: end;
    }
  }

  .card-title:hover {
    text-decoration: underline;
    color: var(--card-title-color-hover);
  }

  .card-price {
    font-size: 12px;
    font-weight: 500;
    color: var(--theme-c-gray)
  }

  .card-entity-date-created {
    font-size: 11px;
    font-weight: 600;
    color: var(--theme-c-gray)
  }
}
</style>