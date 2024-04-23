<template>
    <div class="projects" v-if="projects">
        <div class="project-container">
            <div class="project-card" shadow="always" v-for="project in projects" :key="project.id"
                @click="navigateToProject(project.id)">
                <el-card class="card-content">
                    <div class="clearfix">{{ project.title }}</div>
                    <img :src="project.image" class="project-image" />
                    <!--<el-progress class="progress" type="line" color="green"
                        :percentage="percentage(project.target_amount, project.current_amount)" :stroke-width="5"
                        :text-inside="true" status="success" />-->
                    <div class="progress-container">
                        <div class="progress-bar"
                            :style="{ width: percentage(project.target_amount, project.current_amount) + '%' }"></div>
                    </div>
                    <div>
                        <div class="project-funds-title">
                            <div class="fund-target_amount-title">目标金额</div>
                            <div class="fund-target_amount-title">已筹得金额</div>
                        </div>
                        <div class="project-funds">
                            <div class="fund-target_amount">{{ formatCurrency(project.target_amount) }}</div>
                            <div class="fund-current_amount">{{ formatCurrency(project.current_amount) }}</div>
                        </div>
                    </div>
                    <div class="label-container">
                        <el-card v-for="(tag, index) in project.label" :key="index" class="tag"
                            :style="{ backgroundColor: colors[index % colors.length] }">
                            # {{ tag }}
                        </el-card>
                    </div>
                </el-card>
            </div>
        </div>
    </div>
</template>

<script>
// import { ElRow, ElCol, ElCard, ElProgress } from 'element-plus';
// import { ElCard, ElProgress } from 'element-plus';
import { ElCard } from 'element-plus';
import axios from 'axios';

export default {
    name: 'ProjectsView',
    components: {
        //ElRow,
        //ElCol,
        ElCard,
        //ElProgress
    },
    data() {
        return {
            /* projects: [
                {
                    id: 1,
                    title: '帮助山区儿童读书',
                    image: require('@/assets/logo.png'),
                    target_amount: 10000,
                    current_amount: 4500,
                    label: ['教育', '儿童', '山区']
                },
                {
                    id: 2,
                    title: '城市无家可归者援助',
                    image: require('@/assets/logo.png'),
                    target_amount: 8000,
                    current_amount: 5600,
                    label: ['援助', '城市', '无家可归']
                },
                {
                    id: 3,
                    title: '清洁海洋行动',
                    image: require('@/assets/logo.png'),
                    target_amount: 15000,
                    current_amount: 3000,
                    label: ['海洋', '清洁']
                }
            ],*/
            projects: null,
            colors: ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', '#FF4500', '#20B2AA'],
        };
    },

    methods: {
        fetchProjects() {
            const baseUrl = 'http://127.0.0.1:5000/getProjects';  // 确保后端URL正确
            axios.get(baseUrl)
                .then(response => {
                    this.projects = response.data.map(project => {
                        // 假设后端返回的是图片的文件名，需要拼接路径
                        project.image = require(`@/assets/${project.image}`);
                        return project;
                    });
                })
                .catch(error => {
                    console.error('请求项目数据失败:', error);
                });
        },
        formatCurrency(value) {
            return `$${value.toFixed(2)}`;
        },
        percentage(value_1, value_2) {
            value_1 = value_2 / value_1 * 100;
            if (value_1 > 100){
                value_1 = 100
            }
            return `${value_1.toFixed(0)}`
        },
        navigateToProject(projectId) {
            this.$router.push({ path: `/project/${projectId}` });
        }
    },
    mounted() {
        this.fetchProjects();
    }
}
</script>

<style scoped>
.projects {
    padding: 20px;
    /* 为容器添加内边距 */
    background-color: rgb(245, 245, 245);
    /* 设置背景颜色为白色 */
}

.project-container {
    display: flex;
    flex-wrap: wrap;
    gap: 50px;
    margin-left: 100px;
    margin-right: 100px;
    /* 控制卡片间的间隔 */
}


.project-card {
    height: 300px;
    margin-bottom: 10px;
    /* 设置卡片的高度为 250px */
    flex: 0 1 200px;
    /* 卡片基础宽度为 200px，允许灵活缩放 */
    /* border: 1px solid #7FC1BE; /* 浅青绿色边框 */
    background-color: white;
    box-shadow: 0 2px 4px rgba(49, 47, 47, 0.2);
    border-radius: 10px;
    /* 轻微的圆角效果 */
    font-weight: bold;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* 水平居中所有子元素 */
    justify-content: space-around;
    /* 垂直方向的均匀分布 */
    position: relative;
}

.card-content {
    /* box-shadow: none; */
    border-radius: 8px;
    background-color: #ffffff;
    padding-top: 20px;
    padding-bottom: 20px;
    padding-left: 10px;
    padding-right: 10px;
}

.project-image {
    padding-top: 5px;
    height: 140px;
    /* 图片宽度填满卡片 */
    width: auto;
    /* 图片高度自适应 */
    margin-bottom: 15px;
}

.project-funds {
    display: flex;
    justify-content: space-between;
    padding: 5px;
}

.fund-target_amount,
.fund-current_amount {
    text-align: center;
    color: #7FC1BE;
    /* 浅青绿色 */
    font-size: smaller;
    padding-left: 5px;
    padding-right: 5px;
    font-weight: bold;
}

.project-funds-title {
    display: flex;
    justify-content: space-between;
    padding-top: 10px;
    padding-left: 20px;
    padding-right: 10px;
}

.fund-target_amount-title,
.fund-current_amount-title {
    text-align: center;
    color: black;
    font-weight: 500;
    font-size: smaller;
}

.el-progress--circle {
    align-self: center;
    margin-left: 40%;
}


.label-container {
    position: absolute;
    right: 10px;
    top: 275px;
    display: flex;
    flex-wrap: wrap;
    /* 允许内容换行 */
    align-items: center;
}

.tag {
    margin: 2px;
    /* 小间距使得标签不紧挨 */
    padding: 3px 8px;
    border-radius: 5px;
    font-size: 10px;
    color: white;
    /* 白色文字 */
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    /* 轻微的阴影效果 */
}

.clearfix {
    margin-bottom: 5px;
}

.progress {
    border-radius: 5px;
}

.progress-container {
    width: 100%; /* 进度条的总宽度 */
    background-color: #e5e5e5; /* 进度条的背景颜色 */
    border-radius: 15px; /* 如果你喜欢圆角可以设置这个值 */
    height: 12px; /* 进度条的高度 */
}

.progress-bar {
    height: 100%; /* 进度条的高度 */
    background-color: #4caf50; /* 进度条的颜色 */
    border-radius: 15px; /* 圆角 */
    text-align: right; /* 文本对齐 */
    color: white; /* 文本颜色 */
    line-height: 20px; /* 行高与进度条高度相同，使文字垂直居中 */
    padding-right: 5px; /* 文本与进度条右边界的距离 */
}

</style>
