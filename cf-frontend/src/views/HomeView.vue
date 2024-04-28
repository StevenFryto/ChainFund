<template>
	<div class="container">
		<FourCard></FourCard>
		<EveryDay></EveryDay>
		<ChartOne></ChartOne>
	</div>
</template>


<script>
import ChartOne from '@/components/ChartOne.vue';
import FourCard from '@/components/FourCard.vue'
import EveryDay from '@/components/EveryDay.vue'

export default {
	name: 'HomeView',
	components: {
		ChartOne, FourCard, EveryDay,
	}
}

</script>

<style>

</style>