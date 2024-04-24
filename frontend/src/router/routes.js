import ContactView from '@/views/ContactView.vue'
import CRMView from '@/views/CRMView.vue'
import SidebarContact from '@/components/crm/SidebarContact.vue'

const routes = [
    {
        path: '/crm/',
        name: 'crm',
        meta: {
            title: 'CRM',
            icon: 'mdi mdi-application-edit-outline',
        },
        component: CRMView
    },
    {
        path: '/about/',
        name: 'about',
        meta: {
            title: 'About'
        },
        component: () => import('@/views/AboutView.vue')
    },
    {
        path: '/contact/',
        name: 'contact',
        meta: {
            title: 'Контакты'
        },
        component: ContactView,
        children: [
            {
                path: ':idContact(\\d+)',
                component: SidebarContact,
            }
        ]
    },
]

export default routes