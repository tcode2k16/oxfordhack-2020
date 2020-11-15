<template>
  <div class="root">
    <page-title>See what people are doing</page-title>
    <div class="cards">
      <card
        v-for="feed in feeds"
        :key="feed.id"
        slotDirection="column"
        :title="feed.author.name"
        :subtitle="`${feed.author.college} ${feed.author.department} ${feed.author.year}`"
        
        :content="`${feed.activity} ${feed.location} ${feed.time}`"
      >
        <page-button>Let’s hangout!</page-button>
      </card>
      <!-- <card
        slotDirection="column"
        title="Alan"
        subtitle="First-year Computer Science student at St. John’s College"
        content="Walk around Unversity Parks at 12pm on November 14th, 2020"
      >
        <page-button>We met!</page-button>
      </card>
      <card
        slotDirection="column"
        title="Alan"
        subtitle="First-year Computer Science student at St. John’s College"
        content="Walk around Unversity Parks at 12pm on November 14th, 2020"
      >
        <page-button>We met!</page-button>
      </card>
      <card
        slotDirection="column"
        title="Alan"
        subtitle="First-year Computer Science student at St. John’s College"
        content="Walk around Unversity Parks at 12pm on November 14th, 2020"
      >
        <page-button>We met!</page-button>
      </card>
      <card
        slotDirection="column"
        title="Alan"
        subtitle="First-year Computer Science student at St. John’s College"
        content="Walk around Unversity Parks at 12pm on November 14th, 2020"
      >
        <page-button>We met!</page-button>
      </card>
      <card
        slotDirection="column"
        title="Alan"
        subtitle="First-year Computer Science student at St. John’s College"
        content="Walk around Unversity Parks at 12pm on November 14th, 2020"
      >
        <page-button>We met!</page-button>
      </card>
      <card
        slotDirection="column"
        title="Alan"
        subtitle="First-year Computer Science student at St. John’s College"
        content="Walk around Unversity Parks at 12pm on November 14th, 2020"
      >
        <page-button>We met!</page-button>
      </card>
      <card
        slotDirection="column"
        title="Alan"
        subtitle="First-year Computer Science student at St. John’s College"
        content="Walk around Unversity Parks at 12pm on November 14th, 2020"
      >
        <page-button>We met!</page-button>
      </card> -->
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import PageTitle from "../components/PageTitle";
import PageButton from "../components/PageButton";
import Card from "../components/Card";
export default {
  name: "FindHangouts",
  components: {
    "page-title": PageTitle,
    "page-button": PageButton,
    card: Card,
  },
  data() {
    return {
      feeds: {}
    };
  },
  async mounted() {
    let r = await Axios.get("/auth/my_feed");
    console.log(r.data);
    this.feeds = r.data.feeds;
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
  grid-auto-rows: 1fr;
  column-gap: 15px;
  row-gap: 15px;
  /* max-width: 1000px; */
}

button {
  margin-top: 20px;
}
</style>