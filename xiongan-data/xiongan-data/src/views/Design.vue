<template>
  <div class="page index">
    <div class="logo">
      <h1>
        <router-link to="/">
          <img src="../assets/img/logo.png" />
        </router-link>
      </h1>
    </div>
    <div class="panel left">
      <div class="dtable dtable-pwk">
        <h3 class="h3l">排污口实时污染物浓度（mg/L）</h3>
        <div class="tablehead">
          <span class="data head">COD</span>
          <span class="data head">TN</span>
          <span class="data head">NH3-N</span>
          <span class="data head last">TP</span>
        </div>
        <ul
          v-for="(dataItem,index) in outletData.slice(0,3)"
          v-bind:key="index"
        >
          <li>
            <div class="item">
              <div class="icon">
                <span class="id">{{dataItem.id}}</span>
              </div>
              <div class="line line1">
                <!-- <span class="data data1">{{(typeof dataItem.tn)=="number"?dataItem.tn.toFixed(3):dataItem.tn}}</span>
                <span class="data data2">{{(typeof dataItem.COD)=="number"?dataItem.COD.toFixed(2):dataItem.COD}}</span>
                <span class="data data3">{{(typeof dataItem.nh3n)=="number"?dataItem.nh3n.toFixed(3):dataItem.nh3n}}</span>
                <span class="data data4 last">{{(typeof dataItem.tp)=="number"?dataItem.tp.toFixed(3):dataItem.tp}}</span> -->
                <span class="data data2">{{dataItem.cod instanceof Number?dataItem.cod.toFixed(3):dataItem.cod}}</span>
                <span class="data data1">{{dataItem.tn instanceof Number?dataItem.tn.toFixed(3):dataItem.tn}}</span>
                <span class="data data3">{{dataItem.nh3n instanceof Number?dataItem.nh3n.toFixed(3):dataItem.nh3n}}</span>
                <span class="data data4 last">{{dataItem.tp instanceof Number?dataItem.tp.toFixed(3):dataItem.tp}}</span>
              </div>
              <div class="line line2">
                <span class="address">{{dataItem.country}} {{dataItem.town}} {{dataItem.location}}</span>
                <span
                  class="online is_online"
                  v-if="dataItem.monitor_online"
                ><img src="../assets/img/online.png" />在线</span>
                <span
                  class="online is_offline"
                  v-else
                ><img src="../assets/img/offline.png" />离线</span>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="dtable dtable-sz">
        <h3 class="h3l">水质监测站污染物浓度（mg/L）</h3>
        <div class="tablehead">
          <span class="data dataSZ head">名称</span>
          <span class="data head">COD</span>
          <span class="data head">TN</span>
          <span class="data head">NH3-N</span>
          <span class="data head last">TP</span>
        </div>
        <ul
          v-for="(dataItem,index) in sectionData.slice(0,3)"
          v-bind:key="index"
        >
          <li>
            <div class="item">
              <div class="line line1">
                <span class="data dataSZ"><span class="dataSZspan">{{dataItem.STNM}}</span></span>
                <span class="data data1">{{dataItem.COD instanceof Number?dataItem.COD.toFixed(3):dataItem.COD}}</span>
                <span class="data data2">{{dataItem.TN instanceof Number?dataItem.TN.toFixed(3):dataItem.TN}}</span>
                <span class="data data3">{{dataItem.NH3N instanceof Number?dataItem.NH3N.toFixed(3):dataItem.NH3N}}</span>
                <span class="data data4 last">{{dataItem.TP instanceof Number?dataItem.TP.toFixed(3):dataItem.TP}}</span>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <div class="panel right">
      <div class="rvideo">
        <!-- <img src="../assets/img/video.jpg" /> -->
        <video width="320" height="170" controls autoplay preload muted loop>
          <source src="uploads/index/Alpha平台三维JS-API轨迹回放动画.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
      <div class="dtable dlist dlist-dm">
        <h3 class="h3l">各仿真监测站水质等级时间变化曲线</h3>
        <ul>
          <li v-for="n in 6" v-bind:key="n+'sz'">
            <div class="item" :class="isMouseover(n-1)"
              v-on:mouseover="setMouseover(n-1)"
              v-on:mouseout="setMouseout(n-1)">
              <span class="data dataDM">#{{n}} 仿真监测点</span><br>
              <span class="data dataSZ">
                <span class="dataSZspan">{{waterQuality[n-1]}}</span>
              </span>
              <img
                class="graph"
                :src="'uploads/index/right/WQduanmian'+ n +'.png'"
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
          <!-- <li>
            <div class="item active">
              <span class="data dataDM">#2 新思乡桥</span><br>
              <span class="data dataSZ">
                <span class="dataSZspan">劣Ⅴ</span>
              </span>
              <img
                class="graph"
                src="'../../public/uploads/page1/right/断面'+n+'水质曲线.png'"
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
          <li>
            <div class="item">
              <span class="data dataDM">#3 新思乡桥</span><br>
              <span class="data dataSZ">
                <span class="dataSZspan">劣Ⅱ</span>
              </span>
              <img
                class="graph"
                src="../../public/uploads/page1/right/断面3水质曲线.png"
              />
              <div class="action">
                <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                <router-link to="firstPage">
                  <button class="btnArr small">开始模拟</button>
                </router-link>
              </div>
            </div>
          </li> -->
        </ul>
      </div>
    </div>

    <div class="panelwide bottom">
      <div class="sec-qsz">
        <h3>各仿真监测站全时长平均水质等级</h3>
        <div class="graph graph-qsz">

          <div
            class="bgcd2"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">{{waterQuality[0]}}<span class="p">站点1</span></span>
          </div>

          <div
            class="bgcd2"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">{{waterQuality[1]}}<span class="p">站点2</span></span>
          </div>

          <div
            class="bgcd2"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">{{waterQuality[2]}}<span class="p">站点3</span></span>
          </div>

          <div
            class="bgcd2"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">{{waterQuality[3]}}<span class="p">站点4</span></span>
          </div>

          <div
            class="bgcd2"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">{{waterQuality[4]}}<span class="p">站点5</span></span>
          </div>

          <div
            class="bgcd2"
            style="width: calc(0.166*10*4rem)"
          >
            <span class="t">{{waterQuality[5]}}<span class="p">站点6</span></span>
          </div>

          <div class="example">
            <p><span class="c bgcd6"></span> I类</p>
            <p><span class="c bgcd1"></span> II类</p>
            <p><span class="c bgcd5"></span> III类</p>
            <p><span class="c bgcd2"></span> IV类</p>
            <p><span class="c bgcd3"></span> V类</p>
            <p><span class="c bgcd4"></span> VI类</p>
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
            percent="0.091148"
            degree_percent="45.55"
            title="TP"
            color="#C60F00"
          />
        </div>
      </div>
      <div class="sec-mainbtns">
        <router-link to="/secondPage_1"><img src="../assets/img/btnR1.png" /></router-link>
        <router-link to="/fourthPage"><img src="../assets/img/btnR2.png" /></router-link>
        <router-link to="/fifthPage"><img src="../assets/img/btnR3.png" /></router-link>
      </div>
    </div>
  </div>
</template>

<script>
import circleProgress from '@/components/circleProgress.vue';
// 引用排污口数据
import outletData from '../assets/json/outletData.json';
// 引用断面小时数据
import sectionData from '../assets/json/section.json';

export default {
  components: {
    circleProgress,
  },

  data() {
    return {
      outletData: outletData.data,
      sectionData: sectionData.data,
      mouseover: [false, false, false, false, false, false],
      waterQuality: ['Ⅳ类', 'Ⅳ类', 'Ⅳ类', 'Ⅳ类', 'Ⅳ类', 'Ⅳ类'],
    };
  },

  methods: {
    getReadtimeData() {
      // 暂时不用
    },
    getDetPointData() {
      // 暂时不用
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
};
</script>

<style lang="stylus" scoped>
@import '../global.styl';

btnArr();

.index {
  .panel {
    position: fixed;
    top: $padding-page-tb + 8rem;
    width: 42rem;
    padding: 2.5rem 2rem;
    background-color: rgba($ct1, 0.5);

    .line {
      color: #67C0F5;
    }

    &.left {
      left: $padding-page-lr;
      padding-top: 0;

      .dtable {
        &.dtable-pwk {
          .tablehead {
            position: relative;
            left: 4.8rem + 1.8rem;
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
            margin-left -1rem
            width 14rem
          }
        }
      }
    }

    &.right {
      top: $padding-page-tb;
      right: $padding-page-lr;
      background-color: rgba(10,15,24,0.5);
      padding: 0;

      .rvideo {
        max-height: 23rem;
        overflow: hidden;
        box-shadow: 0 0 3rem 0.1rem rgba($ct1, 0.6);

        img, video {
          width: 100%;
          margin-top -1.5rem
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
            top: 0rem;
            padding-left 32px;

            //裁剪图片
            clip: rect(0.2rem 31rem 9.8rem 2.6rem)
          }

          .action {
            display: none;
          }

          &.active {
            border: 1px solid $cd3;
            border-width: 1px 0;
            background-color: rgba($ct1, 0.5);

            .action {
              display: block;
              text-align: right;
              margin: 1.8rem 0 0.6rem 0;
            }
          }
        }
      }
    }
  }

  .panelwide {
    width: 100vw;
    box-sizing: border-box;
    position: fixed;
    padding: 0 $padding-page-lr;

    &.bottom {
      bottom: $padding-page-td;
      text-align: center;

      .sec-qsz {
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
            // height 14rem
            // width 10rem
            background-color rgba($ct1, 0.7)
            padding 1rem 2rem 3rem 2rem
            width 100%
            box-sizing border-box

            p {
              display inline
              margin 0 2rem 0 0
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
        right: $padding-page-tt
        bottom $padding-page-tb


        img {
          width: 11rem;
          margin-left: 2rem;

          &:hover {
            background-color: rgba($ct2, 0.05);
          }
        }
      }
    }
  }
}

.bottom{
  pointer-events: none;
}
.sec-mainbtns{
  pointer-events: auto;
}
</style>
