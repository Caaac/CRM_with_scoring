<script setup>
import InputNumber from "primevue/inputnumber";

const props = defineProps({
  changeMode: {
    type: Boolean,
    default: false,
  },
  fieldTitle: {
    type: String,
    required: true,
  },
  useGrouping: {
    type: Boolean,
    default: false,
  },
  minFractionDigits: Number,
  maxFractionDigits: Number,
  min: Number,
  max: Number,
  currency: String,
  prefix: String,
  suffix: String,
});

const model = defineModel({
  type: Number,
  required: true,
});
</script>

<template>
  <div class="number-field custom-field">
    <div class="field-container">
      <div class="field-title">{{ props.fieldTitle }}</div>
      <div class="field-value">
        <template v-if="!props.changeMode">
          <slot name="display" :model="model"></slot>
        </template>
        <template v-else>
          <InputNumber
            v-model="model"
            :useGrouping="props.useGrouping"
            :minFractionDigits="props.minFractionDigits"
            :maxFractionDigits="props.maxFractionDigits"
            :min="props.min"
            :max="props.max"
            :currency="props.currency"
            :prefix="props.prefix"
            :suffix="props.suffix"
          />
        </template>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.number-field {
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
