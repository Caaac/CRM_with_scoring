<script>
import TheWelcome from '../components/TheWelcome.vue'

export default {
  data() {
    return {
      value: 40
    }
  },

  components: {
    TheWelcome
  }
}

</script>

<template>
  <main>
    <TheWelcome />
    <Knob v-model="value" :min="-50" :max="50" />
  </main>
</template>

<style scoped>
</style>
