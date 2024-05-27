import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    component: () =>
      import('../views/Index.vue'),
    children: [
      {
        path: '/topology',
        children: [
          {
            path: '/topology/control',
            component: () =>
              import("../views/topology/control.vue")
          }
        ]
      },
      {
        path: '/monitor',
        component: () =>
          import("../views/monitor.vue")
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
