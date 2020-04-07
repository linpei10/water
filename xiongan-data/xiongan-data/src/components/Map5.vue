<template>
  <div class="mapBgCtn">
    <div class="map1" id="container"></div>
    <div class="marker">
<!--      <div class="pwk" v-if="false">-->
<!--        <div-->
<!--          v-for="n in pwk.length"-->
<!--          v-bind:key="'pwk'+n"-->
<!--          :class="setClass('marker_pwk', n-1)">-->
<!--          <img src="../assets/img/markDrop.png">-->
<!--        </div>-->
<!--      </div>-->
      <div class="pwk" >
        <div
          v-for="n in pwk.length"
          v-bind:key="'pwk'+n"
          :class="setClass('marker_pwk', n-1)"
          v-on:click="clicked">
          <img v-on:click="gotoFifth()" src="../assets/img/markRed.png">
          <span class="t">拥城思乡桥观测站</span>
        </div>
      </div>
      <div class="dm">
        <div
          v-for="(data,index) in Datas.slice(0,100)"
          v-bind:key="index"
          :class="setClass('marker_dm', index)">
            <img src="../assets/img/markshi.png">
            <span class="t">{{data.STNM}}第{{index+1}}观测站</span>
        </div>
      </div>
    </div>
    <!-- <div class="info">
      <div
        v-for="n in dm.length"
        v-bind:key="'info'+n"
        :id="setClass('info',n-1)">
        <h3 class="content">南山水道{{n}}</h3>
        <span>监测站</span>
      </div>
    </div> -->
  </div>
</template>

<script>

import Datas from '../assets/json/data.json';
import Data1s from '../assets/json/data1.json';

export default {
  data() {
    return {
      Datas: Datas.data,
      offset: [-5, -28],
      pwk: [
        // [115.83868, 38.74641],
        // [115.84044, 38.75296],
        // [115.85259, 38.77733],
        [115.838104, 38.746206],
      ],
      dm: Data1s.data,
      rk: [
        [115.84838, 38.76331],
        [115.85442, 38.76647],
        [115.85525, 38.76972],
        [115.85567, 38.77383],
      ],
      ck: [[115.85577, 38.77699]],

      distPage: this.dist,
      classPage: 'page inpage transPage',
      active: this.isActive,
    };
  },

  props: {
    dist: String,
    isActive: String,
  },
  methods: {
    gotoFifth() {
      this.pageClass = 'page inpage fifthPage';
      this.isShow = true;
    },
    gotoTrans() {
      this.pageClass = 'page inpage transPage';
      this.isShow = false;
    },
    gotoSixth() {
      this.pageClass = 'page inpage sixthPage';
      this.isShow = false;
    },
    isMouseover(index) {
      if (this.mouseover) {
        if (this.mouseover[index]) {
          return 'active';
        }
      }
      return '';
    },
    setMouseover(index) {
      this.mouseover.splice(index, 1, true);
    },
    setMouseout(index) {
      this.mouseover.splice(index, 1, false);
    },
    setPageClick(index) {
      this.$store.commit('setFirstPageClick', index);
    },
    setClass(string, index) {
      return string + index;
    },
    clicked() {
      this.isActive = true;
    },
  },

  mounted() {
    const { offset } = this;

    const map = new YunliMap.Map({
      container: 'container',
      layers: ['tianditu_img'],
      zoom: 11,
      center: [115.874316, 38.897144],
    });

    const mask = new YunliMap.Layer({
      layername: 'mask_layer',
      // maskColor: 'rgba(10,15,24,0.75)',
      maskColor: 'rgba(3,0,28,0.65)',
    });
    map.add(mask);

    // const infoWindows = [];
    // for (let i = 0; i < this.dm.length; i += 1) {
    //   infoWindows[i] = new YunliMap.InfoWindow({
    //     content: document.getElementById(`info${i}`),
    //     position: this.dm[i],
    //     offset: [0, -40], // 偏移量
    //     hasAngle: true,
    //     forceTop: true, // 禁用适应屏幕
    //   });
    //   infoWindows[i].hide();
    //   map.add(infoWindows[i]);
    // }

    // const circles = [];
    // for (let i = 0; i < this.dm.length; i += 1) {
    //   circles[i] = new YunliMap.CircleMarker({
    //     position: this.dm[i],
    //     radius: 35,
    //     style: {
    //       background: 'rgba(51,205,218,0)',
    //       borderColor: '#FFF',
    //       borderWidth: 0,
    //     },
    //   });
    //   map.add(circles[i]);
    //   circles[i].on('mouseenter', () => {
    //     infoWindows[i].show();
    //   });
    //   circles[i].on('mouseleave', () => {
    //     infoWindows[i].hide();
    //   });
    // }

    for (let i = 0; i < this.dm.length; i += 1) {
      const div = document.querySelector(`.marker_dm${i}`);
      console.log(i);
      console.log(this.dm[i]);
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
  },
};
</script>

<style lang="stylus" scoped>

div[class^='marker_dm'], div[class*='marker_dm'], [class~='marker_dm'], [class|="marker"], div[class^='marker_pwk'], div[class*='marker_pwk'], [class~='marker_pwk'], [class|="marker_pwk"] {
  z-index: 2;
  position: relative;

  .t {
    z-index: -1;
    display: inline-block;
    position: absolute;
    left: 3rem;
    top: 1rem;
    min-width: 8rem;
    max-width: 15rem;
    background: rgba(#fff, 0.2);
    padding: 0.5rem 0.8rem 0.5rem 4rem;
    opacity: 0;
    transition: opacity ease 0.1s;
  }

  &:hover {
    .t {
      opacity: 1;
    }
  }
}

.marker {
  z-index: 1;
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
div[class*='marker_pwk']{
    animation: myblink-data-v-3074bd5c 1.2s infinite;
}
</style>
