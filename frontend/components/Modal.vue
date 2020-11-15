<template>
  <div class="modal">
    <div class="container">
      <div>
        <page-title>Create a new hangout</page-title>
        <label for="fname">Activity</label>
        <div id="gender-btns">
          <input type="radio" id="anything" name="activity" value="anything" />
          <label for="anything">Anything</label>
          <br />
          <input type="radio" id="walk" name="activity" value="walk" />
          <label for="walk">Walk</label>
          <br />
          <input type="radio" id="run" name="activity" value="run" />
          <label for="run">Run</label>
          <br />
          <input type="radio" id="bike" name="activity" value="bike" />
          <label for="bike">Bike</label>
          <br />
          <input type="radio" id="sit" name="activity" value="sit" />
          <label for="sit">Sit</label>
        </div>
        <br />
        <label for="fname">Gender</label>
        <div id="gender-btns">
          <input type="radio" id="anywhere" name="location" value="anywhere" />
          <label for="anywhere">Anywhere</label>
          <br />
          <input type="radio" id="christ" name="location" value="christ" />
          <label for="christ">Christ Church Meadow</label>
          <br />
          <input type="radio" id="university" name="location" value="university" />
          <label for="university">University Parks</label>
          <br />
          <input type="radio" id="port" name="location" value="port" />
          <label for="port">Port Meadow</label>
        </div>
        <br />
        <label for="dateTime">Date and time</label>
        <br />
        <input type="text" id="dateTime" name="dateTime" />
        <br />
        <label for="additional">Additional info</label>
        <br />
        <input type="text" id="additional" name="additional" />
        <br />
        <div id="buttons">
          <button @click.prevent="close" v-if="close">Create hangout</button>
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
import PageTitle from "../components/PageTitle";
export default {
  name: "Modal",
  methods: {
    close() {
      console.log("close!!");
      this.$emit("close", false);
    }
  },
  props: {
    value: {
      type: Boolean,
      default: true
    }
  },
  components: {
    "page-title": PageTitle
  }
};
</script>
    
    
<style lang="css" scoped>
.modal {
  background-color: #fff;
  position: fixed;
  top: 10%;
  left: 10%;
  right: 10%;
  bottom: 10%;
  width: 100%;
  max-width: 1100px;
  padding: 20px;
  border-radius: 16px;
  border-color: #428fea;
  z-index: 99;
}

#buttons {
  margin-top: 100px;
  display: flex;
  justify-content: flex-end;
  width: 100%;
  max-width: 350px;
}

#buttons > button {
  margin-left: 20px;
  background-color: #428fea;
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

#gender-btns {
  display: flex;
  justify-content: flex-start;
  /* flex-wrap: wrap; */
  /* width: 100%; */
}
#gender-btns > button {
  /* margin-left: 20px;
  background-color: #428FEA;
  color: #FFFFFF;
  border: none;

  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 21px;
  padding: 10px;
  border-radius: 5px; */

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
  /* width: 100%; */
}

.selected {
  background-color: #428fea !important;
  color: #ffffff;
}

input[type="radio"] {
  display: none;
}
input[type="radio"] + label {
  user-select: none;
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
  margin-right: 10px;
  padding-left: 5px;
  padding-right: 5px;
}
input[type="radio"]:checked + label {
  background-color: #428fea !important;
  color: #ffffff;
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
</style>