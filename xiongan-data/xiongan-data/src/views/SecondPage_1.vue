<template>
  <div class="page inpage second">
    <div style="display:none">
      <!-- <div class="popup-ctn popup-ctn-blur popup-jcdselect"> -->
      <!-- onclick=close-popup -->
      <div class="popup">
        <div class="popup-title">
          <h4>监测点选择</h4>
          <a class="close">
            <img src="../assets/img/delete.png" />
          </a>
        </div>
        <div class="popup-body">
          <ul class="ulcheck small">
            <li>新思乡桥</li>
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
            <img src="../assets/img/logo.png" />
          </router-link>
        </h1>
      </div>
      <h3 class="h3l">方案列表</h3>
      <ul class="ulselect">
        <li class="active">示例方案</li>
        <router-link to="/secondPage">
          <li>新建方案</li>
        </router-link>
      </ul>
      <h3 class="h3l">方案简介</h3>
      <textarea class="desc">该方案为"排污治理方案效果预测"示例方案，展示在规定的减排指标下，河流水质可以优化到什么程度。</textarea>
    </div>
    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png" />排污治理方案效果预测
          <router-link
            to="/Combine"
            class="back"
          >
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <div class="tipbox-group">
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
      <div class="dtable dlist img">
        <h3 class="h3l">排污口设定</h3>
        <ul class="images">
          <li v-for="n in 3" v-bind:key="'pwk'+n" class="item">
            <div class="img-container">
              <img src="../assets/img/graphbig.png">
            </div>
          </li>
        </ul>
      </div>
      <div class="dtable dlist dlist-dm">
        <h3 class="h3l">方案效果评估</h3>
        <ul>
          <li>
            <router-link to="/thirdPage">
              <div class="item">
                <span class="data dataDM">#2 新思乡桥</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">劣I</span>
                </span>
                <img
                  class="graph"
                  src="../assets/img/graph.png"
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
                <span class="data dataDM">#2 新思乡桥</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">劣I</span>
                </span>
                <img
                  class="graph"
                  src="../assets/img/graph.png"
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
                <span class="data dataDM">#2 新思乡桥</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">劣I</span>
                </span>
                <img
                  class="graph"
                  src="../assets/img/graph.png"
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
                <span class="data dataDM">#2 新思乡桥</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">劣I</span>
                </span>
                <img
                  class="graph"
                  src="../assets/img/graph.png"
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
                <span class="data dataDM">#2 新思乡桥</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">劣I</span>
                </span>
                <img
                  class="graph"
                  src="../assets/img/graph.png"
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
                <span class="data dataDM">#2 新思乡桥</span><br>
                <span class="data dataSZ">
                  <span class="dataSZspan">劣I</span>
                </span>
                <img
                  class="graph"
                  src="../assets/img/graph.png"
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
        margin-top: -1.8rem;
        background-color rgba(10,15,24,0.5)
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
          position: absolute;
          right: 0;
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
.images{
  list-style-type: none;
  .item{
    margin: 0rem 0rem 0.5rem 1.2rem;
    display: inline-block;
    width: 21rem;
    .img-container{
      img{
        max-width: 100%;
        max-height: 100%;
      }

    }
  }
}

.ymap{
  &>>>.tt{
    display: none;
  }
}

</style>
