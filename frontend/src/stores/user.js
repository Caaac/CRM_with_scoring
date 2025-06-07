/* Vue */
import { ref } from "vue";
/* Pinia */
import { defineStore } from "pinia";

export const userStore = defineStore("user", () => {

  const params = ref({
    account: {
      id: 1,
    },
  });


  return {
    /* Store vars */
    params
    /* Store methods */
  };
});
