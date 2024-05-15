<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'

const store = rootStore()
const router = useRouter()
const route = useRoute()

const isEddit = ref(false)
const { dealDetail } = storeToRefs(store.crmStore())

const getStageName = (stageCode) => {
    return store.settingsStore().stages.find(stage => stage.code == stageCode)?.name
}

watch(isEddit, (n, o) => {
    if (n) return
    store.crmStore().updateDeal(route.params.idDeal, dealDetail.value)
        .then((result) => {
            dealDetail.value.id = result.data.id
        })
})

const a = () => {
    console.log('123');
    dealDetail.value.leeee = '123'
}

</script>

<template>
    <div class="crm-crm-about-deal-main">
        <div class="crm-crm-about-deal">
            <div class="crm-crm-about-deal-wrapper">
                <div class="crm-sidebar-about-header">
                    <span>О сделке</span>
                    <span @click="isEddit = !isEddit" class="hover:underline cursor-pointer">{{ isEddit ? 'сохранить' :
                        'изменить' }}</span>
                </div>

                <Divider />
                <Buttom @click="a">123 </Buttom>

                <div class="crm-sidebar-about-body">
                    <div v-if="isEddit" class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Название сделки</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <InputText type="text" class="crm-sidebar-about-input" v-model="dealDetail.title" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Сумма кредита</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <InputNumber inputId="withoutgrouping" :useGrouping="false"
                                class="crm-sidebar-about-input-int price" v-model="dealDetail.loan_amount" />
                        </div>
                        <div v-else class="crm-sidebar-info-item-value money-template">{{ dealDetail?.loan_amount }} ₽</div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Сумма кредита</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <InputNumber inputId="withoutgrouping" :useGrouping="false"
                                class="crm-sidebar-about-input-int" v-model="dealDetail.loan_amount" />
                        </div>
                        <div v-else class="crm-sidebar-info-item-value">{{ dealDetail?.loan_amount }} ₽</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.money-template {
    font-size: 27px;
}

.crm-crm-about-deal {
    background: white;
}

.crm-crm-about-deal {
    width: 41%;
    border-radius: 16px;
}

.crm-crm-about-deal-wrapper {
    padding: 10px;
}


.crm-sidebar-about-input-int.price .p-inputtext.p-component.p-inputnumber-input{
    font-size: 25px;
}
</style>