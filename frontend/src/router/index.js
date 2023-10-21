import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
//import { useSession } from '@/stores/session'
//import { computed } from 'vue'

const routes = [
	{
		name: 'Home',
		path: '/home',
		component: Home
	},
	{
		name: 'Login',
		path: '/',
		component: () => import('@/views/Login.vue')
	},
	{
		name: 'Deposit',
		path: '/story1',
		component: () => import('@/views/Deposit.vue')
	},
	{
		name: 'ChangePoint',
		path: '/story4',
		component: () => import('@/views/ChangePoint.vue')
	}
]

const router = createRouter({
		history: createWebHistory(process.env.BASE_URL),
		routes
	})

/*Nav guard
const session = useSession()
const isAuthenticated = computed(() => session.login)

router.beforeEach((to, next) => {
	console.log(isAuthenticated.value)
})*/

export default router
