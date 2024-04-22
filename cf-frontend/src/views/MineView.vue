<template>
    <div class="related-projects">
        <div v-for="(project, index) in projects" :key="index" class="project"
            :style="{ backgroundColor: project.raisedAmount >= project.neededAmount ? '#FFC0CB' : '#7ad2ba' }">
            <div class="project-left">
                <img :src="project.image" alt="Project Image" class="project-image">
            </div>
            <div class="project-center">
                <div class="project-title">{{ project.title }}</div>
                <div class="project-description">{{ project.description }}</div>
                <div class="project-tags">
                    <div v-for="(tag, tagIndex) in project.tags" :key="tagIndex" class="tag"
                        :style="{ backgroundColor: tag.color }">{{ tag.name }}</div>
                </div>
            </div>
            <div class="project-right">
                <div class="amount-info">
                    <div class="raised-amount">已筹金额: 
                        <div class="amount-number">${{ project.raisedAmount }}</div>
                    </div>
                    <div class="needed-amount">需要金额: 
                        <div class="amount-number">${{ project.neededAmount }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            projects: [
                {
                    title: '帮助小明战胜白血病，拯救他的生命',
                    description: '小明是一个充满活力的孩子，但他最近被确诊患有白血病。他需要进行长期的治疗和贵重的药物，但是他的家庭无法负担这样高昂的费用。我们希望能够伸出援手，帮助小明度过难关，重新踏上健康的道路。',
                    image: 'https://th.bing.com/th/id/R.222dd6d4f4137e0b00c8fd0b0c2cd000?rik=ER4bVVbu8E%2fw%2bw&riu=http%3a%2f%2fpimg.39.net%2fPictureLib%2fA%2ff80%2fc9%2f20161227%2forg%2f845132.jpg&ehk=XyMzslmAhaTx%2beRn%2bwrWHJbjz7%2bqYRIDPPmWa%2fRKzKs%3d&risl=&pid=ImgRaw&r=0',
                    tags: [
                        { name: '白血病', color: '#ADD8E6' },
                        { name: '儿童', color: '#F08080' },
                        { name: '慢性病管理', color: '#FFD700' },
                        { name: '药物', color: '#ADD8E6' }
                    ],
                    raisedAmount: 5200,
                    neededAmount: 30000
                },
                {
                    title: '支持王大夫治疗肺癌，为他祈福',
                    description: '王大夫是一位敬业的医生，但是最近他被确诊患有晚期肺癌。他需要进行紧急的手术和放疗治疗，但是这些治疗费用非常昂贵。我们希望能够众筹足够的资金，帮助王大夫早日康复，继续为社会做出贡献。',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.a84fbfeb76702e5fe6a7a8741f1fd5db?rik=4EGjYUg7%2fFVFpA&riu=http%3a%2f%2fi2.sinaimg.cn%2fdy%2fc%2f2013-09-07%2f1378492195_X9w3BT.jpg&ehk=3tYMQ%2bJeaKiggvNJpznE6%2f64pdQRykYGFCbLHsEChyg%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1',
                    tags: [
                        { name: '癌症', color: '#FFA07A' },
                        { name: '化疗', color: '#DDA0DD' },
                        { name: '医生', color: '#F08080' }
                    ],
                    raisedAmount: 65000,
                    neededAmount: 50000
                },
                {
                    title: '帮助张阿姨支付心脏手术费用，拯救她的生命',
                    description: '张阿姨是一个善良而坚强的人，但她最近被确诊患有严重的心脏病。她需要进行紧急的心脏手术，但是手术费用非常昂贵，她的家庭无法负担。我们希望能够众筹足够的资金，帮助张阿姨早日康复。',
                    image: 'https://www.wahh.com.cn/Sites_OldFiles/UploadFiles/news/2015/9/201509091540338708.jpg',
                    tags: [
                        { name: '心脏病', color: '#FFA07A' },
                        { name: '手术', color: '#F08080' },
                        { name: '药物费用', color: '#FFD700' },
                    ],
                    raisedAmount: 15000,
                    neededAmount: 20000
                },
                {
                    title: '支持李叔叔抗击脑瘤，为他祈福',
                    description: '李叔叔是我们社区的一位著名人士，但是最近他被确诊患有脑瘤。他需要进行复杂的手术和放疗治疗，但是这些治疗费用非常昂贵。我们希望能够众筹足够的资金，帮助李叔叔战胜疾病，重获健康。',
                    image: 'https://4g.lsznk.com/wzuploads/allimg/170304/6-1F304142212W6.jpg',
                    tags: [
                        { name: '脑瘤', color: '#ADD8E6' },
                        { name: '手术', color: '#FFA07A' },
                        { name: '放疗治疗', color: '#DDA0DD' },
                    ],
                    raisedAmount: 100000,
                    neededAmount: 60000
                }
            ]

        };
    }
};
</script>

<style scoped>
.related-projects {
    width: 70%;
    margin: 0 auto;
}

.project {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
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
    width: 220px;
    height: 220px;

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
    height: 240px;
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
}

.project-right {
    flex: 2;
}

.amount-info {
    height: 220px;
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