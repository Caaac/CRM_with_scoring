<script setup>
import { ref, onMounted, watch } from 'vue'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'
import { useRouter, useRoute } from 'vue-router'

const store = rootStore()
const route = useRoute()

const { dealDetail } = storeToRefs(store.crmStore())

const stageEl = ref(null)
const findedEl = ref(null)

watch(dealDetail, (n, o) => {
    stageEl.value = store.settingsStore().stages.filter(st => st.code == n.stage)[0]
    findedEl.value = stageEl.value
})

const checkStage = () => {
    stageEl.value = store.settingsStore().stages.filter(st => st.code == dealDetail.value.stage)[0]
    findedEl.value = stageEl.value
    stageEl.value = findedEl.value
}

const getStageStyle = (stageData) => {
    let resultStyle = {
        background: '',
        color: ''
    }

    if (!stageEl.value) {
        resultStyle.background = stageData.color
    }
    else if (stageData.id <= stageEl.value.id) {
        resultStyle.background = stageData.color
        resultStyle.color = stageData?.textColor
    }

    return resultStyle
}

const changeStage = (stageData) => {
    if (stageData.code == 'END') dealDetail.value.date_closed = new Date().format('yyyy-mm-dd')
    else dealDetail.value.date_closed = null
    dealDetail.value.stage = stageData.code
    store.crmStore().updateDeal(route.params.idDeal, dealDetail.value)
        .then((result) => {
            dealDetail.value.id = result.data.id
        })
}

</script>

<template>
    <div class="crm-stage-bar">
        <div v-for="stage in store.settingsStore().stages" :key="stage.id" class="crm-stage"
            :style="getStageStyle(stage)" @mouseenter="stageEl = stage" @mouseleave="checkStage"
            @click="changeStage(stage)">
            {{ stage.name }}
        </div>
    </div>
</template>

<style>
.crm-stage-bar {
    display: flex;
    margin: 10px 0;
    width: 100%;
    height: 27px;
}

.crm-stage {
    width: 100%;
    border-radius: 0 30px 30px 0;
    border: 1px solid rgb(156, 156, 156);
    text-align: center;
}
</style>