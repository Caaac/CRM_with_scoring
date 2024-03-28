<script setup>
import { onActivated, onMounted, ref } from 'vue'

const stages = ref([
  { name: 'Новая', color: 'red' },
  { name: 'В согласовании', color: 'yellow' },
  { name: 'В очереди', color: 'green' },
  { name: 'В работе', color: 'blue' },
  { name: 'На проверке', color: 'gray' },
  { name: 'Ожидание', color: 'purple' },
  { name: 'Завершена', color: 'red' }
])

// const stages = ref([
//   { name: 'Новая', color: 'red' },
//   { name: 'В согласовании', color: 'yellow' },
//   { name: 'В очереди', color: 'green' }
// ])

let crmStyles = ref({
  width: ''
})

const mainBlock = ref(null)

const onResizeLister = () => {
  crmStyles.value.width = mainBlock.value.offsetWidth + 'px'
  console.log('resize', crmStyles.value)
}

onMounted(() => {
  if (window.innerWidth == 1920) {
    crmStyles.value.width = '1580px'
  } else if (window.innerWidth == 1536) {
    crmStyles.value.width = '1200px'
  }
  //   onResizeLister()
  //   addEventListener('resize', onResizeLister)
})

onActivated(() => {
  onResizeLister()
  console.log('onActivated')
})
</script>

<template>
  <!-- :style="{ width: mainBlockWidth + 'px' }"   -->
  <div class="crm-crm-main-block" ref="mainBlock" :style="crmStyles">
    <div class="hh">
      <div class="crm-header-block">
        <div
          v-for="stage in stages"
          :key="stage.name"
          :style="{ 'background-color': stage.color }"
          class="crm-header-stage"
        >
          {{ stage.name }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.crm-crm-main-block {
  overflow-x: auto;
  white-space: nowrap;
  /* max-height: 100%; */
}

.hh {
  display: inline-block;
}

.ss {
  height: 20px;
  width: 100%;
  background-color: brown;
}

.crm-header-block {
  /* width: 100%; */
  display: flex;
}

.crm-header-stage {
  min-width: 250px;
  width: 100%;
}
</style>