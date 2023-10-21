<template>
  <div class="progress-container">
    <div v-for="story in stories" :key="story.id" class="story-bar">
      <div :class="{'bar-active': story.isActive}" :style="{width: story.progress + '%'}"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    stories: Array
  }
}
</script>

<style scoped>
.progress-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.story-bar {
  height: 3px;
  flex: 1;
  margin: 0 2px;
  background-color: #D1A120;
  position: relative;
  overflow: hidden;
}

.bar-active {
  @apply absolute top-0 left-0 h-full w-0 bg-amber-400;
  transition: width 3s linear;
}

</style>
