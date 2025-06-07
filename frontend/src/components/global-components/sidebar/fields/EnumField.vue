<script setup>
/* Primevue components */
import Select from 'primevue/select';

const props = defineProps({
  changeMode: {
    type: Boolean,
    default: false,
  },
  fieldTitle: {
    type: String,
    required: true,
  },
  multiple: {
    type: Boolean,
    default: false,
  },
  validItems: {
    type: Array,
    default: () => [],
  },
  template: {
    type: Object,
    default: () => ({}.deepCopy())
  },
  mandatory: {
    type: Boolean,
    default: false
  }
});

const model = defineModel({
  type: Array,
  required: true,
});

const getItemById = (id) => props.validItems.find(item => item.id == id)

const addNewItem = () => {
  const newItem = props.template.deepCopy()
  model.value.push(newItem)
}

</script>

<template>
  <div class="enum-field custom-field">
    <div class="field-container">
      <div class="field-title">{{ props.fieldTitle }}<span v-if="props.mandatory" class="required-field"></span></div>
      <div class="field-value field-enum">
        <div v-for="(enumElement, index) in model" :key="enumElement.id" class="field-enum-item">
          <template v-if="!props.changeMode">
            {{ getItemById(enumElement.value_int)?.value }}
          </template>
          <template v-else>
            <Select v-model="enumElement.value_int" :options="props.validItems" 
              @update:modelValue="$emit('update:modelValue', model)" showClear optionLabel="value" 
              optionValue="id" placeholder="Выберете элемент" />
          </template>
        </div>

        <template v-if="props.changeMode && !props.multiple">
          <div @click="addNewItem" class="field-enum-item-add">Добавить элемент</div>
        </template>

      </div>
    </div>
  </div>
</template>

<style lang="scss">
.enum-field {
  .field-container {
    display: flex;
    flex-direction: column;

    .field-title {
      font-size: 12px;
      color: var(--theme-c-white-gray);
      font-weight: 400;
    }

    .field-enum {
      display: flex;
      flex-direction: column;

      .p-select {
        margin-bottom: 10px;
        width: 100%;
      }

      .field-enum-item-add {
        font-size: 13px;
        color: var(--theme-c-gray);
        font-weight: 500;
        margin-bottom: 10px;
      }

      .field-enum-item-add::before {
        content: '+';
        margin-right: 5px;
        margin-left: 10px;
        color: inherit;
        font-size: 15px;
      }

      .field-enum-item-add:hover {
        cursor: pointer;
        text-decoration: underline;
      }
    }
  }
}
</style>
