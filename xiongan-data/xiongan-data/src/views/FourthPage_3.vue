<template>
  <div class="page inpage second">
    <ymap/>
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
        <router-link to="/FourthPage">
          <li>河口湿地水质净化工程</li>
        </router-link>
        <router-link to="/FourthPage_2">
          <li>新建污水净化工程</li>
        </router-link>
        <li class="active">新建排污工程</li>
      </ul>
      <h3 class="h3l">工程简介</h3>
      <textarea class="desc">该方案为"新建工程污染影响仿真"新建方案，展示在特定的新建工程排放下，河流水质可以优化到什么程度。</textarea>
    </div>
    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png" />新建工程污染影响仿真
          <router-link to="/Combine" class="back">
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
      <h3 class="h3l">工程信息 <span class="h3laddbtn">+ 新建项目</span></h3>
      <ul class="ulcheck">
        <li class="inputgroup">
          <input
            type="text"
            class="wide"
            value="经纬度信息"
          >
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">经度</span>
              <input
                type="text"
                class="small"
                value="115.85426"
              >
              <span class="after">(double)</span>
            </div>
            <div class="labelgroup">
              <span class="before">纬度</span>
              <input
                type="text"
                class="small"
                value="38.76392"
              >
              <span class="after">(double)</span></div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup ">
          <input
            type="text"
            class="wide"
            value="入口1"
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
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="100"
              >
              <span class="after">m3/S</span></div>
                          <div class="labelgroup">
              <span class="before">PH</span>
              <input
                type="text"
                class="small"
                value="8.200"
              >
              <span class="after"></span></div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup active">
          <input
            type="text"
            class="wide"
            value="入口2"
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
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="105"
              >
              <span class="after">m3/S</span></div>
                          <div class="labelgroup">
              <span class="before">PH</span>
              <input
                type="text"
                class="small"
                value="7.930"
              >
              <span class="after"></span></div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup">
          <input
            type="text"
            class="wide"
            value="入口3"
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
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="110"
              >
              <span class="after">m3/S</span></div>
                          <div class="labelgroup">
              <span class="before">PH</span>
              <input
                type="text"
                class="small"
                value="7.790"
              >
              <span class="after"></span></div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup">
          <input
            type="text"
            class="wide"
            value="入口4"
          >
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="13.000"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.090"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH-H</span>
              <input
                type="text"
                class="small"
                value="0.302"
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
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="115"
              >
              <span class="after">m3/S</span></div>
                          <div class="labelgroup">
              <span class="before">PH</span>
              <input
                type="text"
                class="small"
                value="7.930"
              >
              <span class="after"></span></div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup">
          <input
            type="text"
            class="wide"
            value="出口1"
          >
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="0.1"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.00"
              >
              <span class="after">g/m3</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH-H</span>
              <input
                type="text"
                class="small"
                value="0.01"
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
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="110"
              >
              <span class="after">m3/S</span></div>
                          <div class="labelgroup">
              <span class="before">PH</span>
              <input
                type="text"
                class="small"
                value="7"
              >
              <span class="after"></span></div>
          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>

      <h3>
        <div class="h3laddbtn">+ 新增污染源</div>
        <div class="h3laddbtn">+ 新增工程入水口</div>
        <div class="h3laddbtn">+ 新增工程出水口</div>
      </h3>
      <li>
      <button class="btnGrey"><i class="i">&#xe659;</i>是否叠加模拟区域现有污染源</button>
      </li>
      <br>
      <br>
      <button class="btnArr startFz">开始仿真</button>
      </ul>
    </div>
  </div>
</template>

<script>
import ymap from '@/components/Map4-1.vue';

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

.inpanel {
  &.left {
    textarea {
      width: 100%;
      height: 16rem;
      box-sizing: border-box;
    }

    .ulselect {
      li {
        padding-top 1.8rem
        padding-bottom 1.8rem

        &::before {
          content ''
          display inline-block
          width 2.2rem
          height 2.2rem
          margin-right 1.2rem
          background-size cover
          background-image url('../assets/img/pj-f.png')
          background-repeat no-repeat
          vertical-align middle
          position relative
          top -0.2rem
        }

        &.active::before {
          background-image url('../assets/img/pj-t.png')
        }
      }
    }
  }

  &.right {
    .startFz {
      width $width-inpanel-r1 - 2 * $padding-pagei-lr
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
          border-color $ct9
        }

        &.dm {
          ul {
            li {
              color $cd3
              .type {
                color $ct2
                margin-left 0.8rem
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

</style>
