<template>
  <div class="index">
    index
    <el-button @click="TSignup=true">注册</el-button>
    <el-dialog :visible.sync="TSignup" width="450px" :close-on-click-modal="false">
      <signup></signup>
    </el-dialog>
  </div>
</template>

<script>
import signup from "../components/signup";
export default {
  name: "Index",
  components: {
    signup
  },
  data() {
    return {
      TSignup: false
    };
  }
};
</script>
<style>
</style>
