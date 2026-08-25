<template>
  <div class="last-news-container">
    <div class="news-item" v-for="(item,index) in news_list" :key="index">
        <div class="news-title">
            <div>{{ item.newsTitle }}</div>
            <div>{{item.createTime}}</div>
        </div>
        <div class="news-desc">
            <div>{{item.newsSummary}}</div>
        </div>
    </div>
  </div>
</template>

<script>
import { getNewsListAPI } from '@/utils/api/news'
export default {
    data() {
        return {
            news_list:[
            ]
        }
    },
    created(){
        getNewsListAPI().then((res=>{
            console.log(res)
            this.news_list=res.data.data
        }))
    }
}
</script>

<style lang="less" scoped>
.last-news-container{
    height: 300px;
    overflow-y: scroll;
    border: 2px rgb(181, 181, 181) solid;
    &:hover{
        border: 2px rgb(31, 184, 255) solid;
    }
}
.news-item{
    display: flex;
    flex-direction: column;
    padding: 0 10px;
    font-weight: 500;
    .news-title{
        display: flex;
        justify-content: space-between;
        font-size: 18px;
        font-family: 'times new roman';
        color: rgb( 68 , 78 , 103 );
    }
    .news-desc{
        text-align: start;
        font-size: 15px;
        font-family: 'times new roman';
    }
}
</style>