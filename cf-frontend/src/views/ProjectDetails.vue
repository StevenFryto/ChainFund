<template>
    <div>
        <div class="project-details" v-if="project">
            <div class="detail-card" v-show="showDetailCard">
                <div class="title">{{ project.title }}</div>
                <div class="time-cards">
                    <div class="time-card" shadow="hover">发布时间：{{ project.create_time }}</div>
                    <div class="owner-card" @mouseover="handleMouseEnter" @mouseleave="handleMouseLeave">   
                        <template v-if="showDetails">
                            <div class="owner-details">
                                <div>
                                    <p><b>担保人信息</b></p>
                                    <p>姓名：{{ project.surety_info.name }}</p>
                                    <p>身份证号：{{ project.surety_info.id_card }}</p>
                                    <p>联系方式：{{ project.surety_info.phone }}</p>
                                </div>
                            </div>
                        </template>
                        <template v-else>
                            <div class="patient-info">
                                {{ project.patient_name }} ({{ project.patient_gender }}, {{ project.patient_birth }} 岁)
                                &nbsp;&nbsp;&nbsp; {{ project.patient_occupation
                                }}
                            </div>
                        </template>
                    </div>
                    <div class="time-card" shadow="hover">截止时间：{{ project.deadline }}</div>
                </div>
                <div class="funding-cards">
                    <div class="money-card" shadow="hover">
                        <p>目标金额: {{ formatCurrency(project.target_amount) }} &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                            已筹得金额: {{
            formatCurrency(project.current_amount) }}</p>
                    </div>
                </div>

                <div class="project-images">
                    <img v-for="(img, index) in project.photos" :key="index" :src="img.src" alt="Project Image"
                        class="project-image" />
                </div>
                <div class="project-description">{{ project.description }}</div>

                <!-- 捐款按钮 -->
                <button @click="openDonationDialog">进行捐款</button>

                <div class="tags">
                    <div v-for="(tag, index) in project.label" :key="index" class="tag"
                        :style="{ backgroundColor: colors[index % colors.length] }" shadow="hover">
                        #&nbsp;{{ tag }}
                    </div>
                </div>
            </div>

            <div>
                <el-dialog v-model="donationDialogVisible" title="捐款" width="550" @close="resetDonationDialog">
                    <el-dialog v-model="innerVisible" width="400" append-to-body>
                        <span>确认捐款吗？（不可申请退款）</span>
                        <div class="inner-buttons">
                            <el-button class="inner-dialog-button" @click="notConfirmed" type="danger">取消</el-button>
                            <el-button class="inner-dialog-button" @click="isConfirmed" type="primary">确认</el-button>
                        </div>
                    </el-dialog>
                    <el-form v-model="donationAmount">
                        <div class="amount-indicator">
                            <div v-for="(digit, index) in amountDigits" :key="index" class="digit-container">
                                <div class="digit">{{ digit }}</div>
                                <div class="label">{{ digitLabels[index] }}</div>
                            </div>
                        </div>
                        <el-form-item label="金额">
                            <el-input v-model="donationAmount" @input="checkInput" :min="1" :max="100000" placeholder="输入捐款金额"
                                type="number">
                                <template #append>RMB 元/￥</template>
                            </el-input>
                        </el-form-item>
                        <div class="tips-money">
                            <div v-for="tip in commonAmounts" :key="tip" class="tip-money"
                                @click="setDonationAmount(tip)">{{ tip }}
                            </div>
                        </div>
                        <el-form-item label="留言">
                            <el-input v-model="donationMessage" placeholder="您的留言（可选）" maxlength="100" show-word-limit
                                type="textarea" />
                        </el-form-item>
                        <div class="tips-message">
                            <div v-for="tip in commonMessages" :key="tip" class="tip-message"
                                @click="setDonationMessage(tip)">{{ tip }}</div>
                        </div>
                    </el-form>
                    <div class="quote-container">
                        <div class="quote"><span class="italic">人并非为获取而给予；给予本身即是无与伦比的欢乐。</span></div>
                        <div class="author">—— <span class="italic">弗罗姆</span></div>
                    </div>
                    <template #footer>
                        <div class="dialog-footer">
                            <el-button class="dialog-button" @click="donationDialogVisible = false">返回</el-button>
                            <el-button class="dialog-button" type="primary" @click="confirmDonation">捐款</el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog title="感谢您的捐款🙏下面是您本次捐款的区块信息" v-model="blockVisible" width="50%" center>
                    <div class="dialog-content">
                        <p>🟣 区块哈希 (Block Hash): {{ responseData.blockHash }}</p>
                        <p>🟣 区块编号 (Block Number): {{ responseData.blockNumber }}</p>
                        <p>🟣 发起账户 (From): {{ responseData.from }}</p>
                        <p>🟣 接收账户 (To): {{ responseData.to }}</p>
                        <p>🟣 消耗 Gas (Gas Used): {{ responseData.gasUsed }}</p>
                        <p>🟣 剩余 Gas (Remaining Gas): {{ responseData.remainGas }}</p>
                        <p>🟣 根 (Root): {{ responseData.root }}</p>
                        <p>🟣 状态 (Status): {{ responseData.status }}</p>
                        <p>🟣 状态消息 (Status Message): Success</p>
                        <p>🟣 交易哈希 (Transaction Hash): {{ responseData.transactionHash }}</p>
                        <p>🟣 交易索引 (Transaction Index): {{ responseData.transactionIndex }}</p>
                    </div>
                    <template #footer>
                        <el-button type="primary" @click="blockVisible = false">关闭</el-button>
                    </template>
                </el-dialog>
            </div>
        </div>
        <div class="component" v-if="project">
            <div class="bubble-wall">
                <div class="bubble-title"><b>🧱 捐款者泡泡墙</b></div>
                <BubbleWall></BubbleWall>
            </div>
            <div class="message-wall">
                <div class="message-title"><b>🧱 捐款者留言墙</b></div>
                <MessageWall></MessageWall>
            </div>
        </div>
    </div>
</template>


<script>
// import { ElCard, ElDialog, ElButton, ElInput, ElForm, ElFormItem } from 'element-plus';
import { ElDialog, ElButton, ElInput, ElForm, ElFormItem } from 'element-plus';
import axios from 'axios';
// import ProjectFlow from '@/components/ProjectFlow.vue';
import MessageWall from '@/components/MessageWall.vue';
import BubbleWall from '@/components/BubbleWall.vue';

export default {
    components: {
        // ElCard, 
        ElDialog, ElButton, ElInput, ElForm, ElFormItem,
        // ProjectFlow, 
        MessageWall,
        BubbleWall
    },
    data() {
        return {
            project: null,
            showDetailCard: true,
            showDetails: false,
            donationDialogVisible: false,   // 控制弹出框的显示与否
            innerVisible: false,            // 控制确认框的显示与否
            blockVisible: false,            // 控制区块信息是否显示
            donationAmount: 10,             // 默认的捐款金额
            donationMessage: '',            // 捐赠者留言
            timeoutId: null,
            colors: ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', '#FF4500', '#20B2AA'], // 七种不同的颜色
            amountDigits: [0, 0, 0, 0, 0, 0],
            digitLabels: ['十万', '万', '千', '百', '十', '个'],
            commonAmounts: [10, 100, 500, 1000, 9999, 19999],
            commonMessages: [
                '人总会遇到很多无耐的事情，人生总有很多的不得也；未来的路上，还会有无数曲折；此时的你所碰到的挫折，在人生路上真的不算什么？祝早日安康。',
                '惦记，无声，却很甘甜；问候，平常，却很温暖；祝福，遥远，却最贴心；在此送上我衷心的祝福，祝你：早日康复！',
                '东风轻轻吹柳，桃花开了许久，不知见到没有，病毒世间少有，切忌四处游走，留意消毒洗手，病毒莫能长久，闲来挂念吾友，祝愿健康永久！',
            ],
            responseData: {
                blockHash: "0xbc0b40b260e8abacc3e310891b453b2579634c4d2e07154d20027bf516aff8a2",
                blockNumber: "0x2a",
                from: "0x2de5c210370daef452eb610af76c3a293ae1661f",
                to: "0xf2818ae69ef667d120584b981a818b982cd6d7f5",
                gasUsed: "0x44b0a",
                remainGas: "0x0",
                root: "0x6a75181852741c72cd7b954f5483c753f7da3fbf704bf7cb28e240988de5780e",
                status: "0x0",
                statusMsg: "Success",
                transactionHash: "0xce2d5c0d8a0708b68fdcab7cf091184a2bb77e39790580f7876ce3cf4789f329",
                transactionIndex: "0x0"
            },
        };
    },
    methods: {
        fetchProject(id) {
            const baseUrl = 'http://127.0.0.1:5000/getProjectDetails'; // 根据实际后端服务地址调整
            axios.get(`${baseUrl}/${id}`)
                .then(response => {
                    console.log("get project details success!");
                    console.log(response.data);
                    this.project = response.data;

                    // 如果photos是一个JSON字符串，先解析它
                    if (typeof this.project.photos === 'string') {
                        this.project.photos = JSON.parse(this.project.photos);
                    }
                    // 假设返回的photos是一个路径数组，将其转换为可由Vue模板解析的对象数组
                    this.project.photos = this.project.photos.map(photo => {
                        return {
                            // 这里我们使用了动态导入，适用于已知图片放在静态资源文件夹中的情况
                            src: require(`@/assets/projects/${photo}`),
                        };
                    });
                })
                .catch(error => {
                    this.error = error;
                    console.error('请求错误:', error);
                });
        },
        formatCurrency(value) {
            return `$${value.toFixed(2)}`;
        },
        percentage(goal, raised) {
            return (raised / goal) * 100;
        },

        openDonationDialog() {
            // this.showDetailCard = false; // 隐藏detail-card
            this.donationDialogVisible = true; // 打开捐款弹出框
        },
        resetDonationDialog() {
            this.donationAmount = 10; // 重置默认捐款金额
            this.donationMessage = ''; // 重置留言
            this.showDetailCard = true;
            this.donationDialogVisible = false;
            this.amountDigits = [0, 0, 0, 0, 0, 0];
        },
        confirmDonation() {
            // 弹出确认框
            // const userConfirmed = window.confirm('是否确认捐款？');
            this.innerVisible = true;
        },
        isConfirmed() {
            const donationData = {
                user_id: parseInt(this.$route.params.userId),
                project_id: parseInt(this.project.id),
                raised_amount: parseInt(this.donationAmount),
                message: this.donationMessage,
            };
            axios.post('http://127.0.0.1:5000/donate', donationData) // 发送捐款请求
                .then((response) => {
                    // alert(typeof response.data)
                    // console.log(response.data.block);
                    if (response.data.status === true) {
                        this.responseData = response.data.block;
                        const projectId = this.$route.params.id;
                        this.project = this.fetchProject(projectId);
                        this.showDetailCard = true; // 捐款后再次显示detail-card
                        this.innerVisible = false;
                        this.donationDialogVisible = false; // 关闭弹出框
                        this.blockVisible = true;
                    } else {
                        alert("捐款错误，请稍后重试！")
                    }
                })
                .catch((error) => {
                    console.error('捐款失败:', error);
                });
        },
        notConfirmed() {
            this.innerVisible = false;
            this.userConfirmed = false;
        },
        checkInput() {
            if (this.donationAmount === '') {
                this.donationAmount = 0
            }
        },
        setDonationAmount(amount) {
            this.donationAmount = amount.toString();
            this.updateAmountDigits(parseInt(this.donationAmount));
        },
        setDonationMessage(message) {
            this.donationMessage = message;
        },
        updateAmountDigits() {
            const amount = parseInt(this.donationAmount);
            const digits = amount
                .toString()
                .padStart(6, '0')
                .split('')
                .map(digit => parseInt(digit));
            this.amountDigits = digits;
        },
        handleMouseLeave() {
            // 设置延时
            this.timeoutId = setTimeout(() => {
                this.showDetails = false;
            }, 100); // 500毫秒后隐藏，你可以根据需要调整这个时间
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
    },
    watch: {
        donationAmount() {
            this.updateAmountDigits();
        }
    }
}
</script>

<style scoped>
.title {
    font-size: xx-large;
    font-weight: bolder;
    margin-top: 20px;
    margin-bottom: 20px;
    padding-bottom: 20px;

    border-bottom: 1px solid #000;
}

.project-details {
    position: relative;
    /* 添加相对定位 */
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
    margin-left: 18%;
    margin-right: 18%;
    margin-bottom: 10px;
}

.time-card {
    /* border: 1px solid #7FC1BE; */
    border-radius: 5px;
    /* padding: 10px; */
    color: grey;
    font-weight: bold;
    border-radius: 10px;
}

.owner-card {
    margin-bottom: 20px;
    border-radius: 5px;
    position: relative;
    cursor: pointer;
}

.owner-details {
    display: flex;
    justify-content: space-between;
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 5px;
    padding-bottom: 5px;
    background-color: white;
    border: 2px solid #42b983;
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
    justify-content: space-evenly;
    /* 保持图片间有间隔 */
    margin-bottom: 40px;
    margin-top: 40px;
    margin-left: 10%;
    margin-right: 10%;
}

.project-image {
    flex: 0 1 18%;
    height: 200px;
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
    font-size: 12.5px;
    font-weight: 600;
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
    font-size: larger;
    font-weight: bolder;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.component {
    display: flex;
    justify-content: space-between;
    padding-left: 20px;
    padding-right: 20px;
}

.bubble-wall {
    width: 30%;
    height: 500px;
    margin-left: 10%;
    border-radius: 25px;
    background-color: white;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);

    display: flex;
    flex-direction: column;
}

.message-wall {
    width: 49%;
    height: 500px;
    margin-right: 10%;
    border-radius: 25px;
    background-color: white;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);

    display: flex;
    flex-direction: column;
}

.bubble-title {
    font-size: 20px;
    text-align: center;
    margin-top: 20px;
    padding-bottom: 20px;

    border-bottom: 1px solid #000;
}

.message-title {
    font-size: 20px;
    text-align: center;
    margin-bottom: 20px;
    margin-top: 20px;
    padding-bottom: 20px;

    border-bottom: 1px solid #000;
}

.el-dialog {
    /* display: flex; */
    justify-content: center;
    /* display: flex;
    position: fixed; 改为fixed定位 */
    /* top: 50%; 居中显示 */
    /* left: 50%; */
    /* transform: translate(-50%, -50%); 同时垂直和水平居中 */
    /* 确保弹出框宽度适应内容或不超过屏幕宽度 */
    /* 添加阴影和圆角以提升美观 */
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
}

.el-dialog__title {
    font-size: 120px;
    /* 调整标题的字体大小 */
    font-weight: bold;
    /* 设置标题的字体粗细 */
    color: #3498db;
    /* 设置标题的颜色 */
    text-align: center;
    /* 标题居中 */
    padding: 10px;
    /* 增加标题的内边距 */
    background-color: #f5f5f5 !important;
    /* 设置标题背景色 */
}

/* 输入框样式 */
.el-input {
    /* margin: 10px 0; */
    /* 添加上下边距 */
    border-radius: 5px;
    /* 轻微圆角 */
}

/* 名人名言 */
.quote-container {
    width: 90%;
    margin-left: 5%;
    margin-top: 20px;
}

.quote {
    font-size: 16px;
    color: #999;
    text-align: left;
}

.author {
    font-size: 16px;
    color: #999;
    margin-top: 5px;
    text-align: right;
}

.italic {
    font-style: italic;
}

.dialog-footer {
    display: flex;
    justify-content: space-around;
}

.dialog-button {
    width: 80px;
    height: 40px;
    font-size: medium;
}

.inner-buttons {
    display: flex;
    justify-content: space-around;
}

.inner-dialog-button {
    width: 80px;
    height: 40px;
    font-size: medium;
    background-color: #3375b9;
}

.amount-indicator {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 10px;
}

.digit-container {
    width: 80px;
    height: 70px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
    margin-bottom: 30px;
    margin-left: 5px;
    margin-right: 5px;

    background-color: #f5f5f5;
    border-color: black;
    border-style: solid;
    border-width: 1px;

    border-radius: 5px;
}

.digit {
    font-size: 32px;
    font-weight: bold;
    margin-top: 5px;
}

.label {
    font-size: 14px;
    margin-top: 5px;
}

.tips-money,
.tips-message {
    width: 82%;
    display: flex;
    justify-content: left;
    margin-top: 10px;
    margin-left: 8%;
    flex-wrap: wrap;
}

.tips-money {
    margin-bottom: 30px;
}

.tip-money,
.tip-message {
    padding: 5px 10px;
    margin-right: 5px;
    margin-bottom: 5px;
    border-radius: 5px;
    font-size: small;
    color: white;
    /* background-color: #4682b4; */
    background-color: #42b983;

    text-align: left;
    box-shadow: 0 0 1px 1px rgba(255, 255, 255, 0.2);

    cursor: pointer;
}

.dialog-content {
    color: #333;
    width: 80%;
    padding-left: 10%;
}

.dialog-content p {
    margin: 20px 0;
}

.dialog-content p span {
    color: #42b983;
}
</style>