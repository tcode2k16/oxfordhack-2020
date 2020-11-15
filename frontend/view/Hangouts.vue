<template>
  <div class="root">
    <page-title>Upcoming Hangouts</page-title>
    <button class="btn" @click="openModal">Open Modal</button>
    <div class="modal-overlay" v-if="modalOpen" @click="closeModal"></div>
    <modal v-if="modalOpen" @close="closeModal"></modal>
    <div id="first">
      <div id="cards">
        <card
          v-for="hangout in upcoming"
          :key="hangout.id"
          slotDirection="row"
          :title="hangout.peer.name"
          :subtitle="`${hangout.peer.college} ${hangout.peer.department} ${hangout.peer.year}`"
          :content="`${hangout.activity} ${hangout.location} ${hangout.time}`"
        />
        <!-- <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020"/>
        <card slotDirection="row" title="Alan" subtitle="First-year Computer Science student at St. John’s College" content="Walk around Unversity Parks at 12pm on November 14th, 2020"/> -->
      </div>

      <img src="/img/human3.svg" alt="" />
    </div>
    <br />
    <page-title>Past Hangouts</page-title>
    <div id="second">
      <div id="cards">
        <card
          v-for="hangout in past"
          :key="hangout.id"
          slotDirection="row"
          :title="hangout.peer.name"
          :subtitle="`${hangout.peer.college} ${hangout.peer.department} ${hangout.peer.year}`"
          :content="`${hangout.activity} ${hangout.location} ${hangout.time}`"
        >
          <page-button>We met!</page-button>
        </card>
        <!-- <card
          slotDirection="row"
          title="Alan"
          subtitle="First-year Computer Science student at St. John’s College"
          content="Walk around Unversity Parks at 12pm on November 14th, 2020"
        >
          <page-button>We met!</page-button>
        </card> -->
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import PageTitle from "../components/PageTitle";
import Card from "../components/Card";
import PageButton from "../components/PageButton";
import moment from "moment";
import Modal from "../components/HangoutDetailsModal";
export default {
  name: "Hangouts",
  components: {
    "page-title": PageTitle,
    card: Card,
    "page-button": PageButton,
    Modal,
  },
  data() {
    return {
      upcoming: [],
      past: [],
      modalOpen: false,
    };
  },
  methods: {
    openModal() {
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
    }
  },
  async mounted() {
    let hangouts = [];
    let r = await Axios.post("/auth/my_hangouts", {
      hangout_type: "matched",
    });
    hangouts = hangouts.concat(r.data.hangouts);

    r = await Axios.post("/auth/my_hangouts", {
      hangout_type: "finalized",
    });
    hangouts = hangouts.concat(r.data.hangouts);

    console.log(hangouts);
    for (let each of hangouts) {
      if (moment(each.time).isBefore(moment())) {
        this.past.push(each);
      } else {
        this.upcoming.push(each);
      }
    }

    // console.log(moment('2020-01-01').isBefore(moment()));
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

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 98;
  background-color: #ffffff;
  opacity: 50%;
}

#cards {
  display: grid;
  row-gap: 15px;
  min-width: 50vw;
}

#second {
  max-width: 1000px;
  margin-bottom: 5vh;
}
</style>