import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);


  const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "about" */ '../src/components/Home.vue'),
  },
  {
    path: '/transfert-learning',
    name: 'transfert-learning',
    component: () => import(/* webpackChunkName: "about" */ '@/components/TransfertLearning.vue'),
  },
  {
    path: '/cnn',
    name: 'cnn',
    component: () => import(/* webpackChunkName: "about" */ '../src/components/CNN.vue'),
  },
  {
    path: "*",
    redirect: "/"
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  window.scrollTo(0, 0)
  next()
})

export default router
