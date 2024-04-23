<template>
    <div class="container">
        <div class="main">
            <!-- 整个注册盒子 -->
            <div class="loginbox">
                <!-- 左侧的注册盒子 -->
                <div class="loginbox-in">
                    <div class="userbox">
                        <span class="iconfont">&#xe817;</span>
                        <input class="user" id="user" v-model="name" placeholder="用户名">
                    </div>
                    <br>
                    <div class="pwdbox">
                        <span class="iconfont">&#xe775;</span>
                        <input class="pwd" id="password" v-model="pwd" type="password" placeholder="密码">
                    </div>
                    <br>
                    <div class="pwdbox">
                        <span class="iconfont">&#xe775;</span>
                        <input class="pwd" id="re_password" v-model="repwd" type="password" placeholder="确认密码">
                    </div>

                    <br>
                    <button type="primary" class="register_btn" @click="register">点击注册</button>
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
export default {
    name: "RegisterView",
    data: function () {
        return {
            name: '',
            pwd: '',
            repwd: '',
            user_list: [
                {
                    username: 'admin',
                    password: '123'
                },

            ]
        }
    },
    methods: {
        register() {
            var flag = 1;
            //如果用户名已存在，则需要换一个用户名
            this.user_list.forEach((item) => {
                if (item.username == this.name) {
                    alert('用户已存在,请换一个用户名');
                    flag = 0;
                }
            }
            )
            //如果用户名不存在，则继续判断
            if (flag) {
                // 判断两次输入的密码是否一致，如果密码不一致，则需要重新输入
                if (this.pwd != this.repwd) {
                    alert('两次输入的密码不一致,请重新输入');
                }
                // 如果密码也一直，则存到用户列表里面
                else {
                    var item = {};
                    // 获取到用户名
                    item.username = this.name;
                    // 获取到密码
                    item.password = this.pwd;
                    // 存储到用户列表
                    this.user_list.push(item);
                    alert('注册成功');
                    //    this.user_list.forEach((item) => {
                    //       console.log( item.username);
                    // })

                    this.$router.push({
                        path: '/',
                        query: {
                            list: this.user_list,
                        }
                    })
                }
            }
        }
    }
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

.register_btn {
    background-color: #5f8276;
    /* Green */
    border: none;
    color: #FAFAFA;
    padding: 10px 30px;
    text-align: center;
    text-decoration: none;
    border-radius: 20px;
    outline: none;

    margin-top: 40%;
    font-size: 16px;
}

.register_btn:hover {
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
    cursor: pointer;
    background-color: #0b5137;
    transition: all 0.2s ease-in;
}

.warn {
    margin-top: 50%;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 16px;
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