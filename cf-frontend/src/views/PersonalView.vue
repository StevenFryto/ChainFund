<template>
    <div class="personal-container">
        <!-- 个人信息 -->
        <div class="user-profile">
            <img class="avatar" :src="user.avatarUrl" alt="用户头像" />
            <div class="user-details">
                <h1 class="user-name">{{ user.name }}</h1>
                <!-- <p class="user-id"><b>身份证号：</b>{{ user.id }}</p>
                <p class="user-phone"><b>电话号码：</b>{{ user.phone }}</p> -->
                <div class="user-email"><b>📫 您的注册邮箱为 </b>{{ user.email }}</div>
                <div class="user-id">🥳 感谢您成为链上智筹的 <b>第 {{ $route.params.userId }} 位</b> 用户</div>
                <div class="user-tips">📅 下面是您的 <b>浏览记录</b> 您可以查看或删除 </div>
            </div>
        </div>
        
        <!-- 浏览记录 -->
        <div class="user-history">
            <div class="search-bar-container">
                <input type="text" v-model="searchQuery" @input="fetchSearchResults" placeholder="搜索您的浏览记录" class="search-bar" />
                <button @click="fetchSearchResults" class="search-button">模糊搜索</button>
                <button @click="fetchSearchResults" class="search-button">正则匹配</button>
            </div>
            <div class="history-list">
                <div v-for="record in history" :key="record.id" class="history-section" @click="viewRecord(record.id)">
                    <div class="history-content">
                        <div class="history-title">{{ record.title }}</div>
                        <div class="history-meta">观看时间: {{ record.watchedAt }}</div>
                        <button class="history-delete" @click.stop.prevent="deleteRecord(record.id)">
                            删除
                        </button>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'PersonalView',
    methods: {
        deleteRecord(id) {
            const recordId = id;
            this.history = this.history.filter(record => record.id !== id);
            // 向后端发送删除请求
            axios.delete(`http://localhost:5000/deleteHistory?id=${recordId}`)
                .then(response => {
                    console.log("成功删除:", response.data.message);
                })
                .catch(error => {
                    if (error.response) {
                        console.error("删除失败:", error.response.data.error);  // 显示详细错误信息
                    } else {
                        console.error("网络错误或其他问题");  // 网络问题或其他未处理的错误
                    }
                });

        },
        viewRecord(recordId) {
            // 跳转到指定的 /project/:id 页面
            this.$router.push({ name: 'ProjectDetails', params: { id: recordId } });
        },
        async fetchPersonalInfo() {
            const currentUserId = this.$route.params.userId;
            try {
                const response = await axios.get(`http://localhost:5000/getPersonalInfo?id=${currentUserId}`);
                this.user = response.data;
                this.user.avatarUrl = require(`@/assets/avatars/${this.user.avatar}`)
            } catch (error) {
                console.error('获取用户信息失败', error);
            }
        },
        async fetchHistory() {
            const currentUserId = this.$route.params.userId;
            try {
                const response = await axios.get(`http://localhost:5000/getHistory?id=${currentUserId}`);
                this.history = response.data.history;
            } catch (error) {
                console.error('获取浏览记录失败', error);
            }
        },
    },
    data() {
        return {
            user: {
                name: '',
                // id: '11',
                // phone: '',
                email: '',
                avatarUrl: ''
            },
            history: []
        };
    },
    mounted() {
        this.fetchPersonalInfo();
        this.fetchHistory();
    }
}
</script>

<style scoped>
.personal-container {
    padding: 20px;
}

/* 个人信息的样式 */
.personal-container {
    padding: 20px;
}

.user-profile {
    align-items: center;
    margin-bottom: 20px;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    width: 60%;
    margin-left: auto;
    margin-right: auto;

    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}

.avatar {
    width: 200px;
    height: 200px;
    border-radius: 50%;
}

.user-details {
    display: flex;
    flex-direction: column;
    text-align: left;
}

.user-name {
    font-size: 36px;
    font-weight: bold;
}

.user-email, 
.user-tips,
.user-id {
    font-size: 16px;
    color: #666;

    margin-bottom: 10px;
}

.search-bar-container {
    display: flex;
    justify-content: center;
    padding: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.search-bar {
    width: 70%;
    padding-left: 20px;
    border: none;
    border-radius: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    font-weight: 600;
}

.search-button {
    padding: 10px 20px;
    margin-left: 10px;
    border: none;
    background-color: #007BFF;
    color: white;
    border-radius: 20px;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    font-weight: 700;

    transition: background-color 0.3s ease, transform 0.2s ease;
}

.search-button:hover {
    transform: scale(1.05);
}

/* 浏览记录样式 */
.user-history {
    width: 60%;
    margin: 20px auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.history-list {
    padding: 20px 0;
}

.history-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background-color: #f5f5f5;
    border-radius: 10px;

    margin-bottom: 20px;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.history-section:hover {
    transform: scale(1.02);
}

.history-section:last-child {
    border-bottom: none;
    /* 最后一条记录不需要底部分隔线 */
}

.history-content {
    flex-grow: 1;
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    height: 45px;
    line-height: 45px;
}

.history-title {
    font-size: 18px;
    font-weight: 600;
}

.history-meta {
    font-size: 14px;
    color: #666;
}

.history-delete {
    padding: 10px;
    background-color: #e63946;
    border-radius: 6px;
    color: white;
    transition: background-color 0.3s ease, transform 0.2s ease;
    cursor: pointer;
}

.history-delete:hover {
    background-color: #d32f2f;
    transform: scale(1.05);
    /* 悬停时按钮放大 */
}
</style>
