import { defineStore } from "pinia";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";

export const userFieldStore = defineStore("userField", () => {

  const router = useRouter();
  const route = useRoute();

  const validTypes = ref([
    {
      type: "string",
      options: {
        title: "Строка",
      },
    },
    {
      type: "number",
      options: {
        title: "Число",
      },
    },
    {
      type: "integer",
      options: {
        title: "Целое число",
      },
    },
    {
      type: "boolean",
      options: {
        title: "Да/Нет",
      },
    },
    {
      type: "date",
      options: {
        title: "Дата",
      },
    },
    {
      type: "datetime",
      options: {
        title: "Дата со временем",
      },
    },
    {
      type: "enumirate",
      options: {
        title: "Список",
      },
    },
  ]);

  const params = ref({
    fields: [],
    detailData: {},
  });

  const init = () => {
    Rest.callMethod("crm.userField.list", {}, (response) => {
      params.value.fields = response.data;
    });
  };

  const initDetail = (options) => {
    Rest.callMethod(
      "crm.userField.get",
      { field_name: options.field_name },
      (response) => {
        params.value.detailData = response.data;
      }
    );
  };

  const resetDetail = () => {
    params.value.detailData = {};
  };

  // const addUserField = async () => {
  //   return new Promise((resolve, reject) => {
  //     Rest.callMethod(
  //       "crm.userField.add",
  //       params.value.detailData,
  //       (response) => {
  //         console.log(response);
  //         if (response.data.status == "success") {
  //           console.log(1);
  //           resolve(response.data);
  //         }
  //         console.log(2);
  //         reject(response.data);
  //       }
  //     );
  //   })
  // };

  const addUserField = async () => {
    Rest.callMethod(
      "crm.userField.add",
      params.value.detailData,
      (response) => {
        if (response.data.status != "success") return
        params.value.detailData = response.data.data;
      }
    );
  };

  const updateUserField = async () => {
    console.log(params.value.detailData);
    return new Promise((rs, rj) => {
      Rest.callMethod(
        "crm.userField.update",
        params.value.detailData,
        (response) => {
          rs(rs)
        }
      );
    })

  };

  const deleteUserField = () => {
    Rest.callMethod(
      "crm.userField.delete",
      { id: params.value.detailData.id },
      (response) => { router.push({ name: "uf-deal" }) }
    );
  }

  return {
    params,
    validTypes,
    init,
    initDetail,
    resetDetail,
    addUserField,
    updateUserField,
    deleteUserField,
  };
});
