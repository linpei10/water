<template>
  <div class="page inpage third">
    <ymap display="true"/>
    <h1>{{this.$store.state.firstPageClick}}</h1>
    <div class="inpanel left">
      <div class="logo">
        <h1>
          <router-link to="/">
            <img src="../assets/img/logo.png" />
          </router-link>
        </h1>
      </div>
      <thirdleft class="page1left"
                 display="none"
                 videoname2=".mp4"/>
      <thirdleft class="page1left sec"
                 display="none"
                 videoname2="-2.mp4"
      />
<!--      <thirdleft class="page1left"-->

<!--                 page="first"-->
<!--                 videoname=".mp4"/>-->
<!--      <thirdleft class="page1left sec"-->

<!--                 titleDisplay="none"-->
<!--                 page="first"-->
<!--                 videoname="-2.mp4"/>-->
    </div>

    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png" />治理方案对比
          <router-link to="/SecondPage_1" class="back">
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <thirdmiddle class="page1middle"
                     videoname1=".mp4"
        />
        <thirdmiddle class="page1middle sec"
                     videoname1="-2.mp4"
        />
      </div>
    </div>

    <div class="inpanel right">
      <h2 class="mtitle">
        <img src="../assets/img/Shape.png" />方案一
      </h2>
      <thirdright class="page1right"
                  image_name=".png"
      />
      <h2 class="mtitle sec">
        <img src="../assets/img/Shape.png" />方案二
      </h2>
      <thirdright class="page1right sec"
                  image_name="-2.png"
      />
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map.vue';
import thirdleft from '@/components/thirdpage/thirdLeft.vue';
import thirdright from '@/components/thirdpage/thirdRight.vue';
import thirdmiddle from '@/components/thirdpage/thirdMiddle.vue';

export default {
  components: {
    ymap,
    thirdleft,
    thirdright,
    thirdmiddle,
  },
};
</script>

<style lang="stylus" scoped>
@import '../global.styl';

layout-three($width-inpanel-l1, $width-inpanel-r1);

$lf-offset = $padding-pagei-lr;

$top-offset1 = $padding-pagei-tb;

.inpanel{
  &.left{
    .page1left{
      margin: 1rem 0rem;

      &.sec{
        position: relative;
        top: $top-offset1;
      }
    }
  }

  &.right{

    .mtitle{
      &.sec{
        position: relative;
        top: $top-offset1;
      }
    }

    .page1right{

      &.sec{
        position: relative;
        top: $top-offset1;
      }

      &>>>ul{
        margin: 0rem;
        position: relative;
        left: -1rem;
        top: -2rem;

        li{
          display inline-block
          width: 22rem;
          height: 14rem;

          .item{
            margin: 0rem 0rem 0rem 1rem;

            .image{
              left: 3rem;
              img{
                max-width: 90%
              }
            }
          }
        }
      }
    }
  }
}

.inmiddle{

  .page1middle{
    position: relative;
    top: $top-offset1

    &.sec{
      position: relative;
      top: $top-offset1 + $top-offset1;
    }

    &>>>.image{
      img{
        max-height: 31.8rem;
      }
    }
    &>>>.button{
      position: absolute;
      width: 4rem;
      top: 7.4rem;
      left: 50rem;
      .btn{
        margin: 0.72rem 0rem;
        font-size: 2.5rem;
        width: 12rem;
        height: 6rem;
        line-height: 6rem;
      }
    }
  }
}
</style>
