import { createWebHistory, createRouter } from 'vue-router'

  const routes = [
    {path: '/', name: 'Home', component: () => import('@/pages/Home.vue')},
    {path: '/internships', name: 'Internships', component: () => import('@/pages/Internships.vue')},
    {path: '/internships/apply/:id', name: 'ApplyForm', component: () => import('@/pages/InternshipApplication.vue'), props: true},
    {path: '/internships/applications', name: 'AllApplications', component: () => import('@/pages/AllApplications.vue')}
  ]

  export const router = createRouter({
    history: createWebHistory(),
    routes,
  })

