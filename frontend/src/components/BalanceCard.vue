<template>
  <div class="balance-container">
    <span class="balance-amount">1.400,58 €</span>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const balance = ref(1400);
</script>

<style scoped>
.balance-container {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #FBBF24, #FFA726);
  background-size: 200% 200%;
  padding: 20px; 
  border-radius: 30px; 
  animation: shiny 20s infinite linear; 
  box-shadow: 0 0 15px #FBBF24; 
}

@keyframes shiny {
  0% {
    background-position: 100% 0;
  }
  100% {
    background-position: 0 100%;
  }
}

.balance-amount {
  color: #fff;
  font-size: 2.5rem; 
  font-weight: 900;
  text-shadow: 0 0 10px #FFA726;
}
</style>
