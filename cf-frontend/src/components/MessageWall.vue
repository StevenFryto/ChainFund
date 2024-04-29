<template>
    <vue-danmaku v-model:danmus="danmus" useSlot loop :channels=0 speeds=100 debounce=50 style="height:500px; width:100;">
        <template v-slot:dm="{ danmu }">
            <div class="danmu"><span>{{ danmu.username }}：{{ danmu.message }}</span></div>
        </template>
    </vue-danmaku>
</template>

<script>
import vueDanmaku from 'vue3-danmaku';
import { ref } from 'vue';
import axios from 'axios';

// const danmus = ref(['danmu1', 'danmu2', 'danmu3', '...'])
export default {
    components: {
        vueDanmaku,
    },
    data() {
        return {
            danmus: ref([
                { "username": "且放白鹿", "message": "愿你的每一天都充满阳光" },
                { "username": "红烛", "message": "坚定信心，病魔终将退去，愿你在康复的路上步步为赢🌹" },
                { "username": "皮蛋瘦肉周", "message": "🙏病魔无情，人间有爱。" },
                { "username": "硬撑", "message": "每一个黎明都预示着新的开始，康复的日子即将到来，加油！" },
                { "username": "爱笑的眼睛", "message": "🌹愿你的笑容早日绽放，病魔远离，健康与你同在。" },
                { "username": "Mavericks", "message": "愿你的心中永远有一束阳光，照亮前行的路。" },
                { "username": "青山如故", "message": "坚持就是胜利，你的康复之路虽曲折，但终会抵达健康的彼岸。" },
                { "username": "Lil-Guy", "message": "愿这份微薄之力能为你带去温暖" }, 
                { "username": "雷爆龙", "message": "病魔虽猛，但你的意志更坚❤️" },
                { "username": "小牛走起", "message": "你的勇敢与坚强是我们学习的榜样" },
                { "username": "峰歌", "message": "🙏助你战胜病魔，迎接美好的未来。" },
                { "username": "祝您平安", "message": "每一个微小的进步都是胜利的曙光，你的康复之路正在一步步向前延伸❤️" },
                { "username": "醉挽清风", "message": "病魔只是暂时的困扰，你的康复才是最终的胜利。加油，我们相信你！" },
                { "username": "无双", "message": "🕯️愿你的每一天都充满希望与力量🕯️" },
                { "username": "晴天", "message": "愿你的康复之路充满阳光与希望，早日战胜病魔，重拾健康。" },
                { "username": "拐卖人口处", "message": "你的坚强与勇敢让我们深受鼓舞🌹" },
                { "username": "零落浮华", "message": "愿这份爱心的力量能为你带来康复的希望，加油，我们与你同在。" },
                { "username": "健康之王", "message": "🙏病魔虽猛，但你的意志更坚。" },
                { "username": "库里MVP", "message": "你的康复是我们所有人的期待，愿你在病痛中坚强，早日康复❤️" },
                { "username": "你好我也好", "message": "愿你的心情如春天般明媚，身体快速康复，重获健康与活力。" }
            ]),
        }
    },
    methods: {
        fetchMessages() {
            axios.get(`http://127.0.0.1:5000/getMessage/${this.$route.params.id}`) // 发送捐款请求
                .then((response) => {
                    console.log(response.data.results);
                    // this.danmus.value = response.data.results;
                })
                .catch((error) => {
                    console.error('捐款失败:', error);
                });
        }
    },
    mounted() {
        this.fetchMessages();
    }
}
</script>

<style>
.danmu {
    /* height: 30px; */
    padding: 8px 12px;
    border: 10px;
    border-radius: 20px;
    background-color: green;
    font-size: 16px;
    color: white;
}
</style>