$(window).load(function () {
    $(".loading").fadeOut()
})
$(function () {

    echarts_4();
    echarts_5();
    topo();
    function topo() {
        var myChart1 = echarts.init(document.getElementById('topo'));
        var host = new Image();  // 创建 Image 对象
        host.src = '../../assets/images/host.png';
        var switchs = new Image();  // 创建 Image 对象
        switchs.src = '../../assets/images/switch.png';
        var option = {
            tooltip: {
                textStyle: {
                    fontSize: 20
                },
                show: true,
                trigger: 'item',
                backgroundColor: 'gray',
                formatter: function (params) {
                    var ipString = '';
                    if (params.data.ip !== null && params.data.ip != undefined) {
                        ipString = '<br><span style="color: blue;">●</span> IP地址：' + params.data.ip;
                    }
                    return '<span style="color: blue;">●</span>' + params.name + ipString;
                }
            },



            series: [
                {
                    type: 'graph',
                    layout: 'force',
                    force: {
                        repulsion: 300,  // 修改 repulsion 参数为 100
                        edgeLength: 200
                    },
                    animation: false,
                    roam: true,
                    label: {
                        show: true
                    },
                    data: [
                        {
                            name: 'h1',
                            id: 0,
                            ip: '10.0.1.1',
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + host.src,
                        },
                        {
                            name: 'h2',
                            id: 1,
                            ip: '10.0.2.2',
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + host.src,
                        },
                        {
                            name: 'h3',
                            id: 2,
                            ip: '10.0.3.3',
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + host.src,
                        },
                        {
                            name: 'h4',
                            id: 3,
                            ip: '10.0.4.4',
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + host.src,
                        },
                        {
                            name: 's1',
                            id: 4,
                            ip: null,
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + switchs.src,
                        },
                        {
                            name: 's2',
                            id: 5,
                            ip: null,
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + switchs.src,
                        },
                        {
                            name: 's3',
                            id: 6,
                            ip: null,
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + switchs.src,
                        },
                        {
                            name: 's4',
                            id: 7,
                            ip: null,
                            symbolSize: 70,
                            draggable: true,
                            symbol: 'image://' + switchs.src,
                        },
                    ],
                    links: [
                        {
                            source: 4,
                            target: 0,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },
                        {
                            source: 4,
                            target: 1,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },
                        {
                            source: 4,
                            target: 6,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },
                        {
                            source: 4,
                            target: 7,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },

                        {
                            source: 5,
                            target: 2,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },
                        {
                            source: 5,
                            target: 3,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },
                        {
                            source: 5,
                            target: 6,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },
                        {
                            source: 5,
                            target: 7,
                            lineStyle: {
                                color: 'white',
                                width: 5
                            },
                        },
                    ],
                },
            ]

        };
        myChart1.setOption(option);
    }





    function echarts_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart4'));

        option = {

        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
    function echarts_5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart5'));

        var lightBlue = {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [{
                offset: 0,
                color: 'rgba(41, 121, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 192, 255, 1)'
            }],
            globalCoord: false
        }

        var option = {
            tooltip: {
                show: false
            },
            grid: {
                top: '0%',
                left: '60',
                right: '50',
                bottom: '0%',
            },
            xAxis: {
                min: 0,
                //max: 12000,
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: false

                },
                axisLabel: {
                    show: false
                }
            },
            yAxis: {
                data: ['交换机1-1', '交换机4-2', '交换机2-3', '交换机3-2', '交换机1-3', '交换机3-1'],
                offset: -8,
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: false
                },
                axisLabel: {
                    color: 'rgba(255,255,255,.6)',
                    fontSize: 13,


                }
            },
            series: [{
                type: 'bar',
                label: {
                    show: true,
                    zlevel: 10000,
                    position: 'right',
                    padding: 6,
                    color: '#4e84a1',
                    fontSize: 14,
                    formatter: '{c}'

                },
                itemStyle: {
                    barBorderRadius: 25,
                    color: '#3facff'
                },
                barWidth: '15',

                data: [1594.53, 1077.36, 948.06, 818.75, 691.37, 561.69],
                z: 6
            }
            ],
        };


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }





})


















