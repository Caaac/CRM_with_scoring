import CRMView from '@/views/CRMView.vue'
import ContactView from '@/views/ContactView.vue'
import CompanyView from '@/views/CompanyView.vue'
import ReportsView from '@/views/ReportsView.vue'
import UserAccount from '@/views/user/UserAccount.vue'
import SidebarCard from '@/components/crm/SidebarCard.vue'
import ReportDetail from '@/components/report/ReportDetail.vue'
import SidebarContact from '@/components/contact/SidebarContact.vue'
import SidebarCompany from '@/components/company/SidebarCompany.vue'

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
      },
      {
        path: 'company/details/:idCompany(\\d+)/',
        component: SidebarCompany
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
    component: CompanyView,
    children: [
      {
        path: 'details/:idCompany(\\d+)/',
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
    path: '/report/',
    name: 'report',
    meta: {
      title: 'Отчеты',
      display: true,
      icon: 'mdi mdi-chart-bar'
    },
    component: ReportsView,
  },
  {
    path: '/report/details/:idReport(\\d+)/',
    name: 'reportDetail',
    meta: {
      title: 'Отчет',
      display: false,
      icon: 'mdi mdi-chart-bar'
    },
    component: ReportDetail,
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
      display: false
    },
    component: Test,
  }
]

export default routes
