<template>
  <div class="root">
    <h1>Hello, Alan! It's a good day to make a new friend :)</h1>
    <button class="btn" @click="openModal">Open Modal</button>
    <modal v-if="modalOpen"></modal>
    <page-title>Waiting for a friend for your hangouts...</page-title>
    <div id="first">
      <div id="cards">
        <card
          slotDirection="row"
          title="Alan"
          subtitle="First"
          content="Walk around Unversity Parks at 12pm on November 14th, 2020"
        />
        <card
          slotDirection="row"
          title="Alan"
          subtitle="First"
          content="Walk around Unversity Parks at 12pm on November 14th, 2020"
        />
      </div>
    </div>
    <page-title>Exciting hangouts coming up...</page-title>
    <div id="second">
      <div id="cards">
        <card
          slotDirection="row"
          title="Alan"
          subtitle="First-year Computer Science student at St. John’s College"
          content="Walk around Unversity Parks at 12pm on November 14th, 2020"
        />
        <card
          slotDirection="row"
          title="Alan"
          subtitle="First-year Computer Science student at St. John’s College"
          content="Walk around Unversity Parks at 12pm on November 14th, 2020"
        />
        <card
          slotDirection="row"
          title="Alan"
          subtitle="First-year Computer Science student at St. John’s College"
          content="Walk around Unversity Parks at 12pm on November 14th, 2020"
        />
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle";
import Modal from "../components/Modal";
import Card from "../components/Card";
export default {
  name: "Home",
  components: {
    "page-title": PageTitle,
    card: Card,
    Modal
  },
  data() {
    return {
      modalOpen: false
    };
  },
  methods: {
    openModal() {
      this.modalOpen = !this.modalOpen;
    }
  }
};
</script>

<style scoped>
.root {
  margin-top: 5vh;
  display: flex;
  flex-direction: column;
}

h1 {
  font-family: Roboto;
  font-style: normal;
  font-weight: bold;
  font-size: 40px;
}

#cards {
  display: grid;
  row-gap: 15px;
}

#first {
  max-width: 300px;
}

#second {
  max-width: 1000px;
}
</style>