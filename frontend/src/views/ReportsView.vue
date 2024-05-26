<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter()

const period = ref(null)
const showComment = ref(false)

</script>

<template>
    <div class="crm-report">
        <div class="crm-report-header">
            <div class="crm-reposrt-celendar">
                Выберете отчетный месяц
                <Calendar v-model="period" view="month" dateFormat="MM yy" />
            </div>
            <Button class="mb-1" severity="secondary" raised text outlined >Сгенерировать отчет</Button>
        </div>
        <div class="crm-report-body grid grid-cols-4 gap-4">
            <div class="crm-report-item w-full">
                <div class="crm-report-item-wrapper">
                    <div v-if="!showComment" class="crm-report-front">
                        <div class="crm-report-item-title" @click="router.push({ path: `/report/details/${0}/` })">Отчет за May 2024</div>
                        <div class="crm-report-item-resp">Alexandr Vedyaev</div>
                        <div class="crm-report-item-info">Обслужено клиентов: <label>3</label></div>                    
                        <div class="crm-report-item-info">Обслужено компаний: <label>2</label></div>                    
                        <div class="crm-report-item-info">Оборот: <label>1055600 ₽</label></div>  
                        <div class="crm-report-item-info"><span class="mdi mdi-comment-processing-outline" @click="showComment=true"></span></div>
                    </div>
                    <div v-else class="crm-report-back">
                        <div>
                            <div class="crm-report-item-title">Комментарий</div>
                            <div class="crm-report-item-comment">В текущем месяце удалось добиться рекондного оборота с начала текущего года (2024)</div>
                        </div>
                        <div class="crm-report-item-info"><span class="mdi mdi-page-previous-outline" @click="showComment=false"></span></div>
                    </div>                  
                </div>
            </div>
            <!-- <div class="crm-report-item w-full"></div>
            <div class="crm-report-item w-full"></div>
            <div class="crm-report-item w-full"></div>
            <div class="crm-report-item w-full"></div>
            <div class="crm-report-item w-full"></div>
            <div class="crm-report-item w-full"></div> -->
        </div>
    </div>
</template>

<style>
.crm-report-header {
    display: inline-flex;
    justify-content: center;
    align-items: end;
    margin-bottom: 30px;
}

.crm-report-header button {
    height: 40px;
}

.crm-reposrt-celendar {
    display: flex;
    flex-direction: column;
    font-size: 15px;
    width: 350px;
    color: var(--lable-color);
} 

.crm-reposrt-celendar input {
    max-width: 300px;
}

.crm-report-body {}

.crm-report-item {
    height: 200px;
    background-color: rgb(255, 255, 255);
    border-radius: 16px;
    box-shadow: 3px 3px 2px 2px rgba(212, 212, 212, 0.651);
}

.crm-report-item-wrapper {
    padding: 10px 15px;
    height: 100%;
}

.crm-report-item-title {
    font-weight: bold;
    color: #334155;
    font-size: 20px;
}

.crm-report .crm-report-front .crm-report-item-title{
    cursor: pointer;
}

.crm-report .crm-report-front .crm-report-item-title:hover {
    text-decoration: underline;
}

.crm-report-item-resp {
    color: var(--lable-color);
    font-size: 14px;
    line-height: 14px;
    margin-bottom: 20px;
}


.crm-report-item-info {}

.crm-report-item-info label {
    font-weight: 600;
}

.crm-report-item-info span {
    font-size: 25px;
    color: var(--text-color-secondary);
}

.crm-report-item-info,
.crm-report-item-info label {
    font-size: 16px;
    color: #465161;
}

.crm-report-back {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}


.crm-report-back > .crm-report-item-title {
    font-size: 16px;
}

.crm-report-item-comment {
    font-size: small;
    text-align: justify;
    color: #515d6e;
}

</style>