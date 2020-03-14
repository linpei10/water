<template>
<div>
  <div class="result" :style="{display:titleDisplay}">
    <span class="font">污染物浓度</span>
  </div>
  <h3 class="h3l" :style="{display:textDisplay}">{{text}}</h3>
    <!-- <img src="../../assets/img/video.jpg"/> -->
    <video width="100%" height="100%" controls autoplay preload muted loop>
      <source :src="'uploads/'+page+'/'+this.$store.state.firstPageClick+'/'+videoname" type="video/mp4">
      Your browser does not support the video tag.
    </video>
</div>
</template>

<script>
// 引用断面小时数据
// import sectionData from '../../assets/json/section.json';

export default {
  props: {
    testDisplay: {
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
  margin: 0rem 0rem 3rem;
  padding: 1rem 0rem;
  width: 90%;
  background-color:#39AAFF;
  text-align: center;
  font-size: 4rem;

  // &.yellow{
  //   background-color:#E4BD07;
  // }
}
</style>
