<template>
  <div class="page inpage second">
    <div class="inpanel right">
      <div class="dtable dlist dlist-dm">
        <h3 class="h3l">方案效果评估</h3>
        <ul>
          <li>
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
          </li>
                    <li>
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
          </li>
                    <li>
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
          </li>
                    <li>
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
          </li>
                    <li>
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
          </li>
                    <li>
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
</style>
