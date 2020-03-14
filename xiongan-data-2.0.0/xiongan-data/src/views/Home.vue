<template>
  <div class="home">
    <router-link to="/combine">index</router-link><br>
    <router-link to="/firstPage">firstPage</router-link><br>
    <router-link to="/secondPage">secondPage</router-link><br>
    <router-link to="/SecondPage_1">SecondPage_1</router-link><br>
    <router-link to="/thirdPage">thirdPage</router-link><br>
    <router-link to="/ThirdPage-2">ThirdPage-2</router-link><br>
    <router-link to="/FourthPage">FourthPage</router-link><br>
    <router-link to="/FourthPage_2">FourthPage-2</router-link><br>
    <router-link to="/FifthPage">FifthPage</router-link><br>
    <router-link to="/2_1right">2_1right</router-link><br>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'home',
  components: {},
};
</script>

<style lang="stylus" scoped>
.home {
  margin-top: 2rem;
  font-size: 2rem;
  text-align: center;
}
</style>
