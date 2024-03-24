
<template>
  <div class="card">
      <Message severity="info" icon="pi pi-send">Info Message</Message>
      <Message severity="success">
          <template #messageicon>
              <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
          </template>
          <span class="ml-2">How may I help you?</span>
      </Message>
  </div>
</template>

<script setup>
</script>
