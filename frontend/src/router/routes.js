import ContactView from '@/views/ContactView.vue'
import CRMView from '@/views/CRMView.vue'
import SidebarContact from '@/components/contact/SidebarContact.vue'
import SidebarCompany from '@/components/company/SidebarCompany.vue'
import SidebarCard from '@/components/crm/SidebarCard.vue'
import UserAccount from '@/views/user/UserAccount.vue'

import Test from '@/views/Test.vue'

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
        path: 'contact/details/:idContact(\\d+)/',
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
    component: () => import('@/views/AboutView.vue'),
    children: [
      {
        path: 'details/:idContact(\\d+)/',
        component: SidebarCompany
      }
    ]
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
        path: 'details/:idContact(\\d+)/',
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
  },
  {
    path: '/test/',
    name: 'test',
    meta: {
      title: 'Тестовая страница',
      display: true
    },
    component: Test,
  }
]

export default routes
