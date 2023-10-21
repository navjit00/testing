<template>
  <canvas ref="canvas"></canvas>
</template>

<script>
import { Chart, LineElement, CategoryScale, LinearScale, PointElement, LineController } from 'chart.js';

Chart.register(LineElement, CategoryScale, LinearScale, PointElement, LineController);

export default {
  props: {
    data: Object,
  },
  mounted() {
    this.createChart();
  },
  methods: {
    createChart() {
      const ctx = this.$refs.canvas.getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: this.data,
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    },
  },
};
</script>
