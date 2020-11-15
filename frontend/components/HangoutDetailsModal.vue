<template>
  <div class="modal">
    <div class="center">
      <page-title>Details about {{ hangout.peer.name }}'s Hangout</page-title>
      <div>
        <label>
          {{ hangout.activity }} @ {{ hangout.location }} <br />
          {{ time }}</label
        >
      </div>
      <div class="contact">
        <label> {{ hangout.peer.name }}'s info </label>
        <div class="details">
          <p>
            {{ hangout.peer.pronouns }} pronouns <br />
            {{ hangout.peer.gender }} <br />
            {{ hangout.peer.department }} student at {{ hangout.peer.college }}
            <br />
            Graduates {{ hangout.peer.year }} <br />
            {{ hangout.peer.description }}
          </p>
          <div class="row">
            <img class="icon" src="/img/email.svg" alt="" />
            <p>{{ hangout.peer.email }}</p>
          </div>
          <div class="row">
            <img class="icon" src="/img/phone.svg" alt="" />
            <p>{{ hangout.peer.phone_number }}</p>
          </div>
        </div>
      </div>
      <div class="btns">
        <button id="close-button" @click="close">Close Window</button>
        <button id="cancel-button" @click="close">Cancel Hangout</button>
      </div>
    </div>
  </div>
</template>
    
<script>
import moment from 'moment';
import PageTitle from "../components/PageTitle";
export default {
  name: "Modal",
  props: ["hangout"],
  methods: {
    close(event) {
      this.$emit("close");
    },
  },
  computed: {
    time() {
      return moment(this.hangout.time).fromNow();
    }
  },
  components: {
    "page-title": PageTitle,
  },
};
</script>
    
    
<style lang="css" scoped>
.modal {
  background-color: #fff;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  max-width: 1050px;
  max-height: 600px;
  /* top: 10%;
  left: 10%;
  right: 10%;
  bottom: 10%;
  width: 100%;
  max-width: 1100px;
  border-radius: 5px;
  padding: 40px; */
  background-color: #F8F8F8;
  border: 3px solid #428fea;
  z-index: 99;
}

* {
  font-size: 14px;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
}

.icon {
  margin-right: 10px;
  /* margin-left: 20%; */
  height: min-content;
}

.row {
  display: flex;
  width: 100%;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 30px;
  align-items: center;
}
.row > p {
  margin-top: 0;
  margin-bottom: 0;
}

.btns {
  display: flex;
  width: 100%;
  justify-content: space-around;
}

.contact {
  background: #e9f0f8;
  border: 1px solid #428fea;
  box-sizing: border-box;
  border-radius: 5px;
  padding: 10px 20px;
  align-items: left;
  margin-top: 20px;
  margin-bottom: 20px;
}

#buttons {
  margin-top: 60px;
  display: flex;
  justify-content: flex-end;
  width: 100%;
  max-width: 350px;
}

#cancel-button{
  background-color: #DF6C6C;
  color: #ffffff;
  border: none;

  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 21px;
  padding: 10px;
  border-radius: 5px;
  height: fit-content;

  cursor: pointer;
}

#close-button{
  background-color: #428FEA;
  color: #FFFFFF;
  border: none;

  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 21px;
  padding: 10px;
  border-radius: 5px;
  height: fit-content;

  cursor: pointer;
}

label {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;

  color: #000000;
}

input {
  background: #eeeeee;
  border-radius: 5px;
  outline: none;
  border: none;
  /* height: 44px; */
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;
  /* padding: 5px; */
  padding-top: 5px;
  padding-bottom: 5px;
  width: 100%;
  max-width: 350px;
  padding-left: 10px;
  padding-right: 10px;
}

.center {
  margin: auto;
  max-width: 50%;
  padding: 10px;
  text-align: center;
  display: grid;
  row-gap: 10px;
  /* height: 100%; */
  /* flex-direction: column; */
}

.details {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 23px;
  padding:30px
}
</style>
