<template>
  <div>
    <div class="result" :style="{display:titleDisplay}">
      <span class="font">{{water_num}}</span>
    </div>
<!--.result-->
    <!-- <img src="../../assets/img/video.jpg"/> -->
    <video :src="'uploads/govern/govern-chi/first/L1/'+this.$store.state.firstPageClick+'/'+this.$store.state.imgUrl1+videoname2" type="video/mp4" class="video_third1"  controls autoplay preload muted loop>

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
      num2: this.$store.state.imgUrl1,
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
    water_num: {
      type: [String],
      default: '',
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
  video.video_third1{
    width: 45rem;
    height: 25.3rem
  }
</style>
