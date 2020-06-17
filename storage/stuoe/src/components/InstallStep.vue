<template>
  <el-steps :active="n">
      <el-step title="填写基本信息"></el-step>
      <el-step title="--"></el-step>
      <el-step title="--"></el-step>
    </el-steps>
</template>

<script>
export default {
  name:"InstallStep",
  props:["n"]
}
</script>

<style>

</style>
