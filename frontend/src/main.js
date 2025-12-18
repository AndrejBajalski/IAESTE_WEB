import { createApp } from 'vue'
import App from './App.vue'
import { router } from './routing/router.js'

const app = createApp(App)

app.use(router)

app.mount('#app')
