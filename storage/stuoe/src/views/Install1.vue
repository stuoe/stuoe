<template>
  <div class="page-start">
    <h1>开始安装</h1>
    <h3 class="subtitle">安装你的 <strong>Stuoe</strong>!</h3>
    <el-divider></el-divider>
    <br />
    <InstallStep :n='0'></InstallStep>
    <br />
    <el-divider>基本信息</el-divider>
    <el-form
      label-width="100px"
      :model="formData"
      :rules="formRules"
      ref="form"
    >
      <el-form-item label="论坛名称:" prop="name">
        不如起个好名字吧，例如“shyfcka fourm"
        <el-input placeholder="好听的名称往往被记住" v-model="formData.name">
          <i slot="prefix" class="el-input__icon fa fa-bookmark-o"></i>
        </el-input>
      </el-form-item>
      <el-form-item prop="email" label="管理员邮箱:">
        通知论坛重要事务和绑定管理员账号
        <el-input placeholder="可不要乱填写哦" v-model="formData.email">
          <i slot="prefix" class="el-input__icon fa fa-envelope-o"></i>
        </el-input>
      </el-form-item>
      <el-form-item prop="desc" label="论坛描述:">
        这将被填写在SEO中
        <el-input
          placeholder="聊天聊地聊空气! 向大家介绍一下你的论坛吧!"
          type="textarea"
          v-model="formData.desc"
        >
        </el-input>
      </el-form-item>
      <!-- smtp的host,port,user,password
地址
端口
邮箱
密码/授权码 -->
      <br />
      <el-divider>SMTP设置</el-divider>
      <el-form-item prop="smtp_host" label="地址:">
        <el-input placeholder="SMTP主机地址" v-model="formData.smtp.host">
        </el-input>
      </el-form-item>
      <el-form-item prop="smtp_port" label="端口:">
        <el-input placeholder="SMTP端口号" v-model="formData.smtp.port">
        </el-input>
      </el-form-item>

      <el-form-item prop="smtp_email" label="邮箱:">
        <el-input placeholder="SMTP邮箱" v-model="formData.smtp.email">
        </el-input>
      </el-form-item>
      <el-form-item prop="smtp_password" label="密码/授权码:">
        <el-input
          placeholder="SMTP密码/授权码"
          v-model="formData.smtp.password"
        >
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit()">下一步</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import $ from "jquery";
import InstallStep from "../components/InstallStep";
export default {
  name: "Install1",
  components: {
    InstallStep,
  },
  data() {
    return {
      formData: {
        name: "",
        email: "",
        desc: "",
        smtp: {
          host: "",
          port: "",
        },
      },
      formRules: {
        email: [
          { required: true, message: "请输入邮箱地址", trigger: "blur" },
          {
            type: "email",
            message: "请输入正确的邮箱地址",
          },
        ],
        name: [
          { required: true, message: "总要有个名字的", trigger: "blur" },
          { min: 3, max: 24, message: "名称必须是3~24个字符" },
          {
            pattern: /^[_A-Za-z0-9]+$/,
            message: "名称只能包含大小写字母,数字和下划线",
            transform(v) {
              return v.trim();
            },
          },
        ],
        desc: [
          { required: true, message: "随便写点什么吧~", trigger: "blur" },
          { max: 1000, message: "这有些太长了,语言再精炼一些吧~" },
        ],
        smtp_host: [{ required: true, message: "此项必填", trigger: "blur" }],
        smtp_email: [{ required: true, message: "此项必填", trigger: "blur" }],
        smtp_port: [{ required: true, message: "此项必填", trigger: "blur" }],
        smtp_password: [
          { required: true, message: "此项必填", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    submit() {
      let f = this.$refs.form;
      let fd = this.formData;
      f.validate((v) => {
        if (!v) {
          return;
        }

        $.ajax({
          url: "/install/start",
          method: "POST",
          data: {
            form_name: fd.name,
            admin_mail: fd.email,
            forum_des: fd.desc,
          },
        });
      });
    },
  },
};
</script>
<style>
.page-start {
  padding: 50px 400px;
}
</style>
