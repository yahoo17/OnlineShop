import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Cate from '../components/goods/Cate.vue'
import Users from '../components/user/Users.vue'
Vue.use(Router)
export default new Router({
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    {
      path: '/home',
      component: Home,
      children: [
        { path: '/categories', component: Cate },
        { path: '/users', component: Users }
      ]
    }

  ]
})
