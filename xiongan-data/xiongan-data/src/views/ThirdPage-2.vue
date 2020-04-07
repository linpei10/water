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
      <fourthleft class="page1left"
                 display="none"
                 water_num1="新建湿地水质净化工程前 Ⅳ类"
                 videoname2=".mp4"/>
      <fourthleft class="page1left sec"
                 display="none"
                 water_num1="新建湿地水质净化工程后水质等级 Ⅳ类"
                 videoname2="-2.mp4"
      />
      <!--      <fourthleft class="page1left"-->

      <!--                 page="first"-->
      <!--                 videoname=".mp4"/>-->
      <!--      <fourthleft class="page1left sec"-->

      <!--                 titleDisplay="none"-->
      <!--                 page="first"-->
      <!--                 videoname="-2.mp4"/>-->
    </div>

    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png" />新建工程前后对比
          <router-link to="/FourthPage" class="back">
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <fourthmiddle class="page1middle"
                     videoname1=".mp4"
        />
        <fourthmiddle class="page1middle sec"
                     videoname1="-2.mp4"
        />
      </div>
    </div>

    <div class="inpanel right">
      <h2 class="mtitle">
        <img src="../assets/img/Shape.png" />新建湿地水质净化工程前
      </h2>
      <fourthright class="page1right"
                  image_name=".png"
      />
      <h2 class="mtitle sec">
        <img src="../assets/img/Shape.png" />新建湿地水质净化工程后
      </h2>
      <fourthright class="page1right sec"
                  image_name="-2.png"
      />
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map.vue';
import fourthleft from '@/components/fourthpage/fourthLeft.vue';
import fourthright from '@/components/fourthpage/fourthRight.vue';
import fourthmiddle from '@/components/fourthpage/fourthMiddle.vue';

export default {
  components: {
    ymap,
    fourthleft,
    fourthright,
    fourthmiddle,
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
<!--<template>-->
<!--  <div class="page inpage third">-->
<!--    <ymap display="true"/>-->

<!--    <div class="inpanel left">-->
<!--      <div class="logo">-->
<!--        <h1>-->
<!--          <router-link to="/">-->
<!--            <img src="../assets/img/logo.png" />-->
<!--          </router-link>-->
<!--        </h1>-->
<!--      </div>-->
<!--      <fourthleft class="fourthleft" display="none"/>-->
<!--      <fourthleft class="fourthleft sec" display="none"/>-->
<!--    </div>-->

<!--    <div class="inmiddle-ctn">-->
<!--      <div class="inmiddle">-->
<!--        <h2 class="mtitle">-->
<!--          <img src="../assets/img/Shape.png" />治理方案对比-->
<!--          <router-link to="/FourthPage" class="back">-->
<!--            <i class="i">&#xe658;</i>返回-->
<!--          </router-link>-->
<!--        </h2>-->
<!--        <fourthmiddle class="fourthmiddle" />-->
<!--        <fourthmiddle class="fourthmiddle sec"/>-->
<!--      </div>-->
<!--    </div>-->

<!--    <div class="inpanel right">-->
<!--      <h2 class="mtitle">-->
<!--        <img src="../assets/img/Shape.png" />方案一-->
<!--      </h2>-->
<!--      <fourthright class="fourthright"/>-->
<!--      <h2 class="mtitle sec">-->
<!--        <img src="../assets/img/Shape.png" />方案二-->
<!--      </h2>-->
<!--      <fourthright class="fourthright sec"/>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import ymap from '@/components/Map.vue';-->
<!--import fourthleft from '@/components/fourthpage/fourthLeft.vue';-->
<!--import fourthright from '@/components/fourthpage/fourthRight.vue';-->
<!--import fourthmiddle from '@/components/fourthpage/fourthMiddle.vue';-->

<!--export default {-->
<!--  components: {-->
<!--    ymap,-->
<!--    fourthleft,-->
<!--    fourthright,-->
<!--    fourthmiddle,-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<style lang="stylus" scoped>-->
<!--@import '../global.styl';-->

<!--layout-three($width-inpanel-l1, $width-inpanel-r1);-->

<!--$lf-offset = $padding-pagei-lr;-->

<!--$top-offset1 = $padding-pagei-tb;-->

<!--.inpanel{-->
<!--  &.left{-->
<!--    .fourthleft{-->
<!--      margin: 1rem 0rem;-->

<!--      &.sec{-->
<!--        position: relative;-->
<!--        top: $top-offset1;-->
<!--      }-->
<!--    }-->
<!--  }-->

<!--  &.right{-->

<!--    .mtitle{-->
<!--      &.sec{-->
<!--        position: relative;-->
<!--        top: $top-offset1;-->
<!--      }-->
<!--    }-->

<!--    .fourthright{-->

<!--      &.sec{-->
<!--        position: relative;-->
<!--        top: $top-offset1;-->
<!--      }-->

<!--      &>>>ul{-->
<!--        margin: 0rem;-->
<!--        position: relative;-->
<!--        left: -1rem;-->
<!--        top: -2rem;-->
<!--        width 100%-->

<!--        li{-->
<!--          display inline-block-->
<!--          width: 22rem;-->
<!--          height: 14rem;-->

<!--          .item{-->
<!--            margin: 0rem 0rem 0rem 1rem;-->

<!--            .image{-->
<!--              left: 3rem;-->
<!--              img{-->
<!--                max-width: 90%-->
<!--              }-->
<!--            }-->
<!--          }-->
<!--        }-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--}-->

<!--.inmiddle{-->

<!--  .fourthmiddle{-->
<!--    position: relative;-->
<!--    top: $top-offset1-->

<!--    &.sec{-->
<!--      position: relative;-->
<!--      top: $top-offset1 + $top-offset1;-->
<!--    }-->

<!--    &>>>.image{-->
<!--      img{-->
<!--        max-height: 31.8rem;-->
<!--      }-->
<!--    }-->
<!--    &>>>.button{-->
<!--      position: absolute;-->
<!--      width: 32rem;-->
<!--      top: 15.5rem;-->
<!--      left: 37rem;-->
<!--      .btn{-->
<!--        margin: 1rem 0rem;-->
<!--        font-size: 2.5rem;-->
<!--        width: 12rem;-->
<!--        height: 6rem;-->
<!--        line-height: 6rem;-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</style>-->
