<template>
<div>
  <div class="mid-box">
    <hr class="horizontal" :style="{display:display}"/>
    <div class="midfont" :style="{display:display}">
      <span class="midleft"># 第{{num}}监测断面</span>
      <span class="midright">断面水质分析展示</span>
    </div>

    <!-- <div class="image">
      <img id="wrw" :src="require('../../assets/img/temp/'+imgUrl+'.png')"/>
    </div> -->
    <video width="100%" height="100%" controls autoplay preload muted loop
      :src="'uploads/index/index-chi/'+page+'/M/'+this.$store.state.firstPageClick+'/'+imgUrl">
      <!-- <source :src="'uploads/'+page+'/'+this.$store.state.firstPageClick+'/middle/'+imgUrl" type="video/mp4"> -->
      Your browser does not support the video tag.
    </video>
    <!-- <video width="100%" height="100%" controls autoplay preload muted loop>
      <source :src="'uploads/'+page+'/'+this.$store.state.firstPageClick+'/middle/'+imgUrl" type="video/mp4">
      Your browser does not support the video tag.
    </video> -->
    <div class="button" >
      <div v-for="(item,index) in pollutant"
        v-bind:key="'img'+index"
        class="btn"
        tabindex="0"
        v-on:click="changeImg(index)">{{item}}</div>
    </div>
  </div>
</div>
</template>

<script>

export default {
  data() {
    return {
      pollutant: ['COD', 'TN', 'NH3', 'TP'],
      imgUrl: 'case1-0.mp4',
      num: this.$store.state.firstPageClick + 1,
    };
  },
  methods: {
    changeImg(index) {
      this.imgUrl = `case1-${index}.mp4`;
    },
  },
  props: {
    display: {
      type: [String],
      default: 'auto',
    },
    page: {
      type: [String],
    },
  },

};
</script>

<style lang="stylus" scoped>

$btn-height = 7.4rem;

.horizontal{
  height: 0.2rem;
  border: none;
  background-color: #FFFF00
}

.midfont{
  position: relative;
  font-size: 2rem;
  margin: 1rem 0rem 4rem;

  .midleft{
    color: #FFFF00
  }
  .midright{
    position: absolute;
    right: 0rem;
    color: #6AADE1
  }
}

.mid-box{
  .image{
    img{
      max-width: 100%;
      margin: auto;
    }
  }

  .button{
    position: relative;
    left: 1rem;
    top: 2rem;

    .btn{
      display: inline-block;
      width: $btn-height*2;
      height: $btn-height;
      line-height: $btn-height;
      font-size: 3rem;
      text-align: center;

      &:hover{
        background-image: url('../../assets/img/btnBox.png');
        background-size: 100% 100%;
      }

      &:focus{
        outline: none;
        background-image: url('../../assets/img/btnBox.png');
        background-size: 100% 100%;
      }
    }
  }
}


</style>
