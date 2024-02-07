<template>
  <p>
    Not a member?
    <router-link to="/register" class="router-link">Sign Up</router-link>
  </p>
  <Login />
</template>

<script>
  import Login from '@/components/Login.vue'

  export default {
    name: 'LoginView',
    components: {
      Login
    }
  }
</script>

<style scoped>
  .router-link {
    color: #42b983;
  }

  p {
    position: absolute;
    left: 83%;
  }
</style>