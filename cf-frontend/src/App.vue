<template>
    <nav id="top-bar">
        <div class="nav">
            <div class="nav-item" :class="{ 'active': $route.path === '/home' }">
                <router-link to="/home">ChainFund主页</router-link>
            </div>
            <div class="nav-item" :class="{ 'active': $route.path === '/projects' }">
                <router-link to="/projects">项目广场</router-link>
            </div>
            <div class="nav-item" id="raise" :class="{ 'active': $route.path === '/raise' }">
                <router-link to="/raise">发起众筹</router-link>
            </div>
            <div class="nav-item" :class="{ 'active': $route.path === '/mine' }">
                <router-link to="/mine">我的项目</router-link>
            </div>
            <div class="nav-item" :class="{ 'active': $route.path === '/personal' }">
                <router-link to="/personal">个人主页</router-link>
            </div>
        </div>
    </nav>
    
    <router-view></router-view>
</template>

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
        font-size: larger;
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

// #raise {
//     font-size: large;
// }</style>
