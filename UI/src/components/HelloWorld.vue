<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      AgileFlow empowers individuals and teams to navigate the dynamic landscape of task management with agility and ease.</p>
    <p>Say goodbye to the complexities of task tracking and embrace a seamless experience that adapts to your workflow.
      
    </p>

    <br/>
    
    <div class="footer">
      <h3>Learn More</h3>
      <ul>
        <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
        <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
        <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
        <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
        <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.hello {
  padding: 10% 0;
}

.hello p {
  font-size: large;
}
.footer {
  position: relative;
  top: 60px;
  width: 100%;
  height: 60px;
  text-align: center;
}
</style>
