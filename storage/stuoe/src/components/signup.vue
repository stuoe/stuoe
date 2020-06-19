<template>
  <div class="signup">
    <div class="sign_ubox">
      <el-form :model="signUp" :rules="sUp_r" ref="signUp">
        <h1 class="sign-h">注册</h1>
        <el-form-item prop="email">
          <input type="text" v-model="signUp.email" placeholder="邮箱" class="sign-input" />
        </el-form-item>
        <el-form-item prop="email_v">
          <input
            type="text"
            v-model="signUp.email_v"
            placeholder="邮箱验证码"
            class="sign-input sign-up_e-vinput"
            style="width:50%"
          />
          <el-button
            type="primary"
            :disabled="email_vTD"
            style="width:40%;margin-left:2%"
            @click="getEmail_v"
          >{{email_vT}}</el-button>
        </el-form-item>
        <el-form-item prop="password">
          <input
            type="password"
            v-model="signUp.password"
            placeholder="密码(6-20个字符)"
            class="sign-input"
          />
        </el-form-item>
        <el-form-item prop="passwordA">
          <input type="password" v-model="signUp.passwordA" placeholder="再次输入密码" class="sign-input" />
        </el-form-item>
        <el-form-item prop="UA">
          <el-checkbox v-model="signUp.UA">我已阅读并同意</el-checkbox>
          <a style="cursor:pointer" @click="user_agr = true">《用户协议》</a>
        </el-form-item>
        <el-button type="primary" round style="width:50%" @click="signUpform('signUp')">注册账号</el-button>
        <el-dialog title="源码星球用户协议" :visible.sync="user_agr" width="50%" append-to-body>
          <userAgr class="user_agr"></userAgr>
          <div slot="footer" class="dialog-footer">
            <el-button @click="signUp.UA = false;user_agr=false">不同意</el-button>
            <el-button type="primary" @click="signUp.UA = true;user_agr=false">同意</el-button>
          </div>
        </el-dialog>
      </el-form>
    </div>
  </div>
</template>

<style>
.sign_ubox {
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 50px;
  height: 100%;
  text-align: center;
}
.sign-h {
  text-align: center;
  font-size: 22px;
  color: #333;
  margin-bottom: 20px;
}
.sign-input {
  width: 100%;
  border: none;
  font-size: 15px;
  padding: 12px;
  background: #eee;
  color: #666;
  outline: none;
  border-radius: 5px;
}

.other {
  cursor: pointer;
  color: #888;
  font-size: 14px;
  display: inline-block;
  width: 50%;
}
</style>
<script>
import userAgr from "./user_agreement";
export default {
  name: "signup",
  data() {
    var UA = (rule, value, callback) => {
      if (value == false) {
        return callback(new Error("请勾选同意用户协议"));
      } else {
        callback();
      }
    };
    var email_v = (rule, value, callback) => {
      return callback(new Error("验证码错误"));
    };
    var passwordA = (rule, value, callback) => {
      if (value == this.signUp.password) {
        callback();
      } else {
        return callback(new Error("两次密码不一样"));
      }
    };
    return {
      email_vT: "发送验证码",
      time: "60",
      email_vTD: false,
      sign: 0,
      signUp: {
        email: "",
        email_v: "",
        password: "",
        passwordA: "",
        UA: true
      },
      sUp_r: {
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            min: 6,
            max: 20,
            message: "密码长度需在6-20个字符",
            trigger: "blur"
          }
        ],
        email: [
          { required: true, message: "请输入邮箱地址", trigger: "blur" },
          {
            type: "email",
            message: "请输入正确的邮箱地址",
            trigger: ["blur", "change"]
          }
        ],
        UA: [{ validator: UA, trigger: "blur" }],
        email_v: [{ validator: email_v, trigger: "blur" }],
        passwordA: [{ validator: passwordA, trigger: "blur" }]
      }
    };
  },
  methods: {
    signUpform(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          // $.ajax({
          //   url: "/signup",
          //   method: "POST",
          //   data: {
          //     //name
          //     password: signUp.password,
          //     email: signUp.email
          //   }
          // });
        } else {
          return;
        }
      });
    },
    getEmail_v() {
      var e = /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/;
      if (e.test(this.signUp.email)) {
        this.email_vTD = true;
        this.timer();
      } else {
        this.email_vT = "邮箱格式错误";
      }
    },
    timer() {
      if (this.time > 0) {
        this.time--;
        this.email_vT = this.time + "s后重新获取";
        setTimeout(this.timer, 1000);
      } else {
        this.time = 0;
        this.email_vT = "获取验证码";
        this.email_vTD = false;
      }
    }
  },
  components: {
    userAgr
  }
};
</script>
