<template>
    <v-timeline>
        <v-timeline-item
          v-for="(item) in dataList"
          :key="item.newsId"
          :color="colors[item.newsId%colors.length]"
          small
        >
          <template v-slot:opposite>
            <span
              :class="`text-body-1 headline font-weight-bold ${colors[item.newsId%colors.length]}--text`"
              v-text="item.createTime"
            ></span>
          </template>
          <div class="py-4" @click="toDesc(item.outsideUrl,item.insideUrl)">
            <h2 :class="`mb-4 headline font-weight-light ${colors[item.newsId%colors.length]}--text`">
              {{ item.newsTitle }}
            </h2>
            <div class="desc text-body-2">
              {{ item.newsSummary }}
            </div>
          </div>
        </v-timeline-item>
      </v-timeline>
</template>

<script>
import { getNewsListAPI } from '@/utils/api/news'
 export default {
    data: () => ({
      colors:['cyan','green','pink','amber','orange'],
      dataList:[]
    }),
    async created(){
      const res=await getNewsListAPI({currentPage:1,size:10})
      // console.log(res)
      if (res&&res.code==200){
        this.dataList=res.data.data
      }else{
        this.dataList=[]
      }
    },
    methods:{
      toDesc(outsideUrl,insideUrl){
            if(outsideUrl){
                window.open(outsideUrl)  
            }else{
                if(insideUrl){
                    this.$router.push(insideUrl)
                }
            }
        }
    }
  }
</script>

<style lang="less" scoped>
.desc{
    color: #747474;
}
</style>