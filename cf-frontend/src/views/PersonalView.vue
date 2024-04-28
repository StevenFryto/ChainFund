<template>
    <div class="personal-container">
        <!-- 个人信息 -->
        <div class="user-profile">
            <img class="avatar" :src="user.avatarUrl" alt="用户头像" />
            <div class="user-details">
                <h1 class="user-name">{{ user.name }}</h1>
                <!-- <p class="user-id"><b>身份证号：</b>{{ user.id }}</p>
                <p class="user-phone"><b>电话号码：</b>{{ user.phone }}</p> -->
                <p class="user-email"><b>邮箱：</b>{{ user.email }}</p>
            </div>
        </div>

        <!-- 浏览记录 -->
        <div class="user-history">
            <h2>浏览记录</h2>

            <div class="history-list">
                <div v-for="record in history" :key="record.projectId" class="history-section" @click="viewRecord(record.projectId)">
                    <div class="history-content">
                        <h3 class="history-title">{{ record.title }}</h3>
                        <p class="history-meta">观看时间: {{ record.watchedAt }}</p>
                    </div>
                    <button class="history-delete" @click.stop.prevent="deleteRecord(record.id)">
                        删除
                    </button>
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
        deleteRecord(projectId) {
            // this.history = this.history.filter(record => record.projectId !== projectId);
            // 向后端发送删除请求
            axios.delete(`http://localhost:5000/deleteHistory`, {
                params: {
                    userId: this.$route.params.userId,
                    projectId: projectId,
                }
            })
                .then(response => {
                    console.log("成功删除:", response.data.message);
                    this.fetchHistory();
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
                // id: '',
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
    width: 75%;
    margin-left: auto;
    margin-right: auto;
}

.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.user-details {
    display: flex;
    flex-direction: column;
}

.user-name {
    font-size: 36px;
    font-weight: bold;
}

.user-id,
.user-phone,
.user-email {
    font-size: 16px;
    color: #666;
}

/* 浏览记录样式 */
.user-history {
    width: 75%;
    margin: 20px auto;
    padding: 20px;
    background-color: #7ad2ba;
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
    background-color: #ffffff;
    /* 绿色背景 */
    border-bottom: 5px solid #7ad2ba;
    /* 底部分隔线 */
    border-radius: 10px;
}

.history-section:last-child {
    border-bottom: none;
    /* 最后一条记录不需要底部分隔线 */
}

.history-content {
    flex-grow: 1;
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
