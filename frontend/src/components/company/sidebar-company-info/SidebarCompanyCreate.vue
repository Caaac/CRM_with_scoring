<script setup>
import { onMounted, ref, computed, inject } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'
import { useToast } from 'primevue/usetoast'

const $axios = inject("$axios");
const store = rootStore()
const router = useRouter()
const route = useRoute()
const toast = useToast()

const isEddit = ref(true)
const newCompnay = ref({})
const { isLoading } = storeToRefs(store.settingsStore())

onMounted(() => {
    const tml = store.companyStore().companies.shift()
    Object.keys(tml).map(key => {
        if (key == 'id') delete tml[key]
        else if (tml[key] instanceof Array) tml[key] = []
        else tml[key] = null
    })
    newCompnay.value = tml
})

const canCreate = computed(() => {
    let result = true
    Object.entries(newCompnay.value).forEach(([_key, value]) => {
        if (value == null) result = false
    });

    return result
})

const createNewCompany = () => {
    $axios.post('company/', newCompnay.value)
        .then(function (response) {
            router.push({ path: `/company/details/${response.data.id}/` })
        })
        .catch(function (error) {
            alertOfError('Компания не зарегистрирована', 'Что-то пошло не так')
        })
}

const alertOfError = (summary = '', detail = '') => {
    toast.add({
        severity: 'error',
        summary: summary,
        detail: detail,
        life: 3000
    })
}

</script>

<template>
    <div class="crm-sidebar-about-create-wrapper">
        <div class="crm-sidebar-about-create-bg"></div>
        <div class="crm-sidebar-about">
            <div class="crm-sidebar-about-wrapper">
                <div class="crm-sidebar-about-header">
                    <span>О компании</span>
                    <span @click="isEddit = !isEddit" class="hover:underline cursor-pointer">{{ isEddit ? 'сохранить' :
                        'изменить' }}</span>
                </div>

                <Divider />

                <div class="crm-sidebar-about-body">
                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Наименование компании</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputText v-else type="text" class="crm-sidebar-about-input" v-model="newCompnay.name" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Полное аименование</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputText v-else type="text" class="crm-sidebar-about-input"
                                v-model="newCompnay.ful_name" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Отрасль</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputText v-else type="text" class="crm-sidebar-about-input"
                                v-model="newCompnay.industry" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Годовой оборот</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputNumber v-else inputId="integeronly" class="crm-sidebar-about-input-int"
                                v-model="newCompnay.revenue" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Имя представителя</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputText v-else type="text" class="crm-sidebar-about-input"
                                v-model="newCompnay.representative_name" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Фамилия представителя</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputText v-else type="text" class="crm-sidebar-about-input"
                                v-model="newCompnay.representative_last_name" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Телефон</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputMask id="phone" unmask="true" mask="+9 (999) 999-9999" inputId="withoutgrouping"
                                :useGrouping="false" class="crm-sidebar-about-input-int" v-model="newCompnay.phone" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">E-mail</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputText v-else type="text" class="crm-sidebar-about-input" v-model="newCompnay.email" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">Адресс</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputText v-else type="text" class="crm-sidebar-about-input"
                                v-model="newCompnay.address" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">ИНН</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputNumber v-else inputId="withoutgrouping" :useGrouping="false"
                                class="crm-sidebar-about-input-int" v-model="newCompnay.inn" />
                        </div>
                    </div>

                    <div class="crm-sidebar-info-item">
                        <div class="crm-sidebar-info-item-title">КПП</div>
                        <div class="crm-sidebar-info-item-value">
                            <Skeleton v-if="isLoading" class="mb-2" height="32px" width="244px"></Skeleton>
                            <InputNumber v-else inputId="withoutgrouping" :useGrouping="false"
                                class="crm-sidebar-about-input-int" v-model="newCompnay.kpp" />
                        </div>
                    </div>

                </div>

            </div>
        </div>
        <div class="crm-sidebar-about-create-btns">
            <Button @click="createNewCompany" :disabled="!canCreate"> Cохранить </Button>
            <Button class="ml-10">Отмена</Button>
        </div>
    </div>
</template>

<style>
.crm-sidebar-about-create-btns {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 70px;
    background-color: white;
    z-index: 120;
    border-radius: 16px 16px 0 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}

.crm-sidebar-about-create-bg {
    position: absolute;
    top: -1px;
    left: -1px;
    border-radius: 16px 0 0 16px;
    width: calc(100% + 2px);
    height: calc(100% + 2px);
    background-color: rgba(0, 0, 0, 0.116);
    z-index: 100;
}

.crm-sidebar-about {
    position: relative;
    z-index: 110;
}

.p-sidebar-close.p-sidebar-icon.p-link {
    z-index: 1000;
}
</style>