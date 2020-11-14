import Vue from 'vue';
import VueRouter from "vue-router";

import Home from "./view/Home";
import User from "./view/User";
import Hangouts from "./view/Hangouts";
import FindHangouts from "./view/FindHangouts";

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home, name: "Home" },
  { path: '/user', component: User, name: "User" },
  { path: '/hangouts', component: Hangouts, name: "Hangouts" },
  { path: '/find-hangouts', component: FindHangouts, name: "FindHangouts" },
];

const router = new VueRouter({
  routes
});

export default router;