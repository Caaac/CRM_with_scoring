<script setup>
import Calendar from "primevue/calendar";
import { computed } from "vue";

const props = defineProps({
  changeMode: {
    type: Boolean,
    default: false,
  },
  fieldTitle: {
    type: String,
    required: true,
  },
  dateFormat: String,
  manualInput: {
    type: Boolean,
    default: false
  },
  selectionMode: {
    type: String,
    default: 'single'
  },
  showTime: {
    type: Boolean,
    default: false
  },
  options: {
    type: Object,
    default: () => ({
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false // 24-часовой формат
    })
  },
  mandatory: {
    type: Boolean,
    default: false
  }
});

const emits = defineEmits(["click"]);

const model = defineModel({
  type: String,
  required: true,
});

const formatedDate = computed(() => {
  return model.value
    ? (new Date(model.value)).toLocaleString('ru-RU', props.options).replace(',', '')
    : 'отсуствует'
})

</script>

<template>
  <div class="calendar-field custom-field">
    <div class="field-container">
      <div class="field-title">{{ props.fieldTitle }}<span v-if="props.mandatory" class="required-field"></span></div>
      <div class="field-value">
        <template v-if="!props.changeMode">
          {{ formatedDate }}
        </template>
        <template v-else>
          <Calendar v-model="model" :dateFormat="props.dateFormat" :manualInput="props.manualInput"
            :selectionMode="props.selectionMode" :showTime="props.showTime">
            <template #inputicon="{ clickCallback }">
              <slot name="inputicon" @click="clickCallback"></slot>
            </template>
          </Calendar>
        </template>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.calendar-field {
  .field-container {
    display: flex;
    flex-direction: column;

    .field-title {
      font-size: 12px;
      color: var(--theme-c-white-gray);
      font-weight: 400;
    }
  }
}
</style>
