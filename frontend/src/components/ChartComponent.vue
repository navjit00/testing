<template>
  <div class="chart-container">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import Chart from 'chart.js/auto';

const chartCanvas = ref(null);

onMounted(() => {
  const ctx = chartCanvas.value.getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June'],
      datasets: [{
        label: 'Demo Data',
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
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});
</script>

<style scoped>
.chart-container {
  width: 100%;
  max-width: 400px;
  height: 300px;
}
</style>
