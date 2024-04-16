import './assets/main.css'
import 'primevue/resources/themes/aura-light-indigo/theme.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';
import App from './App.vue'
import Router from './router'
import Store from '@/stores/index'


const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(Router)
app.use(Store)
app.use(PrimeVue)

app.mount('#app')
