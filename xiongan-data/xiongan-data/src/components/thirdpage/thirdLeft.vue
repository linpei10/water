<template>
  <div>
    <div class="result" :style="{display:titleDisplay}">
      <span class="font">减排前仿真水质等级 Ⅳ类</span>
    </div>
    <h3 class="h3l" :style="{display:textDisplay}">{{text}}</h3>
    <!-- <img src="../../assets/img/video.jpg"/> -->
    <video width="100%" height="100%" controls autoplay preload muted loop>
      <source :src="'uploads/index/index-chi/'+page+'/L2/'+this.$store.state.firstPageClick+'/'+videoname" type="video/mp4">
      <!--      <source :src="'uploads/'+page+'/0/'+videoname" type="video/mp4">-->
      Your browser does not support the video tag.
    </video>
  </div>
</template>

<script>
// 引用断面小时数据
// import sectionData from '../../assets/json/section.json';

export default {
  props: {
    textDisplay: {
      type: [String],
      default: 'auto',
    },
    titleDisplay: {
      type: [String],
      default: 'auto',
    },
    text: {
      type: [String],
      default: '断面污染物三维分布',
    },
    page: {
      type: [String],
    },
    videoname: {
      type: [String],
    },
  },
};
</script>

<style scoped lang="stylus">
  @import '../../global.styl';

  .result{
    margin: 0rem 0rem 0rem;
    padding: 0rem 0rem;
    width: 100%;
    background-color:#39AAFF;
    text-align: center;
    font-size: 3rem;

    // &.yellow{
    //   background-color:#E4BD07;
    // }
  }
</style>
