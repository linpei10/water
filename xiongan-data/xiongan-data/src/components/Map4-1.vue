<template>
  <div class="mapBgCtn">
    <!-- 因为会显示不出来，为了调试所以写在 marker div 外了 -->

    <div
      class="map1"
      id="container"
    ></div>
    <div
      class="marker"
      v-if="display"
    >
      <div class="dm">
        <div
          v-for="n in dm.length"
          v-bind:key="'dm'+n"
          :class="setClass('marker_dm', n-1)"
        >
          <!--          <div class="flag" v-if="flagShow">-->
          <div class="flag">
            <div class="flagT">
              <span class="t1">#{{n}}仿真监测站</span>
            </div>
          </div>
          <router-link to="/ThirdPage-2">
            <img
              src="../assets/img/markMonitor.png"
              v-on:click="setPageClick(n-1)"
            >
          </router-link>
          <!--          <span class="t" v-if="(n-3)&&infoShow">污染源正常</span>-->
          <!--          <span class="t" v-else-if="!(n-3)&&infoShow">污染源关停</span><br>-->
        </div>
      </div>
      <div class="pwk">
        <div
          v-for="n in pwk.length"
          v-bind:key="'pwk'+n"
          :class="setClass('marker_pwk', n-1)"
        >
          <img src="../assets/img/markIn.png">
          <span class="t tt" >#{{n}} 工程入水口</span>
        </div>
      </div>
      <div class="ck">
        <div
          v-for="n in ck.length"
          v-bind:key="'ck'+n"
          :class="setClass('marker_ck', n-1)"
        >
          <img src="../assets/img/markOut.png">
          <span class="t tt" >#{{n}} 工程出水口</span>
        </div>
      </div>
      <div class="lk">
        <div
          v-for="n in lk.length"
          v-bind:key="'lk'+n"
          :class="setClass('marker_lk', n-1)"
        >
          <img src="../assets/img/engineering.png">
          <span class="t tt" >孝义河河口湿地水质净化工程</span>
        </div>
      </div>
<!--      <div class="marker_ck0">-->
<!--        <img src="../assets/img/markOut.png">-->
<!--      </div>-->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // offset: [-5, -28],
      offset: [10, -18],

      pwk: [
        [115.848192, 38.76312],
        [115.854502, 38.766283],
        [115.85484, 38.769723],
        [115.855296, 38.773803],
      ],
      dm: [
        [115.84024, 38.75112],
        [115.84724, 38.76248],
        [115.8547, 38.76712],
        [115.85605, 38.77626],
        [115.85831, 38.7812],
        [115.86568, 38.78848],
      ],
      rk: [
        [115.84838, 38.76331],
        [115.85442, 38.76647],
        [115.85525, 38.76972],
        [115.85567, 38.77383],
      ],
      ck: [
        [115.855573, 38.776965],
      ],
      lk: [
        [115.855144, 38.75999],
      ],
    };
  },

  props: {
    distPage: {
      type: [String],
      default: '#',
    },
    display: {
      type: [Boolean],
      default: true,
    },
    infoShow: {
      type: [Boolean],
      default: false,
    },
    flagShow: {
      type: [Boolean],
      default: false,
    },
  },

  methods: {
    setPageClick(index) {
      this.$store.commit('setFirstPageClick', index);
      if (this.distPage === '#-6') {
        this.$emit('callFather');
      }
    },
    setClass(string, index) {
      return string + index;
    },
  },

  mounted() {
    const { offset } = this;

    const map = new YunliMap.Map({
      container: 'container',
      layers: ['tianditu_img'],
      zoom: 14,
      center: [115.8547, 38.76812],
    });

    const mask = new YunliMap.Layer({
      layername: 'mask_layer',
      // maskColor: 'rgba(10,15,24,0.75)',
      maskColor: 'rgba(3,0,28,0.65)',
    });
    map.add(mask);

    for (let i = 0; i < this.dm.length; i += 1) {
      const div = document.querySelector(`.marker_dm${i}`);
      const marker = new YunliMap.CustomMarker({
        position: this.dm[i],
        offset, // 默认居中
        content: div,
      });
      map.add(marker);
    }

    for (let i = 0; i < this.pwk.length; i += 1) {
      const div = document.querySelector(`.marker_pwk${i}`);
      const marker = new YunliMap.CustomMarker({
        position: this.pwk[i],
        offset, // 默认居中
        content: div,
      });
      map.add(marker);
    }

    for (let i = 0; i < this.ck.length; i += 1) {
      const div = document.querySelector(`.marker_ck${i}`);
      const marker = new YunliMap.CustomMarker({
        position: this.ck[i],
        offset, // 默认居中
        content: div,
      });
      map.add(marker);
    }

    for (let i = 0; i < this.lk.length; i += 1) {
      const div = document.querySelector(`.marker_lk${i}`);
      const marker = new YunliMap.CustomMarker({
        position: this.lk[i],
        offset, // 默认居中
        content: div,
      });
      map.add(marker);
    }
  },
};
</script>

<style lang="stylus" scoped>
  .flag {
    pointer-events: none;
    padding-bottom: 3rem;
    border-left: 0.2rem solid #f7c809;

    .flagT {
      background: rgba(#09101A, 0.5);
      padding: 1.6rem 1.4rem;
      max-width: 18rem;
      display: inline-block;
      position: relative;

      span {
        display: block;

        &.t1 {
          color: #f7c809;
          margin-bottom: 0.4rem;
        }

        &.t2 {
          color: #67c0f5;
        }
      }
    }
  }

  div[class^='marker'], div[class*='marker'], [class~='marker'], [class|="marker"] {
  }

  div[class^='marker_dm'], div[class*='marker_dm'], [class~='marker_dm'], [class|="marker"], div[class^='marker_pwk'], div[class*='marker_pwk'], [class~='marker_pwk'], [class|="marker_pwk"], div[class^='marker_ck'], div[class*='marker_ck'], [class~='marker_ck'], [class|="marker_ck"], div[class^='marker_lk'], div[class*='marker_lk'], [class~='marker_lk'], [class|="marker_lk"]{
    z-index: 2;
    position: relative;

    .t {
      z-index: -1;
      display: inline-block;
      position: absolute;
      left: 3rem;
      top: 1rem;
      min-width: 11rem;
      max-width: 15rem;
      background: rgba(#fff, 0.2);
      padding: 0.5rem 0.8rem 0.5rem 4rem;
      opacity: 0;
      transition: opacity ease 0.1s;

      &.tt{
        opacity: 1;
      }
    }

    &:hover {
      .t {
        opacity: 1;
      }
    }
  }

  div[class^='marker_dm'], div[class*='marker_dm'], [class~='marker_dm']{
    :hover{
      animation: myblink 1.2s infinite;
    }
  }
  @keyframes myblink{
    50% {
      opacity: 0.4;
    }
  }

  #container {
    width: 100%;
    height: 100vh;
  }

  img {
    // 图片是43:32
    // height: 12.9rem;
    // width: 9.6rem;
    height: 8.6rem;
    width: 6.4rem;
    // height: 6.45rem;
    // width: 4.8rem;
  }
</style>

<style lang="stylus">
  .mapBgCtn .ol-overlaycontainer {
    &::before {
      pointer-events: none;
      content: '';
      display: block;
      width: 100vw;
      height: 100vh;
      position: fixed;
      left: 0;
      top: 0;
      z-index: 0;
      background-size: 20rem auto;
      background-image: url('../assets/img/bgdot.png');
    }

    &::before {
      pointer-events: none;
      content: '';
      display: block;
      width: 100vw;
      height: 100vh;
      position: fixed;
      left: 0;
      top: 0;
      z-index: 0;
      background-size: cover;
      background-image: url('../assets/img/bgshadow.svg');
    }
  }
</style>


<!--<template>-->
<!--<div>-->
<!--  <div class="map4_1" id="container"></div>-->
<!--  <div class="marker">-->
<!--    <div class="marker_dm0">-->
<!--      <router-link to="/ThirdPage-2">-->
<!--        <img src="../assets/img/markMonitor.png">-->
<!--      </router-link>-->
<!--    </div>-->
<!--    <div class="marker_dm1">-->
<!--      <router-link to="/ThirdPage-2">-->
<!--        <img src="../assets/img/markMonitor.png">-->
<!--      </router-link>-->
<!--    </div>-->
<!--    <div class="marker_dm2">-->
<!--      <router-link to="/ThirdPage-2">-->
<!--        <img src="../assets/img/markMonitor.png">-->
<!--      </router-link>-->
<!--    </div>-->
<!--    <div class="marker_dm3">-->
<!--      <router-link to="/ThirdPage-2">-->
<!--        <img src="../assets/img/markMonitor.png">-->
<!--      </router-link>-->
<!--    </div>-->
<!--    <div class="marker_dm4">-->
<!--      <router-link to="/ThirdPage-2">-->
<!--        <img src="../assets/img/markMonitor.png">-->
<!--      </router-link>-->
<!--    </div>-->
<!--    <div class="marker_dm5">-->
<!--      <router-link to="/ThirdPage-2">-->
<!--        <img src="../assets/img/markMonitor.png">-->
<!--      </router-link>-->
<!--    </div>-->
<!--    <div class="marker_rk0">-->
<!--      <img src="../assets/img/markIn.png">-->
<!--    </div>-->
<!--    <div class="marker_rk1">-->
<!--      <img src="../assets/img/markIn.png">-->
<!--    </div>-->
<!--    <div class="marker_rk2">-->
<!--      <img src="../assets/img/markIn.png">-->
<!--    </div>-->
<!--    <div class="marker_rk3">-->
<!--      <img src="../assets/img/markIn.png">-->
<!--    </div>-->
<!--    <div class="marker_ck0">-->
<!--      <img src="../assets/img/markOut.png">-->
<!--    </div>-->
<!--  </div>-->
<!--</div>-->
<!--</template>-->

<!--<script>-->

<!--const pwk = [-->
<!--  [115.83868, 38.74641],-->
<!--  [115.84044, 38.75296],-->
<!--  [115.85259, 38.77733],-->
<!--];-->
<!--const dm = [-->
<!--  [115.84024, 38.75112],-->
<!--  [115.84724, 38.76248],-->
<!--  [115.8547, 38.76712],-->
<!--  [115.85605, 38.77626],-->
<!--  [115.85831, 38.7812],-->
<!--  [115.86568, 38.78848],-->
<!--];-->
<!--const rk = [-->
<!--  [115.84838, 38.76331],-->
<!--  [115.85442, 38.76647],-->
<!--  [115.85525, 38.76972],-->
<!--  [115.85567, 38.77383],-->
<!--];-->
<!--const ck = [-->
<!--  [115.85577, 38.77699],-->
<!--];-->

<!--const offset = [-5, -28];-->

<!--export default {-->

<!--  data() {-->
<!--    return {-->
<!--      distPage: this.dist,-->
<!--    };-->
<!--  },-->

<!--  props: {-->
<!--    dist: String,-->
<!--  },-->

<!--  // methods: {-->
<!--  //   distPage(distPage) {-->

<!--  //   },-->

<!--  mounted() {-->
<!--    const map = new YunliMap.Map({-->
<!--      container: 'container',-->
<!--      layers: ['tianditu_img'],-->
<!--      zoom: 14,-->
<!--      center: [115.8547, 38.76812],-->
<!--    });-->

<!--    const mask = new YunliMap.Layer({-->
<!--      layername: 'mask_layer',-->
<!--      maskColor: 'rgba(3,0,28,0.65)',-->
<!--    });-->
<!--    map.add(mask);-->

<!--    for (let i = 0; i < dm.length; i += 1) {-->
<!--      const div = document.querySelector(`.marker_dm${i}`);-->
<!--      const marker = new YunliMap.CustomMarker({-->
<!--        position: dm[i],-->
<!--        offset, // 默认居中-->
<!--        content: div,-->
<!--      });-->
<!--      map.add(marker);-->
<!--    }-->

<!--    for (let i = 0; i < rk.length; i += 1) {-->
<!--      const div = document.querySelector(`.marker_rk${i}`);-->
<!--      const marker = new YunliMap.CustomMarker({-->
<!--        position: rk[i],-->
<!--        offset, // 默认居中-->
<!--        content: div,-->
<!--      });-->
<!--      map.add(marker);-->
<!--    }-->

<!--    for (let i = 0; i < ck.length; i += 1) {-->
<!--      const div = document.querySelector(`.marker_ck${i}`);-->
<!--      const marker = new YunliMap.CustomMarker({-->
<!--        position: ck[i],-->
<!--        offset, // 默认居中-->
<!--        content: div,-->
<!--      });-->
<!--      map.add(marker);-->
<!--    }-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<style lang="stylus" scoped>-->

<!--#container{-->
<!--  width: 100%;-->
<!--  height: 100vh;-->
<!--}-->

<!--img{-->
<!--  //图片是43:32-->
<!--  // height: 12.9rem;-->
<!--  // width: 9.6rem;-->
<!--  height: 8.6rem;-->
<!--  width: 6.4rem;-->
<!--  // height: 6.45rem;-->
<!--  // width: 4.8rem;-->
<!--}-->

<!--</style>-->
