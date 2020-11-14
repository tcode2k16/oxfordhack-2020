<template>
  <div id="app">
    <navbar />
    <transition name="fade">
      <router-view id="router" />
    </transition>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";

export default {
  name: "App",
  components: {
    navbar: Navbar,
  },
};
</script>

<style scoped>
#app {
  display: grid;
  grid-template-columns: 2.3fr 9.7fr;
  column-gap: 50px;
  height: 100vh;
}

#router {
  overflow: scroll;
}

.fade-enter-to, .v-leave {
  /* display: none; */
}

.fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
    /* display: none; */
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
    /* display: none; */
}
</style>

