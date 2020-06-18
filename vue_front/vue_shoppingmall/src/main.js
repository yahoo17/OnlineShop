import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'

// 导入组件
import TreeTable from 'vue-table-with-tree-grid'
// 导入全局样式表
import './assets/css/global.css'
// 导入axios包
import axios from 'axios'

//  配置请求根路径
axios.defaults.baseURL = 'http://127.0.0.1:5000/'
Vue.prototype.$http = axios
Vue.config.productionTip = false

// 注册树形结构为全局可用的组件
Vue.component('tree-table', TreeTable)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
