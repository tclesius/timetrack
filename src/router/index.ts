import { createRouter, createWebHistory } from 'vue-router';
import {useAuthStore} from "@/stores/authStore";




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
      beforeEnter: async (to, from, next) => {
        // Check if the user is authenticated
        const {applyLocalStorageToken} = useAuthStore()
        if (await applyLocalStorageToken()) {
          next();
        } else {
          // If not authenticated, redirect to the 'login' route or any other route of your choice
          next('/login');
        }
      }
    },
  ],
});

export default router;
