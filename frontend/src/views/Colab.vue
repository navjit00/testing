<template>
  <div class="story-container">
    <button @click="closeStory">x</button>
    <StoryProgressBar :stories="stories" />
    <Splide @click="handleClick" ref="splideRef" class="mt-3 z-10" :options="options">
      <SplideSlide v-for="story in stories" :key="story.id">
        <img :src="story.imgSrc" :alt="story.altText">
      </SplideSlide>
    </Splide>
  </div>
</template>

<script setup>
import { ref, reactive, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/splide.min.css';
import StoryProgressBar from './StoryProgressBar.vue';

const options = {
  arrows: false,
  autoplay: true,
  perPage: 1,
  type: 'loop',
  interval: 2500,
  pauseOnHover: false
};

const stories = reactive([
  { id: 1, progress: 0, isActive: true, imgSrc: '/stories/colab1.png', altText: 'Sample 1' },
  // Add more stories here
]);

const router = useRouter();
const splideRef = ref(null);

const closeStory = () => {
  router.push({ name: 'Home' });
};

const updateProgress = () => {
  for (const story of stories) {
    if (story.isActive) {
      story.progress += (100 / (options.interval / 25));
      if (story.progress >= 100) {
        const currentIndex = stories.indexOf(story);
        if (currentIndex < stories.length - 1) {
          story.isActive = false;
          stories[currentIndex + 1].isActive = true;
          stories[currentIndex + 1].progress = 0;
          splideRef.value.go('>');
        } else {
          closeStory(); // Close the story viewer when the last story is done
        }
      }
      break;
    }
  }
};


const intervalId = setInterval(updateProgress, 25);

onBeforeUnmount(() => {
  clearInterval(intervalId);
});

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

<style scoped>
img {
  width: 100%;
  border-radius: 8px;
}

button {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 20;
  padding: 8px;
  background-color: #FBC02D;
  border: none;
  border-radius: 50%;
  font-weight: bold;
  cursor: pointer;
}

.story-container {
  position: relative;
}
</style>
