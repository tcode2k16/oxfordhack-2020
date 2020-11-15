<template>
  <button @click="onclick"><slot></slot></button>
</template>

<script>
export default {
  name: "PageButton",
  methods: {
    onclick(e) {
      this.$emit("click", e);
    },
  },
};
</script>

<style scoped>
button {
  margin-left: 20px;
  background-color: #428FEA;
  color: #FFFFFF;
  border: none;

  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 21px;
  padding: 10px;
  border-radius: 5px;
  height: fit-content;
}
</style>