<template>
  <div>
    <h1>Create a New Task</h1>
    <form @submit.prevent="createTask">
      <p>Task Name:
        <input type="text" id="taskName" v-model="taskName" required>
      </p>
      <p>Task Date: 
        <input type="datetime-local" id="taskDate" v-model="taskDate" required>
      </p>
      <p>User ID: {{ userId }}</p>
      <button type="submit">Create Task</button>
    </form>
  </div>
  <div class="update-task" v-if="showUpdateForm">
    <h1>
      Update Task Form
      <i @click="closeForm" class="fas fa-times"></i>
    </h1>
    <form @submit.prevent="updateTask">
      <p>Task Name: <input type="text" id="updateName" v-model="newName" required></p>
      <p>Task Date: <input type="datetime-local" id="updateDate" v-model="newDate" required></p>
      <button type="submit">Update Task</button>
    </form>
  </div>
  <div class="dashboard-footer">
    <h1>Task Tracker</h1>
    <ul>
      <li v-for="task in tasks" :key="task.name" @dblclick="showForm(task.id)">
        {{ task.title }} --> {{ task.date }}
        <i @click="onDelete(task.id)" class="fas fa-times"></i>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Task',
  props: ['userId'],
  data() {
    return {
      taskName: '',
      taskDate: '',
      newName: '',
      newDate: '',
      newTaskId: '',
      tasks: [],
      showUpdateForm: false
    };
  },
  methods: {
    onDelete(id) {
      if (confirm('Are you sure you want to delete this task?')) {
        this.tasks = this.tasks.filter(task => task.id !== id);

      // Also send the delete request to the server using fetch
        fetch(`api/tasks/${id}`, {
          method: 'DELETE'
        })
      }
    },
    createTask() {
      // Add your logic here to create a new task
      let task = {
        title: this.taskName,
        date: this.taskDate,
        status: 'pending',
        user_id: this.userId
      }
      this.tasks.push(task);

      // Also send the task to the server using fetch
      fetch('api/tasks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(task)
      });

      // Reset the taskName after creating the task
      this.taskName = '';
      this.taskDate = '';
    },
    async updateTask() {
      // Find the task in the tasks array
      // Update the task properties
      const taskToUpdate = this.tasks.find(task => task.id === this.newTaskId);

      // First load the task properties into the input fields
      taskToUpdate.title = this.newName;
      taskToUpdate.date = this.newDate;
      
      // Add your logic here to update the task
      fetch(`api/tasks/${this.newTaskId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: this.newName,
          date: this.newDate
        })
      })

      // Reset the taskName after creating the task
      .then(() => {
        this.newName = '';
        this.newDate = '';
      })
      },
    showForm(id) {
      if (confirm('Are you sure you want to update this task?')) {
        this.showUpdateForm = true;
        this.newTaskId = id;
         // Find the task in the tasks array
        const taskToUpdate = this.tasks.find(task => task.id === this.newTaskId);

        // First load the task properties into the input fields
        this.newName = taskToUpdate.title;
        this.newDate = taskToUpdate.date;
      }
    },
    closeForm(e) {
      e.preventDefault();
      this.newName = '';
      this.newDate = '';
      this.showUpdateForm = false;
    },
    async fetchTasks() {
      // Fetch tasks from server
      const res = await fetch('api/tasks')
      const data = await res.json()

      return data
    }
  },
  async created() {
    // Fetch the tasks from the server that belong to the user
    const allTasks = await this.fetchTasks();
    this.tasks = allTasks.filter(task => task.user_id === this.userId);
  }
}

</script>

<style scoped>
  .fas {
    color: rgb(153, 155, 155);
    margin-left: 6px;
  }
  .fas:hover {
    color: red;
    cursor: pointer;
  }

  button {
    position: relative;
    width: 35%;
    transition-duration: 0.4s;
  }

  button:hover {
    background: #00ff80;
  }

  ul {
    color: wheat;
  }

  li {
    color: wheat;
    cursor: pointer;
  }

  .update-task {
    display: block;
    background: rgb(75, 74, 74);
    min-width: max-content;
    min-height: max-content;
  }
</style>
