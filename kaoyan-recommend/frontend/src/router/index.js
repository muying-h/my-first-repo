import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileForm from '../views/ProfileForm.vue'
import ResultView from '../views/ResultView.vue'
import UniversityList from '../views/UniversityList.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/profile', component: ProfileForm },
  { path: '/result/:profileId', component: ResultView },
  { path: '/universities', component: UniversityList },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})