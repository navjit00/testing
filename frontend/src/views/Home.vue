<style scoped>
.title {
  @apply font-semibold text-success text-lg;
  @apply font-semibold text-success text-lg;
}
.chatbox {
  border: 1px solid #e0e0e0;
  padding: 10px;
  height: 400px;
  overflow-y: auto;
  border-radius: 15px;
}
.chat-interface {
  display: flex;
  align-items: center;
  margin-top: 10px;
}
.chat-input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 30px 0 0 30px;
}
.send-button {
  padding: 10px;
  border: none;
  background-color: rgb(0, 203, 146);
  color: white;
  border-radius: 0 30px 30px 0;
  cursor: pointer;
  font-size: 18px;
  transition: transform 0.2s;
}
.send-button:hover {
  transform: scale(1.1);
}
.message {
  margin: 10px;
  padding: 8px;
  border-radius: 10px;
  animation: fadeIn 0.6s;
}
.user-message {
  background-color: #e0e0e0;
  align-self: flex-end;
}
.bot-message {
  background-color: #d2ffd6;
}
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>

<template>
	<main class="pt-20">
		<HeaderHome />
		<BalanceCard />
    <section>
      <h1 class="title">Chatbot</h1>
      <div class="chatbox" ref="chatbox">
        <div v-for="msg in messages" :key="msg.id" class="message" :class="msg.type">{{ msg.text }}</div>
      </div>
      <div class="chat-interface">
        <input v-model="userInput" class="chat-input" type="text" placeholder="Type your message..." @keyup.enter="sendMessage" />
        <button class="send-button" @click="sendMessage"><i class="fas fa-paper-plane"></i></button>
      </div>
    </section>

	</main>
</template>	

<script setup>

import { ref, onMounted } from 'vue';
import HeaderHome from '@/components/HeaderHome.vue'
import BalanceCard from '@/components/BalanceCard.vue'

const userInput = ref("");
const messages = ref([]);
onMounted(() => {
  messages.value.push({
    id: Date.now(),
    type: "bot-message",
    text: "Hello there! How can I help you today?"
  });
  setTimeout(() => {
    const chatbox = document.querySelector(".chatbox");
    chatbox.scrollTop = chatbox.scrollHeight;
  }, 0);
});
function sendMessage() {
  if (userInput.value.trim() !== "") {
    messages.value.push({
      id: Date.now(),
      type: "user-message",
      text: userInput.value
    });
    userInput.value = "";
    setTimeout(() => {
      messages.value.push({
        id: Date.now() + 1,
        type: "bot-message",
        text: "Thank you for your message. I'll respond soon!"
      });
    }, 500);
  }
}

</script>
