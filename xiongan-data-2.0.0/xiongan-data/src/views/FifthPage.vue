<template>
  <!-- <div class="page inpage fifthPage"> -->
  <!-- <div class="page inpage transPage"> -->
  <div :class="pageClass">
    <!-- <div class="page inpage sixthPage"> -->
    <div v-if="isShow">
      <ymap/>
    </div>
    <div v-else>
      <ymap1 @callFather="gotoSixth" distPage="#-6" v-bind:infoShow="true"/>
    </div>

    <div class="inpanel left">
      <div class="logo">
        <h1>
          <a href="/">
            <img src="../assets/img/logo.png" />
          </a>
        </h1>
      </div>
      <div class="isTrans selectedSite">
        <h4><span class="site">南山水道东</span> 监测站</h4>
        <img
          class="siteImg"
          src="../assets/img/site.png"
        />
        <div class="btnRight">
          <button class="btnGrey small" v-on:click="gotoFifth()"><i class="i">&#xe659;</i>返回重新选择</button>
        </div>
        <i class="i siteRight">&#xe659;</i>
      </div>
      <div class="isSixth">
        <h3 class="h3l">超标水质等级</h3>
        <page1left class="page1left" title="仿真断面" v-bind:isChange="true"/>
        <page1right class="page1right"/>
      </div>
    </div>
    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle isFifth">
          <img src="../assets/img/Shape.png" />应急污染灾害预测
          <router-link to="/Combine" class="back">
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <h2 class="mtitle isTrans">
          <img src="../assets/img/Shape.png" />应急污染灾害预测
        </h2>
        <h2 class="mtitle isSixth">
          <img src="../assets/img/Shape.png" />污染超标后 <span class="s">126</span> S
          <a v-on:click="gotoTrans()" class="back">
            <i class="i">&#xe658;</i>返回
          </a>
        </h2>
        <li class="isFifth">
            <div class="site-item active">
              <span class="data dataDM">南山水道东 </span>
              <span class="data dataSZ">
                <span class="dataSZspan">监测站</span>
              </span>
              <div class="site-img">
                <img class="graph" src="../assets/img/site.png"/>
              </div>
              <div class="action">
                <button class="btnArr small" v-on:click="gotoTrans()">选择监测站</button>
              </div>
            </div>
          </li>
        <div class="tipbox-group isSixth">
          <div class="tipbox pwk">
            <h4><img src="../assets/img/icon-drop.png" />排污口列表</h4>
            <ul>
              <li>#1采蒲北码头 <span class="online is_online"><img src="../assets/img/online.png" />在线</span>
              </li>
              <li>#2邸庄信号塔 <span class="online is_offline"><img src="../assets/img/offline.png" />离线</span>
              </li>
              <li>#3邸庄东码头 <span class="online is_online"><img src="../assets/img/online.png" />在线</span>
              </li>
            </ul>
          </div>
          <div class="tipbox dm">
            <h4><img src="../assets/img/icon-wave.png" />断面列表</h4>
            <ul>
              <li>#思乡桥1 <span class="type">生态补偿考核断面1</span></li>
              <li>#思乡桥2 <span class="type">生态补偿考核断面2</span></li>
              <li>#思乡桥3 <span class="type">生态补偿考核断面3</span></li>
              <li>#思乡桥4 <span class="type">生态补偿考核断面4</span></li>
              <li>#思乡桥5 <span class="type">生态补偿考核断面5</span></li>
              <li>#思乡桥6 <span class="type">生态补偿考核断面6</span></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="inpanel right">
      <div class="isFifth panelFloat">
        <h3 class="h3l">监测点预警标准设定</h3>
        <div class="inputgroup">
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="0.7"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.05"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH-N</span>
              <input
                type="text"
                class="small"
                value="0.14"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0.05"
              >
              <span class="after">g/m3</span></div>
          </div>
          <div class="btnRight">
            <button class="btnGrey small"><i class="i">&#xe659;</i>保存标准</button><br>
            <button class="btnGrey small"><i class="i">&#xe808;</i>开始仿真</button>
          </div>
        </div>
      </div>
      <div class="isTrans panelFloat">
        <div class="dtable dtable-cb">
          <h3 class="h3l">超标输出值</h3>
          <div class="tablehead">
            <span class="data head">名称</span>
            <span class="data head">流速</span>
            <span class="data head">浊度</span>
            <span class="data head last">pH</span>
          </div>
          <ul>
            <li>
              <div class="item">
                <div class="line line1">
                  <span class="data data1">新思乡桥</span>
                  <span class="data data2">132.2 MPh</span>
                  <span class="data data3">7.0</span>
                  <span class="data data4 last">8.08</span>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="isSixth">
        <h3 class="h3l">污染物扩散模拟</h3>
        <page1middle class="page1middle" display="none"/>
        <h3 class="h3l">流域污染仿真演示</h3>
        <div class="wrfz-img">
          <img src="../assets/img/temp/fp4.png">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map5.vue';
import ymap1 from '@/components/Map.vue';
import page1left from '@/components/firstpage/Page1Left.vue';
import page1right from '@/components/firstpage/Page1Right.vue';
import page1middle from '@/components/firstpage/Page1Middle.vue';


export default {
  data() {
    return {
      pageClass: 'page inpage fifthPage',
      isShow: true,
    };
  },
  methods: {
    gotoFifth() {
      this.pageClass = 'page inpage fifthPage';
      this.isShow = true;
    },
    gotoTrans() {
      this.pageClass = 'page inpage transPage';
      this.isShow = false;
    },
    gotoSixth() {
      this.pageClass = 'page inpage sixthPage';
      this.isShow = false;
    },
  },
  components: {
    ymap,
    ymap1,
    page1left,
    page1right,
    page1middle,
  },
};
</script>

<style lang="stylus" scoped>
@import '../global.styl';

// register func & components
layout-three($width-inpanel-l1, $width-inpanel-r1);
btnArr();

// page trans
.transPage .isFifth, .sixthPage .isFifth, .fifthPage .isTrans, .sixthPage .isTrans, .fifthPage .isSixth, .transPage .isSixth {
  display: none;
}

// page inner style
.mapsCtn {
  width: 100vw;
  height: 100vh;
  display: flex;

  .mapSample {
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    z-index: $z-index-map;
    color: rgba(#fff, 0.2);
    font-size: 30rem;
    transition: all ease 0.1s;
  }
}

.fifthPage {
  .mapsCtn {
    .map1 {
      width: 100vw;
    }

    .map2 {
      flex: 0;
    }
  }

  .inpanel {
    &.left {
      @extend .bgTrans;
    }

    &.right {
      @extend .bgTrans;
    }
  }

  .inmiddle-ctn {
    .inmiddle {
    }
  }
}

.transPage {
  .mapsCtn {
    .map1 {
      width: $width-inpanel-l1;
    }

    .map2 {
      flex: 1;
    }
  }

  .inpanel {
    &.left {
      border-right: 0.2rem solid $cd3;

      .selectedSite {
        position: relative;
        background: rgba($ct1, 0.5);
        padding: 1rem 4rem 2rem 4rem;

        h4 {
          font-weight: normal;
          font-size: 1.8rem;
          color: $ct2;

          .site {
            color: $cd3;
          }
        }

        img {
          width: $width-inpanel-l1 - 2 * $padding-pagei-lr;
          margin: 1rem -4rem 0 -4rem;
        }

        .siteRight {
          background: rgba($ct1, 0.3);
          position: absolute;
          height: 100%;
          display: flex;
          justify-content: center;
          align-items: center;
          width: $padding-pagei-lr;
          top: 0;
          right: -($padding-pagei-lr);
        }
      }
    }

    &.right {
      @extend .bgTrans;

      .panelFloat {
        width: 32rem;
        float: right;
      }

      .dtable {
        .item {
          color: $ct2;
        }
      }
    }
  }

  .inmiddle-ctn {
    .inmiddle {
    }
  }
}

.sixthPage {
  .inpanel {
    &.left {
    }

    &.right {
    }
  }

  .inmiddle-ctn {
    .inmiddle {
      .s {
        color $cd3
      }
      .tipbox-group {
        position: absolute;
        right: 3rem;
        bottom: 0;

        .tipbox {
          margin-bottom: 3rem;

          &.pwk {
            border-color: $ct9;
          }

          &.dm {
            ul {
              li {
                color: $cd3;

                .type {
                  color: $ct2;
                  margin-left: 0.8rem;
                }
              }
            }
          }
        }
      }
    }
  }
}

.inmiddle-ctn{
  pointer-events: none;
}

.back{
  pointer-events: auto;
}
.page1middle{
  &>>>.button{
    .btn{
      margin: 1rem 0rem;
      font-size: 2.5rem;
      width: 11.2rem;
      height: 5.6rem;
      line-height: 5rem;
    }
  }
}
.wrfz-img{
  img{
    max-width: 100%;
    margin: auto;
  }
}

.page1right{


  &>>>ul{
    margin: 0rem;
    position: relative;
    left: -1rem;
    top: -2rem;

    li{
      display inline-block
      width: 22rem;
      height: 11rem;

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
.site-item {
  padding: 1.2rem 1.6rem;

  .dataDM {
    color: $cd3;
  }

  .dataSZspan {
    color: #007EFF;
    display: inline-block;
    margin-top: 1rem;
  }
  .site-img{
    img {
      height: 18rem;
      position: relative;
      top: 2rem;
    }
  }

  .action {
    display: none;
  }

  &.active {
    width: 36rem;
    border: 1px solid $cd3;
    border-width: 1px 0;
    background-color: rgba($ct1, 0.5);

    .action {
      display: block;
      position: relative;
      top: 1rem;
      left: 18rem;
      margin: 1.8rem 0 0.6rem 0;
    }
  }
}

.action{
  pointer-events: auto;
}
</style>
