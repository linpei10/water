<template>
  <div class="progressCircle">
    <div class="rect right">
      <div
        class="circle rightcircle"
        :style="{borderBottomColor: color, borderLeftColor: color, transform: 'rotate('+rightDeg+'deg)'}"
      ></div>
    </div>
    <div class="rect left">
      <div
        class="circle leftcircle"
        :style="{borderTopColor: color, borderRightColor: color, transform: 'rotate('+leftDeg+'deg)'}"
      ></div>
    </div>
    <div class="text">
      <span class="p">{{ Number(percent).toFixed(4) }}</span>
      <span class="t">{{ title }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'circleProgress',
  props: ['percent', 'degree_percent', 'title', 'color'],
  computed: {
    real_percent() {
      // 圆圈显示百分比的设定方法：取以下数值为100%基准值TP:0.2，NH3-N:2.0, COD:40，TN:2.0.。然后取其数值对其百分比
      if (this.title === 'TP') {
        if (this.percent / 0.2 * 100 <= 100) {
          return Number(this.percent / 0.2 * 100);
        }
        return 100;
      }
      if (this.title === 'NH3-H') {
        return Number(this.percent / 2 * 100);
      }
      if (this.title === 'COD') {
        return Number(this.percent / 40 * 100);
      }
      if (this.title === 'TN') {
        return Number(this.percent / 2 * 100);
      }
      return 0;
    },
    rightDeg() {
      return Number(this.real_percent) >= 50 ? 225 : 45 + (225 - 45) * (Number(this.real_percent) / 50);
    },
    leftDeg() {
      return Number(this.real_percent) <= 50 ? 45 : 45 + (225 - 45) * ((Number(this.real_percent) - 50) / 50);
    },
  },
  data: () => ({
    // percent: this.percent,
    // title: this.title,
    // color: this.color,
    //   // 45~225
  }),
};
</script>

<style scoped lang="stylus">
  // @import '../global.styl';
  $width = 11.6rem;
  $width-border = 0.8rem;
  $width-border-sm = 0.1rem;

  .progressCircle {
    width: $width;
    height: $width;
    // margin: (($width)/2) auto;
    position: relative;
    display: inline-block;
  }

  .rect {
    width: ($width / 2);
    height: $width;
    position: absolute;
    top: 0;
    overflow: hidden;
  }

  .progress2::before {
    content: '';
    display: block;
    border-radius: 50%;
    border: 1px solid rgba(#ddd, 0.3);
    width: $width - 2 * $width-border-sm;
    height: $width - 2 * $width-border-sm;
  }

  .text {
    position: absolute;
    width: $width;
    height: $width;
    top: $width * 0.22;

    span {
      display: block;

      &.p {
        font-size: 2.2rem;
        font-weight: 500;
        line-height 4rem
      }

      &.t {
        margin-top: 0.4rem;
      }
    }
  }

  .right {
    right: 0;
  }

  .left {
    left: 0;
  }

  .circle {
    width: $width - 2 * $width-border;
    height: $width - 2 * $width-border;
    border: $width-border solid rgb(41, 137, 216);
    border-radius: 50%;
    position: absolute;
    top: 0;
    // transform: rotate(45deg);
  }

  .rightcircle {
    border-top: $width-border solid transparent;
    border-right: $width-border solid transparent;
    right: 0;
    transform: rotate(45deg);
  }

  .leftcircle {
    border-bottom: $width-border solid transparent;
    border-left: $width-border solid transparent;
    left: 0;
    transform: rotate(45deg);
  }
</style>
