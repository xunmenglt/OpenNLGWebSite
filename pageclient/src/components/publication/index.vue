<template>
  <div class="publiction-container">
    <div class="pb_ct" v-for="item in dataList" :key="item.publicationId">
        <PublicationCard 
            :publicationId="item.publicationId" 
            :publicationCover="item.publicationCover" 
            :publicationTitle="item.publicationTitle" 
            :publicationDesc="item.publicationDesc" 
            :insideUrl="item.insideUrl" 
            :outsideUrl="item.outsideUrl"/>
    </div>
  </div>
</template>

<script>
import PublicationCard from '@/components/publication-card'
import { getPublicationListAPI } from '@/utils/api/publication'
export default {
    components:{
        PublicationCard
    },
    data() {
      return {
        dataList:[]
      }
    },
    async created(){
      const res=await getPublicationListAPI({currentPage:1,size:10})
      if (res&&res.code==200){
        this.dataList=res.data.data
      }else{
        this.dataList=[]
      }
    }
}
</script>

<style lang="less" scoped>
.publiction-container {
    width: 1400px;
    margin: 0 auto;
}
.pb_ct {
    margin-left: 20px;
    width: 310px;
    float: left;
}
@media only screen and (max-width: 1000px){
    .publiction-container {
        width: 100%;
        height: 100%;
    }
    .pb_ct {
      margin-left: 0 !important;
      width: 100% !important;
      float: none;
  }
  .pub_img{
    width: 100% !important;
    height: auto !important;
  }
}

</style>