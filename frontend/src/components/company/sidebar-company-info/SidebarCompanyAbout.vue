<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'

const store = rootStore()
const router = useRouter()
const route = useRoute()

const isEddit = ref(false)
const {companyDetail} = storeToRefs(store.companyStore())

watch(isEddit, (n, o) => {
  if (n) return
  store.companyStore().updateCompany(route.params.idCompany)
})
</script>

<template>
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
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="companyDetail.name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.name }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Полное аименование</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="companyDetail.ful_name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ companyDetail?.ful_name }}</div>
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
  color: #adb5bd;
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

.crm-sidebar-about-header span {
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
</style>