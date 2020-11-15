<template>
  <transition name="fade">
    <div id="notification">
      <p>{{msg}}</p>
    </div>
  </transition>
</template>

<script>
export default {
  name: "Notification",
  props: ['msg', 'time'],
  mounted() {
    setTimeout(() => {
      this.$emit("close");
    }, this.time);
  },
};
</script>

<style scoped>
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

#notification {
  position: absolute;
  top: 15px;
  /* background-color: red; */
  right: 15px;

  background: #e9f0f8;
  border: 1px solid #428fea;
  box-sizing: border-box;
  border-radius: 5px;
  padding: 10px 20px;
  display: flex;
  height: min-content;
  justify-content: space-between;
  align-items: center;
  height: min-content;
}

#notification > p {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 23px;
  margin: 10px;

  color: #000000;
}
</style>