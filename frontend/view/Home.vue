<template>
  <div class="root">
    <h1 class="heading">
      Hello, Alan! <br />
      It's a good day to make a new friend :)
    </h1>
    <!-- <button class="btn" @click="openModal">Open Modal</button> -->
    <div class="modal-overlay" v-if="modalOpen" @close="closeModal"></div>
    <modal v-if="modalOpen" @close="closeModal"></modal>
    <page-title>Waiting for a match for your hangouts...</page-title>
    <div id="first">
      <div id="grid">
        <card
          v-for="hangout in requests"
          :key="hangout.id"
          slotDirection="row"
          title=""
          subtitle=""
          content="Walk around Unversity Parks at 12pm on November 14th, 2020"
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
              v-for="hangout in upcoming.slice(0, Math.min(3, upcoming.length))"
              :key="hangout.id"
              slotDirection="row"
              :title="hangout.peer.name"
              :subtitle="`${hangout.peer.college} ${hangout.peer.department} ${hangout.peer.year}`"
              :content="`${hangout.activity} ${hangout.location} ${hangout.time}`"
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
import PageTitle from "../components/PageTitle";
import Modal from "../components/CreateHangoutModal";
import Card from "../components/Card";
export default {
  name: "Home",
  components: {
    "page-title": PageTitle,
    card: Card,
    Modal,
  },
  data() {
    return {
      modalOpen: false,
      upcoming: [],
      requests: [],
    };
  },
  methods: {
    openModal() {
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
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

</style>
