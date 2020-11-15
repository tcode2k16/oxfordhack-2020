import Vue from 'vue';
import VueRouter from "vue-router";
import Axios from 'axios';

import Home from "./view/Home";
import User from "./view/User";
import Hangouts from "./view/Hangouts";
import FindHangouts from "./view/FindHangouts";
import Login from "./view/Login";


Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home, name: "Home" },
  { path: '/user', component: User, name: "User" },
  { path: '/hangouts', component: Hangouts, name: "Hangouts" },
  { path: '/find-hangouts', component: FindHangouts, name: "FindHangouts" },
  { path: '/login', component: Login, name: "Login" },
];

const router = new VueRouter({
  routes
});

router.beforeEach(async (to, from, next) => {
  try {
    let r = await Axios.get('/auth/user_info');
    if (r.status === 200 && !r.data.error) {
      if (r === '/login') {
        next({ name: 'Home' });
        return;
      }
      next();
      return;
    }


    if (to.path === '/login') {
      next();
      return;
    }

    next({ name: 'Login' });
  } catch (e) {
    console.log(e);
    next();
  }

})

export default router;