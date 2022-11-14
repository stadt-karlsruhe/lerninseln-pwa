import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import PickUp from '../views/PickUp.vue'
import IntroView from '../views/IntroView.vue'
import MapView from '../views/MapView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/intro'
  },
  {
    path: '/',
    component: PickUp,
    children: [
      {
        path: '',
        redirect: '/intro'
      },
      {
        path: 'intro',
        component: IntroView
        
      },
      {
        path: 'map',
        component: MapView
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
