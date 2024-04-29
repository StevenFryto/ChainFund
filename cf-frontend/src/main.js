import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import Elementplus from 'element-plus'
import 'element-plus/dist/index.css'

const app =  createApp(App)

// // 初始化 currentUserId
// let currentUserId = 1;

// // 获取 currentUserId 方法
// app.provide('getCurrentUserId', () => currentUserId);

// // 修改 currentUserId 方法
// app.provide('setCurrentUserId', (newId) => {
//     currentUserId = newId;
// })


app.use(store).use(router)
app.use(Elementplus)
app.mount('#app')