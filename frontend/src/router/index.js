import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

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
		name: 'FinEd',
		path: '/story1',
		component: () => import('@/views/FinEd.vue'),
		meta: { imageSrc: '/previews/fined.png' }
	},
	{
		name: 'Colab',
		path: '/story2',
		component: () => import('@/views/Colab.vue'),
		meta: { imageSrc: '/previews/colab.png' }
	},
	{
		name: 'Offer',
		path: '/story3',
		component: () => import('@/views/Offer.vue'),
		meta: { imageSrc: '/previews/offer.png' }
	},
	{
		name: 'News',
		path: '/story4',
		component: () => import('@/views/News.vue'),
		meta: { imageSrc: '/previews/news.png' }
	},
]

const router = createRouter({
		history: createWebHistory(process.env.BASE_URL),
		routes
	})

export default router
