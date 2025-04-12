import '@/assets/main.scss'
import 'primeicons/primeicons.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import ConfirmationService from 'primevue/confirmationservice';

import App from './App.vue'
import router from './router'

import Axios from '@/api/axios'
import {RestService} from '@/api/rest'
import '@/mixins/index'

window.Rest = new RestService()

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      darkModeSelector: '.my-app-dark'
    }
  }
});
app.use(ConfirmationService);
app.provide('$axios', Axios)
app.mount('#app')