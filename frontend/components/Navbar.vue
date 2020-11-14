<template>
  <div class="root">
    <div class="link-box">
      <router-link
        v-for="[route, name] in [
          ['/', 'Home'],
          ['/find-hangouts', 'Find Hangouts'],
          ['/hangouts', 'Hangouts'],
          ['/user', 'User'],
        ]"
        :key="route"
        :to="route"
        :class="'links ' + (currPath === route ? 'selected' : 'unselected')"
      >
        {{ name }}
      </router-link>
    </div>

    <img src="/img/Standing.svg" id="human" />
  </div>
</template>

<script>
export default {
  name: "Navbar",
  computed: {
    currPath() {
      console.log(this.$route);
      return this.$route.path;
    },
  },
};
</script>

<style lang="less" scoped>
.root {
  // background-color: red;
  color: #9E9E9E;
  min-height: 100vh;

  // position: absolute;
  // display: flex;
  // flex-direction: column;
  // justify-content: center;
  // align-items: flex-end;
  display: grid;
  grid-template-rows: 70% 30%;
  user-select: none;
}

#human {
  margin-bottom: 0;
  align-self: flex-end;
  width: 256px;
  z-index: -100;
}

.link-box {
  display: grid;
  align-self: center;
  row-gap: 20px;
}
.links {
  // justify-self: flex-end;
  align-self: flex-end;

  text-decoration: none;

  font-family: Roboto;
  font-style: normal;
  font-weight: bold;
  font-size: 40px;
  line-height: 47px;
  text-align: right;
}

.selected {
  color: #428FEA;
}

.unselected {
  color: #9E9E9E;
}
</style>