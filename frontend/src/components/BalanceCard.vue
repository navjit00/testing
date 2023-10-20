<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

h1 {
    @apply text-base font-semibold m-0 text-white truncate; /* Keeping the modifications */
}

.transaction-icon {
    @apply text-base cursor-pointer hover:text-gray-500 text-white mr-2; /* Changed the hover color for a more subtle effect */
}

main {
    @apply font-inter w-full h-10 bg-gradient-to-r from-green-300 to-green-700 shadow-lg ring-4 ring-green-500 px-3 flex items-center justify-between rounded-full; /* Enhanced gradient, added shadow for depth, increased height slightly, and made it fully rounded */
}
</style>



<template>
	<main>
		<h1>{{ animatedBalance }} €</h1>
		<i class="fas fa-list-ul transaction-icon" title="Transaction History"></i>
	</main>
</template>


<script setup>

import { ref, onMounted, computed } from 'vue'
import { useBalance } from '@/stores/balance'

const balance = useBalance()
const currentBalance = computed(() => balance.current)

const animatedBalance = ref(0)

onMounted(() => {
    let startBalance = 0;
    const endBalance = parseFloat(currentBalance.value);
    const step = endBalance / 50;  // Reduced steps for faster animation
    
    const updateBalance = () => {
        startBalance += step;
        if (startBalance < endBalance) {
            animatedBalance.value = startBalance.toFixed(2);
            requestAnimationFrame(updateBalance);
        } else {
            animatedBalance.value = endBalance.toFixed(2);
        }
    };

    updateBalance();
});

</script>
