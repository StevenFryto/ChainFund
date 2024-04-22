<template>
    <div class="project-details" v-if="project">
        <el-card class="detail-card">
            <div class="title">{{ project.title }}</div>
            <div class="time-cards">
                <el-card class="time-card" shadow="hover">发布时间：{{ project.created }}</el-card>
                <el-card class="time-card" shadow="hover">截止时间：{{ project.deadline }}</el-card>
            </div>
            <div class="funding-cards">
                <el-card class="money-card" shadow="hover">
                    <p>目标金额: {{ formatCurrency(project.goal) }} &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; 已筹得金额: {{
                        formatCurrency(project.raised) }}</p>
                </el-card>
                <el-progress type="circle" :percentage="percentage(project.goal, project.raised)" />
            </div>
            <el-card class="owner-card" @mouseover="handleMouseEnter" @mouseleave="handleMouseLeave">
                <template v-if="showDetails">
                    <div class="owner-details">
                        <div>
                            <p><b>担保人信息</b></p>
                            <p>姓名：{{ project.surety_info.surety_name }}</p>
                            <p>身份证号：{{ project.surety_info.surety_id_card }}</p>
                            <p>联系方式：{{ project.surety_info.surety_phone }}</p>
                        </div>
                        <img :src="project.surety_info.surety_id_photo" alt="Owner Image" class="owner-image" />
                    </div>
                </template>
                <template v-else>
                    <div class="patient-info">
                        {{ project.owner }} ({{ project.gender }}, {{ project.age }}岁) &nbsp;&nbsp;&nbsp; {{ project.job
                        }}
                    </div>
                </template>
            </el-card>
            <div class="project-images">
                <img v-for="(img, index) in project.images" :key="index" :src="img" alt="Project Image"
                    class="project-image" />
            </div>
            <div class="project-description">{{ project.description }}</div>
            <button @click="donate()">进行捐款</button>
            <div class="tags">
                <el-card v-for="(tag, index) in project.tags" :key="index" class="tag"
                    :style="{ backgroundColor: colors[index % colors.length] }" shadow="hover">
                    #&nbsp;{{ tag }}
                </el-card>
            </div>
        </el-card>
    </div>
</template>

<script>
import { ElCard } from 'element-plus';
export default {
    components: {
        //ElRow,
        //ElCol,
        ElCard
    },
    data() {
        return {
            project: null,
            showDetails: false,
            colors: ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', '#FF4500', '#20B2AA'], // 七种不同的颜色
        };
    },
    methods: {
        fetchProject(id) {
            // 模拟的获取数据逻辑
            return {
                id: id,
                title: '战胜疾病：共同支持健康恢复',
                created: '2024-4-21',
                deadline: '2024-7-31',
                owner: '李明宇',
                age: 44,
                gender: '男',
                job: '教师',
                surety_info: { surety_name: '苏萨', surety_phone: '123123123', surety_id_card: '110110110110', surety_id_photo: require('@/assets/sample_2.webp') },
                goal: 100000,
                raised: 85000,
                images: [
                    require('@/assets/sample_1.webp'),
                    require('@/assets/sample_3.webp'),
                    require('@/assets/sample_4.webp'),
                    // 更多图片
                ],
                description: '这个众筹项目专注于帮助患有罕见的遗传性血液病——地中海贫血的患者。地中海贫血是一种由基因突变引起的疾病，导致体内不能正常生产血红蛋白，从而引起贫血、疲劳和发展迟缓。如果不进行治疗，这种病可能会威胁生命，治疗方法通常包括定期的血液输注和可能的骨髓移植。',
                tags: ['紧急', '健康', '教育']
            };
        },
        formatCurrency(value) {
            return `$${value.toFixed(2)}`;
        },
        percentage(goal, raised) {
            return (raised / goal) * 100;
        },
        donate() {
            // Donation logic
        },
        handleMouseLeave() {
            // 设置延时
            this.timeoutId = setTimeout(() => {
                this.showDetails = false;
            }, 1500); // 500毫秒后隐藏，你可以根据需要调整这个时间
        },
        handleMouseEnter() {
            // 当鼠标再次进入时，清除之前的延时操作
            clearTimeout(this.timeoutId);
            this.showDetails = true;
        }
    },
    mounted() {
        const projectId = this.$route.params.id;
        this.project = this.fetchProject(projectId);
    }
}
</script>

<style scoped>
.title {
    font-size: xx-large;
    font-weight: bolder;
    margin-top: 20px;
    margin-bottom: 5px;
}

.project-details {
    display: flex;
    justify-content: center;
    padding: 20px;
}

.detail-card {
    width: 80%;
    border-radius: 25px;
    background-color: white;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.funding-cards {
    display: flex;
    justify-content: center;
    /* 使金额卡片整体居中 */
    align-items: center;
    /* 垂直居中 */
    margin-bottom: 20px;
    margin-top: 5px;
}

.money-card {
    padding-left: 15px;
    padding-right: 15px;
    box-shadow: 2px 2px 2px 2px rgba(63, 60, 60, 0.1);
    border-radius: 15px;
    color: #42b983;
    font-size: medium;
    font-weight: bold;
}

.time-cards {
    display: flex;
    justify-content: space-between;
    margin-left: 35%;
    margin-right: 35%;
    margin-bottom: 10px;
}

.time-card {
    /* border: 1px solid #7FC1BE; */
    border-radius: 5px;
    padding: 10px;
    color: grey;
    font-weight: bold;
    border-radius: 10px;
}

.owner-card {
    margin-bottom: 20px;
    border-radius: 5px;
    position: relative;
    cursor: pointer;
    margin-left: 30%;
    margin-right: 30%;
}

.owner-details {
    display: flex;
    justify-content: space-between;
    padding-left: 20px;
    padding-top: 5px;
    padding-bottom: 5px;
    background-color: white;
    border: 2px solid red;
    border-radius: 15px;
    text-align: left;
    font-weight: 600;
}

.owner-image {
    width: 80px;
    height: 80px;
    object-fit: cover;
    padding-top: 5%;
    padding-right: 5%;
}

.funding-details {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
}

.project-images {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    /* 保持图片间有间隔 */
    margin-bottom: 40px;
    margin-top: 40px;
    margin-left: 20%;
    margin-right: 20%;
}

.project-image {
    flex: 0 1 18%;
    height: 250px;
    /* 固定图片高度 */
    object-fit: cover;
    /* 保持图片比例 */
    border-radius: 10px;
    /* 图片圆角 */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    /* 图片阴影 */
    margin-bottom: 20px;
}

.patient-info {
    font-weight: bold;
    font-size: large;
}

.project-description {
    padding-left: 25%;
    padding-right: 25%;
    font-size: 17px;
    /* 示例：设置为16px，可以根据需要调整 */
    text-align: left;
    /* 设置文字左对齐 */
    line-height: 1.7;
    /* 设置行间距为1.5，这是一种常见的行间距设置 */
}

.tags {
    display: flex;
    justify-content: flex-end;
    /* 标签靠左对齐 */
    align-items: center;
    margin-right: 5%;
    /* 从左侧有一定间距 */
    /* 与上方元素的间距 */
    margin-bottom: 20px;
    /* 与下方元素的间距 */
}

.tag {
    margin-right: 10px;
    /* 标签之间的间距 */
    padding: 5px 10px;
    /* 标签内部的填充 */
    color: white;
    /* 文字颜色 */
    font-weight: 400px;
    /* 文字加粗 */
    border-radius: 5px;
    /* 圆角 */
    font-size: 15px;
}

button {
    width: 200px;
    height: 50px;
    padding: 10px 20px;
    background-color: #42b983;
    border: none;
    color: white;
    cursor: pointer;
    margin-top: 30px;
    margin-bottom: 20px;
    border-radius: 15px;
    font-size: large;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
