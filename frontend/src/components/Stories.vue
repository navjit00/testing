<template>
  <main class="flex justify-between gap-3 mt-3">
    <template v-for="(service, x) in services" :key="x">
      <IconMenu :source="service" />
    </template>
  </main>
</template>

<script setup>

import IconMenu from '@/components/IconMenu.vue'

const services = [
  {
    name: 'FinEd',
    to: 'FinEd',
    imageSrc: '/previews/fined.png'
  },
  {
    name: 'Colab',
    to: 'Colab',
    imageSrc: '/previews/colab.png'
  },
  {
    name: 'Offer',
    to: 'Offer',
    imageSrc: '/previews/offer.png'
  },
  {
    name: 'News',
    to: 'News',
    imageSrc: '/previews/news.png'
  }
]


</script>