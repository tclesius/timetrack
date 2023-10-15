import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import {OpenAPI} from "@/client";

OpenAPI.BASE = "http://127.0.0.1:8000"

const app = createApp(App)
export const pinia = createPinia()
app.use(pinia)
app.use(router)

app.mount('#app')
