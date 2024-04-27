<script setup>
import { RouterView, useRouter } from 'vue-router'; const router = useRouter()
import { ref } from 'vue'
import { storeToRefs } from 'pinia';
import { rootStore } from '@/stores'

const store = rootStore()

const { isLoading } = storeToRefs(store.settingsStore())

const ll = ref([
  {
    id: 11,
    name: 'James Butt',
    country: {
      name: 'Algeria',
      code: 'dz'
    },
    company: 'Benton, John B Jr',
    date: '2015-09-13',
    status: 'unqualified',
    verified: true,
    activity: 17,
    representative: {
      name: 'Ioni Bowcher',
      image: 'ionibowcher.png'
    },
    balance: 70663
  },
  {
    id: 12,
    name: 'Josephine Darakjy',
    country: {
      name: 'Egypt',
      code: 'eg'
    },
    company: 'Chanay, Jeffrey A Esq',
    date: '2019-02-09',
    status: 'proposal',
    verified: true,
    activity: 0,
    representative: {
      name: 'Amy Elsner',
      image: 'amyelsner.png'
    },
    balance: 82429
  },
  {
    id: 13,
    name: 'Art Venere',
    country: {
      name: 'Panama',
      code: 'pa'
    },
    company: 'Chemel, James L Cpa',
    date: '2017-05-13',
    status: 'qualified',
    verified: false,
    activity: 63,
    representative: {
      name: 'Asiya Javayant',
      image: 'asiyajavayant.png'
    },
    balance: 28334
  },
  {
    id: 14,
    name: 'Lenna Paprocki',
    country: {
      name: 'Slovenia',
      code: 'si'
    },
    company: 'Feltz Printing Service',
    date: '2020-09-15',
    status: 'new',
    verified: false,
    activity: 37,
    representative: {
      name: 'Xuxue Feng',
      image: 'xuxuefeng.png'
    },
    balance: 88521
  },
  {
    id: 15,
    name: 'Donette Foller',
    country: {
      name: 'South Africa',
      code: 'za'
    },
    company: 'Printing Dimensions',
    date: '2016-05-20',
    status: 'proposal',
    verified: true,
    activity: 33,
    representative: {
      name: 'Asiya Javayant',
      image: 'asiyajavayant.png'
    },
    balance: 93905
  },
  {
    id: 16,
    name: 'Simona Morasca',
    country: {
      name: 'Egypt',
      code: 'eg'
    },
    company: 'Chapman, Ross E Esq',
    date: '2018-02-16',
    status: 'qualified',
    verified: false,
    activity: 68,
    representative: {
      name: 'Ivan Magalhaes',
      image: 'ivanmagalhaes.png'
    },
    balance: 50041
  },
  {
    id: 17,
    name: 'Mitsue Tollner',
    country: {
      name: 'Paraguay',
      code: 'py'
    },
    company: 'Morlong Associates',
    date: '2018-02-19',
    status: 'renewal',
    verified: true,
    activity: 54,
    representative: {
      name: 'Ivan Magalhaes',
      image: 'ivanmagalhaes.png'
    },
    balance: 58706
  },
  {
    id: 18,
    name: 'Leota Dilliard',
    country: {
      name: 'Serbia',
      code: 'rs'
    },
    company: 'Commercial Press',
    date: '2019-08-13',
    status: 'renewal',
    verified: true,
    activity: 69,
    representative: {
      name: 'Onyama Limba',
      image: 'onyamalimba.png'
    },
    balance: 26640
  },
  {
    id: 19,
    name: 'Sage Wieser',
    country: {
      name: 'Egypt',
      code: 'eg'
    },
    company: 'Truhlar And Truhlar Attys',
    date: '2018-11-21',
    status: 'unqualified',
    verified: true,
    activity: 76,
    representative: {
      name: 'Ivan Magalhaes',
      image: 'ivanmagalhaes.png'
    },
    balance: 65369
  }
])

const userSelect = (event) => {
  // router.push({ name: 'contact', params: { idContact: event.data.id } })
  router.push({ path: `/contact/details/${event.data.id}/` })
}

const userCreate = (event) => {
  router.push({ path: `/contact/details/0/` })
}

</script>

<template>
  <div class="card">
    <Button @click="userCreate" class="mb-5"> Создать </Button>

    <DataTable :value="ll" @rowSelect="userSelect" :loading="isLoading" selectionMode="single" dataKey="id" :metaKeySelection="false"
      paginator stripedRows removableSort :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="width: 100%">
      <Column field="name" header="Name" style="width: 25%" sortable></Column>
      <Column field="country.name" header="Country" style="width: 25%" sortable></Column>
      <Column field="company" header="Company" style="width: 25%" sortable></Column>
      <Column field="representative.name" header="Representative" style="width: 25%" sortable></Column>
    </DataTable>

    <RouterView />
  </div>
</template>

<style scoped></style>
