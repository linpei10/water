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
    <ymap distPage="/thirdPage" v-bind:infoShow="true"/>
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
        <router-link to="/SecondPage_1">
          <li>示例方案</li>
        </router-link>
        <li class="active">新建方案</li>
      </ul>
      <h3 class="h3l">方案简介</h3>
      <textarea class="desc">该方案为"排污治理方案效果预测"新建方案，展示在新设定的减排指标下，河流水质可以优化到什么程度。</textarea>
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
      <h3 class="h3l">排污口设定 <span class="h3laddbtn">+ 新增排污口</span></h3>
      <ul class="ulcheck">
        <li class="inputgroup ">
          <input
            type="text"
            class="wide"
            value="#1采蒲北码头 "
          >
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="14.000"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.060"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH-H</span>
              <input
                type="text"
                class="small"
                value="0.197"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0"
              >
              <span class="after">g/m3</span>
            </div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup active">
          <input
            type="text"
            class="wide"
            value="#2邸庄信号塔"
          >
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="10.000"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.050"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH-H</span>
              <input
                type="text"
                class="small"
                value="0.262"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0"
              >
              <span class="after">g/m3</span>
            </div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup">
          <input
            type="text"
            class="wide"
            value="#3邸庄东码头 "
          >
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="12.000"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.060"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH-H</span>
              <input
                type="text"
                class="small"
                value="0.259"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0"
              >
              <span class="after">g/m3</span>
            </div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
      </ul>
      <button class="btnGrey"><i class="i">&#xe659;</i>添加监测点数据</button>
      <button class="btnGrey"><i class="i">&#xe808;</i>进行现状对比分析</button>
      <br>
      <button class="btnArr startFz">开始仿真</button>
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
    .ulcheck {
    }

    .btnGrey {
      margin-top: 2rem;
    }

    .startFz {
      position: fixed;
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
</style>
