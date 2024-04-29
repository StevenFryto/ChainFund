<!-- d3js 气泡图 -->
<template>
    <div id="bubble" style="width: 500px; height :500px"></div>
</template>

<script>
import * as echarts from 'echarts/core';
import * as d3 from 'd3';
import { DatasetComponent, TooltipComponent, VisualMapComponent } from 'echarts/components';
import { CustomChart } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';

echarts.use([
    DatasetComponent,
    TooltipComponent,
    VisualMapComponent,
    CustomChart,
    CanvasRenderer
]);

export default {
    data() {
        return {
            user: {},
            colorList: ['#4e79a7', '#f28e2c', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#af7aa1', '#ff9da7', '#9c755f']
        };
    },
    mounted() {
        let that = this
        let seriesData = [
            { depth: 0, id: 'user', index: 0, value: 0 },
            { depth: 1, id: 'user.三寸不烂之蛇', index: 1, value: 50 },
            { depth: 1, id: 'user.且放白鹿', index: 3, value: 166 },
            { depth: 1, id: 'user.零落浮华', index: 4, value: 88 },
            { depth: 1, id: 'user.城南旧雨', index: 5, value: 108 },
            { depth: 1, id: 'user.青衫如故', index: 6, value: 52 },
            { depth: 1, id: 'user.花非花雾非雾', index: 7, value: 28 },
            { depth: 1, id: 'user.皮蛋瘦肉周', index: 8, value: 35 },            
            { depth: 1, id: 'user.雷爆龙', index: 9, value: 50 },
            // { depth: 1, id: 'user.且放白鹿', index: 10, value: 99 },
            { depth: 1, id: 'user.微雨燕双飞', index: 6, value: 80 },
            { depth: 1, id: 'user.泪过无痕', index: 7, value: 31 },
            { depth: 1, id: 'user.醉挽清风', index: 8, value: 62 },            
            { depth: 1, id: 'user.硬撑', index: 9, value: 66 },
            { depth: 1, id: 'user.红烛', index: 10, value: 93 },
            { depth: 1, id: 'user.拐卖人口处', index: 9, value: 66 },
            { depth: 1, id: 'user.压到我腿毛了', index: 10, value: 94 },
            { depth: 1, id: 'user.晴天', index: 9, value: 66 },
        ];
        let displayRoot = stratify1();
        function stratify1() {
            return d3
                .stratify()
                .parentId(function (d) {
                    return d.id.substring(0, d.id.lastIndexOf('.'));
                })(seriesData)
                .sum(function (d) {
                    return d.value || 0;
                })
                .sort(function (a, b) {
                    return b.value - a.value;
                });
        }
        function overallLayout(params, api) {
            let context = params.context;
            d3
                .pack()
                .size([api.getWidth() - 2, api.getHeight() - 2])
                .padding(0)(displayRoot);
            context.nodes = {};

            displayRoot.descendants().forEach(function (node) {
                context.nodes[node.id] = node;
            });
        }
        function renderItem(params, api) {
            let context = params.context;
            let idx = params.dataIndex;

            // 每次调用setuser时，只能进行一次布局。
            if (!context.layout) {
                context.layout = true;
                overallLayout(params, api);
            }

            let nodePath = api.value('id');
            let nodeName = nodePath
                .slice(nodePath.lastIndexOf('.') + 1)
                .split(/(?=[A-Z][^A-Z])/g)
                .join('\n')
            let node = context.nodes[nodePath];
            if (node.id === 'user') {
                node.r = 0
            }
            if (!node) {
                // Reder nothing.
                return;
            }

            let z2 = api.value('depth') * 2;
            return {
                type: 'circle',
                shape: {
                    cx: node.x,
                    cy: node.y,
                    r: node.r
                },
                z2: z2,
                textContent: {
                    type: 'text',
                    style: {
                        // transition: isLeaf ? 'fontSize' : null,
                        text: nodeName,
                        fill: '#fff',
                        fontFamily: 'Arial',
                        width: node.r * 1.3,
                        overflow: 'truncate',
                        fontSize: node.r / 3
                    },
                    emphasis: {
                        style: {
                            overflow: null,
                            fontSize: Math.max(node.r / 3, 12)
                        }
                    }
                },
                textConfig: {
                    position: 'inside'
                },
                style: {
                    fill: that.colorList[idx % that.colorList.length]
                },
                emphasis: {
                    style: {
                        fontFamily: 'Arial',
                        fontSize: 12,
                        shadowBlur: 20,
                        shadowOffsetX: 3,
                        shadowOffsetY: 5,
                        shadowColor: 'rgba(0,0,0,0.3)'
                    }
                }
            };
        }
        this.user = {
            dataset: {
                source: seriesData
            },
            tooltip: {},
            hoverLayerThreshold: Infinity,
            series: [{
                type: 'custom',
                colorBy: 'data',
                renderItem: renderItem,
                progressive: 0,
                coordinateSystem: 'none',
                encode: {
                    tooltip: 'value',
                    itemName: 'id'
                }
            }]
        }
        this.initEcharts()
    },
    methods: {
        initEcharts() {
            let myChart = echarts.init(document.getElementById('bubble'))
            myChart.setOption(this.user)
        }
    }
}
</script>