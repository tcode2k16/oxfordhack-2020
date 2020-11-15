<template>
  <div class="root">
    <page-title>Login</page-title>
    <div id="info">
      <div>
        <label for="email">Email</label>
        <input
          type="text"
          id="email"
          name="email"
          autocomplete="off"
          v-model="email"
        />

        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          name="password"
          autocomplete="off"
          v-model="password"
          @keyup.enter="
            login
          "
        />
        <div id="buttons">
          <page-button @click="login">Enter</page-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

import PageTitle from "../components/PageTitle";
import PageButton from "../components/PageButton";

export default {
  name: "Login",
  components: {
    "page-title": PageTitle,
    "page-button": PageButton,
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      let { email, password } = this;
      let r = await Axios.post("/auth/login", {
        email,
        password,
      });
      console.log(r.data);
      if (!r.data.error) {
        this.$router.push("/");
      }
    },
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
  margin-top: 50px;
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
</style>