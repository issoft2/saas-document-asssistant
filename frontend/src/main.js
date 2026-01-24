import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import { Aura } from '@primeuix/themes'          // or Lara, Nora, etc.

import ToastService from 'primevue/toastservice'
import Toast from 'primevue/toast'

import App from './App.vue'
import router from './router'

import 'primeicons/primeicons.css'               // icons only

const app = createApp(App)

app.use(router)

app.use(PrimeVue, {
  theme: {
    preset: Aura,                               // pick one preset
    options: {
      darkModeSelector: '.dark'                 // optional, if you use dark mode
    }
  }
})

app.use(ToastService)
app.component('Toast', Toast)

app.mount('#app')
