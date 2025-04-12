import DealView from "@/views/crm/DealView.vue";
import DealDetail from "@/components/crm/deal/DealDetail.vue";

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
      icon: "mdi mdi-application-edit-outline",
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
        component: DealView,
        children: [
          {
            path: "/crm/deal/details/:idDeal(\\d+)/",
            component: DealDetail,
          },
        ],
      },
    ],
  },
  {
    path: "/settings/",
    name: "settings",
    meta: {
      title: "CRM",
      display: true,
      icon: "mdi mdi-application-edit-outline",
    },
    component: () => import("@/views/settings/SettingsView.vue"),
    children: [
      {
        path: "user-field/:entity/",
        name: "uf-deal",
        component: () => import("@/components/settings/UserField.vue"),
      },
      {
        path: "user-field/:entity/:field_name/",
        name: "uf-deal-detail",
        component: () => import("@/components/settings/UserFieldDetail.vue"),
      },
    ],
  },


];

export default routes;
