<template>
  <div id="gender-btns">
    <button>Male</button>
    <button>Female</button>
    <button class="selected">Non-binary</button>
    <button>Prefer not to disclose</button>
  </div>
</template>

<script>

export default {
  name: "RadioBox",
  components: {
    "page-title": PageTitle,
  },
};
</script>

