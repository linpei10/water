<template>
  <div class="page inpage third">
    <ymap display="true"/>
    <h1>{{this.$store.state.firstPageClick}}1111</h1>
    <div class="inpanel left">
      <div class="logo">
        <h1>
          <router-link to="/">
            <img src="../assets/img/logo.png" />
          </router-link>
        </h1>
      </div>
      <page1left class="page1left" display="none"/>
      <page1left class="page1left sec" display="none"/>
    </div>

    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png" />治理方案对比
          <router-link to="/SecondPage_1" class="back">
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <page1middle class="page1middle" />
        <page1middle class="page1middle sec"/>
      </div>
    </div>

    <div class="inpanel right">
      <h2 class="mtitle">
        <img src="../assets/img/Shape.png" />方案一
      </h2>
      <page1right class="page1right"/>
      <h2 class="mtitle sec">
        <img src="../assets/img/Shape.png" />方案二
      </h2>
      <page1right class="page1right sec"/>
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map.vue';
import page1left from '@/components/firstpage/Page1Left.vue';
import page1right from '@/components/firstpage/Page1Right.vue';
import page1middle from '@/components/firstpage/Page1Middle.vue';

export default {
  components: {
    ymap,
    page1left,
    page1right,
    page1middle,
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
      width: 32rem;
      top: 15.5rem;
      left: 37rem;
      .btn{
        margin: 1rem 0rem;
        font-size: 2.5rem;
        width: 12rem;
        height: 6rem;
        line-height: 6rem;
      }
    }
  }
}
</style>
