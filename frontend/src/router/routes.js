const routes = [
  {
    path: "/",
    name: "home",
    redirect: (to) => {
      return { path: "/crm/" };
    },
  },
  {
    path: "/crm/",
    name: "crm",
    meta: {
      title: "CRM",
      display: true,
      sort: 100,
      icon: "mdi mdi-chart-box-multiple-outline",
    },
    redirect: (to) => ({ path: "/crm/deal/kanban/" }),
    children: [
      {
        path: "deal/",
        name: "deal",
        // component: // TODO list of deal
        redirect: (to) => ({ path: "/crm/deal/kanban/" }),
      },
      {
        path: "deal/kanban/",
        component: () => import("@/views/crm/DealView.vue"),
        children: [
          {
            path: "/crm/deal/details/:idDeal(\\d+)/",
            component: () => import("@/components/crm/deal/DealDetail.vue"),
          },
        ],
      },
      {
        path: "contact/",
        name: "contact",
        meta: {
          title: "Контакты",
          display: true,
          sort: 200,
          icon: "mdi mdi-account-group",
        },
        redirect: (to) => ({ path: "/crm/contact/list/" }),
        children: [
          {
            path: "list/",
            name: "contact-list",
            // component: ContactView,
            component: () => import("@/views/crm/ContactView.vue"),
            children: [
              // {
              //   path: "/crm/contact/details/:idContact(\\d+)/",
              //   component: ContactDetail,
              // },
            ]
          },
        ],
      },
    ],
  },
  {
    path: '/reports/',
    name: 'reports',
    meta: {
      title: 'Отчеты',
      display: true,
      sort: 300,
      icon: 'mdi mdi-chart-bar',
    },
    // component: () => import("@/views/reports/ReportsView.vue"),
  },
  {
    path: "/settings/",
    name: "settings",
    meta: {
      display: false,
    },
    component: () => import("@/views/settings/SettingsView.vue"),
    children: [
      {
        path: "user-field/:entity/",
        name: "uf-deal",
        component: () => import("@/components/settings/crm/user-field/UserField.vue"),
      },
      {
        path: "user-field/:entity/:field_name/",
        name: "uf-deal-detail",
        component: () => import("@/components/settings/crm/user-field/UserFieldDetail.vue"),
      },
      {
        path: "kanban/stages/",
        name: "uf-kanban-stage",
        component: () => import("@/components/settings/crm/kanban/Stage.vue"),
      },
    ],
  },
];

export default routes;
