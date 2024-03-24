<script setup>
import TheWelcome from '../components/TheWelcome.vue'

// import Password from 'primevue/password'
import InputGroup from 'primevue/inputgroup'
import InputGroupAddon from 'primevue/inputgroupaddon'
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
</script>

<template>
  <main>
    <TheWelcome />
    <div class="test">
      <div class="mb-5">fwefewf</div>
      <Password v-model="value" :feedback="false" />
      <div class="card flex flex-col md:flex-row gap-3">
        <InputGroup>
          <InputGroupAddon>
            <i class="pi pi-user"></i>
          </InputGroupAddon>
          <InputText placeholder="Username" />
        </InputGroup>

        <InputGroup>
          <InputGroupAddon>$</InputGroupAddon>
          <InputNumber placeholder="Price" />
          <InputGroupAddon>.00</InputGroupAddon>
        </InputGroup>

        <InputGroup>
          <InputGroupAddon>www</InputGroupAddon>
          <InputText placeholder="Website" />
        </InputGroup>
      </div>

      <InputText style="margin-right: 0.5rem" />
      <Button label="PrimeVue" />
    </div>
  </main>
</template>

<style scoped>
</style>
