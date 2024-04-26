import { ref, inject } from 'vue'
import { defineStore } from 'pinia'

export const useContactStore = defineStore('contact', () => {
  const $axios = inject('$axios')
  //   const contacts = ref({})
  const contacts = ref([
    {
      id: 11,
      name: 'Company A',
      ful_name: 'Company A LLC',
      representative_name: 'John',
      representative_last_name: 'Doe',
      address: '123 Main St, City A',
      inn: 1234567890,
      kpp: 9876543210,
      industry: 'Technology',
      phone: 1234567890,
      email: 'john.doe@companyA.com',
      revenue: 1000000
    },
    {
      id: 12,
      name: 'Company B',
      ful_name: 'Company B Inc.',
      representative_name: 'Jane',
      representative_last_name: 'Smith',
      address: '456 Elm St, City B',
      inn: 2345678901,
      kpp: 8765432109,
      industry: 'Finance',
      phone: 2345678901,
      email: 'jane.smith@companyB.com',
      revenue: 2000000
    },
    {
      id: 13,
      name: 'Company C',
      ful_name: 'Company C Ltd.',
      representative_name: 'Mike',
      representative_last_name: 'Johnson',
      address: '789 Oak St, City C',
      inn: 3456789012,
      kpp: 7654321098,
      industry: 'Healthcare',
      phone: 3456789012,
      email: 'mike.johnson@companyC.com',
      revenue: 3000000
    },
    {
      id: 14,
      name: 'Company D',
      ful_name: 'Company D Corp.',
      representative_name: 'Sarah',
      representative_last_name: 'Williams',
      address: '101 Pine St, City D',
      inn: 4567890123,
      kpp: 6543210987,
      industry: 'Retail',
      phone: 4567890123,
      email: 'sarah.williams@companyD.com',
      revenue: 4000000
    },
    {
      id: 15,
      name: 'Company E',
      ful_name: 'Company E Co.',
      representative_name: 'David',
      representative_last_name: 'Brown',
      address: '202 Maple St, City E',
      inn: 5678901234,
      kpp: 5432109876,
      industry: 'Manufacturing',
      phone: 5678901234,
      email: 'david.brown@companyE.com',
      revenue: 5000000
    },
    {
      id: 16,
      name: 'Company F',
      ful_name: 'Company F Group',
      representative_name: 'Emily',
      representative_last_name: 'Jones',
      address: '303 Cedar St, City F',
      inn: 6789012345,
      kpp: 4321098765,
      industry: 'Hospitality',
      phone: 6789012345,
      email: 'emily.jones@companyF.com',
      revenue: 6000000
    },
    {
      id: 17,
      name: 'Company G',
      ful_name: 'Company G Enterprises',
      representative_name: 'Tom',
      representative_last_name: 'Wilson',
      address: '404 Birch St, City G',
      inn: 7890123456,
      kpp: 3210987654,
      industry: 'Construction',
      phone: 7890123456,
      email: 'tom.wilson@companyG.com',
      revenue: 7000000
    },
    {
      id: 18,
      name: 'Company H',
      ful_name: 'Company H Solutions',
      representative_name: 'Laura',
      representative_last_name: 'Taylor',
      address: '505 Walnut St, City H',
      inn: 8901234567,
      kpp: 2109876543,
      industry: 'Consulting',
      phone: 8901234567,
      email: 'laura.taylor@companyH.com',
      revenue: 8000000
    },
    {
      id: 19,
      name: 'Company I',
      ful_name: 'Company I Holdings',
      representative_name: 'Chris',
      representative_last_name: 'Martinez',
      address: '606 Spruce St, City I',
      inn: 9012345678,
      kpp: 1098765432,
      industry: 'Energy',
      phone: 9012345678,
      email: 'chris.martinez@companyI.com',
      revenue: 9000000
    },
    {
      id: 20,
      name: 'Company J',
      ful_name: 'Company J Ventures',
      representative_name: 'Amy',
      representative_last_name: 'Garcia',
      address: '707 Sycamore St, City J',
      inn: 1234567890,
      kpp: 987654321,
      industry: 'Transportation',
      phone: 1234567890,
      email: 'amy.garcia@companyJ.com',
      revenue: 10000000
    },
    {
      id: 21,
      name: 'Company ABC',
      ful_name: 'ABC Corporation',
      representative_name: 'John',
      representative_last_name: 'Doe',
      address: '123 Main Street, City, Country',
      inn: 1234567890,
      kpp: 987654321,
      industry: 'Technology',
      phone: 1234567890,
      email: 'info@companyabc.com',
      revenue: 1000000
    },
    {
      id: 22,
      name: 'Company ABC',
      ful_name: 'ABC Corporation',
      representative_name: 'John',
      representative_last_name: 'Doe',
      address: '123 Main Street, City, Country',
      inn: 1234567890,
      kpp: 987654321,
      industry: 'Technology',
      phone: 1234567890,
      email: 'info@companyabc.com',
      revenue: 1000000
    }
  ])

  const getContact = () => {
    return new Promise((reject, resolve) => {
      $axios
        .get('company/')
        .then(function (response) {
          contacts.value = response.data
          reject(response)
        })
        .catch(function (error) {
          resolve(error)
        })
    })
  }

  return { contacts, getContact }
})
