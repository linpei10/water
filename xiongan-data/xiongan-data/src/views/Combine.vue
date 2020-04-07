<template>
<!--
  百度地图组件、两个列表以及4个环状图组织成play组件
-->
  <div class="play">
    <ymap distPage="/firstPage" v-bind:flagShow="true"/>
    <design distPage="/firstPage" v-bind:flagShow="true" />
  </div>
</template>

<script>
import ymap from '@/components/Map.vue';
import design from '@/views/Design.vue';

export default {
  name: 'play',
  components: {
    ymap,
    design,
  },
};
</script>

<style>

</style>
