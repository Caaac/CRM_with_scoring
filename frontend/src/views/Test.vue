<script setup>
import { ref, inject } from 'vue'

const $axios = inject("$axios");

const send = async () => {
    let res = await fetch('http://127.0.0.1:8000/api/v1/company/')
    if (res.ok) {
        let jsonData = await res.json()
        sendResult.value = jsonData
        console.log(jsonData);
    } else {
        sendResult.value = res.status
        console.log('Error:', res.status);
    }
}
const sendResult = ref()

const getAxios = () => {
    $axios.get('company/')
        .then(function (response) {
            sendResult.value = response.data
            console.log(response);
        })
        .catch(function (error) {
            sendResult.value = null
            console.log(error);
        })
}

const delAxios = () => {
    $axios.delete('http://127.0.0.1:8000/api/v1/company/')
        .then(function (response) {
            // sendResult.value = response.data
            console.log(response);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
}

const postAxios = () => {
    // const data = {
    //   NAME: "Company ABC",
    //   FUL_NAME: "ABC Corporation",
    //   REPRESENTATIVE_NAME: "John",
    //   REPRESENTATIVE_LAST_NAME: "Doe",
    //   ADDRESS: "123 Main Street, City, Country",
    //   INN: 1234567890,
    //   KPP: 987654321,
    //   INDUSTRY: "Technology",
    //   PHONE: 1234567890,
    //   EMAIL: "info@companyabc.com",
    //   REVENUE: 1000000
    // }

    const data = {
        name: "Company ABC",
        ful_name: "ABC Corporation",
        representative_name: "John",
        representative_last_name: "Doe",
        address: "123 Main Street, City, Country",
        inn: 1234567890,
        kpp: 987654321,
        industry: "Technology",
        phone: 1234567890,
        email: "info@companyabc.com",
        revenue: 1000000
    }

    $axios.post('http://127.0.0.1:8000/api/v1/company/', data)
        .then(function (response) {
            // sendResult.value = response.data
            console.log(response);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
}

</script>

<template>
    <div>
        <Button @click="getAxios">Get Axios</Button>
        <Button class="ms-2" @click="delAxios">Del Axios</Button>
        <Button class="ms-2" @click="postAxios">Post Axios</Button>
        <Button class="ms-2" disabled @click="send">Send</Button>
        <Button class="ms-2" @click="sendResult = null">cls</Button>
        {{ sendResult }}
    </div>
</template>