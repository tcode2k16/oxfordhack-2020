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
    grid-template-columns: 2.5fr 9.5fr;
    column-gap: 10px;
    min-height: 100vh;
}
</style>

