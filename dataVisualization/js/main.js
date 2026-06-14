// ...以下为原index.html中<script>标签内的全部JS代码...

// 初始化所有图表
document.addEventListener('DOMContentLoaded', function() {
    // 价格区间分布柱状图
    const priceChart = echarts.init(document.getElementById('priceDistribution'));
    priceChart.setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        xAxis: {
            type: 'category',
            data: ['200万以下', '200-300万', '300-400万', '400-500万', '500-600万', '600-700万','700-800万',"800万以上"]
        },
        yAxis: {
            type: 'value',
            name: '房源数量'
        },
        series: [{
            name: '房源数量',
            type: 'bar',
            data: [1510,1576,2081,919,498,310,165,273],
            itemStyle: {
                color: '#5470C6'
            }
        }]
    });

    // 户型分布饼图
    const layoutChart = echarts.init(document.getElementById('layoutDistribution'));
    layoutChart.setOption({
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
            orient: 'vertical',
            right: 10,
            top: 'center',
            data: ['3室2厅2卫', '4室2厅2卫', '3室1厅2卫', '2室2厅1卫', '其他']
        },
        series: [
            {
                name: '户型分布',
                type: 'pie',
                radius: ['40%', '70%'],
                center: ['40%', '50%'],
                data: [
                    {value: 3520, name: '3室2厅2卫'},
                    {value: 1454, name: '4室2厅2卫'},
                    {value: 68, name: '3室1厅2卫'},
                    {value: 240, name: '2室2厅1卫'},
                    {value: 1677, name: '其他'},
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                label: {
                    show: false,
                    position: 'center'
                },
                labelLine: {
                    show: false
                }
            }
        ]
    });

    // 区域均价对比雷达图
    const districtChart = echarts.init(document.getElementById('districtPrice'));
    districtChart.setOption({
        tooltip: {},
        legend: {
            data: ['均价(元/㎡)'],
            bottom: 10
        },
        radar: {
            indicator: [
                { name: '上城区', max: 50000 },
                { name: '临安区', max: 50000 },
                { name: '临平区', max: 50000 },
                { name: '余杭市', max: 50000 },
                { name: '富阳区', max: 50000 },
                { name: '拱墅区', max: 50000 },
                { name: '桐庐区', max: 50000 },
                { name: '滨江区', max: 50000 },
                { name: '萧山区', max: 50000 },
                { name: '西湖区', max: 50000 },
                { name: '钱塘区', max: 50000 }

            ],
            splitArea: {
                show: false
            }
        },
        series: [{
            name: '区域均价对比',
            type: 'radar',
            data: [
                {
                    value: ['40657.29', '11488.34', '21589.44', '29992.43', '19635.07','38812.89','10586.75', '43984.83', '34178.68', '36844.88','24432.53'],
                    name: '均价(元/㎡)',
                    areaStyle: {
                        color: 'rgba(121, 134, 203, 0.4)'
                    },
                    lineStyle: {
                        width: 2
                    }
                }
            ]
        }]
    });

    // 建造年份分布折线图
    const yearChart = echarts.init(document.getElementById('yearDistribution'));
    yearChart.setOption({
        tooltip: {
            trigger: 'axis'
        },
        xAxis: {
            type: 'category',
            data:['1970年', '1973年', '1980年', '1982年', '1983年', '1984年', '1985年', '1986年', '1987年', '1988年', '1989年', '1990年', '1991年', '1992年', '1993年', '1994年', '1995年', '1996年', '1997年', '1998年', '1999年', '2000年', '2001年', '2002年', '2003年', '2004年', '2005年', '2006年', '2007年', '2008年', '2009年', '2010年', '2011年', '2012年', '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年', '2020年', '2021年', '2022年', '2023年', '2024年', '2025年', '2026年']

        },
        yAxis: {
            type: 'value',
            name: '房源数量'
        },
        series: [{
            name: '房源数量',
            type: 'line',
            data:[1, 1, 1, 2, 2, 2, 17, 6, 6, 28, 25, 14, 3, 9, 7, 7, 39, 11, 22, 39, 27, 68, 17, 35, 56, 27, 52, 35, 48, 95, 91, 67, 83, 94, 105, 100, 129, 361, 379, 173, 285, 179, 530, 750, 784, 1537, 950, 33]
,
            smooth: true,
            lineStyle: {
                width: 3,
                color: '#91CC75'
            },
            itemStyle: {
                color: '#91CC75'
            },
            areaStyle: {
                color: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 0,
                    y2: 1,
                    colorStops: [{
                        offset: 0,
                        color: 'rgba(145, 204, 117, 0.5)'
                    }, {
                        offset: 1,
                        color: 'rgba(145, 204, 117, 0.1)'
                    }]
                }
            }
        }]
    });

    // 建造年份与均价关系折线图
    const priceYearChart = echarts.init(document.getElementById('priceYearRelation'));
    priceYearChart.setOption({
        tooltip: {
            trigger: 'axis'
        },
        xAxis: {
            type: 'category',
            data: ['1970年', '1973年', '1980年', '1982年', '1983年', '1984年', '1985年', '1986年', '1987年', '1988年', '1989年', '1990年', '1991年', '1992年', '1993年', '1994年', '1995年', '1996年', '1997年', '1998年', '1999年', '2000年', '2001年', '2002年', '2003年', '2004年', '2005年', '2006年', '2007年', '2008年', '2009年', '2010年', '2011年', '2012年', '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年', '2020年', '2021年', '2022年', '2023年', '2024年', '2025年', '2026年']

        },
        yAxis: {
            type: 'value',
            name: '均价(元/㎡)',
        },
        series: [{
            name: '均价(元/㎡)',
            type: 'line',
            data: [29616.0, 42234.0, 53888.0, 46271.5, 40141.0, 56610.5, 37829.35, 33458.5, 33661.67, 37802.82, 34119.28, 38351.71, 47558.0, 35125.22, 22839.14, 28581.57, 30461.85, 25730.09, 27040.68, 29584.31, 23937.07, 24838.84, 38917.0, 26054.49, 28341.57, 26203.3, 26448.1, 32375.69, 30415.15, 26328.03, 27103.63, 25760.24, 22748.31, 22860.74, 27873.75, 28007.12, 25327.25, 34589.52, 36583.67, 33326.07, 37791.91, 35192.82, 32766.15, 32392.89, 31068.16, 36900.0, 35377.67, 35753.76]
,
            smooth: true,
            lineStyle: {
                width: 3,
                color: '#91CC75'
            },
            itemStyle: {
                color: '#91CC75'
            },
            areaStyle: {
                color: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 0,
                    y2: 1,
                    colorStops: [{
                        offset: 0,
                        color: 'rgba(145, 204, 117, 0.5)'
                    }, {
                        offset: 1,
                        color: 'rgba(145, 204, 117, 0.1)'
                    }]
                }
            }
        }]
    });

    // 房产均价与面积关系散点图
    const priceAreaChart = echarts.init(document.getElementById('priceAreaRelation'));
    const priceAreaOption = {
        tooltip: {
            formatter: function (param) {
                return param.data[2] + '<br>面积: ' + param.data[0] + '㎡<br>均价: ' + param.data[1] + '元/㎡';
            }
        },
        grid: {
            left: '3%',
            right: '7%',
            bottom: '7%',
            containLabel: true
        },
        xAxis: {
            name: '面积(㎡)',
            type: 'value',
            max: 450
        },
        yAxis: {
            name: '均价(元/㎡)',
            type: 'value',
            min: 0,
            max: 1000000
        },
        visualMap: {
            min: 5000,
            max: 100000,
            dimension: 1,
            orient: 'horizontal',
            right: 'center',
            top: '1%',
            inRange: {
                color: ['#50a3ba', '#eac736', '#d94e5d']
            },
            text: ['高均价', '低均价'],
            calculable: true
        },
        dataZoom: [
            {
                type: 'slider',
                yAxisIndex: 0,
                filterMode: 'none',
                startValue: 0,
                endValue: 100000,
                width: 16,
                right: 10
            }
        ],
        series: [{
            name: '均价-面积',
            type: 'scatter',
            symbolSize: function(data) {
                return Math.sqrt(data[0]) * 1.5;
            },
            data: [],
            itemStyle: {
                opacity: 0.8,
                borderColor: '#fff',
                borderWidth: 1
            }
        }]
    };
    priceAreaChart.setOption(priceAreaOption);

    // 使用$.get加载数据
    $.get('data//sizeAveragePrice.json', function (data) {
        // data为数组，每项为[面积, 均价, 小区名]
        priceAreaOption.series[0].data = data;
        priceAreaChart.setOption(priceAreaOption);
    });

    // 各小区房源数量TOP10
    const communityChart = echarts.init(document.getElementById('communityTop10'));
    communityChart.setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        xAxis: {
            type: 'value',
            name: '房源数量'
        },
        yAxis: {
            type: 'category',
            data: ['江湘云庐', '杭与城', '荣盛江荣府', '大城小院(别墅)', '翠揽云境', '地铁绿城杨柳郡', '万科公园大道有', '滨康天曜城', '中海河映云集', '九龙仓雍景山(公寓住宅)'],
            axisLabel: {
                interval: 0,
                rotate: 0
            }
        },
        series: [{
            name: '房源数量',
            type: 'bar',
            data: [71, 70, 53, 46, 42, 42, 40, 39, 38, 37],
            itemStyle: {
                color: function(params) {
                    var colorList = ['#c23531','#2f4554','#61a0a8','#d48265','#91c7ae','#749f83','#ca8622','#bda29a','#6e7074','#546570'];
                    return colorList[params.dataIndex];
                }
            },
            label: {
                show: true,
                position: 'right'
            }
        }]
    });

    
    // 窗口大小变化时重新调整图表大小
    window.addEventListener('resize', function() {
        priceChart.resize();
        layoutChart.resize();
        districtChart.resize();
        yearChart.resize();
        priceAreaChart.resize();
        communityChart.resize();
    });
});

// 图片点击放大功能
document.addEventListener('DOMContentLoaded', function() {
    // 图片点击放大功能
    document.querySelectorAll('.enlarge-img').forEach(function(img) {
        img.addEventListener('click', function() {
            var modal = document.getElementById('imgModal');
            var modalImg = document.getElementById('imgModalImg');
            modal.style.display = 'flex';
            modalImg.src = img.getAttribute('data-src') || img.src;
        });
    });
    document.getElementById('imgModalClose').onclick = function(e) {
        document.getElementById('imgModal').style.display = 'none';
        e.stopPropagation(); // 防止冒泡到模态框
    };
    // 点击模态框外部关闭
    document.getElementById('imgModal').onclick = function(e) {
        if (e.target === this) this.style.display = 'none';
    };
});