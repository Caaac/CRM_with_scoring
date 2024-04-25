import ContactView from '@/views/ContactView.vue'
import CRMView from '@/views/CRMView.vue'
import SidebarContact from '@/components/crm/SidebarContact.vue'
import SidebarCard from '@/components/crm/SidebarCard.vue'
import UserAccount from '@/views/user/UserAccount.vue'

const routes = [
  {
    path: '/crm/',
    name: 'crm',
    meta: {
      title: 'CRM',
      display: true,
      icon: 'mdi mdi-application-edit-outline'
    },
    component: CRMView,
    children: [
      {
        path: ':idDeal(\\d+)/',
        component: SidebarCard
      },
      {
        path: 'contact/:idContact(\\d+)/',
        component: SidebarContact
      }
    ]
  },
  {
    path: '/company/',
    name: 'company',
    meta: {
      title: 'Компании',
      display: true,
      icon: 'mdi mdi-domain'
    },
    component: () => import('@/views/AboutView.vue')
  },
  {
    path: '/contact/',
    name: 'contact',
    meta: {
      title: 'Контакты',
      display: true,
      icon: 'mdi mdi-account-group'
    },
    component: ContactView,
    children: [
      {
        path: ':idContact(\\d+)/',
        component: SidebarContact
      }
    ]
  },
  {
    path: '/user/account/',
    name: 'userAccount',
    meta: {
      title: 'Личный кабинет',
      display: false
    },
    component: UserAccount,
  }
]

export default routes
