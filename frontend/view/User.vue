<template>
  <div class="root">
    <page-title>About me</page-title>
    <div id="info">
      <div>
        <label for="fname">Name</label>
        <input type="text" id="fname" name="fname" />

        <label for="fname">Preferred pronouns</label>
        <input type="text" id="fname" name="fname" />
        <label for="fname">Graduation year</label>
        <input type="text" id="fname" name="fname" />
        <label for="fname">Email</label>
        <input type="text" id="fname" name="fname" />
        <label for="fname">College</label>
        <input type="text" id="fname" name="fname" />
      </div>
      <div>
        <label for="fname">Gender</label>
        <div id="gender-btns">
          <input type="radio" id="male" name="gender" value="male" />
          <label for="male">Male</label>
          <br />
          <input type="radio" id="female" name="gender" value="female" />
          <label for="female">Female</label><br />
          <input
            type="radio"
            id="Non-binary"
            name="gender"
            value="Non-binary"
          />
          <label for="Non-binary">Non-binary</label>
          <input
            type="radio"
            id="Prefer not to disclose"
            name="gender"
            value="Prefer not to disclose"
          />
          <label for="Prefer not to disclose">Prefer not to disclose</label>
        </div>
        <!-- <input type="text" id="fname" name="fname" /> -->

        <label for="fname">Department</label>
        <input type="text" id="fname" name="fname" />
        <label for="fname">Hobbies / interests</label>
        <input type="text" id="fname" name="fname" />
        <label for="fname">Phone number</label>
        <input type="text" id="fname" name="fname" />
        <br />

        <div id="buttons">
          <img src="/img/human2.svg" alt="" />
          <page-button>Log out</page-button>
          <page-button>Update</page-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle";
import PageButton from "../components/PageButton";
export default {
  name: "User",
  components: {
    "page-title": PageTitle,
    "page-button": PageButton,
  },
};
</script>

<style scoped>
.root {
  margin-top: 5vh;
  display: flex;
  flex-direction: column;
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

#buttons {
  margin-top: 100px;
  display: flex;
  justify-content: flex-end;
  width: 100%;
  max-width: 370px;
}


#gender-btns {
  display: flex;
  justify-content: flex-start;
  /* flex-wrap: wrap; */
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
  background-color: #428FEA !important;
  color: #FFFFFF;
}
</style>