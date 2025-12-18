import { createWebHistory, createRouter } from 'vue-router'

  const routes = [
    {path: '/', component: () => import('@/pages/Internships.vue')},
  ]

  export const router = createRouter({
    history: createWebHistory(),
    routes,
  })

