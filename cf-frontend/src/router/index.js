import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProjectsView from '../views/ProjectsView.vue'
import RaiseView from '../views/RaiseView.vue'
import MineView from '../views/MineView.vue'
import PersonalView from '../views/PersonalView.vue'
import ProjectDetails from '../views/ProjectDetails.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'

const routes = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/:userId',
        children: [
            {
                path: 'home',
                name: 'home',
                component: HomeView
            },
            {
                path: 'projects',
                name: 'projects',
                component: ProjectsView
            },
            {
                path: 'raise',
                name: 'raise',
                component: RaiseView
            },
            {
                path: 'mine',
                name: 'mine',
                component: MineView
            },
            {
                path: 'personal',
                name: 'personal',
                component: PersonalView
            },
            {
                path: 'project/:id',
                name: 'ProjectDetails',
                component: ProjectDetails
            },
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: LoginView
    },
    {
        path: '/register',
        name: 'register',
        component: RegisterView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

// 在 LoginView 和 RegisterView 不显示导航栏
router.beforeEach((to, from, next) => {
    const hideNavRoutes = ['/login', '/register'];

    if (hideNavRoutes.includes(to.path)) {
        document.getElementById('top-bar').style.display = 'none';
    } else {
        document.getElementById('top-bar').style.display = 'block';
    }

    next();
})


export default router