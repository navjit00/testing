<template>
  <div class="message-list">
    <div v-for="message in messages" :key="message.id" :class="message.sender">
      {{ message.content }}
    </div>
    <div class="input-container">
      <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<style scoped>
.message-list {
  color: aliceblue;
  @apply w-full h-full flex flex-col gap-2;
}

.input-container {
  @apply flex items-center gap-2;
  margin-top: 10px;
}

input {
  @apply w-full rounded-md p-2;
  border: 1px solid #ccc;
  outline: none;
}

button {
  @apply px-4 py-2 bg-blue-500 text-white rounded-md cursor-pointer;
  border: none;
  outline: none;
}
</style>

<script setup>
import { ref } from 'vue';

const messages = ref([
  { id: 1, content: "Hello!", sender: "ChatGPT" },
  { id: 2, content: "Hi there!", sender: "user" },
]);

const newMessage = ref('');

function sendMessage() {
  if (newMessage.value.trim() !== '') {
    messages.value.push({ id: messages.value.length + 1, content: newMessage.value, sender: "user" });
    newMessage.value = ''; // Clear the input field after sending
  }
}
</script>
