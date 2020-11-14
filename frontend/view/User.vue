<template>
  <div class="root">
    <page-title>About me hello</page-title>
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
        <input type="text" id="fname" name="fname" />

        <label for="fname">Department</label>
        <input type="text" id="fname" name="fname" />
        <label for="fname">Hobbies / interests</label>
        <input type="text" id="fname" name="fname" />
        <label for="fname">Phone number</label>
        <input type="text" id="fname" name="fname" />
        <br />

        <div id="buttons">
          <button>Log out</button>
          <button>Update</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle";
export default {
  name: "User",
  components: {
    "page-title": PageTitle,
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
  margin-right: 30%;
}

#info > div {
  display: flex;
  flex-direction: column;
  row-gap: 10px;
  align-items: flex-start;
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
  background: #EEEEEE;
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
}

#buttons {
  margin-top: 100px;
  display: flex;
  justify-content: flex-end;
  width: 100%;
}

#buttons > button {
  margin-left: 20px;
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
}
</style>