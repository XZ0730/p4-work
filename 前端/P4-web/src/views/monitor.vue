<template>
  <div class="Box">

    <div class="line1">
      <!-- <button @click="changeId()"></button> -->
      <el-button type="button" class="btn-primary" @click="changeId()">查询</el-button>
      <el-button type="button" class="btn-primary float-right" id="dataView"
        onclick="window.location.href='http://127.0.0.1:5500/src/views/bigData/index.html'">可视化总览</el-button>
    </div>


    <div ref="mychart" id="myDiv"></div>


  </div>



</template>

<script>

import * as echarts from 'echarts';

import $ from "jquery"
import { useStore } from 'vuex';
import moment from 'moment';
export default {
  setup() {
    const store = useStore();

    const changeId = () => {
      // let switchId = 1;
      // store.commit("updateId", switchId);

    }

    return {
      changeId
    }
  },

  mounted() {
    let myChart = echarts.init(this.$refs.mychart);
    let option = {
      title: {
        text: 'bps'
      },
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        data: ['Switch 1 - Port 1', 'Switch 1 - Port 3', 'Switch 1 - Port 4', 'Switch 2 - Port 3', 'Switch 2 - Port 4', 'Switch 3 - Port 1', 'Switch 3 - Port 2', 'Switch 4 - Port 1', 'Switch 4 - Port 2']
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      toolbox: {
        feature: {
          saveAsImage: {}
        }
      },
      xAxis: {
        type: 'category',
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: 'Switch 1 - Port 1',
          type: 'line',
          stack: 'Total',
          data: [572.0257411583522, 572.0257411583522, 572.0257411583522, 572.0257411583522, 572.0257411583522, 572.0257411583522, 572.0257411583522, 572.0257411583522, 572.0257411583522]
        },
        {
          name: 'Switch 1 - Port 3',
          type: 'line',
          stack: 'Total',
          data: [439.99479339494485, 429.99479339494485, 439.99479339494485, 439.99479339494485, 439.99479339494485, 439.99479339494485, 459.99479339494485, 439.99479339494485, 439.99479339494485]
        },
        {
          name: 'Switch 1 - Port 4',
          type: 'line',
          stack: 'Total',
          data: [308.0008726691392, 308.0008726691392, 308.0008726691392, 408.0008726691392, 308.0008726691392, 308.0008726691392, 308.0008726691392, 358.0008726691392, 308.0008726691392]
        },
        {
          name: 'Switch 2 - Port 3',
          type: 'line',
          stack: 'Total',
          data: [175.9887220560616, 175.9887220560616, 175.98872205606162, 175.9887220560616, 175.9887220560616, 195.9887220560616, 125.9887220560616, 175.9887220560616, 175.9887220560616]
        },
        {
          name: 'Switch 2 - Port 4',
          type: 'line',
          stack: 'Total',
          data: [1547.3254183920883, 1547.3254183920883, 1547.3254183920883, 1647.3254183920883, 1547.3254183920883, 1547.3254183920883, 1547.3254183920883, 1547.3254183920883, 1600.3254183920883]
        },
        {
          name: 'Switch 3 - Port 1',
          type: 'line',
          stack: 'Total',
          data: [1075.4755737700632, 1045.4755737700632, 1045.4755737700632, 1085.4755737700632, 1045.4755737700632, 1045.4755737700632, 1045.4755737700632, 1045.4755737700632, 1045.4755737700632]
        },
        {
          name: 'Switch 3 - Port 2',
          type: 'line',
          stack: 'Total',
          data: [919.9992681824003, 919.9992681824003, 989.9992681824003, 919.9992681824003, 919.9992681824003, 819.9992681824003, 919.9992681824003, 919.9992681824003, 919.9992681824003]
        },
        {
          name: 'Switch 4 - Port 1',
          type: 'line',
          stack: 'Total',
          data: [794.6632091846337, 794.6632091846337, 794.6632091846337, 794.6632091846337, 794.6632091846337, 794.6632091846337, 794.6632091846337, 794.6632091846337, 794.6632091846337]
        },
        {
          name: 'Switch 4 - Port 2',
          type: 'line',
          stack: 'Total',
          data: [669.3382092762606, 669.3382092762606, 669.3382092762606, 669.3382092762606, 669.3382092762606, 669.3382092762606, 669.3382092762606, 669.3382092762606, 669.3382092762606]
        },
      ]
    };
    option && myChart.setOption(option);
    //   const store = useStore();

    //   let idx = 6;
    //   let jsonArr3 = store.state.switchs.Arr.Arr.info3;
    //   let data = [];
    //   let legendArr = [];
    //   let optionSeries = [];
    //   let first = 1;
    //   let myChart = echarts.init(this.$refs.mychart);
    //   let option;
    //   let now = new Date();

    //   function randomData() {
    //     // $.ajax({
    //     //   url: 'http://127.0.0.1:5000/getInfo',
    //     //   type: "get",
    //     //   data: {
    //     //   },
    //     //   success(resp) {
    //     //     store.commit("updateArr", {
    //     //       Arr: resp
    //     //     });
    //     //   },
    //     //   error(resp) {
    //     //   }
    //     // });

    //     // console.log("last" + last_id);
    //     if (first === 1) {
    //       first = 0;
    //       console.log("first!!!!!!!!!");
    //       optionSeries = [];
    //       legendArr = [];
    //       data = [];

    //       // 打印legendArr
    //       for (let i = 6; i < 15; i++) {
    //         let t = "";
    //         for (const myString in jsonArr3[0][i]) {
    //           legendArr.push(myString);
    //           t = myString;
    //         }
    //         optionSeries.push({
    //           // name:'port' + i.toString(),
    //           name: t,
    //           type: 'line',
    //           showSymbol: false,
    //           // smooth:true,
    //         });
    //       }
    //       console.log(legendArr);

    //     }

    //     let newData = [];
    //     now = new Date();

    //     newData.push([now.getHours(), now.getMinutes(), now.getSeconds()].join(':'));
    //     for (let i = 0; i < 9; i++) {
    //       let obj = jsonArr3[0][idx + i];
    //       for (const myString in obj) {
    //         newData.push(obj[myString] * 1000000);
    //         // console.log(obj[myString]); // 输出数字属性
    //       }
    //     }
    //     idx += 9;
    //     if (idx >= jsonArr3[0].length) idx = 6;
    //     if (data.length >= 10) {
    //       data.shift();
    //     }

    //     data.push(newData);
    //     console.log(data);

    //     option = {
    //       title: {
    //         left: 'center',
    //         text: '流量',
    //         textStyle: {
    //           color: "black",
    //           fontSize: 30,
    //         },

    //       },
    //       dataset: {
    //         source: data
    //       },

    //       xAxis: { type: 'category' },
    //       yAxis: {
    //         name: 'bps',
    //         nameTextStyle: {
    //           fontSize: 20
    //         },
    //         type: 'value',
    //         boundaryGap: [0, '100%'],
    //         splitLine: {
    //           show: true
    //         }
    //       },
    //       legend: {
    //         padding: [100, 800, 0, 0], // 上右下左
    //         data: legendArr,
    //       },
    //       series: optionSeries,
    //       tooltip: {
    //         show: 'true',
    //         trigger: "axis",
    //       }
    //     };
    //   }

    //   setInterval(function () {


    //     if (store.state.switchs.switchId !== 0) {

    //       randomData();
    //       // 除去第一个可能出现的无效数据
    //       if (data[0].length < data[1].length) data.shift();
    //       myChart.setOption(option);

    //     }

    //   }, 1000);

    //   option && myChart.setOption(option);
  }
}




</script>

<style scoped>
.Box {
  width: 100%;
  height: 90vh;
}

#myDiv {
  width: 100%;
  height: 80vh;
}

.line1 {
  display: flex;
  align-items: center;
  height: 10vh;
  margin-left: 20px;
}

.line1>input {
  width: 200px;
  height: 30px;
  padding: 0px 20px;
}

.line1>button {
  width: 100px;
  height: 40px;
  font-size: 20px;
}

#dataView {
  margin-left: 50px;
}
</style>