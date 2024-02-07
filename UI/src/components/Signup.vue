<template>
    <div class="signup">
      <div class="flex-box-container">
        <h1 class="app-name">AgileFlow</h1>
        <h1 class="page-name">Sign Up Page</h1>
        <div class="flexbox-item"></div>
      </div>
      <form @submit="onSignup">
        <div class="form-group">
          <label for="fname">First Name </label>
          <input type="text" id="fname" v-model="fname" required placeholder="John">
        </div>
        <div class="form-group">
          <label for="lname">Last Name </label>
          <input type="text" id="lname" v-model="lname" required placeholder="Doe">
        </div>
        <div class="form-group">
          <label for="email">Email </label>
          <input type="email" id="email" v-model="email" required placeholder="johndoe@gmail.com">
          <p v-if="emailError" class="error-msg">{{ emailError }}</p>
        </div>
        <div class="form-group">
          <label for="password">Password </label>
          <input type="password" id="password" v-model="password" required placeholder="babayega">
        </div>
        <div class="form-group" id="testdob">
            <label for="dob">Date of Birth </label>
            <input type="date" id="dob" v-model="dateOfBirth" required>
        </div>
        <button @click="onSignup"
          @mouseover="btnHover = true"
          @mouseleave="btnHover = false"
          :class="{ 'is-hovering': btnHover }"
        >
          Sign Up
        </button>
      </form>
      <img class="cal-3" alt="Calendar picture 2" src="../assets/cal-3.png">
    </div>
</template>
  
<script>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  export default {
    name: 'Signup',
    data() {
      return {
        email: '',
        password: '',
        fname: '',
        lname: '',
        dateOfBirth: '',
        emailError: '',
      }
    },
    setup() {
      const btnHover = ref(false);
      const showSuccessModal = ref(false);
      const fname = ref('');
      const lname = ref('');
  
      return {
        btnHover,
        showSuccessModal,
        fname,
        lname
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
          this.fname = ''
          this.lname = ''
          this.dateOfBirth = ''
        } else {
          this.emailError = '';
          return true;
        }
      },
      async onSignup(e) {
        e.preventDefault()
  
        if(!this.email || !this.password || !this.fname || !this.lname) {
          alert('Please fill in every field')
          return
        }
  
        // Show success modal
        this.showSuccessModal = true;

        // Set the username for DashboardView
        const username = this.fname;

        // Validate email
        if (!this.validateEmail()) {
          return;
        }

        // Add New User to the API
        const newUser = {
          first_name: this.fname,
          last_name: this.lname,
          email: this.email,
          password: this.password,
          date_of_birth: this.dateOfBirth
        }
        await fetch('api/users', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(newUser)
        })
  
        //alert('Account Creation Successful!');
        //alert(`Welcome to AgileFlow! ${this.fname} ${this.lname}!`);
        this.email = ''
        this.password = ''
        this.fname = ''
        this.lname = ''
        this.dateOfBirth = ''
  
        // Redirect to login page to test
        // Actual implementation will be to the dashboard page
        this.$router.push({ name: 'dashboard', query: { username } });
      },
    },
  }
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
    flex-grow: 90;
    margin-left: 28px;
  }

  .app-name {
    flex-grow: 0;
    font-size: 40px;
    width: 130px;
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

  .signup {
    background: black;
    width: 100%;
    height: 750px;
  }

  input {
    margin: 8px 0;
  }

  #email {
    margin-left: 37px;        
  }

  #password {
    margin-left: 10px;
  }

  button {
    text-align: center;
    position: relative;
    margin: 40px 10px;
    margin-bottom: 0;
  }

  .form-group {
    text-align: center;
  }

  .cal-2 {
    position: absolute;
    top: 200px;
    right: 80px;
    width: 200px;
    height: 200px;
  }

  .error-msg {
    color: red;
    margin-top: 5px;
  }
</style>