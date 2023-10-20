<style scoped>

  /* .input-wrapper {
    @apply flex flex-col h-20 text-gray-300;
  }
  input[type=text], select {
    @apply bg-secondary border border-gray-700 text-gray-300 rounded-lg h-full mt-2 text-sm px-2 py-3;
  } */
  img {
    @apply w-full rounded-lg;
  }
</style>
<template>
  <img src="/long_story.png" alt="long story 1">
  <Splide class="mt-3 z-10" :options="options">
    <SplideSlide>
      <img src="/banner-1.jpg" alt="Sample 1">
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
</template>