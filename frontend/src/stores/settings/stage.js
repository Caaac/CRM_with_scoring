import { ref } from "vue";
import { defineStore } from "pinia";

export const stageStore = defineStore("stage", () => {

  const params = ref({
    stages: [],
  });

  const init = async () => {
    return new Promise((rs, rj) => {
      Rest.callMethod("crm.status.list", { entity_id: 'DEAL_STAGE' }, (response) => {
        if (response.status >= 400) rj(response.data);
        params.value.stages = response.data;
        sortStage()
        rs(response.data);
      });
    })
  };

  const updateStage = async (id, data) => {
    return new Promise((rs, rj) => {
      Rest.callMethod("crm.status.update", { id: id, data: data }, (response) => {
        rs(response.data)
      });
    })
  }

  const add = async (data) => {
    return new Promise((rs, rj) => {
      Rest.callMethod("crm.status.add", { data: data }, (response) => {
        rs(response.data)
      });
    })
  }

  const deleteStage = async (id) => {
    return new Promise((rs, rj) => {
      Rest.callMethod("crm.status.delete", { id: id }, (response) => {
        rs(response.data)
      });
    })
  }

  const addStage = async () => {
    return new Promise(async (rs, rj) => {
      await add(
        {
          id: 0,
          title: "Новая стадия",
          xml_id: null,
          sort: 100,
          entity_id: 'DEAL_STAGE',
          semantics: 'P',
          color: "#39cbf7"
        }
      )
      rs(true)
    })
  }

  const sortStage = () => {
    params.value.stages.sort((a, b) => a.sort - b.sort);
  }

  return {
    params,
    init,
    add,
    updateStage,
    addStage,
    deleteStage,
  };
});
