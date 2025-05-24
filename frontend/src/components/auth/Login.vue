<script setup>
/* PrimeVue components */
import Image from 'primevue/image';
import Button from 'primevue/button';
import Password from 'primevue/password';
import InputText from 'primevue/inputtext';
/* Stores */
import { rootStore } from '@/stores';
/* Vue v3 */
import { ref } from 'vue';

const store = rootStore()

const authData = ref({
  login: '',
  password: ''
})

const errorMessage = ref('')

</script>

<template>
  <div id="pl-login">
    <div id="pl-auth-form">
      <div class="from-logo-container">
        <Image src="/src/assets/images/GSlogoHC.png" alt="Image" imageClass="from-logo" />
      </div>
      <div class="form-input">
        <label>Логин</label>
        <InputText name="username" type="text" v-model="authData.login" />
      </div>
      <div class="form-input">
        <label>Пароль</label>
        <Password type="text" v-model="authData.password" :feedback="false" />
      </div>
      <Button @click="store.auth().login(authData)">Войти</Button>
    </div>
  </div>
</template>

<style lang="scss">
#pl-login {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background-color: rgb(35, 169, 231);
  display: flex;
  justify-content: center;
  align-items: center;

  #pl-auth-form {
    width: 600px;
    height: 350px;
    background-color: white;
    border-radius: 16px;
    margin-bottom: 200px;
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    align-items: center;

    .from-logo-container {
      width: 100%;
      display: flex;
      justify-content: center;

      span {
        display: flex;
      }

      .from-logo {
        width: 25%;
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
      }
    }

    .form-input {
      display: flex;
      flex-direction: column;
      width: 50%;
      margin-bottom: 10px;

      label {
        margin-left: 5px;
      }
    }

    .p-inputtext {
      width: 100%;
      margin-top: 5px
    }
  }
}
</style>