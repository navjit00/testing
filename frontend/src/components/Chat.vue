<template>
  <div class="message-list">
    <div v-for="message in messages" :key="message.id" :class="message.sender">
      {{ message.content }}
    </div>
  </div>
</template>

<style scoped>

</style>

<script setup>
import { ref } from 'vue';

const messages = ref([
  { id: 1, content: "Hello!", sender: "ChatGPT" },
  { id: 2, content: "Hi there!", sender: "user" },
]);

// Add logic to receive and display chat messages
</script>
