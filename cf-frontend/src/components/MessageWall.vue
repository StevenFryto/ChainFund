<template>
    <vue-danmaku v-model:danmus="danmus" useSlot loop :channels="6" speeds="150"
        style="height:500px; width:100;" >
        <template v-slot:dm="{ danmu }">
            <div class="danmu"><span>{{ danmu.username }}：{{ danmu.message }}</span></div>
        </template>
    </vue-danmaku>
</template>

<script>
import vueDanmaku from 'vue3-danmaku';
import { ref } from 'vue';

// const danmus = ref(['danmu1', 'danmu2', 'danmu3', '...'])
export default {
    components: {
        vueDanmaku,
    },
    data() {
        return {
            danmus: ref([
                { username : '热心市民', message:'礼'},
                { username : '热心市民', message:'老子'},
                { username : '热心市民', message:'孔子云：'},
                { username : '热心市民', message:'何陋之有'},
                { username : '热心市民', message:'谈笑有鸿儒'},
                { username : '热心市民', message:'孔子云：何陋之有？'},
                { username : '热心市民', message:'山不在高，有仙则名'},
                { username : '热心市民', message:'予谓菊，花之隐逸者也'},
                { username : '热心市民', message:'无丝竹之乱耳，无案牍之劳形'},
                { username : '热心市民', message:'崇祯五年十二月，余住西湖'},
                { username : '热心市民', message:'莫说相公痴，更有痴似相公者。'},
                { username : '热心市民', message:'先天下之忧而忧，后天下之乐而乐'},
                { username : '热心市民', message:'是进亦忧，退亦忧。然则何时而乐耶？'},
                { username : '热心市民', message:'居庙堂之高则忧其民，处江湖之远则忧其君。'},
                { username : '热心市民', message:'嗟夫！予尝求古仁人之心，或异二者之为，何哉？'},
                { username : '热心市民', message:'是日更定矣，余拏一小舟，拥毳衣炉火，独往湖心亭看雪'},
                { username : '热心市民', message:'惟长堤一痕、湖心亭一点、与余舟一芥、舟中人两三粒而已。'},
                { username : '热心市民', message:'醉翁之意不在酒，在乎山水之间也。山水之乐，得之心而寓之酒也。'},
                { username : '热心市民', message:'然而禽鸟知山林之乐，而不知人之乐；人知从太守游而乐，而不知太守之乐其乐也。'},
            ]),
        }
    },
    // setup() {
    //     const danmus = ref([
    //         { avatar: 'http://a.com/a.jpg', name: 'a', text: 'aaa' }, 
    //         { avatar: 'http://a.com/b.jpg', name: 'b', text: 'bbb' },
    //         { avatar: 'http://a.com/c.jpg', name: 'c', text: 'ccc' },
    //         { avatar: 'http://a.com/d.jpg', name: 'd', text: 'ddd' },
    //         { avatar: 'http://a.com/e.jpg', name: 'e', text: 'eee' },
    //         { avatar: 'http://a.com/e.jpg', name: 'f', text: 'fff' },
    //         { avatar: 'http://a.com/f.jpg', name: 'g', text: 'ggg' },
    //     ])
    //     return { danmus }
    // },
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