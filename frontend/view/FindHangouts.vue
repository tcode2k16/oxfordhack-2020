<template>
  <div class="root">
    <notification
      v-if="notiOpen"
      @close="
        () => {
          notiOpen = false;
        }
      "
      msg="Hangout Matched!"
      :time="1000"
    ></notification>
    <div
      class="modal-overlay"
      v-if="modalOpen"
      @click="closeModal"
    ></div>
    <modal v-if="modalOpen" :hangout="selectedHangout" @close="closeModal" @accept="acceptHangout(selectedHangout)"></modal>
    <page-title class="pageTitle">See what people are doing</page-title>
    <transition name="fade">
      <div class="cards">
        <card
          v-for="feed in feeds.filter(e => isFuture(e.time)).sort(sortByRecent)"
          @click="openModal(feed)"
          :key="feed.id"
          slotDirection="column"
          :title="feed.author.name"
          :subtitle="`${feed.author.college} ${feed.author.department} ${feed.author.year}`"
          :content="`${feed.activity} @ ${feed.location} ${getRelTime(feed.time)}`"
        >
          <page-button @click="acceptHangout(feed)">Let’s hangout!</page-button>
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
    </transition>
  </div>
</template>

<script>
import Axios from "axios";
import moment from 'moment';
import PageTitle from "../components/PageTitle";
import PageButton from "../components/PageButton";
import Notification from "../components/Notification";
import Card from "../components/Card";
import Modal from "../components/HangoutRequestModal";
export default {
  name: "FindHangouts",
  components: {
    "page-title": PageTitle,
    "page-button": PageButton,
    notification: Notification,
    card: Card,
    Modal,
  },
  data() {
    return {
      feeds: {},
      interval: undefined,
      notiOpen: false,
      modalOpen: false,
    };
  },
  methods: {
    sortByRecent(a, b) {
      return moment(a.time) - moment(b.time);
    },
    getRelTime(t) {
      return moment(t).fromNow();
    },
    isFuture(t) {
      return moment(t).isAfter(moment());
    },
    openModal(hangout) {
      this.modalOpen = true;
      this.selectedHangout = hangout;
      this.$set(this.selectedHangout, 'peer', hangout.author);
    },
    closeModal() {
      this.modalOpen = false;
    },
    async refreshFeed() {
      let r = await Axios.get("/auth/my_feed");
      console.log(r.data);
      this.feeds = r.data.feeds;
    },
    async acceptHangout(hangout) {
      this.openModal=false;
      console.log(hangout);
      let r = await Axios.post("/auth/take", {
        hid: hangout.hangout_id,
      });

      if (!r.data.error) {
        await this.refreshFeed();
        this.notiOpen = true;
      }
    },
  },
  async mounted() {
    await this.refreshFeed();

    this.interval = setInterval(() => {
      this.refreshFeed();
    }, 1000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
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
</style>