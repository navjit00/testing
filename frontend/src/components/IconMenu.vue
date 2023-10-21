<style scoped>

.aspect-ratio {
  position: relative;
  width: 75%;
  padding-bottom: 75%;
}

.clickable {
  cursor: pointer;
}

</style>

<template>
  <main class="w-full flex flex-col items-center gap-3 text-center">
    <div
         @click="navigate"
         class="aspect-ratio w-full active:scale-75 duration-300 grid place-items-center text-success clickable"
    >
      <img :src="source.imageSrc" :alt="source.name" class="absolute top-0 left-0 w-full h-full object-cover">
    </div>
  </main>
</template>

<script setup>

import { useRouter } from 'vue-router'

const navigate = () => {
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