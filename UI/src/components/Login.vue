<template>
    <div class="login">
      <div class="flex-box-container">
        <h1 class="app-name">AgileFlow</h1>
        <h1>Log-In Page</h1>
        <div class="flexbox-item"></div>
      </div>
      <form @submit="onSubmit">
        <div class="form-group">
          <label for="email">Email </label>
          <input type="email" id="email" v-model="email" required placeholder="johndoe@gmail.com">
          <p v-if="emailError" class="error-msg">{{ emailError }}</p>
        </div>
        <div class="form-group">
          <label for="password">Password </label>
          <input type="password" id="password" v-model="password" required placeholder="babayega">
        </div>
        <button
          @click="onSubmit"
          @mouseover="btnHover = true"
          @mouseleave="btnHover = false"
          :class="{ 'is-hovering': btnHover}"
        >
          Log In
        </button>
      </form>
      <img class="zen" alt="Zenitsu" src="../assets/zen.png">
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    name: 'Login',
    data() {
      return {
          email: '',
          password: '',
          emailError: '',
          users: [],
          user: {}
      }
    },
    setup() {
      const btnHover = ref(false)
  
      return {
        btnHover
      };
    },
    methods: {
      validateEmail() {
        // email regex
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

        // check if email is valid
        if (!emailRegex.test(this.email)) {
          this.emailError = 'Please enter a valid email';
          this.email = ''
          this.password = ''
        } else {
          this.emailError = '';
          return true;
        }
      },
      async fetchUsers() {
        // Fetch users from the API
        const res = await fetch("api/users")

        const data = await res.json()
        return data
      },
      onSubmit(e) {
        e.preventDefault()
  
        if(!this.email || !this.password) {
          alert('Please fill in every field')
          return
        }

        // Validate email
        if (!this.validateEmail()) {
          return;
        }

        // Validate email in the backend
        // If email is not found, display error message
        // If email is found, check if the password matches
        // If password matches, log in the user
        // If password does not match, display error message
        for (let i=0; i < this.users.length; i++) {
          if (this.users[i].email === this.email) {
            if (this.users[i].password !== this.password) {
              alert('Password is incorrect');
              return;
            }
            alert('Logged in');
            this.user= this.users[i];
            break;
          }
          if (i === this.users.length - 1) {
            alert('Email not found');
            return;
          }
        }

        this.email = ''
        this.password = ''

        // Set the username for DashboardView
        const username = this.user.first_name;

        // Redirect to login page to test
        // Actual implementation will be to the dashboard page
        this.$router.push({ name: 'dashboard', query: { username } });
      },
    },
    async created() {
        this.users = await this.fetchUsers();
      }
  };
  </script>
  
  <style scoped>
   h1 {
      font-family: fantasy;
      margin: 20px 0;
    }
  
    .flex-box-container {
      display: flex;
      justify-content: space-around;
      align-items: center;
    }
  
    .page-name {
      align-self: center;
      flex-grow: 2;
    }
  
    .app-name {
      flex-grow: 1;
      font-size: 40px;
      width: 130px;
      margin-left: 5px;
      text-align: left;
      padding-left: 10px;
    }
  
    .flexbox-item {
      border: 2px solid black;
      width: 100px;
      min-height: 50px;
      flex-grow: 1;
      margin: 10px 10px;
    }
    .login {
      background: black;
      width: 100%;
      height: 760px;
    }
  
    /*.zen {
      height: 40%;
      position: relative;
      top: 80px;
    }*/
  
    input {
      margin: 8px 0;
    }
  
    #email{
      margin-left: 27px;        
    }
  
    button {
      text-align: center;
      position: relative;
      margin: 40px 10px;
    }
  
    .form-group {
      text-align: center;
    }

    .error-msg {
    color: red;
    margin-top: 5px;
  }
  </style>