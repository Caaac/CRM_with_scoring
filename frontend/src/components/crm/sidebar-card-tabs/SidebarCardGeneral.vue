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

const getStageName = (stageCode) => store.settingsStore().stages.find(stage => stage.code == stageCode)?.name
const getAvatarLable = (name, last_name) => name.slice(0, 1) + last_name.slice(0, 1)
const getFullName = (name, last_name) => name + ' ' +  last_name

const managers = computed(() => store.userStore().managers.find(el => el.id == dealDetail.value.responsible))
const avatarLable = computed(() => managers.value?.name.slice(0, 1) + managers.value?.last_name.slice(0, 1))
const fullName = computed(() => managers.value?.name + ' ' + managers.value?.last_name)

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
                <!-- <Buttom @click="a">123 </Buttom> -->

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
                        <div v-else class="crm-sidebar-info-item-value money-template">{{ dealDetail?.loan_amount }} ₽
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Источник сделки</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <Dropdown v-model="dealDetail.source" :options="store.settingsStore().source"
                                optionValue="name" optionLabel="name" checkmark class="w-full" />
                        </div>
                        <div v-else class="crm-sidebar-info-item-value">{{ dealDetail?.source }}</div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Срок кредитования</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <Dropdown v-model="dealDetail.loan_duration" :options="store.settingsStore().loan_duration"
                                optionValue="month" optionLabel="name" checkmark class="w-full" />
                        </div>
                        <div v-else class="crm-sidebar-info-item-value">
                        {{ store.settingsStore().loan_duration.find(el => el.month == dealDetail?.loan_duration)?.name || 'Не задано' }}</div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Процентная ставка</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <InputNumber inputId="withoutgrouping" :useGrouping="false"
                                class="crm-sidebar-about-input-int" v-model="dealDetail.loan_amount" />
                        </div>
                        <div v-else class="crm-sidebar-info-item-value">12.5%</div>
                    </div>

                    <Divider />

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Ответственный за сделку</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <Dropdown v-model="dealDetail.responsible" :options="store.userStore().managers" filter optionValue="id" :optionLabel="aa"
                                placeholder="Выберете ответственного за сделку" class="w-full md:w-10rem">
                                <template #value="slotProps">
                                    <div v-if="slotProps.value" class="flex align-items-center">
                                        <Avatar :label="avatarLable" class="mr-2"
                                            style="background-color: #dee9fc; color: #1a2551; font-size: 12px;" shape="circle" />
                                        <div class="flex items-center">{{ fullName }}</div>
                                    </div>
                                    <span v-else>
                                        <div>{{ slotProps.placeholder }}</div>
                                    </span>
                                </template>
                                <template #option="slotProps">
                                    <div class="flex align-items-center">
                                        <Avatar :label="getAvatarLable(slotProps.option.name, slotProps.option.last_name)" class="mr-2"
                                            style="background-color: #dee9fc; color: #1a2551; font-size: 12px;" shape="circle" />
                                        <div class="flex items-center">{{ getFullName(slotProps.option.name, slotProps.option.last_name) }}</div>
                                    </div>
                                </template>
                            </Dropdown>
                        </div>
                        <div v-else class="crm-sidebar-info-item-value my-2">
                            <Avatar :label="avatarLable" class="mr-2"
                                style="background-color: #dee9fc; color: #1a2551; font-size: 12px;" shape="circle" />
                            {{ managers?.name + ' ' + managers?.last_name }}
                        </div>
                    </div>

                    <Divider />

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Клиент</div>
                        <div v-if="isEddit" class="crm-sidebar-info-item-value">
                            <InputNumber inputId="withoutgrouping" :useGrouping="false"
                                class="crm-sidebar-about-input-int" v-model="dealDetail.loan_amount" />
                        </div>
                        <div v-else class="crm-sidebar-info-item-value">Ануфриев Алексей</div>
                    </div>


                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Комментарий</div>
                        <div class="crm-sidebar-info-item-value">
                            <Textarea v-model="dealDetail.comment"
                                :disabled="!isEddit || dealDetail.date_closed != null" autoResize rows="2" cols="30"
                                class="w-full" />
                        </div>
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


.crm-sidebar-about-input-int.price .p-inputtext.p-component.p-inputnumber-input {
    font-size: 25px;
}
</style>