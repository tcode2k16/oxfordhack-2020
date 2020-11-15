<template>
  <div class="root">
    <page-title class="pageTitle">Upcoming Hangouts</page-title>
    <transition name="fade">
    <div class="modal-overlay" v-if="modalOpen" @click="closeModal"></div>
    </transition>
    <transition name="fade">
    <modal
      v-if="modalOpen"
      :hangout="selectedHangout"
      @close="closeModal"
    ></modal>
    </transition>
    <div id="first">
      <div id="cards">
        <card
          v-for="hangout in upcoming"
          :key="hangout.id"
          slotDirection="row"
          :title="hangout.peer.name"
          :subtitle="`${hangout.peer.college} ${hangout.peer.department} ${hangout.peer.year}`"
          :content="`${hangout.activity} @ ${hangout.location} ${getRelTime(hangout.time)}`"
          @click="openModal(hangout)"
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
          :content="`${hangout.activity} @ ${hangout.location} ${getRelTime(hangout.time)}`"
          @click="openModal(hangout)"
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
import moment from 'moment';
import PageTitle from "../components/PageTitle";
import Card from "../components/Card";
import PageButton from "../components/PageButton";
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
      selectedHangout: {},
    };
  },
  methods: {
    openModal(hangout) {
      this.selectedHangout = hangout;
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
    },
    sortByRecent(a, b) {
      return moment(a.time) - moment(b.time);
    },
    getRelTime(t) {
      return moment(t).fromNow();
    },
    isFuture(t) {
      return moment(t).isAfter(moment());
    },
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
  display: flex;
  flex-direction: column;
}

.pageTitle {
  margin-top: 5vh;
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


.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
  /* display: none; */
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
  /* display: none; */
}
</style>