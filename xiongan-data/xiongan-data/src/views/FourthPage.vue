<template>
  <div class="page inpage second">
    <ymap />
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
        <li class="active">孝义河河口湿地水质净化工程</li>
        <router-link to="/FourthPage_2">
          <li>新建污水净化工程</li>
        </router-link>
        <router-link to="/FourthPage_3">
          <li>新建排污工程</li>
        </router-link>
      </ul>
      <h3 class="h3l">工程简介</h3>
      <textarea class="desc">孝义河河口湿地水质净化工程包括水质净化处理能力为20万m3/天。工程总建设面积约2.11km2，湿地工艺采用“前置沉淀生态塘+潜流湿地+多塘系统”体系，生态湿地有效净化面积 1.41km2，其中生态塘2hm2、氧化塘17.4hm2、潜流湿地25.68hm2、多塘系统 96.23hm2。工程建设内容主要包括：水质净化工程、生态修复工程、物联网工程、 配套设施及公共工程等。湿地出水水质主要考核项为总磷。四个入水口的流量分别为：0.694 、0.579 、0.694 和0.347 立方米/s，出口流量为2.3立方米/s。此处设定总磷的去除率为40%，其余污染物无净化效果。</textarea>
    </div>
    <div class="inmiddle-ctn">
      <div class="inmiddle">
        <h2 class="mtitle">
          <img src="../assets/img/Shape.png" />新建工程污染影响仿真
          <router-link
            to="/Combine"
            class="back"
          >
            <i class="i">&#xe658;</i>返回
          </router-link>
        </h2>
        <div class="tipbox-group">
        </div>
      </div>
    </div>
    <div class="inpanel right">
      <h3 class="h3l">工程信息 <span class="h3laddbtn">仿真已结束</span></h3>
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
                value="115.855144"
              >
              <span class="after"></span>
            </div>
            <div class="labelgroup">
              <span class="before">纬度</span>
              <input
                type="text"
                class="small"
                value="38.76599"
              >
              </div>
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
          <div class="labelgroup">
            <span class="before">经度</span>
            <input
              type="text"
              class="small"
              value="115.848192"
            >

          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value="38.76312"
            >
          </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="21.4389"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0.1"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value="0.07878"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.097106"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="0.694"
              >
              <span class="after">m³/s</span></div>

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
          <div class="labelgroup">
            <span class="before">经度</span>
            <input
              type="text"
              class="small"
              value="115.854502"
            >

          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value="38.766283"
            >
          </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="21.4389"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0.1"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value="0.07878"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.097106"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="0.579"
              >
              <span class="after">m³/s</span></div>

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
          <div class="labelgroup">
            <span class="before">经度</span>
            <input
              type="text"
              class="small"
              value="115.85484"
            >

          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value="38.769723"
            >
          </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="21.4389"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0.1"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value="0.07878"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.097106"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="0.694"
              >
              <span class="after">m³/s</span></div>
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
          <div class="labelgroup">
            <span class="before">经度</span>
            <input
              type="text"
              class="small"
              value="115.855296"
            >

          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value="38.773803"
            >
          </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="21.4389"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0.1"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value="0.07878"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.097106"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="0.694"
              >
              <span class="after">m³/s</span></div>

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
          <div class="labelgroup">
            <span class="before">经度</span>
            <input
              type="text"
              class="small"
              value="115.85426"
            >

          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value="38.76392"
            >
          </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value="21.4389"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value="0.1"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value="0.07878"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value="0.058264"
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value="2.314"
              >
              <span class="after">m³/s</span></div>

          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <h3>
          <span class="h3laddbtn">+ 新增污染源</span>
        </h3>
        <li>
          <button class="btnGrey"><i class="i">&#xe659;</i>是否叠加模拟区域现有污染源</button>
        </li>
        <br>
        <br>
        <button class="btnArr startFz">重新仿真</button>
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
      text-indent 28px
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
    .startFz {
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
