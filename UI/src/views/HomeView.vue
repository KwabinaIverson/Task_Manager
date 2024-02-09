<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/AgileFlowLogo2.png">
    <h1>AgileFlow</h1>
    <button
    class="sign-up"
    @mouseover="signUpHover = true"
    @mouseleave="signUpHover = false"
    :class="{ 'is-hovering': signUpHover }"
    ><router-link to="/register">
      Sign-Up
    </router-link></button>
    <button
    class="login"
    @mouseover="loginHover = true"
    @mouseleave="loginHover = false"
    :class="{ 'is-hovering': loginHover }"
    ><router-link to="/login">
      Log-In
    </router-link></button>
    <HelloWorld msg="Welcome to AgileFlow – Your Agile Task Management Solution!"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { ref } from 'vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  setup() {
    const signUpHover = ref(false)
    const loginHover = ref(false)

    return {
      signUpHover,
      loginHover
    };
  }
}

</script>

<style scoped>
  div {
    padding: 20px;
    background: black;
  }

  button {
    background: wheat;
    color: black;
    padding: 10px;
    margin: 10px;
    border-radius: 20px;
    top: 10;
    position: absolute;
    font-family: 'Times New Roman', Times, serif;
    font-size: large;
    width: 10%;
    border: 0;
  }
  .login {
    left: 87%;
    background: white;
    color: black;
    border: 2px solid wheat;
    margin: 8px 8px;
  }

  .sign-up {
    left: 75%;
  }

  .is-hovering {
    background: #00ff80;
    color: black;
    border: 2px solid #00ff80;
  }

  h1 {
    position: absolute;
    left: 5%;
    top: 17%;
    font-family: fantasy;
    font-size: 60px;
    margin: 25px 0;
  }
</style>