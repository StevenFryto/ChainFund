<template>
	<div class="container">
		<FourCard></FourCard>
		<ChartOne></ChartOne>
	</div>
</template>


<script>
import ChartOne from '@/components/ChartOne.vue';
import FourCard from '@/components/FourCard.vue'

export default {
	name: 'HomeView',
	components: {
		ChartOne, FourCard
	}
}

</script>

<style>

</style>