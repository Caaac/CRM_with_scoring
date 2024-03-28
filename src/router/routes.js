import HomeView from '../views/HomeView.vue'
import CRMView from '@/views/CRMView.vue'

const routes = [
    {
        path: '/',
        name: 'crm',
        meta: {
            title: 'CRM',
            icon: 'mdi mdi-application-edit-outline',
        },
        component: CRMView
    },
    {
        path: '/about',
        name: 'about',
        meta: {
            title: 'About'
        },
        component: () => import('@/views/AboutView.vue')
    },
    {
        path: '/home',
        name: 'home',
        meta: {
            title: 'Home'
        },
        component: HomeView
    },
]

export default routes