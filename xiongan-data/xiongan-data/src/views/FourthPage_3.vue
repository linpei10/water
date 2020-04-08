<template>
  <div class="page inpage second">
    <div style="pointer-events:none;z-index:-10"><ymap style="pointer-events:none;z-index:-10" v-bind:display="true"/></div>
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
          <li>孝义河河口湿地水质净化工程</li>
        </router-link>
        <router-link to="/FourthPage_2">
          <li>新建污水净化工程</li>
        </router-link>
        <li class="active">新建排污工程</li>
      </ul>
      <h3 class="h3l">工程简介</h3>
      <textarea class="desc">请对工程进行简要描述……</textarea>
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
                value=""
              >
            </div>
            <div class="labelgroup">
              <span class="before">纬度</span>
              <input
                type="text"
                class="small"
                value=""
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
              value=""
            >
          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value=""
            >
            </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value=""
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
              value=""
            >
          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value=""
            >
            </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value=""
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
              value=""
            >
          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value=""
            >
            </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value=""
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
              value=""
            >
          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value=""
            >
            </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value=""
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
              value=""
            >
          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value=""
            >
            </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">m³/s</span></div>

          </div>
          <a class="delete">
            <img src="../assets/img/delete.png" />
          </a>
        </li>
        <li class="inputgroup templateUl">
          <input
            type="text"
            class="wide"
            value="出口"
          >
          <div class="labelgroup">
            <span class="before">经度</span>
            <input
              type="text"
              class="small"
              value=""
            >
          </div>
          <div class="labelgroup">
            <span class="before">纬度</span>
            <input
              type="text"
              class="small"
              value=""
            >
          </div>
          <div class="labelgroup-2x">
            <div class="labelgroup">
              <span class="before">COD</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TN</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">NH3-N</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">TP</span>
              <input
                type="text"
                class="small"
                value=""
              >
              <span class="after">mg/L</span>
            </div>
            <div class="labelgroup">
              <span class="before">流量</span>
              <input
                type="text"
                class="small"
                value=""
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
import ymap from '@/components/Map4-2.vue';

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
      text-indent 3.85rem
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
