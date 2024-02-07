<template>
  <div class="dashboard">
    <div class="flexbox-item">
      <button class="logout-btn"><router-link to="/">Logout</router-link></button>
      <h1 class="dash-head">Welcome to the Dashboard, {{ username }}!</h1>
      <button class="delete-usr-btn" @click="deleteUser">Delete Profile</button>
    </div>
    <p>Let's get you started:</p> 
    <p>Click the Profile button to load User Account.</p>
    <button @click="toggleUserInfoVisibility">Profile</button>
    <div v-if="showUserInfo && user.id">
      <p>UserID: {{ user.id }}</p>
      <p @dblclick="showNameForm=true">Name: {{ user.first_name }} {{ user.last_name }}</p>
      <p>Email: {{ user.email }}</p>
      <p @dblclick="showPasswordForm=true">Password: {{ user.password }}</p>
      <p>DoB: {{ user.date_of_birth }}</p>
    </div>
    <div class="updNameForm" v-if="showNameForm">
      <form @submit.prevent="updateName">
        <h2>
          Change your name
          <i class="fas fa-times" @click="showNameForm=false"></i>
        </h2>
        <p>First Name: <input type="text" id="updateName" v-model="user.first_name" required></p>
        <p>Last Name: <input type="text" id="updateName" v-model="user.last_name" required></p>
        <br/>
        <button type="submit">Update Name</button>
      </form>
    </div>
    <div class="updPasswordForm" v-if="showPasswordForm">
      <form @submit.prevent="updatePassword">
        <h2>
          Change your password
          <i class="fas fa-times" @click="showPasswordForm=false"></i>
        </h2>
        <p>Password: <input type="password" id="updatePassword" v-model="user.password" required></p>
        <button type="submit">Update Password</button>
      </form>
    </div>
    <Task :userId="user.id"/>
  </div>
</template>
  
<script>
import Task from '@/components/Task.vue'

  export default {
    name: 'DashboardView',
    data() {
      return {
        username: '', // You can pass the username from the signup page or fetch it from the store
        users: [],
        user: {},
        showUserInfo: false,
        showNameForm: false,
        showPasswordForm: false
      };
    },
    components: {
      Task
    },
    methods: {
      async fetchUsers() {
        // Fetch users from the API
        const res = await fetch("api/users")

        const data = await res.json()
        return data
      },
      getUser() {
        //here we will get the user from the users array
        for (let i=0; i < this.users.length; i++) {
          if (this.users[i].first_name === this.username) {
            return this.users[i];
          }
        }
      },
      toggleUserInfoVisibility(e) {
        e.preventDefault()

        this.showUserInfo = !this.showUserInfo
        if (this.showUserInfo) {
          this.getUser()
        }
      },
      async deleteUser() {
        if (confirm('Are you sure you want to delete your profile?')) {
          // Fetch all tasks
          const tasks = await fetch('api/tasks');
          const tasksJSON = await tasks.json();

          // Delete all tasks associated with the user
          for (let i=0; i < tasksJSON.length; i++) {
            if (tasksJSON[i].user_id === this.user.id) {
              fetch(`api/tasks/${tasksJSON[i].id}`, {
                method: 'DELETE'
              })
            }
          }

          // Delete the user
          fetch(`api/users/${this.user.id}`, {
            method: 'DELETE'
          })

          // Redirect to the Home page
          this.$router.push('/')
        }
      },
      updateName() {
        if (confirm('Are you sure you want to update your name?')) {
          // Update the user's name
          fetch(`api/users/${this.user.id}`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              first_name: this.user.first_name,
              last_name: this.user.last_name
            })
          })

          alert('Name updated successfully!');

          // Toggle the form visibility
          this.showNameForm = !this.showNameForm;

          // Redirect to the Home page
          this.$router.push('/')
        }
      },
      updatePassword() {
        if (confirm('Are you sure you want to update your password?')) {
          // Update the user's password
          fetch(`api/users/${this.user.id}`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              password: this.user.password
            })
          })

          alert('Password updated successfully!');

          // Toggle the form visibility
          this.showPasswordForm = !this.showPasswordForm;

          // Redirect to the Home page
          this.$router.push('/')
        }
      }
    },
    async created() {
      // Fetch the username from the store  or pass it from the signup page
      this.username = this.$route.query.username || 'User';

      this.users = await this.fetchUsers();
      this.user = this.getUser();
    }
};
</script>

<style scoped>
  .flexbox-item {
    width: 100%;
  }
  .dashboard {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: max-content;
    cursor: default;
  }
  .dashboard h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  .flexbox-item {
    position: relative;
    display: flex;
    justify-content: space-between;
  }
  .delete-usr-btn:hover {
    background: rgb(210, 48, 23);
  }

  button {
    position: relative;
    text-align: center;
    transition-duration: 0.4s;
    padding: 10px 0;
  }

  button:hover {
    background: #00ff80;
  }
  .updNameForm {
    background: rgb(75, 74, 74);
    display: flex;
  }
  .updNameForm button {
    width: 50%;
  }
  .updNameForm h2 {
    justify-content: center;
    align-items: center;
    text-align: center;
    display: flex;
  }

  .updPasswordForm {
    background: rgb(75, 74, 74);
    display: flex;
  }
  .updPasswordForm button {
    width: 50%;
  }
  .updPasswordForm h2 {
    justify-content: center;
    align-items: center;
    text-align: center;
    display: flex;
  }

  .fas {
    color: rgb(153, 155, 155);
    position: relative;
    top: -20px;
    margin-right: 10px;
  }
  .fas:hover {
    color: red;
    cursor: pointer;
  }
</style>
  