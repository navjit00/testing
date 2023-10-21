<template>
  <div class="story-container">
    <button @click="closeStory">
      <img src="/x.png" alt="Close">
    </button>
    <StoryProgressBar :stories="stories" />
    <Splide @click="handleClick" ref="splideRef" class="mt-3 z-10" :options="options">
      <SplideSlide v-for="story in stories" :key="story.id">
        <img :src="story.imgSrc" :alt="story.altText">
      </SplideSlide>
    </Splide>
  </div>
</template>

<script setup>
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/splide.min.css';
import StoryProgressBar from './StoryProgressBar.vue';
import { reactive, ref, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';

const options = {
  arrows: false,
  autoplay: true,
  perPage: 1,
  type: 'loop',
  interval: 2500,
  pauseOnHover: false
};

const stories = reactive([
  { id: 1, progress: 0, isActive: true, imgSrc: '/stories/fined1.png', altText: 'Sample 1' },
  { id: 2, progress: 0, isActive: false, imgSrc: '/stories/fined2.png', altText: 'Sample 2' },
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
    goToNextStory();
  } else {
    goToPreviousStory();
  }
};

const goToNextStory = () => {
  const activeIndex = stories.findIndex(story => story.isActive);
  if (activeIndex < stories.length - 1) {
    stories[activeIndex].isActive = false;
    stories[activeIndex].progress = 100;
    stories[activeIndex + 1].isActive = true;
    stories[activeIndex + 1].progress = 0;
    splideRef.value.go('>');
  } else {
    closeStory();
  }
};

const goToPreviousStory = () => {
  const activeIndex = stories.findIndex(story => story.isActive);
  if (activeIndex > 0) {
    stories[activeIndex].isActive = false;
    stories[activeIndex].progress = 0;
    stories[activeIndex - 1].isActive = true;
    stories[activeIndex - 1].progress = 0;
    splideRef.value.go('<');
  }
};
</script>

<style scoped>
img {
  @apply w-full rounded-lg;
}

button {
  @apply absolute top-2 right-2 z-20 p-2 bg-amber-400;
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

button img {
  @apply w-full h-full;
}


.story-container {
  @apply relative;
}
</style>
