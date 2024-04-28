import { ref, inject } from 'vue'
import { defineStore } from 'pinia'

export const useContactStore = defineStore('contact', () => {
  const $axios = inject('$axios')
    const contacts = ref({})

  // const getContact = () => {
  //   return new Promise((reject, resolve) => {
  //     $axios
  //       .get('company/')
  //       .then(function (response) {
  //         contacts.value = response.data
  //         reject(response)
  //       })
  //       .catch(function (error) {
  //         resolve(error)
  //       })
  //   })
  // }

  // const findContactById = (id) => {
  //   return contacts.value.find(el => el.id == id)
  // }

  // return { contacts, getContact, findContactById }
})
