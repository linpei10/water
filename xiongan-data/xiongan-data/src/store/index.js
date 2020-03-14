import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    firstPageClick: 0,
  },

  mutations: {
    setFirstPageClick(state, index) {
      state.firstPageClick = index;
      console.log(state.firstPageClick);
    },
  },

  getters: {
    getFirstPageClick(state) {
      console.log(state.firstPageClick);
      return state.firstPageClick;
    },
  },
});