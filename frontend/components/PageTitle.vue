<template>
  <h1 id="title"><slot></slot></h1>
</template>

<script>
export default {
  name: "PageTitle",
};
</script>

<style scoped>
#title {
  font-family: Roboto;
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  line-height: 28px;

  color: #428FEA;
}
</style>