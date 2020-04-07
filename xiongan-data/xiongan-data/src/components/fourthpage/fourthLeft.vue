<template>
  <div>
    <div class="result" :style="{display:titleDisplay}">
      <span class="font">{{water_num1}}</span>
    </div>
<!--.result-->
    <!-- <img src="../../assets/img/video.jpg"/> -->
    <video :src="'uploads/sim/sim-chi/first/L1/'+this.$store.state.firstPageClick+'/'+this.$store.state.imgUrl2+videoname2" type="video/mp4" class="video_four1"  controls autoplay preload muted loop>
      <!--      <source :src="'uploads/'+page+'/0/'+videoname" type="video/mp4">-->
      Your browser does not support the video tag.
    </video>
  </div>
</template>

<script>
// 引用断面小时数据
// import sectionData from '../../assets/json/section.json';

export default {
  data() {
    return {
      num2: this.$store.state.imgUrl2,
    };
  },
  props: {
    textDisplay: {
      type: [String],
      default: 'auto',
    },
    titleDisplay: {
      type: [String],
      default: 'auto',
    },
    water_num1: {
      type: [String],
      default: '断面污染物三维分布',
    },
    page: {
      type: [String],
    },
    videoname2: {
      type: [String],
    },
  },
};
</script>

<style scoped lang="stylus">
  @import '../../global.styl';

  .result{
    margin: 0rem 0rem 3rem;
    padding: 0rem 0rem;
    width: 100%;
    background-color:#39AAFF;
    text-align: center;
    font-size: 3rem;

    // &.yellow{
    //   background-color:#E4BD07;
    // }
  }
  video.video_four1{
    width: 45rem;
    height: 25.3rem
  }
</style>
