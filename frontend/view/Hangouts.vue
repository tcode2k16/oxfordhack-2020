<template>
  <div class="root">
    <page-title>Upcoming Hangouts</page-title>
    <div id="first">
      <div id="cards">
        <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020"/>
        <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020"/>
        <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020"/>
      </div>
      
      <img src="/img/human3.svg" alt="">
    </div>
    <br>
    <page-title>Past Hangouts</page-title>
    <div id="second">
      <div id="cards">
        <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
          <button>hello</button>
        </card>
        <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
          <button>hello</button>
        </card>
        <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020">
          <button>hello</button>
        </card>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle";
import Card from "../components/Card";
import Button from "../components/Button";
export default {
  name: "Hangouts",
  components: {
    "page-title": PageTitle,
    'card': Card,
    'button': Button,
  },
};
</script>

<style scoped>
.root {
  margin-top: 5vh;
  display: flex;
  flex-direction: column;
  
}

#first {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  max-width: 1000px;
}

#cards {
  display: grid;
  row-gap: 15px;

}

#second {
  max-width: 1000px;
}


</style>