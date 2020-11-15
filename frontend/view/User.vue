<template>
  <div class="root">
    <notification v-if="notiOpen" @close="()=>{notiOpen = false}" msg="Updated!" :time="1000"></notification>
    <page-title>About me</page-title>
    <div id="info">
      <div>
        <label for="name">Name</label>
        <input type="text" id="name" name="name" v-model="name" />

        <label for="pronouns">Preferred pronouns</label>
        <input type="text" id="pronouns" name="pronouns" v-model="pronouns" />
        <label for="year">Graduation year</label>
        <input type="text" id="year" name="year" v-model="year" />
        <label for="email">Email</label>
        <input type="text" id="email" name="email" v-model="email" />
        <label for="college">College</label>
        <input type="text" id="college" name="college" v-model="college" />
      </div>
      <div>
        <label for="fname">Gender</label>
        <div id="gender-btns">
          <input
            v-model="gender"
            type="radio"
            id="male"
            name="gender"
            value="male"
          />
          <label for="male">Male</label>
          <br />
          <input
            v-model="gender"
            type="radio"
            id="female"
            name="gender"
            value="female"
          />
          <label for="female">Female</label><br />
          <input
            v-model="gender"
            type="radio"
            id="NonBinary"
            name="gender"
            value="non-binary"
          />
          <label for="NonBinary">Non-binary</label>
          <input
            v-model="gender"
            type="radio"
            id="Prefernottodisclose"
            name="gender"
            value="prefer not to disclose"
          />
          <label for="Prefernottodisclose">Prefer not to disclose</label>
        </div>
        <!-- <input type="text" id="fname" name="fname" /> -->

        <label for="department">Department</label>
        <input
          type="text"
          id="department"
          name="department"
          v-model="department"
        />
        <label for="description">Hobbies / interests</label>
        <input
          type="text"
          id="description"
          name="description"
          v-model="description"
        />
        <label for="phonenumber">Phone number</label>
        <input
          type="text"
          id="phonenumber"
          name="phonenumber"
          v-model="phone_number"
        />
        <br />

        <div id="buttons">
          <img src="/img/human2.svg" alt="" />
          <page-button @click="logout">Log out</page-button>
          <page-button id="update" @click="updateProfile">Update</page-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import PageTitle from "../components/PageTitle";
import PageButton from "../components/PageButton";
import Notification from "../components/Notification";
export default {
  name: "User",
  components: {
    "page-title": PageTitle,
    "page-button": PageButton,
    'notification': Notification,
  },
  data() {
    return {
      id: undefined,
      name: undefined,
      college: undefined,
      department: undefined,
      email: undefined,
      year: undefined,
      phone_number: undefined,
      gender: undefined,
      pronouns: undefined,
      description: undefined,
      notiOpen: false,
    };
  },
  methods: {
    async logout() {
      await Axios.get("/auth/logout");
      this.$router.push("/login");
    },
    async updateProfile() {
      let r = await Axios.post("/auth/user_update", {
        name: this.name,
        id: this.id,
        name: this.name,
        college: this.college,
        department: this.department,
        email: this.email,
        year: this.year,
        phone_number: this.phone_number,
        gender: this.gender,
        pronouns: this.pronouns,
        description: this.description,
      });
      if (!r.data.error) {
        this.notiOpen = true;
      }
    },
  },
  async mounted() {
    let r = await Axios.get("/auth/user_info");
    if (r.status === 200 && !r.data.error) {
      this.name = r.data.user.name;
      this.id = r.data.user.id;
      this.name = r.data.user.name;
      this.college = r.data.user.college;
      this.department = r.data.user.department;
      this.email = r.data.user.email;
      this.year = r.data.user.year;
      this.phone_number = r.data.user.phone_number;
      this.gender = r.data.user.gender;
      this.pronouns = r.data.user.pronouns;
      this.description = r.data.user.description;
    }
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