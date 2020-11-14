import Vue from 'vue';

// fonts
import 'typeface-roboto';

import App from './view/App';


import router from './router';



const app = new Vue({
  render: h => h(App),
  router,
}).$mount('#app');