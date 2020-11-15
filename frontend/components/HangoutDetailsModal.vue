<template>
  <div class="modal">
    <div class="container">
      <div>
        <div class="center">
            <page-title >Details about Alan's Hangout</page-title>
        </div>
        <div id="info">
            <div> 
                <p>Walk around University Parks <br> at 12 pm on November 14th</p>
            </div>
            <div class="contact">
                <label>
                    Alan
                </label>
                <p>
                    He/him pronouns <br>
                    Male <br>
                    Computer Science student at St. John’s <br>
                    Graduating in 2022 <br>
                    Enjoys reading/biking <br>
                </p>
            </div>
        </div>
        <div id="cancel-buttons">
          <button @click="close">Cancel hangout</button>
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
  border: 3px solid #428fea;
  z-index: 99;
}

* {
    font-size: 14px;
    font-family: Roboto;
    font-style: normal;
    font-weight: normal;
}

.contact {
    background: #e9f0f8;
    border: 1px solid #428fea;
    box-sizing: border-box;
    border-radius: 5px;
    padding: 10px 20px;
    align-items: left;
    max-width: 400px;
}

#buttons {
  margin-top: 20px;
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


#info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 70px;
  max-width: 1000px;
}

#info > div {
  display: flex;
  flex-direction: column;
  row-gap: 10px;
  align-items: flex-start;
  white-space: nowrap;

  /* margin: 10px; */
  /* column-gap: 10px; */
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

.center {
  margin: auto;
  width: 60%;
  padding: 10px;
  justify-content: center;
  text-align: center;
}
</style>
