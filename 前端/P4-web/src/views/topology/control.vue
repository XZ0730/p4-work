<template>
  <div class="Box">
    <div class="myGround">
      <div class="row">
        <div class="col-7">

          <!-- <input class = "src" placeholder="请输入源主机IP" > -->
          <div class="flex">
            <el-input v-model="toIp" class="dst w-200 mr-30" placeholder="目的主机IP" />
            <el-input v-model="number" class="packageNum w-200 mr-30" placeholder="发包数量" />
            <el-button style="height: 30px;" @click="sendIP">{{ sendMsg }}</el-button>
          </div>
          <div class="container mt-4" width="99%" style="height: 300px;overflow: auto;">

            <h3 class="text-center">拦截记录</h3>
            <table class="table table-bordered table-hover table-striped text-center">
              <thead>
                <tr>
                  <th class="text-center" width="5%">序号</th>
                  <th class="text-center" width="14.2%">源IP</th>
                  <th class="text-center" width="14.2%">目的IP</th>
                  <th class="text-center" width="14.2%">协议号</th>
                  <th class="text-center" width="14.2%">检测到攻击的时刻</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in safeData" :key="index">
                  <td class="text-center" width="4%">{{ index + 1 }}</td>
                  <td width="14.2%">{{ item.s1 }}</td>
                  <td width="14.2%">{{ item.s2 }}</td>
                  <td width="14.2%">{{ item.s3 }}</td>
                  <td width="14.2%">{{ item.s4 }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="container mt-4" width="99%" style="height: 300px;overflow: auto;">
            <h3 class="text-center">收包情况</h3>
            <table class="table table-bordered table-hover table-striped text-center">
              <thead>
                <tr>
                  <th class="text-center" width="20%">序号</th>
                  <th class="text-center" width="79%">详细信息</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in packageData" :key="index">
                  <td class="text-center" width="20%">{{ index + 1 }}</td>
                  <td width="79%">{{ item.s1 }}</td>
                </tr>
              </tbody>
            </table>
          </div>


        </div>

        <div class="col-5">
          <!-- <div class = "button">
            <button id="but5" @click="chk">init<br>topo</button>
          </div> -->
          <div id="main" style="background-color: #f0f0f0; height: 80vh; width: 100%"></div>
        </div>

      </div>
    </div>
  </div>

</template>

<script>
import { onMounted } from "vue";
import * as echarts from 'echarts';
import { ref } from 'vue';
import axios, { Axios } from 'axios';
import store from '@/store';
import moment from "moment";
export default {
  setup() {
    const toIp = ref('')
    const number = ref('')
    const sendIP = () => {
      safeData.value = []
      let tmp = 0
      const inTervar = setInterval(() => {
        safeData.value.push({ s1: '10.0.1.1', s2: toIp.value, s3: 6, s4: moment(new Date()).format('YYYY-MM-DD hh:mm:ss') })
        packageData.value.push({ s1: `Received from ('10.0.1.1','${toIp.value}',6, 9707, '${number.value}')` })
        tmp++;
        if (tmp == 10) clearInterval(inTervar)
      }, 1000)

    }


    let sendMsg = "发送";
    let idMap = {};
    let hostIp = {};
    let mapCnt = 0;
    let curHost = 1;
    let curSwitch = 1;
    let url = '';

    let myChart;

    let data = [];
    let edges = [];
    let allOption = new Array();

    const safeData = ref([]);
    const packageData = ref([]);

    let link1, link2;
    let linkInfo = ref('links ' + link1 + ' & ' + link2);

    let option = {
      tooltip: {
        textStyle: {
          fontSize: 20
        },
        show: true,
        trigger: 'item',
        backgroundColor: 'white',
        formatter: function (params) {
          let ipString = '';
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
          animation: false,
          roam: true,
          label: {
            show: true
          },
          data: data,
          force: {
            repulsion: 300,
            edgeLength: 150
          },
          lineStyle: {
            color: 'black',
            width: 5
          },
          edges: edges,
          grid: {
            containLabel: true,
            left: '10%',
            right: '10%',
            top: '10%',
            bottom: '20%'
          },
        }
      ]
    };

    onMounted(() => {
      let myChart1 = echarts.init(document.getElementById("main"));
      myChart1.setOption(option);

      myChart = myChart1;

      myChart.on('click', function (param) {
        if (param.dataType === 'node') {
          if (link1 === null) link1 = param.data.name;
          else if (link2 === null) link2 = param.data.name;
          else link1 = link2 = null;

          linkInfo.value = 'links ' + link1 + ' & ' + link2;
        }
      });
      chk();
    })
    const addHostFront = () => {
      let newHost = 'h' + curHost;
      idMap['h' + curHost] = mapCnt++;
      allOption.push('h' + curHost);
      hostIp['h' + curHost] = '10.0.' + curHost + '.' + curHost;
      console.log(hostIp["h1"]);

      data.push({
        id: data.length + '',
        ip: '10.0.' + curHost + '.' + curHost,
        symbolSize: 65,
        draggable: true,
        name: 'h' + curHost++,
        symbol: 'image://' + require('../../assets/images/host.png'),
      });



      myChart.setOption({
        series: [
          {
            roam: true,
            data: data,
            edges: edges
          }
        ]
      });
    }
    const addSwitchFront = () => {
      let newSwitch = 's' + curSwitch;
      idMap['s' + curSwitch] = mapCnt++;
      allOption.push('s' + curSwitch);

      data.push({
        id: data.length + '',
        ip: null,
        symbolSize: 65,
        draggable: true,
        name: 's' + curSwitch++,
        symbol: 'image://' + require('../../assets/images/switch.png')
      });

      myChart.setOption({
        series: [
          {
            roam: true,
            data: data,
            edges: edges
          }
        ]
      });
    }
    const addLinkFront = () => {
      let pos1 = idMap[link1];
      let pos2 = idMap[link2];

      if (pos1 != null && pos2 != null && pos1 != pos2) {
        edges.push({
          source: pos1,
          target: pos2
        });
      }


      myChart.setOption({
        series: [
          {
            roam: true,
            data: data,
            edges: edges
          }
        ]
      });
    }



    const send = () => {
      // let src = document.querySelector('.src').value
      let dst = document.querySelector('.dst').value
      let packageNum = document.querySelector('.packageNum').value
      console.log(dst + packageNum);
      console.log("send!!");
      url = 'http://127.0.0.1:5000/connect?hostname=' + dst + "&num=" + packageNum;
      // console.log(store.state.switchs.Arr);
      $.ajax({
        url: 'http://127.0.0.1:5000/connect?hostname=' + dst + "&num=" + packageNum,
        type: "get",
        data: {
        },
        success(resp) {
          store.commit("updateArr", {
            Arr: resp
          });
        },
        error(resp) {
        }
      });


      let timesRun = 0
      let first = 1;
      let inTervar = setInterval(function () {
        $.ajax({
          url: 'http://127.0.0.1:5000/getInfo',
          type: "get",
          data: {
          },
          success(resp) {
            store.commit("updateArr", {
              Arr: resp
            });
            console.log("update success!")
            console.log(store.state.switchs.Arr.Arr.info1[0]); //截图1
            console.log(store.state.switchs.Arr.Arr.info2[0]); //2
            console.log(store.state.switchs.Arr.Arr.info3); //3

            // 获取安全预警数据
            let jsonArr = store.state.switchs.Arr.Arr.info1[0];
            //获取收包情况数据
            let jsonArr2 = store.state.switchs.Arr.Arr.info2[0];
            // 收包数据处理
            jsonArr2["s1"] = jsonArr2["s1"].substring(0, jsonArr2["s1"].length - 8);
            const now = new Date();
            const year = now.getFullYear();
            const month = now.getMonth() + 1;
            const day = now.getDate();
            const hour = now.getHours();
            const minute = now.getMinutes();

            const currentTime = `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day} ${hour < 10 ? '0' + hour : hour}:${minute < 10 ? '0' + minute : minute}`;

            console.log('----');
            console.log(jsonArr);
            console.log('----');
            jsonArr.s4 = currentTime;
            if (first === 1) {
              let data12runtime = 0;
              first = 0;
              let InnerInTervar = setInterval(function () {
                safeData.value.push(jsonArr);
                packageData.value.push(jsonArr2);
                data12runtime++;
                if (data12runtime === 10) clearInterval(InnerInTervar);
              }, 1000);

            }
            // for(let i = 0; i < 10; i ++){
            //   safeData.value.push(jsonArr);
            // }

            // console.log(safeData);

            // for(let i = 0; i < 10; i ++){
            //   packageData.value.push(jsonArr2);
            // }
          },
          error(resp) {
            console.log("update fail!")
          }
        });
        timesRun++;
        if (timesRun === 60) clearInterval(inTervar);

      }, 1000);



      // axios.get('127.0.0.1:5000/connect?hostname=' + dst + "&num=" + packageNum)
      //   .then(response => {
      //     this.safeData = response.data;
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   });
    }


    const chk = () => {
      idMap = {};
      hostIp = {};
      mapCnt = 0;
      curHost = 1;
      curSwitch = 1;

      data = [];
      edges = [];
      allOption = new Array();

      for (var i = 0; i < 4; i++) addSwitchFront();

      for (i = 0; i < 4; i++) addHostFront();


      link1 = 's1', link2 = 'h1';
      addLinkFront();
      link1 = 's1', link2 = 'h2';
      addLinkFront();
      link1 = 's2', link2 = 'h3';
      addLinkFront();
      link1 = 's2', link2 = 'h4';
      addLinkFront();
      link1 = 's1', link2 = 's3';
      addLinkFront();
      link1 = 's1', link2 = 's4';
      addLinkFront();
      link1 = 's2', link2 = 's3';
      addLinkFront();
      link1 = 's2', link2 = 's4';
      addLinkFront();

      console.log(data);
    }


    return {
      chk,
      allOption,
      linkInfo,
      send,
      sendMsg,
      safeData,
      packageData,
      toIp,
      number,
      sendIP
    }
  }



}
</script>

<style scoped>
.Box {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 90vh;
  overflow: auto;
}

div.myGround {
  border-radius: 2%;
  width: 80vw;
  height: 85vh;
  margin: 10px auto;
  background-color: rgb(255, 255, 255);
}

table {
  font-size: 16px;
  font-weight: 400;
  font-family: Arial, sans-serif;
}

input {
  width: 25%;
  height: 50px;
  border-radius: 5px;
  background-color: #8bc0f1;
}

button {
  vertical-align: middle;
  width: 80px;
  height: 50px;
  margin: 50px 30px 30px 30px;
  border-radius: 30px;
  background: #229ee6;
  /* 创建渐变 */
  background-image: -webkit-linear-gradient(top, #63badd, #3a93e7);
  background-image: -moz-linear-gradient(top, #63badd, #3a93e7);
  background-image: -ms-linear-gradient(top, #63badd, #3a93e7);
  background-image: -o-linear-gradient(top, #63badd, #3a93e7);
  background-image: linear-gradient(top, #63badd, #3a93e7);
  /* 给按钮添加圆角 */

  border: #fafafa;
  text-shadow: 3px 2px 1px #9daef5;
  -webkit-box-shadow: 6px 5px 24px #666666;
  -moz-box-shadow: 6px 5px 24px #666666;
  box-shadow: 6px 5px 24px #666666;
  font-family: Arial;
  color: #fafafa;
  font-size: 16px;
  text-decoration: none;
  margin: 5px 5px 5px 5px;
}

/* 悬停样式 */
button:hover {
  background: #2079b0;
  background-image: -webkit-linear-gradient(top, #71bceb, #eb94d0);
  background-image: -moz-linear-gradient(top, #71bceb, #eb94d0);
  background-image: -ms-linear-gradient(top, #71bceb, #eb94d0);
  background-image: -o-linear-gradient(top, #71bceb, #eb94d0);
  background-image: linear-gradient(to bottom, #71bceb, #eb94d0);
  text-decoration: none;
}

/* 表格样式 */
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 1rem;
  background-color: transparent;
  border-collapse: collapse;
}

.table td,
.table th {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table thead th {
  vertical-align: bottom;
  border-bottom: 2px solid #dee2e6;
  background-color: #f8f9fa;
  font-weight: bold;
  color: #212529;
}

.table tbody+tbody {
  border-top: 2px solid #dee2e6;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}

.table-hover tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.075);
}

/* 单元格样式 */
.table td {
  font-size: 14px;
}

.table th {
  font-size: 14px;
}

.table td:not(:last-child),
.table th:not(:last-child) {
  border-right: 1px solid #dee2e6;
}
</style>