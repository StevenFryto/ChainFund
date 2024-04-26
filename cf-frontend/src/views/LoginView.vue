<template>
    <div class="container">
        <div class="main">
            <!-- 整个注册盒子 -->
            <div class="loginbox">
                <!-- 左侧的注册盒子 -->
                <div class="loginbox-in">
                    <div class="userbox">
                        <span class="iconfont">&#xe817;</span>
                        <input class="user" id="user" v-model="username" placeholder="用户名">
                    </div>
                    <br>
                    <div class="pwdbox">
                        <span class="iconfont">&#xe775;</span>
                        <input class="pwd" id="password" type="password" v-model="password" placeholder="密码">
                    </div>
                    <br>
                    <div class="log-box">
                        <div class="log-box-text"> 忘记密码</div>
                        <button type="primary" class="login_btn" @click="login">登录</button>
                    </div>

                    <br>
                    <div class="warn">系统信息</div>
                    <button type="primary" class="register_btn" @click="register">若无账号请点击注册</button>
                </div>

                <!-- 右侧的注册盒子 -->
                <div class="background">
                    <div class="title">ChainFund —— 基于区块链和推荐算法的智能众筹系统</div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
// import { Axios } from 'axios';
import axios from 'axios';

export default {
    name: "LoginView",
    data: () => {
        return {
            username: '',
            password: ''
        }
    },
    inject: ['getCurrentUserId', 'setCurrentUserId'],
    methods: {
        register() { this.$router.push("register") },
        async login() {
            try {
                const response = await axios.post('http://localhost:5000/user-login', {
                    username: this.username,
                    password: this.password
                })
                console.log(response.data);
                
                if (response.data.status === true) {
                    const currentUserId = response.data.id;
                    // this.setCurrentUserId(currentUserId);
                    // this.$router.push(`${currentUserId}/home`);
                    this.$router.push(`${currentUserId}/home`);
                } else {
                    alert("用户名或密码错误，请重新输入");
                    this.username = '';
                    this.password = '';
                }
            } catch (error) {
                console.log(error);
                alert("出现错误，联系开发人员");
            }
        }
    },
}
</script>

<style scoped>
.loginbox {
    display: flex;
    position: absolute;
    width: 70%;
    height: 70%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 #4E655D;
}

.loginbox-in {
    flex: 1;
    background-color: #89AB9E;
}

.userbox {
    margin-top: 40%;
    display: flex;
    margin-left: 10%;
}

.pwdbox {
    margin-top: 10%;
    display: flex;
    margin-left: 10%;
}

.background {
    flex: 3;
    background-image: url('../assets/Trees.png');
    background-size: cover;
    font-family: sans-serif;
}

.title {
    margin-top: 60%;
    font-weight: bold;
    font-size: 20px;
    color: #4E655D;
}

.title:hover {
    font-size: 21px;
    transition: all 0.4s ease-in-out;
    cursor: pointer;
}

.uesr-text {
    position: left;
}

input {
    outline-style: none;
    border: 0;
    border-bottom: 1px solid #E9E9E9;
    background-color: transparent;
    height: 20px;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;
}

/* input::-webkit-input-placeholder{
      color:#E9E9E9;
   } */
input:focus {
    border-bottom: 2px solid #445b53;
    background-color: transparent;
    transition: all 0.2s ease-in;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;

}

input:hover {
    border-bottom: 2px solid #445b53;
    background-color: transparent;
    transition: all 0.2s ease-in;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;

}

input:-webkit-autofill {
    /* 修改默认背景框的颜色 */
    box-shadow: 0 0 0px 1000px #89AB9E inset !important;
    /* 修改默认字体的颜色 */
    -webkit-text-fill-color: #445b53;
}

input:-webkit-autofill::first-line {
    /* 修改默认字体的大小 */
    font-size: 15px;
    /* 修改默认字体的样式 */
    font-weight: bold;
}

.log-box {
    display: flex;
    justify-content: space-between;
    width: 70%;
    margin-top: 10%;
    margin-left: 30px;
    color: #4E655D;
    align-items: center;
}

.log-box-text {
    color: #4E655D;
    font-size: 14px;
    text-decoration: underline;
}

.login_btn {
    background-color: #5f8276;
    /* Green */
    border: none;
    color: #FAFAFA;
    padding: 10px 30px;
    text-align: center;
    text-decoration: none;
    border-radius: 20px;
    outline: none;

    font-size: 16px;
}

.login_btn:hover {
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
    cursor: pointer;
    background-color: #0b5137;
    transition: all 0.2s ease-in;
}

.warn {
    margin-top: 50%;
    /* margin-right: 120px; */
    /* margin-left: -120px; */
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 16px;
}

.register_btn {
    background-color: transparent;
    /* Green */
    border: none;
    text-decoration: none;
    font-size: 14px;
    /* border-radius: 20px;   */
    color: #4E655D;
    text-decoration: underline;
    display: flex;
    margin-top: 10%;
    margin-left: 10%;
    outline: none;

}

.register_btn:hover {
    font-weight: bold;
    cursor: pointer;
}

@font-face {
    font-family: "iconfont";
    src: url('../assets/font/iconfont.eot');
    src: url('../assets/font/iconfont.eot?#iefix') format('embedded-opentype'),
        url('../assets/font/iconfont.woff2') format('woff2'), url('../assets/font/iconfont.woff') format('woff'), url('../assets/font/iconfont.ttf') format('truetype'),
        url('../assets/font/iconfont.svg#iconfont') format('svg');
}

.iconfont {
    font-family: "iconfont" !important;
    font-size: 20px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    height: 22px;
    color: #4E655D;
    margin-right: 10px;
    margin-top: 3px;
}

.icon-key:before {
    content: "\e775";
}

.icon-account:before {
    content: "\e817";
}
</style>