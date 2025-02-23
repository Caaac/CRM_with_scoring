import DealView from "@/views/DealView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    redirect: to => {
      return { path: "/crm/" };
    }
  },
  {
    path: "/crm/",
    name: "crm",
    meta: {
      title: "CRM",
      display: true,
      icon: "mdi mdi-application-edit-outline",
    },
    redirect: to => ({path: '/crm/deal/kanban/'}),
    children: [
      {
        path: "deal/",
        // component: // TODO list of deal
        redirect: to => ({path: '/crm/deal/kanban/'})
      },
      {
        path: "deal/kanban/",
        component: DealView
      }
    ],
  },
];

export default routes