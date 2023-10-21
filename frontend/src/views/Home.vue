<style scoped>

.title {
  @apply font-semibold text-amber-400 text-lg;
}

.chatbox::-webkit-scrollbar {
  width: 1vw;
  height: 1vh;
}

.chatbox::-webkit-scrollbar-track {
  background-color: #e0e0e0;
  border-radius: 0.4vw;
}

.chatbox::-webkit-scrollbar-thumb {
  background-color: #FFCA28;
  border-radius: 0.4vw;
}

.chatbox::-webkit-scrollbar-thumb:hover {
  background-color: #D1A120;
}

.chatbox {
  margin-top: 5vh;
  border: 0.5px solid #e0e0e0;
  padding: 10px;
  height: 55vh;
  overflow-y: auto;
  border-radius: 0.5vw;
}
.chat-interface {
  display: flex;
  align-items: stretch;
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
  background-color: #FFCA28;
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
.received-image {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
}

.bot-message {
  background-color: #FFCA28;
}

.list-enter-active,
.list-leave-active {
  transition: opacity 0.6s;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
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
	<main class="pt-1">
    <HeaderHome/>
    <section class="mt-0">
      <Services />
    </section>
    <div class="bg-amber-400 h-[1px]"></div>
    <BalanceCard />
    <section>
      <div class="chatbox" ref="chatbox">
        <TransitionGroup name="list" tag="div">
          <div v-for="msg in messages" :key="msg.id" class="message" :class="msg.type">
            <div v-if="msg.text">{{ msg.text }}</div>
            <img v-if="msg.image" :src="msg.image" alt="Received Image" class="received-image">
          </div>
        </TransitionGroup>
      </div>
      <div class="chat-interface">
        <input v-model="userInput" class="chat-input" type="text" placeholder="Send a message" @keyup.enter="sendMessage" />
        <button class="send-button" @click="sendMessage"><i class="fas fa-paper-plane"></i></button>
      </div>
    </section>

	</main>
</template>	

<script setup>

import { ref, onMounted } from 'vue';
import HeaderHome from '@/components/HeaderHome.vue'
import BalanceCard from '@/components/BalanceCard.vue'
import axios from 'axios';
import Services from "@/components/Stories.vue";

const userInput = ref("");
const messages = ref([]);

async function sendMessage() {
  if (userInput.value.trim() !== "") {
    const userMessage = {
      id: Date.now(),
      type: "user-message",
      text: userInput.value,
      image: null,
    };

    messages.value.push(userMessage);

    userInput.value = "";

    if (userMessage.text.toLowerCase() === "show me an image") {
      messages.value.push({
        id: Date.now() + 1,
        type: "bot-message",
        text: "Here is an image:\n",
        image: "https://picsum.photos/400/300"
      });
    } else {
      try {
        const response = await axios.post('http://127.0.0.1:5001/message', { userMessage: userMessage.text });
        const apiResponse = response.data;

        if (apiResponse.type === "image") {
          messages.value.push({
            id: Date.now() + 1,
            type: "bot-message",
            text: "",
            image: apiResponse.data
          });
        } else {
          messages.value.push({
            id: Date.now() + 1,
            type: "bot-message",
            text: apiResponse.botReply
          });
        }
      } catch (error) {
        messages.value.push({
          id: Date.now() + 1,
          type: "bot-message",
          text: "Unable to connect to the server."
        });
      }
    }
  }
}
onMounted(async () => {
  try {
    // Attempt to delete all messages from the database
    await axios.delete('http://127.0.0.1:5001/delete-messages');
  } catch (error) {
    console.error("Failed to delete messages:", error);
  }

  // Push the initial bot message
  messages.value.push({
    id: Date.now(),
    type: "bot-message",
    text: "Hello John! How can I help you today?"
  });

  // Scroll to the bottom of the chatbox
  scrollToBottom();
});

</script>
