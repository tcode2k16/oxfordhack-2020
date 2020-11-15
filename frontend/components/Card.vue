<template>
  <div class="card-root" :style="'flex-direction: '+slotDirection+';'">
    <div class="text">
      <p class="bold" style="margin-bottom: 0">{{ title }}</p>
      <p style="margin-top: 0">{{ subtitle }}</p>
      <p class="bold">{{ content }}</p>
    </div>
    <slot></slot>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle";
export default {
  name: "Card",
  props: ["title", "subtitle", "content", 'slotDirection'],
};
</script>

<style scoped>
.card-root {
  background: #e9f0f8;
  border: 1px solid #428fea;
  box-sizing: border-box;
  border-radius: 5px;
  padding: 10px 20px;
  display: flex;
  height: min-content;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}

.text {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.bold {
  font-weight: bold;
}

p {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 23px;
  margin: 10px;

  color: #000000;
}
</style>