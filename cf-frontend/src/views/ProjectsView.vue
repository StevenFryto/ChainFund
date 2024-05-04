<template>
    <div>
        <div class="search-bar-container">
            <button @click="showAllProjects" v-bind:class="{ active: isAllProjectsSelected }"
                class="project-toggle-button">所有项目</button>
            <button @click="showRecommendedProjects" v-bind:class="{ active: isRecommendedSelected }"
                class="project-toggle-button">推荐项目</button>
            <input type="text" v-model="searchQuery" @input="fetchSearchResults" placeholder="搜索相关项目"
                class="search-bar" />
            <button @click="fetchSearchResults" class="search-button">搜索</button>
        </div>

        <div class="dropdown-menu" v-if="searchResults.length">
            <div v-for="result in searchResults" :key="result.id" @click="navigateToProject(result.id)"
                class="dropdown-item">
                {{ result.title }}
            </div>
        </div>
        <div class="projects" v-if="projects">
            <div class="project-container">
                <div class="project-card" shadow="always" v-for="project in projects" :key="project.id"
                    @click="navigateToProject(project.id)">
                    <div class="card-content">
                        <div class="clearfix">{{ project.title }}</div>
                        <img :src="project.image" class="project-image" />
                        <!--<el-progress class="progress" type="line" color="green"
                            :percentage="percentage(project.target_amount, project.current_amount)" :stroke-width="5"
                            :text-inside="true" status="success" />-->
                        <div class="progress-container">
                            <div class="progress-bar"
                                :style="{ width: percentage(project.target_amount, project.current_amount) + '%' }">
                            </div>
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
                    </div>
                    <div class="label-container">
                        <div v-for="(tag, index) in project.label" :key="index" class="tag"
                            :style="{ backgroundColor: colors[(index + project.id) % colors.length] }">
                            # {{ tag }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: 'ProjectsView',
    data() {
        return {
            searchQuery: '',
            searchResults: [],
            projects: null,
            is_search: false,
            isAllProjectsSelected: true,
            isRecommendedSelected: false,
            colors: ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', '#FF4500', '#20B2AA'],
        };
    },

    methods: {
        fetchProjects() {
            const baseUrl = 'http://127.0.0.1:5000/getProjects';  // 确保后端URL正确
            this.is_search = false;
            axios.get(baseUrl)
                .then(response => {
                    this.projects = response.data.map(project => {
                        // 假设后端返回的是图片的文件名，需要拼接路径
                        project.image = require(`@/assets/projects/${project.image}`);
                        return project;
                    });
                })
                .catch(error => {
                    console.error('请求项目数据失败:', error);
                });
        },
        fetchSearchResults() {
            if (!this.searchQuery.trim()) {
                this.searchResults = [];
                return;
            }
            axios.get(`http://localhost:5000/search?query=${encodeURIComponent(this.searchQuery)}`)
                .then(response => {
                    this.searchResults = response.data;
                })
                .catch(error => {
                    console.error('搜索请求失败:', error);
                    this.searchResults = [];
                });
        },
        showSearchResults() {
            this.is_search = true;
            console.log(this.searchResults);
            if (this.searchResults.length != 0) {
                this.projects = this.projects.filter(project =>
                    this.searchResults.some(result => result.id === project.id));
            }
            else this.fetchProjects();
        },

        formatCurrency(value) {
            return `$${value.toFixed(2)}`;
        },
        percentage(value_1, value_2) {
            value_1 = value_2 / value_1 * 100;
            if (value_1 > 100) {
                value_1 = 100
            }
            return `${value_1.toFixed(0)}`
        },
        navigateToProject(projectId) {
            axios.post('http://localhost:5000/record', {
                userId: this.$route.params.userId,
                projectId: projectId
            })
                .catch(error => {
                    console.error('日志记录失败，请查看后端', error);
                });
            this.$router.push({ path: `/${this.$route.params.userId}/project/${projectId}` });
        },
        showAllProjects() {
            this.isAllProjectsSelected = true;
            this.isRecommendedSelected = false;
            this.fetchProjects(); // Fetch all projects again
        },

        showRecommendedProjects() {
            this.isAllProjectsSelected = false;
            this.isRecommendedSelected = true;
            this.fetchInterestedProjects(); // Fetch recommended projects
        },

        fetchInterestedProjects() {
            const userId = this.$route.params.userId; // Assuming user ID is available in the route params
            axios.get(`http://localhost:5000/${userId}/interested_projects`)
                .then(response => {
                    const projectIds = response.data;
                    this.projects = this.projects.filter(project => projectIds.includes(project.id));
                })
                .catch(error => {
                    console.error('请求推荐项目数据失败:', error);
                });
        }
    },
    mounted() {
        this.fetchProjects();
        this.needFetch = false;
        this.showAllProjects();
    }
}
</script>

<style scoped>
.search-bar-container {
    display: flex;
    justify-content: center;
    padding: 20px;
}

.search-bar {
    width: 30%;
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
}

.project-toggle-button {
    padding: 10px 20px;
    margin-right: 5px;
    border: none;
    background-color: white;
    /* Default background */
    color: black;
    border-radius: 20px;
    cursor: pointer;
    font-weight: 700;
}

.active {
    background-color: #ccc;
    /* Active state background */
}

.dropdown-menu {
    position: absolute;
    background-color: white;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    width: 30%;
    left: 53.3%;
    transform: translateX(-50%);
    z-index: 100;
    border-radius: 5px;
}

.dropdown-item {
    padding: 10px;
    cursor: pointer;
    font-size: smaller;
    text-align: left;
    /* 文本左对齐 */
    /* border-bottom: 1px solid #ddd; /* 添加灰色边框 */
    margin: 0;
    /* 移除任何默认边距 */
    box-sizing: border-box;
    /* 确保包括padding和border在内的总宽度和高度 */
}

.dropdown-item:not(:last-child) {
    border-bottom: 1px solid #ddd;
}

.dropdown-item:hover {
    background-color: #f0f0f0;
}

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
    margin-left: 10%;
    margin-right: 100px;
    /* 控制卡片间的间隔 */
}


.project-card {
    height: 300px;
    /* margin-bottom: 10px; */
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
    /* width: auto; */
    width: 200px;
    /* 图片高度自适应 */
    margin-bottom: 15px;
    object-fit: cover;
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
    /* height: 20px;
    width: 40px; */

    margin-left: 2px;
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
    width: 100%;
    /* 进度条的总宽度 */
    background-color: #e5e5e5;
    /* 进度条的背景颜色 */
    border-radius: 15px;
    /* 如果你喜欢圆角可以设置这个值 */
    height: 12px;
    /* 进度条的高度 */
}

.progress-bar {
    height: 100%;
    /* 进度条的高度 */
    background-color: #4caf50;
    /* 进度条的颜色 */
    border-radius: 15px;
    /* 圆角 */
    text-align: right;
    /* 文本对齐 */
    color: white;
    /* 文本颜色 */
    line-height: 20px;
    /* 行高与进度条高度相同，使文字垂直居中 */
    padding-right: 5px;
    /* 文本与进度条右边界的距离 */
}

.project-toggle-button {
    padding: 10px 20px;
    margin-right: 5px;
    border: none;
    background-color: white;
    /* Default background */
    color: black;
    border-radius: 20px;
    cursor: pointer;
    font-weight: 700;
}

.active {
    background-color: #ccc;
    /* Active state background */
}
</style>
