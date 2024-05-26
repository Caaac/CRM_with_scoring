<script setup>
import { ref, onMounted } from "vue";

onMounted(() => {
    chartData_doughnut.value = setChartData_chartOptions();
    chartOptions_doughnut.value = setChartOptions_chartOptions();
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
});

const chartData_doughnut = ref();
const chartOptions_doughnut = ref(null);
const chartData = ref();
const chartOptions = ref();

const setChartData_chartOptions = () => {
    const documentStyle = getComputedStyle(document.body);

    return {
        labels: ['Реклама в интернете', 'Партнерская программа', 'Рекомендация коллеги'],
        datasets: [
            {
                data: [2, 3, 1],
                backgroundColor: [documentStyle.getPropertyValue('--cyan-500'), documentStyle.getPropertyValue('--orange-500'), documentStyle.getPropertyValue('--gray-500')],
                hoverBackgroundColor: [documentStyle.getPropertyValue('--cyan-400'), documentStyle.getPropertyValue('--orange-400'), documentStyle.getPropertyValue('--gray-400')]
            }
        ]
    };
};

const setChartOptions_chartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');

    return {
        plugins: {
            legend: {
                labels: {
                    cutout: '60%',
                    color: textColor
                }
            }
        }
    };
};

const setChartData = () => {
    return {
        labels: ['Юридические лица', 'Физические лица'],
        datasets: [
            {
                label: 'Оборот',
                data: [710600, 345000],
                backgroundColor: ['rgba(249, 115, 22, 0.2)', 'rgba(6, 182, 212, 0.2)'],
                borderColor: ['rgb(249, 115, 22)', 'rgb(6, 182, 212)'],
                borderWidth: 2
            }
        ]
    };
};
const setChartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
    const surfaceBorder = documentStyle.getPropertyValue('--surface-border');

    return {
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            },
            y: {
                beginAtZero: true,
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder
                }
            }
        }
    };
}

</script>

<template>
    <div class="crm-report-detail">
        <div class="flex">
            <div class="w-1/4">
                <div class="crm-report-item w-full mb-6">
                    <div class="crm-report-item-wrapper">
                        <div class="crm-report-front">
                            <div class="crm-report-item-title">Отчет за May 2024</div>
                            <div class="crm-report-item-resp">Alexandr Vedyaev</div>
                            <div class="crm-report-item-info">Обслужено клиентов: <label>3</label></div>
                            <div class="crm-report-item-info">Обслужено компаний: <label>2</label></div>
                            <div class="crm-report-item-info">Оборот: <label>1055600 ₽</label></div>
                        </div>
                    </div>
                </div>
                <div class="crm-report-item w-full">
                    <div class="crm-report-item-wrapper">
                        <div class="crm-report-back">
                            <div>
                                <div class="crm-report-item-title"><span>Комментарий</span><label>редактировать</label></div>
                                <div class="crm-report-item-comment">В текущем месяце удалось добиться рекондного оборота с начала текущего года (2024)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-3/4 flex justify-around">
                <Chart type="doughnut" :data="chartData_doughnut" :options="chartOptions_doughnut" class="w-1/3 flex flex-wrap content-center" />
                <Chart type="bar" :data="chartData" :options="chartOptions" class="w-1/2 flex flex-wrap content-center" />
            </div>
        </div>
    </div>
</template>

<style>
.crm-report-back .crm-report-item-title {
    display: flex;
    justify-content: space-between;
}

.crm-report-item-title label {
    font-size: 12px;
    color: var(--lable-color);
    vertical-align:bottom;
    vertical-align: text-bottom;
}
</style>