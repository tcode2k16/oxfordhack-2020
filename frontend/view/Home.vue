<template>
  <div class="root">
    <h1>this is Home</h1>
    <hr>
    <router-link to="/hangouts">Go to Hangouts</router-link><br/>
    <router-link to="/find-hangouts">Go to Find Hangouts</router-link><br/>
    <router-link to="/user">Go to User</router-link><br/>

  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped>

</style>