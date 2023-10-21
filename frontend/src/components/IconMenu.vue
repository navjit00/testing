<style scoped>

.aspect-ratio {
  position: relative;
  width: 75%;
  padding-bottom: 75%;
}

.clickable {
  cursor: pointer;
}

.image-shadow {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

</style>

<template>
  <main class="w-full flex flex-col items-center gap-3 text-center">
    <div v-if="isVisible"
         @click="navigate"
         class="aspect-ratio w-full active:scale-75 duration-300 grid place-items-center bg-secondary shadow text-success clickable"
    >
      <img :src="source.imageSrc" :alt="source.name" class="absolute top-0 left-0 w-full h-full object-cover image-shadow">
    </div>
    <small class="text-gray-300">{{ source.name }}</small>
  </main>
</template>

<script setup>

import { useRouter } from 'vue-router'
import { ref } from 'vue'

const isVisible = ref(true);  // Define the reactive variable

const navigate = () => {
  isVisible.value = false;
  setTimeout(() => {
    router.push({ name: props.source.to });
  }, 300);
}

const router = useRouter()
const props = defineProps({
  source: {
    type: Object
  }
})

</script>