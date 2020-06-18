<template>
  <div id="app">
    <router-view />
  </div>
</template>
<script>
export default {
  // created() {
  //   this.$router.push("/start");
  // }
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
*::-webkit-scrollbar {
  width: 10px;
}
*::-webkit-scrollbar-thumb {
    border-radius: 5px;
    background: #ddd;
}
*::-webkit-scrollbar-thumb:hover {
  background: #ccc;
}
html,
body {
  width: 100%;
  height: 100vh;
  padding: 0px;
  margin: 0px;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
