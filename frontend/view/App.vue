<template>
  <div>
    <div id="app">
      <navbar />
      <transition name="fade">
        <router-view id="router" />
      </transition>
    </div>
    
    <svg class="graphic-header" width="883px" height="584px" viewBox="0 0 883 584" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="a">
          <stop stop-color="#F7FAFC" offset="0%"></stop>
          <stop stop-color="#DFEBF7" offset="100%"></stop>
        </linearGradient>
      </defs>
      <path d="M835.746-2.683c58.652 62.415 62.704 127.241 12.158 194.48C772.084 292.655 402.786 394.5 283.349 387.5 203.725 382.833 108.61 449-2 586V-14L835.746-2.683z" fill="url(#a)" fill-rule="evenodd"></path>
    </svg>
    <svg style="position: absolute; left: 0;margin-top:auto; margin-bottom:auto;top:0;bottom:0; transform: translate(-250px,0px);z-index:-1;" width="365px" height="372px" viewBox="0 0 365 372" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <path d="M178.746 371C281.059 371 364 288.173 364 186S328.634 1 178.746 1C28.857 1 65.06 129 24.004 186c-76.087 105.633 52.429 185 154.742 185z" stroke="#FDDF46" fill="none" fill-rule="evenodd"></path>
    </svg>
    
    
    
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
.graphic-header {
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
#app {
  display: grid;
  grid-template-columns: 2.5fr 7.5fr;
  column-gap: 50px;
  height: 100vh;
  overflow: hidden;
}

#router {
  overflow: scroll;
  /* overflow-x: hidden; */
}

.fade-enter-to,
.v-leave {
  /* display: none; */
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
  /* display: none; */
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
  /* display: none; */
}
</style>

