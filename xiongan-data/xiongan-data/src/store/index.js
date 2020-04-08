import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    firstPageClick: 0,
    imgUrl1: 'case2-0',
    imgUrl: 'case1-0',
    imgUrl2: 'case1-0',
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
      return state.firstPageClick && state.imgUrl && state.imgUrl1 && state.imgUrl2;
    },
  },

});
