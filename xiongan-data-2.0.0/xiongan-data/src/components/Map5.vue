<template>
  <div class="mapBgCtn">
    <div class="map1" id="container"></div>
    <div class="marker">
      <div class="pwk" v-if="false">
        <div
          v-for="n in pwk.length"
          v-bind:key="'pwk'+n"
          :class="setClass('marker_pwk', n-1)">
          <img src="../assets/img/markDrop.png">
        </div>
      </div>
      <div class="pwk" v-else>
        <div
          v-for="n in pwk.length"
          v-bind:key="'pwk'+n"
          :class="setClass('marker_pwk', n-1)"
          v-on:click="clicked">
          <img src="../assets/img/markMonitor.png">
        </div>
      </div>
      <div class="dm">
        <div
          v-for="n in dm.length"
          v-bind:key="'dm'+n"
          :class="setClass('marker_dm', n-1)">
            <img src="../assets/img/markMonitor.png">
            <span class="t">南山水道#{{n}} 观测站</span>
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
export default {
  data() {
    return {
      offset: [-5, -28],

      pwk: [
        // [115.83868, 38.74641],
        // [115.84044, 38.75296],
        // [115.85259, 38.77733],
        [115.84824, 38.75112],
      ],
      dm: [
        [115.68024, 38.65112],
        [115.69024, 38.64112],
        [115.72158, 38.64512],
        [115.73898, 38.64612],
        [115.76359, 38.65212],
        [115.77024, 38.66112],
        [115.78024, 38.66812],
        [115.81024, 38.67112],
        [115.82624, 38.69112],
        [115.82024, 38.71112],

        [115.83024, 38.72112],
        [115.83724, 38.73112],
        [115.85568, 38.76848],
        [115.86368, 38.78448],
        [115.54568, 38.72358],
        [115.75668, 38.56548],
        [115.78668, 38.78848],
        [115.79468, 38.76848],
        [115.65768, 38.75448],
        [115.72868, 38.78748],

        [115.45868, 38.74848],
        [115.75868, 38.67748],
        [115.68748, 38.76848],
        [115.46668, 38.78448],
        [115.86768, 38.68748],
        [115.64868, 38.74648],
        [115.82468, 38.75348],
        [115.78268, 38.76448],
        [115.84368, 38.67848],
        [115.67868, 38.74548],

        [115.84568, 38.76548],
        [115.68768, 38.69848],
        [115.75868, 38.67448],
        [115.73468, 38.64448],
        [115.67468, 38.57848],
        [115.57668, 38.68948],
        [115.47668, 38.78648],
        [115.76568, 38.67848],
        [115.64768, 38.65748],
        [115.46868, 38.74648],

        [115.83168, 38.74148],
        [115.83268, 38.61448],
        [115.83468, 38.64148],
        [115.84168, 38.71448],
        [115.62468, 38.75148],

        [115.71468, 38.78148],
        [115.54768, 38.68648],
        [115.76868, 38.46748],
        [115.46868, 38.78788],
        [115.88468, 38.67848],
      ],
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
      center: [115.77024, 38.72112],
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
</style>
