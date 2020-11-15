<template>
  <div class="root">
    <notification v-if="notiOpen" @close="()=>{notiOpen = false}" msg="Created a new hangout!" :time="2000"></notification>
    <h1 class="heading">
      Hello, Nicole! <br />
      It's a good day to make a new friend :)
    </h1>
    <!-- <button class="btn" @click="openModal">Open Modal</button> -->
    <transition name="fade">
      <div class="modal-overlay" v-if="modalOpen" @click="closeModal"></div>
    </transition>
    <transition name="fade">
      <modal v-if="modalOpen" @close="closeModal" @success="showNoti"></modal>
    </transition>

    <transition name="fade">
      <div class="modal-overlay" v-if="modalOpen2" @click="closeModal2"></div>
    </transition>
    <transition name="fade">
      <detailmodal v-if="modalOpen2" @close="closeModal2" :hangout="selectedHangout"></detailmodal>
    </transition>
    <page-title>Waiting for a match for your hangouts...</page-title>
    <div id="first">
      <div id="grid">
        <card
          v-for="hangout in requests.filter(e => isFuture(e.time)).sort(sortByRecent)"
          :key="hangout.id"
          slotDirection="row"
          title=""
          subtitle=""
          @click="openModal2(hangout)"
          :content="`${hangout.activity} @ ${hangout.location} ${getRelTime(hangout.time)}`"
        />

        <card
          @click="openModal"
          slotDirection="row"
          title=""
          subtitle=""
          id="gray"
          content="Create a new hangout!"
        />
      </div>
    </div>
    <div id="split">
      <div>
        <page-title>Exciting hangouts coming up...</page-title>
        <div id="second">
          <div id="cards">
            <card
              v-for="hangout in upcoming.filter(e => isFuture(e.time)).sort(sortByRecent).slice(0, Math.min(3, upcoming.length))"
              :key="hangout.id"
              slotDirection="row"
              :title="hangout.peer.name"
              @click="openModal2(hangout)"
              :subtitle="`${hangout.peer.college} ${hangout.peer.department} ${hangout.peer.year}`"
              :content="`${hangout.activity} @ ${hangout.location} ${getRelTime(hangout.time)}`"
            />
          </div>
        </div>
      </div>
      <div>
        <img src="/img/human4.svg" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import moment from "moment";
import Notification from "../components/Notification";
import PageTitle from "../components/PageTitle";
import Modal from "../components/CreateHangoutModal";
import Modal2 from "../components/HangoutDetailsModal";
import Card from "../components/Card";
export default {
  name: "Home",
  components: {
    "page-title": PageTitle,
    card: Card,
    Modal,
    'detailmodal': Modal2,
    'notification': Notification,
  },
  data() {
    return {
      modalOpen: false,
      modalOpen2: false,
      upcoming: [],
      requests: [],
      notiOpen: false,
      selectedHangout: {},
    };
  },
  methods: {
    openModal() {
      this.modalOpen = true;
    },
    closeModal() {
      console.log("close modal");
      this.modalOpen = false;
    },
    openModal2(h) {
      this.modalOpen2 = true;
      this.selectedHangout = h;
    },
    closeModal2() {
      console.log("close modal");
      this.modalOpen2 = false;
    },
    showNoti() {
      console.log("show noti");
      this.notiOpen = true; 
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
        continue;
      } else {
        this.upcoming.push(each);
      }
    }

    hangouts = [];
    r = await Axios.post("/auth/my_hangouts", {
      hangout_type: "available",
    });
    console.log(r);

    hangouts = hangouts.concat(r.data.hangouts);
    for (let h of hangouts) {
      this.requests.push(h);
    }
    console.log(this.requests);
  },
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
}

#first {
  max-width: 1100px;
}

#second {
  max-width: 1100px;
}

#grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 1fr;
  column-gap: 15px;
  row-gap: 15px;
}

#gray {
  background: #F0F0F0;
  border: 1px solid #838383;
  box-sizing: border-box;
  border-radius: 5px;
}

#split {
  display: grid;
  grid-template-columns: 3fr 1fr;
  max-width: 1100px;
}

#heading {
  font-family: Roboto;
  font-style: normal;
  font-weight: bold;
  font-size: 30px;
  line-height: 35px;

  color: #000000;
  margin-bottom: 100px;
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
