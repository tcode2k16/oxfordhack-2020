<template>
  <div class="root">
    <page-title>See what people are doing</page-title>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle";
export default {
  name: "FindHangouts",
  components: {
    "page-title": PageTitle
  }
};
</script>

<style scoped>
.root {
  margin-top: 5vh;
  display: flex;
  flex-direction: column;
}
</style>