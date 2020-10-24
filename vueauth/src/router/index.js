
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Login from '@/views/Login.vue';
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/consulta',
    name: 'Consulta',
    component: () => import('../views/Consulta.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/ingreso',
    name: 'Ingreso',
    component: () => import('../views/Ingreso.vue')
  },
  {
    path: '/devoluciones',
    name: 'Devoluciones',
    component: () => import('../views/Devoluciones.vue')
  },
  {
    path: '/imagen',
    name: 'Imagen',
    component: () => import('../views/Imagen.vue')
  },
  {
    path: '/inicio',
    name: 'Inicio',
    component: () => import('../views/Inicio.vue')
  },
  {
    path: '/registro',
    name: 'Registro',
    component: () => import('../views/Registro.vue')
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
