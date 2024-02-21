<template>
  <p>
    Already have an account?
    <router-link to="/login" class="router-link">Login</router-link>
  </p>
  <Signup />
</template>

<script>
  import Signup from '@/components/Signup.vue'

  export default {
    name: 'SignupView',
    components: {
      Signup
    }
  }
</script>

<style scoped>
  .router-link {
    color: #42b983;
  }

  p {
    position: absolute;
    left: 80%;
  }
</style>