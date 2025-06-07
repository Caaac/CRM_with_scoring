<script setup>
import Checkbox from 'primevue/checkbox';

const props = defineProps({
  changeMode: {
    type: Boolean,
    default: false,
  },
  fieldTitle: {
    type: String,
    required: true,
  },
  binary: Boolean,
  trueValue: {
    type: String,
    default: '',
  },
  falseValue: {
    type: [String, Number, Boolean],
    default: '',
  },
  mandatory: {
    type: Boolean,
    default: false
  }
});

const model = defineModel({
  type: Number,
  required: true,
});
</script>

<template>
  <div class="boolean-field custom-field">
    <div class="field-container">
      <div class="field-title">{{ props.fieldTitle }}<span v-if="props.mandatory" class="required-field"></span></div>
      <div class="field-value">
        <template v-if="!props.changeMode">
          {{ model ? 'Да' : 'Нет' }}
        </template>
        <template v-else>
          <Checkbox
            v-model="model"
            :binary="props.binary"
            :trueValue="props.trueValue"
            :falseValue="props.falseValue"
          />
        </template>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.boolean-field {
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
