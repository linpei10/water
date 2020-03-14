<template>
<!--<div class="home">-->
<!--    <router-link to="/combine">index</router-link><br>-->
<!--    <router-link to="/firstPage">firstPage</router-link><br>-->
<!--    <router-link to="/secondPage">secondPage</router-link><br>-->
<!--    <router-link to="/SecondPage_1">SecondPage_1</router-link><br>-->
<!--    <router-link to="/thirdPage">thirdPage</router-link><br>-->
<!--    <router-link to="/ThirdPage-2">ThirdPage-2</router-link><br>-->
<!--    <router-link to="/FourthPage">FourthPage</router-link><br>-->
<!--    <router-link to="/FourthPage_2">FourthPage-2</router-link><br>-->
<!--    <router-link to="/FifthPage">FifthPage</router-link><br>-->
<!--    <router-link to="/2_1right">2_1right</router-link><br>-->
<!--  </div>-->
<div class="home">
  <div class="background">
    <div id="login_frame">
      <form method="post" >

        <p><label class="label_input">用户名</label><input type="text" value="admin" id="username" class="text_field"/></p>
        <p><label class="label_input">密码</label><input type="password" value="***" id="password" class="text_field"/></p>

        <div id="login_control">
          <router-link to="/combine">登陆</router-link>
          <a id="forget_pwd" href="#">忘记密码？</a>
        </div>
      </form>
    </div>
  </div>
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
  @import '../global.styl';

</style>
