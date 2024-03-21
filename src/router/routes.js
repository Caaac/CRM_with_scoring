import HomeView from '../views/HomeView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        meta: {
            title: 'CRM'
        },
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        meta: {
            title: 'Hmm...'
        },
        component: () => import('@/views/AboutView.vue')
    }
]

export default routes