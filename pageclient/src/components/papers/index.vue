<template>
  <div>
    <PageCard v-for="item in dataList" 
          :key="item.reserarchId" 
          :reserarchId="item.reserarchId" 
          :reserarchTitle="item.reserarchTitle" 
          :reserarchSource="item.reserarchSource" 
          :reserarchCover="item.reserarchCover" 
          :reserarchAuthor="item.reserarchAuthor" 
          :outsideUrl="item.outsideUrl" 
          :isNew="item.isNew" 
          :insideUrl="item.insideUrl"/>
  </div>
</template>

<script>
import PageCard from '@/components/papers/page-card'
import { getReserarchListAPI } from '@/utils/api/reserarch'
export default {
    name:"Papers",
    components:{
        PageCard
    },
    data() {
      return {
        dataList:[]
      }
    },
    async created(){
      const res=await getReserarchListAPI({currentPage:1,size:10})
      if (res&&res.code==200){
        this.dataList=res.data.data
      }else{
        this.dataList=[]
      }
    }
}
</script>

<style>

</style>