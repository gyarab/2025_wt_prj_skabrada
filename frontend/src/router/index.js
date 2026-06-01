import { createRouter, createWebHistory } from 'vue-router'
import ColorList from '../views/ColorList.vue'
import ColorDetail from '../views/ColorDetail.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: ColorList},
        { path: '/movie/:id', name: 'movie-detail', component: ColorDetail}
    ]
})

export default router