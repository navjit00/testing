<template>
	 <main class="flex justify-between gap-3 mt-3">
		<template v-for="(service, x) in services" :key="x">
			<IconMenu :source="service" />
		</template>
	</main>
</template>

<script setup>

import IconMenu from '@/components/IconMenu.vue'

const services = [
	{
		name: 'Story1',
		to: 'Deposit'
	},
	{
		name: 'Story2',
		to: 'Transfer'
	},
	{
		name: 'Story3',
		to: 'WithDraw'
	},
	{
		name: 'Story4',
		to: 'ChangePoint'
	}
]

</script>
