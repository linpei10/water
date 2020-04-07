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
            <img src="../assets/img/logo.png"/>
          </a>
        </h1>
      </div>
      <div class="isFifth">
        <li class="isFifth">
          <div class="site-item active">
            <span class="data dataDM">新思乡桥 </span>
            <span class="data dataSZ">
                <span class="dataSZspan">监测站</span>
              </span>
            <div class="action">
              <button class="btnArr small" v-on:click="gotoTrans()">查看监测站详情</button>
            </div>
            <div class="site-img">
              <a v-on:click="gotoTrans()" class="back">
                <img class="graph" src="../assets/img/site_1.png"/>
              </a>
            </div>
          </div>
        </li>
        <div class="dtable dtable-cb dtable-img">
          <h3 class="h3l">图标说明</h3>
          <div style="text-align: center;height: 5rem" class="tablehead">
            <img class="data head" src="../assets/img/markMonitor.png" alt="">
            <img class="data head" src="../assets/img/markshi.png" alt="">
            <img class="data head" src="../assets/img/markDrop.png" alt="">
            <img class="data head" src="../assets/img/markOut.png" alt="">
            <img class="data head" src="../assets/img/markIn.png" alt="">
          </div>
          <ul>
            <li>
              <div class="item">
                <div style="text-align: center;margin-top: 6rem;" class="line line1">
                  <span class="data data1">仿真监测站</span>
                  <span class="data data2">实际监测站</span>
                  <span class="data data3">排污口</span>
                  <span class="data data4">出水口</span>
                  <span class="data data4">进水口</span>
                </div>
              </div>
            </li>
          </ul>
        </div>
        <div class="dtable dtable-cb dtable-text">
          <h3 class="h3l">是否超标</h3>
          <div style="text-align: center" class="tablehead">
            <div class="data head h33 h3g" ></div>
            <div class="data head h33 h3r" ></div>
          </div>
          <ul style="margin-top: 2rem">
            <li>
              <div class="item">
                <div style="text-align: center" class="line line1">
                  <span class="data data1">未超标</span>
                  <span class="data data2">已超标</span>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="isTrans selectedSite">
        <h4><span class="site">新思乡桥</span> 监测站</h4>
        <router-link to="/map_sxq" class="back">
          <img
            class="siteImg"
            src="../assets/img/site.jpg"
          />
        </router-link>
        <div>
          <video class="video_U" controls autoplay preload muted loop>
            <source src="uploads/emer/U.mp4" type="video/mp4">
          </video>
        </div>
      </div>
      <div class="isSixth">
        <page1left class="page1left" title="仿真断面" v-bind:isChange="true" text_1="污染物浓度仿真"
                   text_2="污染物浓度随时间变化分析" videoname=".mp4"/>
        <page1left class="page1left" title="仿真断面" v-bind:isChange="true" text_2="孝义河流域速度分布图"
                   videoname="-2.mp4"/>
      </div>
    </div>
    <div style="pointer-events: none" class="inmiddle-ctn isFifth">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png"/>水质污染灾害应急预警
          <router-link to="/Combine" class="back">
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
      </div>
    </div>
    <div style="pointer-events: none" class="inmiddle-ctn isTrans">
      <div class="inmiddle">
        <h2 class="mtitle isTrans">
          <img src="../assets/img/Shape.png"/>水质污染灾害应急预警
            <a v-on:click="gotoFifth()" class="back">
              <i class="i">&#xe658;</i>返回
            </a>
        </h2>
      </div>
    </div>
    <div class="inmiddle-ctn isSixth">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png"/>#{{num}}仿真监测站
          <a v-on:click="gotoTrans()" class="back">
            <i class="i">&#xe658;</i>返回
          </a>
          <page1middle class="page1middle" title="监测分段"/>
        </h2>
      </div>
    </div>
    <div class="inpanel right">
      <div class="isSixth">
        <page1right class="page1right" title="仿真断面" v-bind:isChange="true"/>
      </div>
      <div class="isFifth panelFloat">
        <h3 class="h3l">水质预警标准设定
          <select>
            <option value ="volvo">GB3838-2002</option>
            <option value ="saab">其他标准</option>
          </select>
        </h3>
        <div class="inputgroup">
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="40"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.4"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH³-N</span>
              <input
                type="text"
                class="small"
                value="2"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="2"
              >
              <span class="after">mg/L</span></div>
          </div>
          <divyarn class="btnRight">
            <button class="btnGrey small"><i class="i">&#xe659;</i>保存标准</button>
          </divyarn >
          <div>
            <p style="text-indent: 20px">根据国家或地方标准，行业标准设定监控预警污染物浓度数值。当各监测站实测数据超过设定数值时，此预警系统启动。</p>
          </div>
        </div>
      </div>
      <div class="isTrans panelFloat">
        <div class="dtable dlist dlist-dm">
          <h3 class="h3l">各仿真监测站水质等级时间变化曲线</h3>
          <ul>
            <li v-for="n in 6" v-bind:key="n+'sz'">
              <div class="item" :class="isMouseover(n-1)"
                   v-on:mouseover="setMouseover(n-1)"
                   v-on:mouseout="setMouseout(n-1)">
                <span class="data dataDM">#{{n}} 仿真监测站</span><br>
                <span class="data dataSZ">
                <span class="dataSZspan">{{waterQuality[n-1]}}</span>
              </span>
                <img
                  class="graph"
                  :src="'uploads/emer/right/case5-'+ n +'.png'"
                />
                <div class="action">
                  <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                  <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                  <router-link to="firstPage">
                    <button class="btnArr small">开始模拟</button>
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
        </div>
        <div class="btnRight">
          <button  style="margin-top: 2rem" class="btnGrey small isTrans"><i class="i">&#xe808;</i>开始仿真</button>
        </div>
        <div>
          <h3 class="h3l">污染物扩散模拟</h3>
          <video class="video_tp" controls autoplay preload muted loop>
            <source src="uploads/emer/case5-TP.mp4" type="video/mp4">
          </video>
        </div>
      </div>
      <div class="isFifth" style="margin-top: 8rem">
        <h3 class="h3l">水质监测站信息</h3>
        <table>
        <tr>
          <td>名称:</td>
          <td>新思乡桥监测站</td>
        </tr>
          <tr>
            <td>经度:</td>
            <td>115.838266</td>
          </tr>
          <tr>
            <td>纬度:</td>
            <td>38.745683</td>
          </tr>
          <tr>
            <td>污染物类别:</td>
            <td>TP</td>
          </tr>
          <tr>
            <td>污染物浓度:</td>
            <td>0.5mg/L</td>
          </tr>
          <tr>
            <td>污染物超标值:</td>
            <td>0.1mg/L</td>
          </tr>
        </table>
<!--        <p>名称：新思乡桥监测站</p>-->
<!--        <p>经度：115.838266</p>-->
<!--        <p>纬度：38.745683</p>-->
<!--        <p>污染物类别：TP</p>-->
<!--        <p>污染物浓度：0.5mg/L</p>-->
<!--        <p>污染物超标量：0.1mg/L</p>-->
        <p>水质监测站概况：</p>
        <textarea name="" id="">雄安新区边界安新县龙化乡拥城村思乡桥水质监测站，主要检测白洋淀孝义河上游来水和监测断面水质情况，监测水质类别为：pH、溶解氧、电导率、浊度、水温、 COD、高锰酸盐指数、化学需氧量、氨氮、总磷
        </textarea>
      </div>
    </div>
    <div class="panelwide bottom isTrans">
      <div class="sec-qsz">
        <h3 class="h3l">各仿真监测站全时长平均水质等级</h3>
        <div class="graph graph-qsz">

          <div
            class="wttype6"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">1<span class="p">站点1</span></span>
          </div>

          <div
            class="wttype6"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">2<span class="p">站点2</span></span>
          </div>

          <div
            class="wttype6"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">3<span class="p">站点3</span></span>
          </div>

          <div
            class="wttype6"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">4<span class="p">站点4</span></span>
          </div>

          <div
            class="wttype6"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">5<span class="p">站点5</span></span>
          </div>

          <div
            class="wttype6"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">6<span class="p">站点6</span></span>
          </div>

          <div class="example">
            <p><span class="c wttype1"></span> I类</p>
            <p><span class="c wttype2"></span> II类</p>
            <p><span class="c wttype3"></span> III类</p>
            <p><span class="c wttype4"></span> IV类</p>
            <p><span class="c wttype5"></span> V类</p>
            <p><span class="c wttype6"></span> 劣V类</p>
          </div>
        </div>
      </div>
      <div class="sec-qpollute">
        <h3>全流域污染物含量平均值（mg/L） <span class="h3ldesc"></span></h3>
        <div class="graph graph-qpollute">
          <circleProgress
            percent="20.10896"
            degree_percent="50"
            title="COD"
            color="#38AAFD"
          />
          <circleProgress
            percent="0.093941"
            degree_percent="4.7"
            title="TN"
            color="#3AC270"
          />
          <circleProgress
            percent="0.073961"
            degree_percent="3.7"
            title="NH3-N"
            color="#F48E2A"
          />
          <circleProgress
            percent="0.4702"
            degree_percent="0.4"
            title="TP"
            color="#C60F00"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map5.vue';
import ymap1 from '@/components/Map6.vue';
import page1left from '@/components/fifthpage/Page1Left.vue';
import page1right from '@/components/fifthpage/Page1Right.vue';
import page1middle from '@/components/fifthpage/Page1Middle.vue';
import circleProgress from '@/components/circleProgress.vue';


export default {
  data() {
    return {
      pageClass: 'page inpage fifthPage',
      waterQuality: ['劣Ⅴ类', '劣Ⅴ类', '劣Ⅴ类', '劣Ⅴ类', '劣Ⅴ类', '劣Ⅴ类'],
      isShow: true,
      num: this.$store.state.firstPageClick + 1,
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
    isMouseover(index) {
      if (this.mouseover) {
        if (this.mouseover[index]) {
          return 'active';
        }
      }
      return '';
    },
    setMouseover(index) {
      this.mouseover.splice(index, 1, true);
    },
    setMouseout(index) {
      this.mouseover.splice(index, 1, false);
    },
  },
  components: {
    ymap,
    ymap1,
    page1left,
    page1middle,
    page1right,
    circleProgress,
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
            width: $width-inpanel-l1 - 2 * $padding-page-tm;
            margin: 1rem -4rem 0 0;
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
          width: 45rem;
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

  .back {
    pointer-events: auto;
  }

  .page1middle {
    position: relative;

    & >>> .button {
      .btn {
        margin: 1rem 0rem;
        font-size: 2.5rem;
        width: 11.2rem;
        height: 5.6rem;
        line-height: 5rem;
      }
    }
  }

  .wrfz-img {
    img {
      max-width: 100%;
      margin: auto;
    }
  }

  .page1right {


    & >>> ul {
      margin: 0rem;
      position: relative;
      left: -1rem;
      top: -2rem;

      li {
        display inline-block
        width: 35rem;
        height: 20rem;

        .item {
          margin: 0rem 0rem 0rem 1rem;

          .image {
            left: 3rem;

            img {
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

    .site-img {
      text-align: center;
      img {
        height: 18rem;
        position: relative;
      }
    }

    .action {
      display: none;
    }

    &.active {
      width: 100%;
      border: 1px solid $cd3;
      border-width: 1px 0;
      background-color: rgba($ct1, 0.5);
      margin: 0 -4rem -4rem -4rem;
      padding: 1rem 4rem 1rem 4rem

      .action {
        display: block;
        position: relative;
        top: -2rem;
        margin: -1rem 0 0.6rem 29rem;
      }
    }
  }

  .action {
    pointer-events: auto;
  }

  video.video_tp {
    width 50rem
  }

  video.video_U {
    width: 39rem;
    margin-top: 3rem;
  }

  div.inmiddle-ctn {
    z-index 2
  }
  div.h33{
    width 50%
    height 2rem
  }
  div.h3g{
    background-color #1eff67
  }
  div.h3r{
    background-color red
  }
  div.dtable-img{
    background-color: rgba(10,15,24,0.5);
    margin: 5rem -4rem -4rem -4rem;
    padding: 1rem 4rem 1rem 4rem;
    img{
      width 9rem !important
    }
    ul{
      span{
        width 9rem!important
      }
    }
  }
  div.dtable-text{
    background-color: rgba(10,15,24,0.5);
    margin: 5rem -4rem -4rem -4rem;
    padding: 1rem 4rem 1rem 4rem;
  }
  div.data{
    img{
      width 9rem !important
    }
  }
  .panelwide {
    width: 100vw;
    box-sizing: border-box;
    position: fixed;
    padding: 0 $padding-page-lr;
    z-index: 10;
    &.bottom {
      bottom: $padding-page-td;
      text-align: center;

      .sec-qsz {
        padding: 5rem 2rem;
        top: 68rem;
        text-align: left;
        position: fixed;
        z-index: $z-index-panel;
        bottom: $padding-page-tb + 0.6rem;
        pointer-events: auto;

        .graph {
          position: relative;

          & > div {
            display: inline-block;
            height: 1.4rem;
            margin-top: 5rem;

            .t {
              position: relative;
              bottom: 4rem;
              font-size: 1.6rem;

              &::before {
                content: '|';
                display: block;
                position: absolute;
                top: 2rem;
                left: -0.1rem;
                color: $fff;
              }

              .p {
                display block
                color: $ct2;
                // margin-left: 0.8rem;
                position relative
                top -4rem
                font-size 0.8em
              }
            }
          }

          & > div.example {
            opacity 0
            transition opacity ease 0.5s
            position absolute
            left 0
            top 2rem
            display block
            text-align center
            // height 14rem
            // width 10rem
            background-color rgba($ct1, 0.7)
            padding 1rem 2rem 3rem 2rem
            width 100%
            box-sizing border-box

            p {
              display inline
              margin 0 1.5rem 0 0
            }

            span.c {
              display inline-block
              width 0.8rem
              height 1rem
              border 1px solid rgba(#fff, 0.2)
              margin-right 0.2rem
            }
          }

          &:hover div.example {
            opacity 1
          }
        }
      }

      .sec-qpollute {
        text-align: center;
        position: fixed;
        bottom: $padding-page-tb + 2.2rem;
        width: 100vw;
        z-index: $z-index-middle;

        .graph {
          text-align: center;

          & > div {
            margin-right: 3rem;
          }
        }
      }

      .sec-mainbtns {
        position: fixed;
        z-index: $z-index-panel;
        right: $padding-page-ty;
        bottom $padding-page-tb;


        img {
          width: 9rem;
          margin: 0 2.8rem;
          margin-top: -3rem;
          &:hover {
            background-color: rgba($ct2, 0.05);
          }
        }
      }
    }
  }
  .bottom {
    pointer-events: none;
  }
  li.isFifth{
    list-style none
  }
  .dtable {
    &.dtable-pwk {
      .tablehead {
        position: relative;
        left: 4.8rem + 1.8rem;
        width 100%
      }

      .data {
        width: 10.1rem;

        &.last {
          width: 5rem;
        }
      }

      .item {
        margin-top: 1.6rem;
        margin-bottom: 2.6rem;

        .icon {
          width: 4.8rem;
          height: 5.8rem;
          float: left;
          clear: both;
          position: relative;
          margin-right: 1.8rem;
          background-image: url('../assets/img/drop.png');
          background-size: 100% auto;
          background-repeat: no-repeat;

          .id {
            position: absolute;
            right: -0.6rem;
            bottom: 0.6rem;
            background-color: $ct9;
            color: $fff;
            padding: 0.1rem 0.2rem;
            border-radius: 0.2rem;
          }
        }

        .line1 {
          padding: 0.2rem 0;

          .data {
            font-size: 1.5rem;
          }
        }

        .line2 {
          font-size: 1.3rem;

          .onlineonline {
            float: right;
          }
        }
      }
    }

    &.dtable-sz {
      .data {
        width 8rem
      }

      .data.last {
        width 3rem
      }

      .dataSZ {
        margin-left 0rem
        width 14rem
      }
    }
  }
  .dlist-dm {
    ul {
      margin-top: -1.8rem;
      max-height calc(100vh - 58rem)
      overflow-y scroll

    }

    .item {
      position: relative;
      padding: 1.2rem 1.6rem;

      .dataDM {
        color: $cd3;
      }

      .dataSZspan {
        display: inline-block;
        margin-top: 1rem;
      }

      img {
        height: 9rem;
        width: 66%;
        position: absolute;
        right: 0;
        top: 0;
        padding-left: 4.4rem;

        //裁剪图片
        clip: rect(0.2rem 31rem 9.8rem 2.6rem)
      }

      .action {
        display: none;
      }

      &.active {
        border: 1px solid $cd3;
        border-width: 1px 0;
        background-color: rgba($ct1, 1);

        .action {
          display: block;
          text-align: right;
          margin: 4rem 0 0.6rem 0;
        }
      }
    }
  }
  textarea {
    text-indent 28px
    width: 100%;
    height: 10.4rem;
    box-sizing: border-box;
  }
  div.isFifth{
    table{
      border: 1px solid #f48e2a;
      width: 100%;
    }
  }
</style>
