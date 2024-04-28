<template>
    <div id="app">
        <svg width="600" height="400" ref="svg"></svg>
    </div>
</template>

<script>
import * as d3 from "d3";

export default {
    data() {
        return {
            data: [
                { projectId: 14, fromUser: 1, fundValue: 2000, message: 'Some message 1' },
                { projectId: 14, fromUser: 2, fundValue: 5000, message: 'Some message 2' },
                { projectId: 1, fromUser: 14, fundValue: 20000, message: 'Some message 3' }
            ],
        }
    },
    mounted() {
        this.createGraph();
    },
    methods: {
        createGraph() {
            const svg = d3.select(this.$refs.svg);
            const width = +svg.attr('width');
            const height = +svg.attr('height');

            // Add your D3.js code here
            const simulation = d3.forceSimulation(this.data)
                .force('link', d3.forceLink().id(d => d.projectId))
                .force('charge', d3.forceManyBody())
                .force('center', d3.forceCenter(width / 2, height / 2));

            const link = svg.selectAll('.link')
                .data(this.data)
                .enter().append('line')
                .attr('class', 'edge');

            const node = svg.selectAll('.node')
                .data(this.data)
                .enter().append('circle')
                .attr('class', 'node')
                .attr('r', 10)
                .attr('fill', 'blue');

            const messageBox = svg.selectAll('.message-box')
                .data(this.data)
                .enter().append('rect')
                .attr('class', 'message-box')
                .attr('width', 100)
                .attr('height', 40)
                .attr('fill', 'white')
                .attr('stroke', 'black')
                .attr('opacity', 0);

            const text = svg.selectAll('.message-text')
                .data(this.data)
                .enter().append('text')
                .attr('class', 'message-text')
                .attr('x', d => d.x - 50)
                .attr('y', d => d.y - 20)
                .attr('fill', 'black')
                .text(d => d.message);

            simulation.on('tick', () => {
                link.attr('x1', d => d.source.x)
                    .attr('y1', d => d.source.y)
                    .attr('x2', d => d.target.x)
                    .attr('y2', d => d.target.y);

                node.attr('cx', d => d.x)
                    .attr('cy', d => d.y)
                    .on('mouseover', (d) => {
                        d3.select(this).attr('r', 15);
                        messageBox.attr('x', d.x + 20)
                            .attr('y', d.y - 20)
                            .attr('opacity', 1);
                        text.attr('x', d.x + 25)
                            .attr('y', d.y + 5)
                            .attr('opacity', 1);
                    })
                    .on('mouseout', () => {
                        d3.select(this).attr('r', 10);
                        messageBox.attr('opacity', 0);
                        text.attr('opacity', 0);
                    });
            });

            simulation.force('link').links(this.data);
        }
    }
};
</script>

<style>
.node {
    fill: #00f;
    stroke: #fff;
}

.edge {
    fill: none;
    stroke: #000;
    stroke-width: 2px;
}

.message-box {
    fill: #fff;
    stroke: #000;
}
</style>
