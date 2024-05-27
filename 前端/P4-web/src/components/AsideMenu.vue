<template>
    <el-menu text-color="#fff" class="menu" :default-active="router.currentRoute.value.fullPath" :unique-opened="true"
        router>

        <!-- <el-sub-menu index="/topology">
            <template #title>
                <el-icon><Menu /></el-icon>
                <span>网络拓扑</span>
            </template>
<el-menu-item index="/topology/control">
    <el-icon>
        <Tools />
    </el-icon>
    拓扑管理
</el-menu-item>
<el-menu-item index="/topology/links">
    <el-icon>
        <ZoomIn />
    </el-icon>
    查看链路
</el-menu-item>
<el-menu-item index="/topology/switches">
    <el-icon>
        <ZoomIn />
    </el-icon>
    设备信息
</el-menu-item>
</el-sub-menu>

<el-sub-menu index="/flowentry">
    <template #title>
                <el-icon><Avatar /></el-icon>
                <span >流量调度</span>
            </template>
    <el-menu-item index="/flowentry/update">
        <el-icon>
            <Promotion />
        </el-icon>
        流表下发/删除
    </el-menu-item>
    <el-menu-item index="/flowentry/watch">
        <el-icon>
            <ZoomIn />
        </el-icon>
        查看流表
    </el-menu-item>
</el-sub-menu>


<el-menu-item index="/monitor">
    <el-icon>
        <Monitor />
    </el-icon>
    <span>流量监控</span>
</el-menu-item>
<el-menu-item index="/check">
    <el-icon>
        <Odometer />
    </el-icon>
    <span>安全监控中心</span>
</el-menu-item> -->


        <el-menu-item index="/topology/control">
            <el-icon>
                <Odometer />
            </el-icon>
            <span>安全预警</span>
        </el-menu-item>
        <el-menu-item index="/monitor">
            <el-icon>
                <Monitor />
            </el-icon>
            <span>流量监控</span>
        </el-menu-item>
        <!-- <el-menu-item index="/topology/safe" >
            <el-icon><Odometer /></el-icon>
            <span>安全预警</span>
        </el-menu-item> -->

    </el-menu>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<style lang="scss" scoped>
.menu {
    width: 15%;
    min-width: 200px;
    height: 90vh;
    background-color: rgb(74, 128, 214);
    color: #fff;
    border: 0px;
    overflow: auto;

    &::-webkit-scrollbar {
        display: none
    }
}

.el-sub-menu {
    .el-menu-item {
        background-color: rgb(18, 25, 39);

        &:hover {
            color: rgb(67, 197, 240);
        }
    }
}

.el-menu-item.is-active {
    color: #fff !important;
    background-color: rgb(24, 166, 213) !important;
}

.menu>.el-menu-item:hover {
    color: rgb(67, 197, 240);
    background-color: rgb(48, 48, 75);
}

::v-deep .el-sub-menu__title:hover {
    span {
        color: rgb(67, 197, 240) !important;
    }

    background-color: rgb(48, 48, 75) !important;
}

// ::v-deep.is-opened .el-sub-menu__title{
//     color:  rgb(67, 197, 240) !important; 
// }
.el-icon {
    color: #fff;
}
</style>