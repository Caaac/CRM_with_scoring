<script setup>
import InputText from 'primevue/inputtext';

const props = defineProps({
  'changeMode': {
    type: Boolean,
    default: false
  },
  'fieldTitle': {
    type: String,
    required: true
  }
});

const model = defineModel({
  type: String,
  required: true,
});

</script>

<template>
  <div class="string-field custom-field">
    <div class="field-container">
      <div class="field-title">{{ props.fieldTitle }}</div>
      <div class="field-value">
        <template v-if="!props.changeMode">
          {{ model }}
        </template>
        <template v-else>
          <InputText type="text" v-model="model" />
        </template>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.string-field {

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
