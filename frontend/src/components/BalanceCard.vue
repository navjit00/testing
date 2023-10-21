<template>
  <div class="balance-container">
    <div class="currency-symbol-container">
      <span class="currency-symbol">€</span>
    </div>
    <span class="balance-amount">{{ formattedBalance }}&#160€</span>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const balance = ref(1400);
const formattedBalance = computed(() => {
  let balanceParts = balance.value.toFixed(2).split(".");
  let formatted = `${balanceParts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ")},${balanceParts[1]}`;
  return formatted;
});
</script>

<style scoped>
.balance-container {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #FBBF24;
  padding: 12px 12px;
  border-radius: 20px;
}

.currency-symbol-container {
  background-color: white;
  border-radius: 50%;
  width: calc((5vw + 5vh) / 2);
  height: calc((5vw + 5vh) / 2);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 3vw;
}

.currency-symbol {
  color: #FBBF24;
  font-size: 2em;
  font-weight: bold;
}

.balance-amount {
  margin-top: 1vh;
  color: black;
  font-size: 1.5rem;
  font-weight: bold;
  margin-right: 15vw;
}
</style>
