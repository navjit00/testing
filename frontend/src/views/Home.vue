<style scoped>

.title {
	@apply font-semibold text-success text-lg;
}

</style>

<template>
	<main class="pt-20">
		<HeaderHome />
		<BalanceCard />
		<section class="mt-12">
			<h1 class="title">Layanan</h1>
			<Services />
		</section>
    <Chat />

	</main>
</template>	

<script setup>

import HeaderHome from '@/components/HeaderHome.vue'
import BalanceCard from '@/components/BalanceCard.vue'
import Services from '@/components/Services.vue'
import Chat from '@/components/Chat.vue'


</script>
