<template>
  <div class="modal">
    <div class="container">
      <div>
        <div class="center">
            <page-title >Details about Alan's Hangout</page-title>
            <div> 
                <label>Walk around University Parks <br> at 12 pm on November 14th</label>
            </div>
            <div class="contact">
                <label>
                    Alan's info
                </label>
                <p>
                    He/him pronouns <br>
                    Male <br>
                    Computer Science student at St. John’s <br>
                    Undergrad 1st year student <br>
                    Enjoys reading/biking 
                </p>
                <div class="row">
                    <img class= "icon" src="/img/email.svg" alt="" />
                    <p> alan@st-johns.ox.ac.uk</p>
                </div>
                <div class="row">
                    <img class= "icon" src="/img/phone.svg" alt="" />
                    <p>7777777</p>
                </div>
            </div>
            <div id="cancel-buttons" class="center">
            <button @click="close">Cancel hangout</button>
            </div>
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
    close(event) {
      this.$emit("close");
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
  border-radius: 5px;
  padding: 40px;
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
    margin-left: 20%;
}

.row {
  display: flex;
  width: 100%; 
  height: 100%;
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

#cancel-buttons > button {
  margin-left: 20px;
  background-color:#DF6C6C;
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
  width: 60%;
  padding: 10px;
  justify-content: center;
  text-align: center;
}
</style>
