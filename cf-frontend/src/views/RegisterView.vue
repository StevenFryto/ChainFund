<template>
    <div class="container">
        <div class="main">
            <!-- 整个注册盒子 -->
            <div class="loginbox">
                <!-- 左侧的注册盒子 -->
                <div class="loginbox-in">
                    <!-- 用户头像上传 -->
                    <input type="file" accept="image/*" @change="handleAvatarChange" ref="avatarInput"
                        style="display: none">
                    <div class="avatar-box">
                        <img :src="avatarPreview" class="avatar-preview" alt="点击上传头像" @click="openAvatarInput">
                    </div>
                    <div class="userbox">
                        <span class="iconfont">&#xe817;</span>
                        <input class="user" id="user" v-model="username" placeholder="用户名">
                    </div>
                    <br>
                    <div class="pwdbox">
                        <span class="iconfont">&#xe775;</span>
                        <input class="pwd" id="password" v-model="password" type="password" placeholder="密码">
                    </div>
                    <br>
                    <div class="emailbox">
                        <span class="iconfont">&#xe775;</span>
                        <input class="email" id="email" v-model="email" type="email" placeholder="电子邮箱（可选）">
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
import axios from 'axios';

export default {
    name: "RegisterView",
    data: function () {
        return {
            username: '',
            password: '',
            email: '',
            avatarFile: null,
            avatarPreview: 'https://s2.loli.net/2024/04/23/6kLR41dJxe23bXv.jpg' // 用于预览用户头像的图片URL
        }
    },
    methods: {
        openAvatarInput() {
            this.$refs.avatarInput.click();
        },
        handleAvatarChange(event) {
            const file = event.target.files[0];
            if (file) {
                this.avatarFile = file;
                this.avatarPreview = URL.createObjectURL(file);
            }
        },
        async register() {
            try {
                // 创建 FormData 对象，用于发送文件和其他数据
                const formData = new FormData();
                if (this.avatarFile != null) {
                    formData.append('avatar', this.avatarFile);
                } else {
                    formData.append('avatar', '');
                }

                formData.append('username', this.username);
                formData.append('password', this.password);
                formData.append('email', this.email);

                const response = await axios.post('http://localhost:5000/user-register', formData);
                console.log(response.data);

                if (response.data.status === true) {
                    const currentUserId = response.data.id;
                    this.$router.push(`${currentUserId}/home`);
                } else {
                    alert("该用户名已注册，请重新输入");
                    this.avatar = '';
                    this.username = '';
                    this.password = '';
                    this.email = '';
                }
            } catch (error) {
                console.log(error);
                alert("出现错误，联系开发人员");
            }
        }
    }
}
</script>

<style scoped>
img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover; 
}

.avatar-box {
    margin-top: 10%;
}

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
    margin-top: 20%;
    display: flex;
    margin-left: 10%;
}

.pwdbox {
    margin-top: 10%;
    display: flex;
    margin-left: 10%;
}

.emailbox {
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

    margin-top: 20%;
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