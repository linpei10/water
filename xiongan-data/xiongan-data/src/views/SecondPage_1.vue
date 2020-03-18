<template>
  <div class="page inpage second">
    <div style="display:none">
      <!-- <div class="popup-ctn popup-ctn-blur popup-jcdselect"> -->
      <!-- onclick=close-popup -->.dlist-dm
      <div class="popup">
        <div class="popup-title">
          <h4>监测点选择</h4>
          <a class="close">
            <img src="../assets/img/delete.png"/>
          </a>
        </div>
        <div class="popup-body">
          <ul class="ulcheck small">
            <li>仿真监测站</li>
            <li class="active">旧思乡桥</li>
          </ul>
        </div>
        <div class="popup-bottom">
          <button class="btnGrey small"><i class="i">&#xe651;</i>确认选择</button>
          <!-- <button class="btnArr small">确认选择</button> -->
        </div>
      </div>
    </div>
    <ymap class="ymap" distPage="/thirdPage" v-bind:infoShow="true"/>
    <div class="inpanel left">
      <div class="logo">
        <h1>
          <router-link to="/">
            <img src="../assets/img/logo.png"/>
          </router-link>
        </h1>
      </div>
      <h3 class="h3l">治理方案列表</h3>
      <ul class="ulselect">
        <li class="active">示例方案</li>
        <router-link to="/secondPage">
          <li>新建方案</li>
        </router-link>
      </ul>
      <h3 class="h3l">方案简介</h3>
      <textarea class="desc">示例旨在演示系统功能，假设本河段存在三个生活污染源，造成区域水质恶化。为此预定采取建立污水处理设施将COD、TN、NH3-N、TP的排放量降低40%。通过仿真平台模拟方案实施后的模拟效果。</textarea>
    </div>
    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png"/>排污治理方案效果预测
          <router-link
            to="/Combine"
            class="back"
          >
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <!--        <div class="tipbox-group">-->
        <!--          <div class="tipbox pwk">-->
        <!--            <h4><img src="uploads/govern/R2/icon-drop.png" />排污口列表</h4>-->
        <!--            <ul>-->
        <!--              <li>#1采蒲北码头 <span class="online is_online"><img src="uploads/govern/R2/online.png" />在线</span>-->
        <!--              </li>-->
        <!--              <li>#2邸庄信号塔 <span class="online is_offline"><img src="uploads/govern/R2/offline.png" />离线</span>-->
        <!--              </li>-->
        <!--              <li>#3邸庄东码头 <span class="online is_online"><img src="uploads/govern/R2/online.png" />在线</span>-->
        <!--              </li>-->
        <!--            </ul>-->
        <!--          </div>-->
        <!--          <div class="tipbox dm">-->
        <!--            <h4><img src="uploads/govern/R2/icon-wave.png" />断面列表</h4>-->
        <!--            <ul>-->
        <!--              <li>#思乡桥1 <span class="type">生态补偿考核断面1</span></li>-->
        <!--              <li>#思乡桥2 <span class="type">生态补偿考核断面2</span></li>-->
        <!--              <li>#思乡桥3 <span class="type">生态补偿考核断面3</span></li>-->
        <!--              <li>#思乡桥4 <span class="type">生态补偿考核断面4</span></li>-->
        <!--              <li>#思乡桥5 <span class="type">生态补偿考核断面5</span></li>-->
        <!--              <li>#思乡桥6 <span class="type">生态补偿考核断面6</span></li>-->
        <!--            </ul>-->
        <!--          </div>-->
        <!--        </div>-->
      </div>
    </div>
    <div class="inpanel right">
      <div class="dtable dlist img">
        <h3 class="h3l">排污口设定</h3>
        <div class="sec1-scorll">
          <ul class="ulcheck">
            <li class="inputgroup ">
              <input
                type="text"
                class="wide"
                value="#1 排污口"
              >
              <div class="labelgroup-2x">
                <div class="labelgroup">
                  <span class="before">经度</span>
                  <input
                    type="text"
                    class="small"
                    value=""
                  >
                  <span class="after">(double)</span>
                </div>
                <div class="labelgroup">
                  <span class="before">纬度</span>
                  <input
                    type="text"
                    class="small"
                    value=""
                  >
                  <span class="after">(double)</span></div>
                <div class="labelgroup">
                  <span class="before">COD</span>
                  <input
                    type="text"
                    class="small"
                    value="8.4"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">TP</span>
                  <input
                    type="text"
                    class="small"
                    value="0.06"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">NH-H</span>
                  <input
                    type="text"
                    class="small"
                    value="0.0582"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">TN</span>
                  <input
                    type="text"
                    class="small"
                    value="0.036"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">流量</span>
                  <input
                    type="text"
                    class="small"
                    value="1"
                  >
                  <span class="after">m³/s</span></div>
              </div>
            </li>
            <li class="inputgroup ">
              <input
                type="text"
                class="wide"
                value="#2 排污口"
              >
              <div class="labelgroup-2x">
                <div class="labelgroup">
                  <span class="before">经度</span>
                  <input
                    type="text"
                    class="small"
                    value=""
                  >
                  <span class="after">(double)</span>
                </div>
                <div class="labelgroup">
                  <span class="before">纬度</span>
                  <input
                    type="text"
                    class="small"
                    value=""
                  >
                  <span class="after">(double)</span></div>
                <div class="labelgroup">
                  <span class="before">COD</span>
                  <input
                    type="text"
                    class="small"
                    value="6"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">TP</span>
                  <input
                    type="text"
                    class="small"
                    value="0.06"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">NH-H</span>
                  <input
                    type="text"
                    class="small"
                    value="0.0372"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">TN</span>
                  <input
                    type="text"
                    class="small"
                    value="0.03"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">流量</span>
                  <input
                    type="text"
                    class="small"
                    value="1"
                  >
                  <span class="after">m³/s</span></div>
              </div>
            </li>
            <li class="inputgroup ">
              <input
                type="text"
                class="wide"
                value="#3 排污口"
              >
              <div class="labelgroup-2x">
                <div class="labelgroup">
                  <span class="before">经度</span>
                  <input
                    type="text"
                    class="small"
                    value=""
                  >
                  <span class="after">(double)</span>
                </div>
                <div class="labelgroup">
                  <span class="before">纬度</span>
                  <input
                    type="text"
                    class="small"
                    value=""
                  >
                  <span class="after">(double)</span></div>
                <div class="labelgroup">
                  <span class="before">COD</span>
                  <input
                    type="text"
                    class="small"
                    value="7.2"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">TP</span>
                  <input
                    type="text"
                    class="small"
                    value="0.06"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">NH-H</span>
                  <input
                    type="text"
                    class="small"
                    value="0.0954"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">TN</span>
                  <input
                    type="text"
                    class="small"
                    value="0.03"
                  >
                  <span class="after">mg/L</span>
                </div>
                <div class="labelgroup">
                  <span class="before">流量</span>
                  <input
                    type="text"
                    class="small"
                    value
                  >
                  <span class="after">m³/s</span></div>
              </div>
            </li>
          </ul>
        </div>
        <!--        <ul class="images">-->
        <!--          <li v-for="n in 3" v-bind:key="'pwk'+n" class="item">-->
        <!--            <div class="img-container">-->
        <!--              <img src="uploads/govern/R2/graphbig.png">-->
        <!--            </div>-->
        <!--          </li>-->
        <!--        </ul>-->
      </div>
      <div class="dtable dlist dlist-dm">
        <h3 class="h3l">示例方案仿真监测站水质等级随时间变化</h3>
        <ul>
          <li>
            <router-link to="/thirdPage">
              <div class="item">
                <span class="data dataDM">#1 仿真监测站</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">Ⅳ类</span>
                </span>
                <img
                  class="graph"
                  src="uploads/govern/R2/case3-0.png"
                />
                <div class="action">
                  <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                  <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                  <router-link to="firstPage">
                    <button class="btnArr small">开始模拟</button>
                  </router-link>
                </div>
              </div>
            </router-link>
          </li>
          <li>
            <router-link to="/thirdPage">
              <div class="item">
                <span class="data dataDM">#2 仿真监测站</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">Ⅳ类</span>
                </span>
                <img
                  class="graph"
                  src="uploads/govern/R2/case3-1.png"
                />
                <div class="action">
                  <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                  <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                  <router-link to="firstPage">
                    <button class="btnArr small">开始模拟</button>
                  </router-link>
                </div>
              </div>
            </router-link>
          </li>
          <li>
            <router-link to="/thirdPage">
              <div class="item">
                <span class="data dataDM">#3 仿真监测站</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">Ⅳ类</span>
                </span>
                <img
                  class="graph"
                  src="uploads/govern/R2/case3-2.png"
                />
                <div class="action">
                  <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                  <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                  <router-link to="firstPage">
                    <button class="btnArr small">开始模拟</button>
                  </router-link>
                </div>
              </div>
            </router-link>
          </li>
          <li>
            <router-link to="/thirdPage">
              <div class="item">
                <span class="data dataDM">#4 仿真监测站</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">Ⅳ类</span>
                </span>
                <img
                  class="graph"
                  src="uploads/govern/R2/case3-3.png"
                />
                <div class="action">
                  <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                  <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                  <router-link to="firstPage">
                    <button class="btnArr small">开始模拟</button>
                  </router-link>
                </div>
              </div>
            </router-link>
          </li>
          <li>
            <router-link to="/thirdPage">
              <div class="item">
                <span class="data dataDM">#5 仿真监测站</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">Ⅳ类</span>
                </span>
                <img
                  class="graph"
                  src="uploads/govern/R2/case3-4.png"
                />
                <div class="action">
                  <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                  <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                  <router-link to="firstPage">
                    <button class="btnArr small">开始模拟</button>
                  </router-link>
                </div>
              </div>
            </router-link>
          </li>
          <li>
            <router-link to="/thirdPage">
              <div class="item">
                <span class="data dataDM">#6 仿真监测站</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">Ⅳ类</span>
                </span>
                <img
                  class="graph"
                  src="uploads/govern/R2/case3-5.png"
                />
                <div class="action">
                  <a class="btnI"><i class="i">&#xe63d;</i> 编辑</a>
                  <a class="btnI"><i class="i">&#xe652;</i> 删除</a>
                  <router-link to="firstPage">
                    <button class="btnArr small">开始模拟</button>
                  </router-link>
                </div>
              </div>
            </router-link>
          </li>
          <br>
          <br>
          <br>
          <button class="btnArr startFz">报告输出</button>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map.vue';

export default {
  components: {
    ymap,
  },
  mounted() {
    this.ulcheckInit();
  },
};
</script>

<style lang="stylus" scoped>
  @import '../global.styl';

  // register func & components
  layout-three($width-inpanel-l1, $width-inpanel-r1);
  ulcheck();
  btnArr();

  // page inner style
  .popup-jcdselect {
    .ulcheck {
    }
  }

  .inpanel {
    &.left {
      textarea {
        width: 100%;
        height: 16rem;
        box-sizing: border-box;
      }

      .ulselect {
        li {
          padding-top: 1.8rem;
          padding-bottom: 1.8rem;

          &::before {
            content: '';
            display: inline-block;
            width: 2.2rem;
            height: 2.2rem;
            margin-right: 1.2rem;
            background-size: cover;
            background-image: url('../assets/img/pj-f.png');
            background-repeat: no-repeat;
            vertical-align: middle;
            position: relative;
            top: -0.2rem;
          }

          &.active::before {
            background-image: url('../assets/img/pj-t.png');
          }
        }
      }
    }

    &.right {
      .rvideo {
        max-height: 23rem;
        overflow: hidden;
        box-shadow: 0 0 3rem 0.1rem rgba($ct1, 0.6);

        img {
          width: 100%;
        }
      }

      .dlist-dm {
        ul {
          padding-top 2rem
          margin-top: 3rem;
          background-color rgba(10, 15, 24, 0.5)
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
            height: 8.5rem;
            position: absolute;
            right: 2rem;
            top: 0rem;
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

      .startFz {
        right: $padding-pagei-lr;
        width: $width-inpanel-r1 - 2 * $padding-pagei-lr;
        bottom: $padding-pagei-tb;
      }
    }
  }

  .inmiddle-ctn {
    .inmiddle {
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

  .inmiddle-ctn {
    pointer-events: none;
  }

  .back {
    pointer-events: auto;
  }

  .images {
    list-style-type: none;

    .item {
      margin: 0rem 0rem 0.5rem 1.2rem;
      display: inline-block;
      width: 21rem;

      .img-container {
        img {
          max-width: 100%;
          max-height: 100%;
        }

      }
    }
  }

  .ymap {
    & >>> .tt {
      display: none;
    }
  }
.sec1-scorll{
  width: 15vm;
  height: 200px;
  overflow-y: scroll;
  max-height: 30vh;
}
</style>
