import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  // {
  //   path: '/',
  //   name: '/',
  //   component: () => import('../views/Combine.vue'),
  // },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/design',
    name: 'design',
    component: () => import('../views/Design.vue'),
  },
  {
    path: '/combine',
    name: './combine',
    component: () => import('../views/Combine.vue'),
  },
  {
    path: '/firstPage',
    name: './firstPage',
    component: () => import('../views/FirstPage.vue'),
  }, {
    path: '/secondPage',
    name: './secondPage',
    component: () => import('../views/SecondPage.vue'),
  }, {
    path: '/SecondPage_1',
    name: './SecondPage_1',
    component: () => import('../views/SecondPage_1.vue'),
  },
  {
    path: '/thirdPage',
    name: './thirdPage',
    component: () => import('../views/ThirdPage.vue'),
  },
  {
    path: '/ThirdPage-2',
    name: './ThirdPage-2',
    component: () => import('../views/ThirdPage-2.vue'),
  }, {
    path: '/FourthPage',
    name: './FourthPage',
    component: () => import('../views/FourthPage.vue'),
  }, {
    path: '/FourthPage_2',
    name: './FourthPage_2',
    component: () => import('../views/FourthPage_2.vue'),
  }, {
    path: '/FourthPage_3',
    name: './FourthPage_3',
    component: () => import('../views/FourthPage_3.vue'),
  }, {
    path: '/FifthPage',
    name: './FifthPage',
    component: () => import('../views/FifthPage.vue'),
  }, {
    path: '/2_1right',
    name: './2_1right',
    component: () => import('../views/2_1right.vue'),
  }, {
    path: '/map_sxq',
    name: './map_sxq',
    component: () => import('../views/map_sxq.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});


export default router;
