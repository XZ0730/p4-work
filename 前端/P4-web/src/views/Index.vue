<template>
    <PageHeader></PageHeader>
    <div class="main">
        <AsideMenuVue></AsideMenuVue>
        <div class="view">
            <router-view></router-view>
        </div>
    </div>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import AsideMenuVue from '@/components/AsideMenu.vue';
</script>

<style lang="scss" scoped>
.main{
    width: 100%;
    position: relative;
    display: flex;
    .view{
        width: 85%;
    }
}
</style>