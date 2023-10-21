<template>
  <div id="div1" class="mx-auto bg-amber-400 ring-0 ring-amber-600 px-1 py-5 rounded-t-xl flex items-center justify-center relative">
    <div class="left-bottom-circle icon-background">
    </div>
    <section>
      <h1 id="header2" class="text-4xl font-semibold my-2 text-center">1,400.00 €</h1>
    </section>
    <div class="right-bottom-circle icon-background">
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useBalance } from '@/stores/balance';

const balance = useBalance();
const balances = computed(() => balance.value);
</script>

<style scoped>
#div1 {
  position: relative;
  width: 70%;
  height: 10vh;
  background-color: #f2f2f2;
  box-shadow: 5px 5px 5px 0px rgba(255, 255, 255, 0.75);
}

.left-bottom-circle, .right-bottom-circle {
  position: absolute;
  width: 40px;
  height: 40px;
}


.left-bottom-circle {
  bottom: 10px;
  left: 10px;
}

.right-bottom-circle {
  bottom: 10px;
  right: 10px;
}

section {
  flex: 1;
}
</style>
