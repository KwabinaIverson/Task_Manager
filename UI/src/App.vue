<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: wheat;
  background: black;
}

nav {
  padding: 30px;
  background: #2c3e50;
}

nav a {
  font-weight: bold;
  color: wheat;
}

nav a.router-link-exact-active {
  color: #42b983;
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

  .is-hovering {
    background: #00ff80;
    color: black;
    border: 2px solid #00ff80;
  }
</style>
