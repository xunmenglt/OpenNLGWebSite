<template>
    <el-carousel :interval="4000000" type="card" height="400px">
        <el-carousel-item v-for="(item,index) in interests_list" :key="index">
            <div class="interests-container">
                <!-- 长宽高 4：3 -->
                <div class="interests-image">
                    <img :src="item.image">
                </div>
                <div class="interests-title">
                    <div class="text">{{item.title}}</div>
                </div>
            </div>
        </el-carousel-item>
    </el-carousel>
</template>

<script>
import { getTeamCultureListAPI } from '@/utils/api/teamculture'
export default {
    data() {
        return {
            interests_list:[]
        }
    },
    created(){
        getTeamCultureListAPI().then((res)=>{
            this.interests_list=res.data.data
        })
    }
}
</script>

<style lang="less" scoped>
.interests-container{
    height: 100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    .interests-image{
        height: 300px;
        width: 400px;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        img{
            width: auto;
            height: 100%;
        }
    }
    .interests-title{
        background: #ffa80678;
        width: 400px;
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
    }
}
</style>