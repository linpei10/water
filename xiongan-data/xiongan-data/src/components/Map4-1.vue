<template>
<div>
  <div class="map4_1" id="container"></div>
  <div class="marker">
    <div class="marker_dm0">
      <router-link to="/ThirdPage-2">
        <img src="../assets/img/markMonitor.png">
      </router-link>
    </div>
    <div class="marker_dm1">
      <router-link to="/ThirdPage-2">
        <img src="../assets/img/markMonitor.png">
      </router-link>
    </div>
    <div class="marker_dm2">
      <router-link to="/ThirdPage-2">
        <img src="../assets/img/markMonitor.png">
      </router-link>
    </div>
    <div class="marker_dm3">
      <router-link to="/ThirdPage-2">
        <img src="../assets/img/markMonitor.png">
      </router-link>
    </div>
    <div class="marker_dm4">
      <router-link to="/ThirdPage-2">
        <img src="../assets/img/markMonitor.png">
      </router-link>
    </div>
    <div class="marker_dm5">
      <router-link to="/ThirdPage-2">
        <img src="../assets/img/markMonitor.png">
      </router-link>
    </div>
    <div class="marker_rk0">
      <img src="../assets/img/markIn.png">
    </div>
    <div class="marker_rk1">
      <img src="../assets/img/markIn.png">
    </div>
    <div class="marker_rk2">
      <img src="../assets/img/markIn.png">
    </div>
    <div class="marker_rk3">
      <img src="../assets/img/markIn.png">
    </div>
    <div class="marker_ck0">
      <img src="../assets/img/markOut.png">
    </div>
  </div>
</div>
</template>

<script>

const pwk = [
  [115.83868, 38.74641],
  [115.84044, 38.75296],
  [115.85259, 38.77733],
];
const dm = [
  [115.84024, 38.75112],
  [115.84724, 38.76248],
  [115.8547, 38.76712],
  [115.85605, 38.77626],
  [115.85831, 38.7812],
  [115.86568, 38.78848],
];
const rk = [
  [115.84838, 38.76331],
  [115.85442, 38.76647],
  [115.85525, 38.76972],
  [115.85567, 38.77383],
];
const ck = [
  [115.85577, 38.77699],
];

const offset = [-5, -28];

export default {

  data() {
    return {
      distPage: this.dist,
    };
  },

  props: {
    dist: String,
  },

  // methods: {
  //   distPage(distPage) {

  //   },

  mounted() {
    const map = new YunliMap.Map({
      container: 'container',
      layers: ['tianditu_img'],
      zoom: 14,
      center: [115.8547, 38.76812],
    });

    const mask = new YunliMap.Layer({
      layername: 'mask_layer',
      maskColor: 'rgba(3,0,28,0.65)',
    });
    map.add(mask);

    for (let i = 0; i < dm.length; i += 1) {
      const div = document.querySelector(`.marker_dm${i}`);
      const marker = new YunliMap.CustomMarker({
        position: dm[i],
        offset, // 默认居中
        content: div,
      });
      map.add(marker);
    }

    for (let i = 0; i < rk.length; i += 1) {
      const div = document.querySelector(`.marker_rk${i}`);
      const marker = new YunliMap.CustomMarker({
        position: rk[i],
        offset, // 默认居中
        content: div,
      });
      map.add(marker);
    }

    for (let i = 0; i < ck.length; i += 1) {
      const div = document.querySelector(`.marker_ck${i}`);
      const marker = new YunliMap.CustomMarker({
        position: ck[i],
        offset, // 默认居中
        content: div,
      });
      map.add(marker);
    }
  },
};
</script>

<style lang="stylus" scoped>

#container{
  width: 100%;
  height: 100vh;
}

img{
  //图片是43:32
  // height: 12.9rem;
  // width: 9.6rem;
  height: 8.6rem;
  width: 6.4rem;
  // height: 6.45rem;
  // width: 4.8rem;
}

</style>
