<template>
    <div class="related-projects">
        <div class="published">
            <div class="title">🔴 <b>您发布的项目</b></div>
            <div v-if="publishedProjects.length == 0" class="no-project">未查询到数据，点击👉发起众筹👈试试吧！</div>
            <div v-for="(project, index) in publishedProjects" :key="index" class="project"
                :style="{ backgroundColor: project.current_amount < project.target_amount ? '#FFC0CB' : '#7ad2ba' }">
                <div class="project-left">
                    <img :src="project.photos" alt="Project Image" class="project-image">
                </div>
                <div class="project-center">
                    <div class="project-title">{{ project.title }}</div>
                    <div class="project-description">{{ project.description }}</div>
                    <div class="project-tags">
                        <div v-for="(tag, tagIndex) in project.label.split(',')" :key="tagIndex" class="tag"
                            :style="{ backgroundColor: getRandomColor() }">{{ tag }}</div>
                    </div>
                </div>
                <div class="project-right">
                    <div class="amount-info">
                        <div class="raised-amount">已筹金额:
                            <div class="amount-number">${{ project.current_amount }}</div>
                        </div>
                        <div class="needed-amount">需要金额:
                            <div class="amount-number">${{ project.target_amount }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="raiseded">
            <div class="title">🟢 <b>您参与的项目</b></div>
            <div v-if="raisedProjects.length == 0" class="no-project">未查询到数据，点击👉项目广场👈看看吧！</div>
            <div v-for="(project, index) in raisedProjects" :key="index" class="project"
                :style="{ backgroundColor: project.current_amount >= project.target_amount ? '#FFC0CB' : '#7ad2ba' }">
                <div class="project-left">
                    <img :src="project.photos" alt="Project Image" class="project-image">
                </div>
                <div class="project-center">
                    <div class="project-title">{{ project.title }}</div>
                    <div class="project-description">{{ project.description }}</div>
                    <div class="project-tags">
                        <div v-for="(tag, tagIndex) in project.label.split(',')" :key="tagIndex" class="tag"
                            :style="{ backgroundColor: getRandomColor() }">{{ tag }}</div>
                    </div>
                </div>
                <div class="project-right">
                    <div class="amount-info">
                        <div class="raised-amount">已筹金额:
                            <div class="amount-number">${{ project.current_amount }}</div>
                        </div>
                        <div class="needed-amount">需要金额:
                            <div class="amount-number">${{ project.target_amount }}</div>
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
    data() {
        return {
            publishedProjects: [],
            raisedProjects: [],
        };
    },
    created() {
        this.fetchPublishedProjects();
        this.fetchRaisedProjects();
    },
    methods: {        
        async fetchPublishedProjects() {
            const currentUserId = this.$route.params.userId;
            try {
                const response = await axios.get(`http://localhost:5000/my_published_projects?id=${currentUserId}`);
                this.publishedProjects = response.data.projects;
                this.publishedProjects.forEach(project => {
                    project.photos = require(`@/assets/projects/${JSON.parse(project.photos)[0]}`)
                    
                    // console.log(typeof parseInt(project.current_amount));
                    project.current_amount = parseInt(project.current_amount);
                    project.target_amount = parseInt(project.target_amount);
                })
            } catch (error) {
                console.error('Error fetching projects:', error);
            }
        },
        async fetchRaisedProjects() {
            const currentUserId = this.$route.params.userId;
            try {
                const response = await axios.get(`http://localhost:5000/my_raised_projects?id=${currentUserId}`);
                this.raisedProjects = response.data.projects;
                this.raisedProjects.forEach(project => {
                    project.photos = require(`@/assets/projects/${JSON.parse(project.photos)[0]}`)
                    
                    // console.log(typeof parseInt(project.current_amount));
                    project.current_amount = parseInt(project.current_amount);
                    project.target_amount = parseInt(project.target_amount);
                })
            } catch (error) {
                console.error('Error fetching projects:', error);
            }
        },
        getRandomColor() {
            const colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', '#FF4500', '#20B2AA'];
            const randomIndex = Math.floor(Math.random() * colors.length);
            return colors[randomIndex];
            // return '#' + Math.floor(Math.random() * 16777215).toString(16);
        }
    }
};
</script>

<style scoped>
.no-project {
    font-size: x-large;
}

.related-projects {
    width: 70%;
    margin: 0 auto;
}

.title {
    text-align: left;
    margin-top: 3%;
    margin-bottom: 3%;
    font-size: large;
}

.project {
    display: flex;
    align-items: center;
    margin-bottom: 25px;
    border-radius: 10px;

    transition: transform 0.5s ease;
}

.project:hover {
    transform: scale(1.01);
}

.project-left {
    flex: 2;
}

.project-image {
    width: 210px;
    height: 200px;

    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    margin-top: 10px;
    /* margin-left: 10px; */
    margin-bottom: 8px;

    object-fit: cover;
}

.project-center {
    flex: 5;
    height: 200px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.project-title {
    font-size: 20px;
    font-weight: bold;
    text-align: left;
    /* 文字左对齐 */
}

.project-description {
    margin-top: 5px;
    margin-bottom: 10px;
    text-align: left;
}

.project-tags {
    display: flex;
    flex-wrap: wrap;
}

.tag {
    padding: 5px 10px;
    margin-right: 5px;
    margin-bottom: 5px;
    border-radius: 5px;
    font-size: small;

    box-shadow: 0 0 1px 1px rgba(255, 255, 255, 0.2);
}

.project-right {
    flex: 2;
}

.amount-info {
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 10px;
}

.raised-amount {
    margin-bottom: 20px;
}

.amount-number {
    margin-top: 5px;
    font-size: larger;
    font-weight: bold;
}
</style>