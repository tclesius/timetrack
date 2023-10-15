import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Route the root URL to LoginView
    {
      path: '/',
      redirect: '/login',
    },
    // Define the route for LoginView
    {
      path: '/login',
      name: 'LoginView',
      component: () => import('@/views/LoginView.vue'),
    },
    // Define the route for RegisterView
    {
      path: '/register',
      name: 'RegisterView',
      component: () => import('@/views/RegisterView.vue'),

    },
    {
      path: '/dashboard',
      name: 'DashboardView',
      component: () => import('@/views/DashboardView.vue'),
    },
  ],
});

export default router;
