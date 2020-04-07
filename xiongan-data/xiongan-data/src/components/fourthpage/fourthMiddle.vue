<template>
  <div>
    <div class="mid-box">
      <hr class="horizontal" :style="{display:display}"/>
      <div class="midfont" :style="{display:display}">
        <span class="midleft">#{{num}} 仿真监测站</span>

      </div>

      <!-- <div class="image">
        <img id="wrw" :src="require('../../assets/img/temp/'+imgUrl+'.png')"/>
      </div> -->
      <video class="video_four2" controls autoplay preload muted loop
             :src="'uploads/sim/sim-chi/first/M1/'+this.$store.state.firstPageClick+'/'+this.$store.state.imgUrl2+videoname1" type="video/mp4">
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
             v-on:click="changeImg1(index)">{{item}}</div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      pollutant: ['COD', 'TN', 'NH3-N', 'TP'],
      num: this.$store.state.firstPageClick + 1,
    };
  },
  methods: {
    changeImg1(index) {
      this.$store.state.imgUrl2 = `case1-${index}`;
      console.log(this.$store.state.imgUrl2);
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
    videoname1: {
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
video.video_four2{
  width: 48.53rem;
  height: 27.5rem
}

</style>
