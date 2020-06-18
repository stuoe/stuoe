<template>
  <div class="error">
    <h1 class="error_h">404</h1>
    <router-link to="/">
        <el-button type="primary" style="display:block;margin:0 auto" round>返回首页</el-button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "404",
};
</script>
<style>
.error{
  background: #eee;
  position: fixed;
  width: 100%;
  height: 100%;
} 
.error_h{
    color: #1280ff;
    text-shadow: 0 8px 12px #1280ff;
    text-align: center;
    font-size: 200px;
    line-height: 100%;
}
</style>
