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
import Services from "@/components/Services.vue";
import ChartComponent from "@/components/ChartComponent.vue";
import LineChartComponent from '@/components/LineChartComponent.vue';

const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
const baseURL = import.meta.env.VUE_APP_API_BASE_URL || `http://127.0.0.1:${isMac ? '5001' : '5000'}`;
console.log(baseURL);
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

    const lowerCaseText = userInput.value.toLowerCase();
    userInput.value = "";

    // Special frontend handlers
    if (lowerCaseText === "show me a graph" || lowerCaseText === "show me a line chart" || lowerCaseText === "show me an image") {
      // Existing special frontend handling code remains unchanged
      // ...
      if (lowerCaseText === "show me a graph") {
      messages.value.push({
        id: Date.now() + 1,
        type: "bar-chart",  // Assuming you have a bar chart component
        data: {
          labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
          datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
          }]
        }
      });
    } 
    else if (lowerCaseText === "show me a line chart") {
  messages.value.push({
    id: Date.now() + 1,
    type: "line-chart",
    data: {
      labels: ['January', 'February', 'March', 'April', 'May'],
      datasets: [
        {
          label: 'Monthly Expenses',
          data: [-15, -25, -35, -20, -30],
          fill: false,
          borderColor: 'rgb(255, 99, 132)',
          tension: 0.1
        },
        {
          label: 'Monthly Profits',
          data: [10, 20, 30, 40, 50],
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        },
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: false,
        },
      },
      responsive: true,
      maintainAspectRatio: false,
    },
  });
}
 
    } else {
      try {
        // Send the user message to the backend
        const response = await axios.post(`${baseURL}/message`, { userMessage: userMessage.text });
        const apiResponse = response.data;
        
        // Extract the bot reply from the response
        const botReply = apiResponse.botReply;
        
        // Handle different types of bot replies
        if (botReply.type === "message") {
          messages.value.push({
            id: Date.now() + 1,
            type: "bot-message",
            text: botReply.content,
            image: null
          });
        } else if (botReply.type === "line-chart") {
          messages.value.push({
          id: Date.now() + 1,
          type: "line-chart",
          data: botReply.content.data,
          options: botReply.content.options
        });
      } 
 
       else if (botReply.type === "image") {
          messages.value.push({
            id: Date.now() + 1,
            type: "bot-message",
            text: "",
            image: botReply.content
          });
        } 
        // Add more 'else if' blocks here for additional types if needed
      } catch (error) {
        console.error("Error connecting to the server:", error);
        messages.value.push({
          id: Date.now() + 1,
          type: "bot-message",
          text: "Unable to connect to the server.",
          image: null
        });
      }
    }
  }
}

onMounted(async () => {
  try {
    // Attempt to delete all messages from the database
    await axios.delete(`${baseURL}/delete-messages`);
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