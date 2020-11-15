<template>
  <div class="root">
    <page-title>See what people are doing</page-title>
    <div class="cards">

      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
      <card slotDirection="column" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
        <page-button>We met!</page-button>
      </card>
    </div>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle";
import PageButton from "../components/PageButton";
import Card from '../components/Card';
export default {
  name: "FindHangouts",
  components: {
    "page-title": PageTitle,
    "page-button": PageButton,
    "card": Card,
  },
};
</script>

<style scoped>
.root {
  margin-top: 5vh;
  display: flex;
  flex-direction: column;
  
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, 350px);
  column-gap: 15px;
  row-gap: 15px;
  /* max-width: 1000px; */

}

button {
  margin-top:20px;
}

</style>