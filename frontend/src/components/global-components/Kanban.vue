<script setup>
/* Vue v3 */
import { onMounted, ref } from 'vue';
/* Stores */
import { rootStore } from '@/stores';
const store = rootStore()

const props = defineProps(['userStages', 'sysStatus'])

const kanbanStyles = ref({})

const kanbanContainer = ref(null)

onMounted(() => {
  setTimeout(() => {
    console.log({
      'userStages': props.userStages,
      'sysStatus': props.sysStatus
    });
  }, 2000);
  
  kanbanStyles.value.height = 500 + 'px'
})

</script>

<template>
  <div class="kanban-container" :style="kanbanStyles">
    <div class="kanban">

      <div v-for="stage in userStages" :key="stage.status_data.status_id" class="kanban-column-container">
        <div class="kanban-column-header">
          <div class="column-title" :style="{ 'background': stage.status_data.color }">
            {{ stage.status_data.title }}
          </div>
          <div v-if="$slots.addItem" class="column-item-add-container">
            <slot name="addItem" :stage="stage.status_data"></slot>
          </div>
          <div v-if="$slots.opportunity" class="kanban-stage-sum">
            <slot name="opportunity" :opportunity="stage.sum_opportunity"></slot>
          </div>
        </div>
        <div class="kanban-column-body">
          <div class="kanban-column">
            <div v-for="entityItem in stage.data" :key="entityItem.id" class="kanban-item">
              <slot v-if="$slots.card" name="card" :item="entityItem"></slot>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<style lang="scss">
.kanban-container {
  width: 100%;
  height: 100%;
  overflow-x: auto;
  overflow-y: hidden;

  .kanban {
    width: fit-content;
    height: 100%;

    display: flex;
    flex-direction: row;

    .kanban-column-container {
      width: var(--kanban-column-width);
      height: 100%;
      display: flex;
      flex-direction: column;
      border-right: 1px dashed lightgray;

      .kanban-column-header {
        width: var(--kanban-column-width);
        height: min-content;
        margin-bottom: 10px;
        position: relative;


        .column-title {
          padding: 3px 10px;
          font-weight: 600;
          width: 100%;
          border-radius: 0 16px 16px 0;
        }

        .kanban-stage-sum {
          display: flex;
          justify-content: center;
          width: 100%;
          padding: 3px 10px;
          font-weight: 600;
          border-radius: 16px;
          background-color: white !important;
          margin-top: 5px;
          border: 1px solid #dddddd;
        }
      }

      // .kanban-column-header::before {
      //   content: '';
      //   position: absolute;
      //   right: -10px;
      //   top: 0;
      //   border: 15px solid transparent;
      //   border-left: 15px solid green;
      // }

      .kanban-column-body {
        width: var(--kanban-column-width);
        height: 100%;
        overflow-x: hidden;
        overflow-y: auto;


        .kanban-column {
          width: var(--kanban-column-width);
          height: fit-content;

          display: flex;
          flex-direction: column;
          align-items: center;

          .kanban-item {}
        }
      }
    }

    .kanban-column-container:first-child {
      border-left: 1px dashed lightgray;
    }
  }
}
</style>