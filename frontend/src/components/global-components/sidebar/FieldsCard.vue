<script setup>
import { ref, watch, onMounted } from 'vue';

const emits = defineEmits(['save'])
const props = defineProps({
  changeMode: {
    type: Boolean,
    default: false
  },
  hideModeBtn: {
    type: Boolean,
    default: false
  }
})

const changeMode = ref(false)

onMounted(() => {
  changeMode.value = props.changeMode
})

watch(changeMode, (n, _) => { if (!n && !props.hideModeBtn.value) emits('save') })
watch(() => props.changeMode, (n, _) => { changeMode.value = n })

</script>

<template>
  <div class="fields-card">
    <div class="fields-card-header">
      <div class="card-title"><slot name="header"></slot></div>
      <div v-if="!props.hideModeBtn" @click="changeMode = !changeMode" class="card-controller">{{ changeMode ? 'сохранить' : 'изменить' }}</div>
    </div>
    <div class="divider"></div>
    <div class="fields-card-body">
      <slot :changeMode="changeMode" ></slot>
    </div>
  </div>
</template>

<style lang="scss">
.fields-card {
  --padding-x: 12px;
  --padding-y: 10px;

  width: 100%;
  height: auto;
  background: var(--theme-c-white-bg-frame);
  border-radius: 16px;

  .fields-card-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: var(--padding-y) var(--padding-x) 0 var(--padding-x);    

    .card-title {
      font-size: 14px;
      font-weight: 500;
      color: var(--theme-c-gray);
    }

    .card-controller {
      font-size: 12px;
      color: var(--theme-c-gray);
    }

    .card-controller:hover {
      cursor: pointer;
      text-decoration: underline;
    }
  }

  .divider {
    width: calc(100% - var(--padding-x) * 2);
    height: 1px;
    background: lightgray;
    margin: 3px var(--padding-x) 3px var(--padding-x);
  }

  .fields-card-body {
    padding: var(--padding-y) var(--padding-x) 0 var(--padding-x);    
  }
}
</style>