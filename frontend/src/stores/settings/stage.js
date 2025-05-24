import { defineStore } from "pinia";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";

export const userFieldStore = defineStore("userField", () => {

  const router = useRouter();
  const route = useRoute();

  const params = ref({
    fields: [],
    detailData: {},
  });

  const init = () => {
    Rest.callMethod("crm.userField.list", {}, (response) => {
      params.value.fields = response.data;
    });
  };

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
