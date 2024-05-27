<template>
  <div class="searchBox">
    <span>交换机选择</span>
    <el-select v-model="value" placeholder="Select">
        <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
  </el-select>
    <el-button type="primary">立即查询</el-button>
  </div>
</template>

<script setup>
import {reactive, ref} from "vue"
const value = ref('')
const options=reactive([
    {value: '1',label: '交换机1',},
    {value: '2',label: '交换机2',},
    {value: '3',label: '交换机3',},
    {value: '4',label: '交换机4',},
    {value: '5',label: '交换机5',},
])
</script>

<style scoped>
.searchBox{
    display: flex;
    justify-content: center;
    align-items:center;
    width: 100%;
    height: 12vh;
}
span{
    color: #666;
    font-size: 14px;
    font-weight: bold;
    margin-right: 20px;
}
.el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}
.el-button{
    margin-left: 20px;
}
</style>