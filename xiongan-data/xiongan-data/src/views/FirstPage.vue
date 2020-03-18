<template>
  <div class="page inpage first">
    <ymap v-bind:display="true"/>

    <div class="inpanel left">
      <div class="logo">
        <h1>
          <router-link to="/">
            <img alt="LOGO" src="../assets/img/logo.png" />
          </router-link>
        </h1>
      </div>
      <page1left class="page1left"
        text="污染物浓度随时间变化"
        page="first"
        videoname=".mp4"/>
      <page1left class="page1left"
        text="孝义河流域地形分布图"
        titleDisplay="none"
        page="first"
        videoname="-2.mp4"/>
    </div>

    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png" />第{{num}}仿真监测站
                    <router-link to="/Combine" class="back">
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <page1middle class="page1middle"
          page="first" />
      </div>
    </div>

    <div class="inpanel right">
      <page1right class="page1right"/>
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map.vue';
import page1left from '@/components/firstpage/Page1Left.vue';
import page1right from '@/components/firstpage/Page1Right.vue';
import page1middle from '@/components/firstpage/Page1Middle.vue';

export default {
  data() {
    return {
      num: this.$store.state.firstPageClick + 1,
    };
  },
  components: {
    ymap,
    page1left,
    page1right,
    page1middle,
  },
};
//
</script>

<style lang="stylus" scoped>
@import '../global.styl';

layout-three($width-inpanel-l1, $width-inpanel-r1);

$top-offset1 = $padding-pagei-tb;

.inpanel{
  &.left{
    .page1left{
      margin: 1rem 0rem;
    }
  }
}

.inmiddle{
  .page1middle{
    position: relative;
    top: $top-offset1
  }
}

</style>
