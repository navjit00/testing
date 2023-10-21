<style scoped>

h1 {
  align-content: center;
  @apply text-xl font-semibold block my-2;
  margin-top: 1px;
}

#header1{
  margin-top:-2vh;
}

#header2{
  align-content: center;
}

#div1{
  position: relative;
  width: 70%;
  height: 10vh;
  background-color: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 5px 5px 5px 0px rgba(255, 255, 255, 0.75);
}

.left-bottom-circle {
  left: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.right-bottom-circle {
  right: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

section {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center the items vertically */
  justify-content: center; /* Center the items horizontally */
}
</style>

<template>
  <div id="div1" class="w-full mx-auto bg-amber-400 ring-0 ring-amber-600 px-1 py-5 rounded-t-xl flex gap-4 items-start justify-evenly">
    <div class="left-bottom-circle">



    </div>
    <div class="right-bottom-circle">

    </div>
    <section>
      <h1 id="header2" style="font-size:30px;">1400,00 €</h1>
    </section>
  </div>
</template>

<script setup>

import { computed } from 'vue'
import { useBalance } from '@/stores/balance'

const balance = useBalance()
const balances = computed(() => balance)

</script>