<template>
    <nav id="top-bar">
        <div class="nav">
            <div class="nav-item" :class="{ 'active': $route.path === `/${userId}/home` }">
                <router-link :to="`/${userId}/home`">ChainFund主页</router-link>
            </div>
            <div class="nav-item" :class="{ 'active': $route.path === `/${userId}/projects` }">
                <router-link :to="`/${userId}/projects`">项目广场</router-link>
            </div>
            <div class="nav-item" id="raise" :class="{ 'active': $route.path === `/${userId}/raise` }">
                <router-link :to="`/${userId}/raise`">发起众筹</router-link>
            </div>
            <div class="nav-item" :class="{ 'active': $route.path === `/${userId}/mine` }">
                <router-link :to="`/${userId}/mine`">我的项目</router-link>
            </div>
            <div class="nav-item" :class="{ 'active': $route.path === `/${userId}/personal` }">
                <router-link :to="`/${userId}/personal`">个人主页</router-link>
            </div>
        </div>
    </nav>

    <router-view></router-view>
</template>

<script>
export default {
    computed: {
        userId() {
            return this.$route.params.userId; // 获取当前用户 ID
        }
    }
}
</script>

<style lang="scss">
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

body {
    background-color: rgb(245, 245, 245);
}

nav {
    padding: 20px;

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 60%;
        margin: 0 auto;
    }

    .nav-item {
        padding: 10px;
        transition: background-color 0.1s ease;
        border-radius: 10px;

        width: 200px;
        height: 30px;

        display: flex;
        align-items: center;
        justify-content: center
    }

    .nav-item:hover {
        background-color: #7ad2ba;
        box-shadow: 0 0 10px 5px rgba(0, 0, 0, 0.2);
    }

    .nav-item.active {
        background-color: #42b983;
        box-shadow: 0 0 10px 5px rgba(0, 0, 0, 0.2);
    }

    a {
        font-weight: bold;
        font-size: 20px;
        color: #2c3e50;
        text-align: center;
        text-decoration: none;

        display: inline-block;
        line-height: 100%;
        // &.router-link-exact-active {
        //     color: #42b983;
        // }
    }
}
</style>
