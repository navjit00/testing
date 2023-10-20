<template>
  <div class="user-input">
    <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type your message..." />
  </div>
</template>

<script setup>
import { ref } from 'vue';

const userMessage = ref('');

const sendMessage = () => {
  // Handle user message input here
};
</script>
