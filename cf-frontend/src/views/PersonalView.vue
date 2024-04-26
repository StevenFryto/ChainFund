<template>
  <div class="personal-container">
    <!-- 个人信息 -->
    <div class="user-profile">
      <img class="avatar" :src="user.avatarUrl" alt="用户头像" />
      <div class="user-details">
        <h1 class="user-name">{{ user.name }}</h1>
        <p class="user-id"><b>身份证号：</b>{{ user.id }}</p>
        <p class="user-phone"><b>电话号码：</b>{{ user.phone }}</p>
      </div>
    </div>
    
    <!-- 浏览记录 -->
    <div class="user-history">
      <h2>浏览记录</h2>

      <div class="history-list">
        <div v-for="record in history" :key="record.id" class="history-section"
             @click="viewRecord(record.id)">
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
export default {
  name: 'PersonalView',
  methods: {
    deleteRecord(id) {
      this.history = this.history.filter(record => record.id !== id);
    },
    viewRecord(recordId) {
      // 跳转到指定的 /project/:id 页面
      this.$router.push({ name: 'ProjectDetails', params: { id: recordId } });
    }
  },
  data() {
    return {
      user: {
        name: '张三',
        id: '12345678901234',
        phone: '12345678901',
        avatarUrl: 'https://th.bing.com/th/id/R.57384e4c2dd256a755578f00845e60af?rik=uy9%2bvT4%2b7Rur%2fA&riu=http%3a%2f%2fimg06file.tooopen.com%2fimages%2f20171224%2ftooopen_sy_231021357463.jpg&ehk=whpCWn%2byPBvtGi1%2boY1sEBq%2frEUaP6w2N5bnBQsLWdo%3d&risl=&pid=ImgRaw&r=0'
      },
      history: [
        { id: 1, title: '123456789', watchedAt: '13:25' },
        { id: 2, title: 'abcdefghij', watchedAt: '13:22' },
        { id: 3, title: 'klmnopqrst', watchedAt: '13:20' },
      ]
    };
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
.user-phone {
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
  background-color: #ffffff; /* 绿色背景 */
  border-bottom: 5px solid #7ad2ba; /* 底部分隔线 */
  border-radius: 10px;
}

.history-section:last-child {
  border-bottom: none; /* 最后一条记录不需要底部分隔线 */
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
  transform: scale(1.05); /* 悬停时按钮放大 */
}
</style>
