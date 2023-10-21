<style scoped>

.input-wrapper {
  @apply w-full h-16 flex items-center mb-3 rounded-lg overflow-hidden gap-2;
}

input {
  @apply text-gray-300 active:ring-1 focus:ring-1 ring-green-500 duration-300 rounded-lg w-full bg-secondary h-full px-3 focus:ring-2 active:ring-2 ring-secondary;
}

</style>

<template>
  <main>

    <section class="mt-16 text-gray-300 text-center w-10/12 mx-auto">
      <p style="text-align:right;"><a href="home"> <i class="fa fa-times"></i></a></p>

      <h1 class="font-semibold text-lg">Outgoing</h1>
      <p class="text-sm">Transact funds to people</p>

    </section>

    <section class="mt-5">
      <form @submit.prevent="transact" action="">
        <div class="input-wrapper">
          <input v-model="form.recipient" type="text" placeholder="recipient">
        </div>
        <div class="input-wrapper">
          <input v-model="form.amount" type="number" placeholder="amount in €">
        </div>

        <section>
          <button class="w-full bg-amber-500 font-semibold text-gray-800 py-3 rounded-lg mt-6">
            <LoadAction :isLoad="isLoad" :isSuccess="isSuccess" :isFail="isFail" action="TRANSACT" />

          </button>
          <small class="mt-3 block text-red-600 font-medium">{{ msgErr }}</small>
        </section>
      </form>
    </section>

    <section class="mt-24 text-gray-300">

    </section>
  </main>
</template>

<script setup>

import { ref, reactive } from 'vue'

import { useRouter } from 'vue-router'
import LoadAction from '@/components/LoadAction.vue'


const router = useRouter()

const form = reactive({
  recipient: '',
  amount: ''
})







const transact = () => {

}




</script>




