<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'
import { useToast } from 'primevue/usetoast'

const store = rootStore()
const router = useRouter()
const route = useRoute()
const toast = useToast()

const isCreatePage = ref(false)
const isEddit = ref(false)
const {companyDetail} = storeToRefs(store.companyStore())
const { isLoading } = storeToRefs(store.settingsStore())

onMounted(() => {
    if (route.params.idCompany == 1) {
        isCreatePage.value = true
        isEddit.value = true

        // const tml = store.companyStore().companies.shift()
        // Object.keys(tml).map(key => {
        // if (key == 'id') delete tml[key]
        // if (key == 'id') tml[key] = 0
        // else if (tml[key] instanceof Array) tml[key] = []
        // else tml[key] = null
        // })
        // // store.companyStore().companies

        let companyTml
    }
})

watch(isEddit, (n, o) => {
  if (n) return
  store.companyStore().updateCompany(route.params.idCompany)
})
</script>

<template>
        {{ isCreatePage }}
        <div v-if="isCreatePage" class="crm-sidebar-about-create-bg"></div>
        <div class="crm-sidebar-about">
        <div class="crm-sidebar-about-wrapper">
            <div class="crm-sidebar-about-header">
                <span>О компании</span>
                <span @click="isEddit = !isEddit" v-show="!isCreatePage" class="hover:underline cursor-pointer">{{ isEddit ? 'сохранить' :
                'изменить' }}</span>
            </div>

            <Divider />

            <div class="crm-sidebar-about-body">
                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Наименование компании</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="companyDetail.name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.name }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Полное аименование</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="companyDetail.full_name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.full_name }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Отрасль</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="companyDetail.industry" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.industry }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Годовой оборот</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputNumber inputId="integeronly" class="crm-sidebar-about-input-int"
                            v-model="companyDetail.revenue" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.revenue }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Имя представителя</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input"
                            v-model="companyDetail.representative_name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.representative_name }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Фамилия представителя</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input"
                            v-model="companyDetail.representative_last_name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.representative_last_name }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Телефон</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputMask id="phone" unmask="true" mask="+9 (999) 999-9999" inputId="withoutgrouping" :useGrouping="false" class="crm-sidebar-about-input-int"
                            v-model="companyDetail.phone" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.phone }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">E-mail</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="companyDetail.email" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.email }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Адресс</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="companyDetail.address" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.address }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">ИНН</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputNumber inputId="withoutgrouping" :useGrouping="false" class="crm-sidebar-about-input-int"
                            v-model="companyDetail.inn" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.inn }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">КПП</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputNumber inputId="withoutgrouping" :useGrouping="false" class="crm-sidebar-about-input-int"
                            v-model="companyDetail.kpp" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.kpp }}</div>
                </div>
            </div>

        </div>
    </div>
    <div v-if="isCreatePage" class="crm-sidebar-about-create-btns">
            <Button @click="createNewCompany" :disabled="!canCreate"> Cохранить </Button>
            <Button class="ml-10">Отмена</Button>
        </div>
</template>

<style>
.crm-sidebar-about-input,
.crm-sidebar-info-item #phone.p-inputtext,
.crm-sidebar-about-input .p-dropdown-label,
.crm-sidebar-about-input-int .p-inputtext.p-component.p-inputnumber-input {
  padding: 2px 12px;
  width: 100%; 
    border: 0px;
}

.crm-sidebar-info-item-title {
  font-size: 13px;
  color: var(--lable-color);
}

.crm-sidebar-info-item-value {
  margin-left: 20px;
}

.crm-sidebar-info-item {
  margin-bottom: 10px;
}

.crm-sidebar-info-item:last-child {
  margin-bottom: 0px;
}

.crm-sidebar-about-body {
  padding: 15px;
}

.crm-sidebar-about-header {
  display: flex;
  justify-content: space-between;
}

.crm-sidebar-about-header span,
.crm-sidebar-about-header button {
  margin-left: 10px;
  margin-right: 10px;
  margin-bottom: 5px;
  font-size: 13px;
  color: #6c757d;
}

.crm-sidebar-about {
  width: 41%;
  border-radius: 16px;
  background: white;
  margin-bottom: 20px;
}


.crm-sidebar-about:last-child {
  margin-bottom: 0px;
}

.crm-sidebar-about-wrapper {
  padding: 10px;
}

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