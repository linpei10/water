<template>
<div>
  <div class="result" :style="{display:titleDisplay}">
    <span class="font">{{text_1}}</span>
  </div>
  <h3 class="h3l" :style="{display:textDisplay}">{{text_2}}</h3>
    <!-- <img src="../../assets/img/video.jpg"/> -->
    <video class="video_fifth1" :src="'uploads/emer/emer-chi/first/L1/'+this.$store.state.firstPageClick+'/'+this.$store.state.imgUrl+videoname" type="video/mp4"  controls autoplay preload muted loop>
<!--      <source :src="'uploads/index/index-chi/'+page+'/L1/'+this.$store.state.firstPageClick+'/'+this.$store.state.imgUrl" type="video/mp4">-->
<!--      <source :src="'uploads/'+page+'/0/'+videoname" type="video/mp4">-->
      Your browser does not support the video tag.
    </video>
</div>
</template>

<script>
// 引用断面小时数据
// import sectionData from '../../assets/json/section.json';
import page1middle from '@/components/firstpage/Page1Middle.vue';

export default {
  data() {
    return {
      num1: this.$store.state.imgUrl,
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
    text_1: {
      type: [String],

    },
    text_2: {
      type: [String],

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
  video.video_fifth1{
    width: 44.13rem;
    height: 24.75rem
  }
</style>
