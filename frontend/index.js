import Vue from 'vue';

import App from './view/App';


const app = new Vue({
  render: h => h(App),
}).$mount('#app');