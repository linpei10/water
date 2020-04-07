<template>
<div>
  <h3 class="h3l">主要污染物浓度随时间变化（mg/L）</h3>
  <ul>
    <li v-for="(item,index) in pollutant" v-bind:key=index>
      <div class="item">
        <div class="head">
          <div class="font">{{item}}</div>
        </div>
        <div class="image">
          <img :src="'uploads/emer/emer-chi/first/R/'+num+'/case1-'+item+'.png'">
        </div>
      </div>
    </li>
  </ul>
</div>
</template>

<script>

export default {
  data() {
    return {
      pollutant: ['COD', 'TN', 'NH3-N', 'TP'],
      num: this.$store.state.firstPageClick,
    };
  },
};
</script>

<style lang="stylus" scoped>
$height = 18rem;

ul{
  list-style-type: none;
  padding: 0rem;
  margin: 5rem 2rem;

  .item{

    display: inline-block;
    margin: 1rem 1rem;
    height: $height;
    line-height: $height;

    .head{
      position: absolute;
      margin: 0rem 1rem;

      .font{
        display: inline-block;
        vertical-align: middle;

        width: 2rem;
        font-size: 2rem;
        line-height:2rem;
        word-wrap: break-word;
      }
    }
    .image{
      position: relative;
      left: 4rem;
      height: $height;

      img{
        vertical-align: middle;
        max-width: 100%;
        max-height: 100%;
        margin: auto;
      }
    }
  }
}
</style>
