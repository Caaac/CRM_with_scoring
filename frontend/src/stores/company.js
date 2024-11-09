import { ref, inject, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCompanyStore = defineStore('company', () => {
  const $axios = inject('$axios')
  
  const companies = ref({})
  const companyDetail = ref({})
  
  const getCompany = () => {
    return new Promise((reject, resolve) => {
      $axios
        .get('company/')
        .then(function (response) {
          companies.value = response.data
          reject(response)
        })
        .catch(function (error) {
          resolve(error)
        })
    })
  }

  const updateCompany = async(id) => {
    const companyData = findCompanyById(id)
    console.log('companyData', companyData );
    Reflect.deleteProperty(companyData, 'id')
    return new Promise((reject, resolve) => {
      $axios
        .put(`company/${id}`, companyData)
        .then(function (response) {
          console.log('yes');
          reject(response)
        })
        .catch(function (error) {
          console.log('no');
          resolve(error)
        })
    })
  }

  const findCompanyById = (id) => {
    return companies.value.find(el => el.id == id)
  }

  const getTemplate = (() => {
    const tml = companies.value.shift()

    Object.keys(tml).map(key => {
      // if (key == 'id') delete tml[key]
      if (key == 'id') tml[key] = 0
      else if (tml[key] instanceof Array) tml[key] = []
      else tml[key] = null
    })

    return tml

  })

  return { companies, getCompany, findCompanyById, updateCompany, companyDetail, getTemplate }
})
