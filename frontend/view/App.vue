<template>
  <div id="app">
    <navbar/>
    <router-view id="router"/>
  </div>
</template>

<script>
import Navbar from '../components/Navbar';

export default {
  name: "App",
  components: {
    'navbar': Navbar,
  },
  
};
</script>

<style scoped>
#app {
    display: grid;
    grid-template-columns: 2.3fr 9.7fr;
    column-gap: 50px;
    min-height: 100vh;
}
</style>

