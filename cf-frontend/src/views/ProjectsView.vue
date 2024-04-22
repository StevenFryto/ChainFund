<template>
    <div class="projects">
        <div class="project-container">
            <div class="project-card" shadow="always" v-for="project in projects" :key="project.id" @click="navigateToProject(project.id)">
                <el-card class="card-content">
                    <template #header>
                        <div class="clearfix">{{ project.title }}</div>
                    </template>
                    <img :src="project.image" class="project-image" />
                    <el-progress type="circle" :width="40" :percentage="percentage(project.goal, project.raised)" :stroke-width="7" :text-inside="true" />
                    <div class="project-funds-title">
                        <div class="fund-goal-title">目标金额</div>
                        <div class="fund-goal-title">已筹得金额</div>
                    </div>
                    <div class="project-funds">
                        <div class="fund-goal">{{ formatCurrency(project.goal) }}</div>
                        <div class="fund-raised">{{ formatCurrency(project.raised) }}</div>
                    </div>
                </el-card>
            </div>
        </div>
    </div>
</template>

<script>
// import { ElRow, ElCol, ElCard, ElProgress } from 'element-plus';
import { ElCard, ElProgress } from 'element-plus';

export default {
    name: 'ProjectsView',
    components: {
        //ElRow,
        //ElCol,
        ElCard,
        ElProgress
    },
    data() {
        return {
            projects: [
                {
                    id: 1,
                    title: '帮助山区儿童读书',
                    image: require('@/assets/logo.png'),
                    progress: 45,
                    goal: 10000,
                    raised: 4500
                },
                {
                    id: 2,
                    title: '城市无家可归者援助',
                    image: require('@/assets/logo.png'),
                    progress: 70,
                    goal: 8000,
                    raised: 5600
                },
                {
                    id: 3,
                    title: '清洁海洋行动',
                    image: require('@/assets/logo.png'),
                    progress: 20,
                    goal: 15000,
                    raised: 3000
                },
                {
                    id: 4,
                    title: '帮助山区儿童读书',
                    image: require('@/assets/logo.png'),
                    progress: 45,
                    goal: 10000,
                    raised: 4500
                },
                {
                    id: 5,
                    title: '城市无家可归者援助',
                    image: require('@/assets/logo.png'),
                    progress: 70,
                    goal: 8000,
                    raised: 5600
                },
                {
                    id: 6,
                    title: '清洁海洋行动',
                    image: require('@/assets/logo.png'),
                    progress: 20,
                    goal: 15000,
                    raised: 3000
                },
                {
                    id: 7,
                    title: '帮助山区儿童读书',
                    image: require('@/assets/logo.png'),
                    progress: 45,
                    goal: 10000,
                    raised: 4500
                },
                {
                    id: 8,
                    title: '城市无家可归者援助',
                    image: require('@/assets/logo.png'),
                    progress: 70,
                    goal: 8000,
                    raised: 5600
                },
                {
                    id: 9,
                    title: '清洁海洋行动',
                    image: require('@/assets/logo.png'),
                    progress: 20,
                    goal: 15000,
                    raised: 3000
                }
            ]
        };
    },

    methods: {
        fetchProjects() {
            // Fetch data logic here
        },
        formatCurrency(value) {
            return `$${value.toFixed(2)}`;
        },
        percentage(value_1, value_2) {
            return `${((value_2)/(value_1+value_2))*100}`
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
    height: 250px;
    margin-bottom: 70px;
    /* 设置卡片的高度为 250px */
    flex: 0 1 200px;
    /* 卡片基础宽度为 200px，允许灵活缩放 */
    /* border: 1px solid #7FC1BE; /* 浅青绿色边框 */
    background-color: white;
    /* box-shadow: none; /* 移除阴影 */
    border-radius: 8px;
    /* 轻微的圆角效果 */
    font-weight: bold;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* 水平居中所有子元素 */
    justify-content: space-around;
    /* 垂直方向的均匀分布 */
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
    padding-top: 15px;
    width: 75%;
    /* 图片宽度填满卡片 */
    height: auto;
    /* 图片高度自适应 */
}

.project-funds {
    display: flex;
    justify-content: space-between;
    padding: 10px;
}

.fund-goal,
.fund-raised {
    text-align: center;
    color: #7FC1BE;
    /* 浅青绿色 */
}

.project-funds-title {
    display: flex;
    justify-content: space-between;
    padding-top: 15px;
    padding-left: 20px;
    padding-right: 10px;
}

.fund-goal-title,
.fund-raised-title {
    text-align: center;
    color: black;
    font-weight: 500;
    font-size: smaller;
}

.el-progress--circle {
    align-self: center;
    margin-left: 40%;
}
</style>
