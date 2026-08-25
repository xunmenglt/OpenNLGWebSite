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
export default {
    data() {
        return {
            interests_list:[
                {
                 "title":"大语言模型",
                 "desc":"",
                 "image":"https://img2.baidu.com/it/u=664406207,2507014690&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=500"   
                },
                {
                 "title":"自然语言处理",
                 "desc":"",
                 "image":"https://img1.baidu.com/it/u=2033602622,521439758&fm=253&fmt=auto&app=138&f=JPEG?w=683&h=461"   
                },
                {
                 "title":"文本生成",
                 "desc":"",
                 "image":"https://img0.baidu.com/it/u=3326062826,4294308451&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=500"   
                },
                {
                 "title":"大模型应用",
                 "desc":"",
                 "image":"https://img1.baidu.com/it/u=1847612787,2202854552&fm=253&fmt=auto&app=138&f=JPEG?w=666&h=500"   
                },
            ]
        }
    },
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
        justify-content: center;
        align-content: center;
        img{
            width: auto;
            height: 100%;
        }
    }
    .interests-title{
        background: #ffe37e78;
        width: 400px;
        font-family: 'Roboto', sans-serif;
        font-size: 30px;
    }
}
</style>