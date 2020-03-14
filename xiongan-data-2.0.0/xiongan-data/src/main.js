import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');

Vue.prototype.ulcheckInit = function ulcheckInit() {
  const ulchecklis = document.querySelectorAll('.ulcheck > li');
  console.log(ulchecklis);
  for (let i = 0; i < ulchecklis.length; i += 1) {
    if (ulchecklis[i].querySelector('.delete')) {
      ulchecklis[i].querySelector('.delete').onclick = function uldelete(e) {
        this.parentNode.id = 'todelete';
        const element = document.getElementById('todelete');
        element.parentNode.removeChild(element);
        e.stopPropagation();
      };
    }
    const ulchecklisinput = ulchecklis[i].querySelectorAll('input');
    console.log(ulchecklisinput);
    if (ulchecklisinput) {
      for (let ii = 0; ii < ulchecklisinput.length; ii += 1) {
        console.log(ulchecklisinput[ii]);
        ulchecklisinput[ii].onclick = function preventIt(e) {
          e.stopPropagation();
        };
      }
    }
    ulchecklis[i].addEventListener(
      'click',
      function ulactive() {
        if (this.className.indexOf('active') !== -1) {
          this.classList.remove('active');
        } else {
          this.className += ' active';
        }
      },
      false,
    );
  }
};
