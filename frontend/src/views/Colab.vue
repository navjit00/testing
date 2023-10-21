<style scoped>
img {
  @apply w-full rounded-lg;
}

button {
  @apply absolute top-2 right-2 z-20 p-2 bg-amber-400 rounded-full;
}

.story-container {
  @apply relative;
}

</style>

<template>
  <div class="story-container">
    <button @click="closeStory">x</button>
    <StoryProgressBar :stories="stories" />
    <Splide @click="handleClick" ref="splideRef" class="mt-3 z-10" :options="options">
      <SplideSlide>
        <img src="/stories/colab1.png" alt="Sample 1">
      </SplideSlide>
      <SplideSlide>
        <img src="/banner-2.jpg" alt="Sample 2">
      </SplideSlide>
      <SplideSlide>
        <img src="/banner-3.jpg" alt="Sample 1">
      </SplideSlide>
      <SplideSlide>
        <img src="/banner-2.jpg" alt="Sample 2">
      </SplideSlide>
    </Splide>
  </div>
</template>


<script setup>
import { Splide, SplideSlide } from '@splidejs/vue-splide'
import '@splidejs/splide/dist/css/splide.min.css';
import StoryProgressBar from './StoryProgressBar.vue';
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router'

const options = {
  arrows: false,
  autoplay: true,
  perpage: 1,
  type: 'loop',
  interval: 3000,
  pauseOnHover: false
}

const stories = reactive([
  {id: 1, progress: 0, isActive: true},
  {id: 2, progress: 0, isActive: false},
  {id: 3, progress: 0, isActive: false},
  {id: 4, progress: 0, isActive: false}
]);

const router = useRouter()

const closeStory = () => {
  router.push({ name: 'Home' });
};


const splideRef = ref(null);

const handleClick = (event) => {
  const splideEl = splideRef.value.$el;
  const splideWidth = splideEl.offsetWidth;
  const clickX = event.clientX - splideEl.getBoundingClientRect().left;

  if (clickX > splideWidth / 2) {
    splideRef.value.go('>');
  } else {
    splideRef.value.go('<');
  }
};



</script>