<template>
  <div class="peoples-container">
    <div class="peo_item" v-for="item in dataList" :key="item.id">
      <PeopleCard 
          :cnName="item.cnName" 
          :enName="item.enName" 
          :memberDesc="item.memberDesc" 
          :avatarUrl="item.avatarUrl" 
          :outsideUrl="item.outsideUrl" 
          :insideUrl="item.insideUrl"
        />
    </div>
    <div class="clear"></div>
  </div>
</template>

<script>
import PeopleCard from '@/components/people-card'
import { getMembersListAPI } from '@/utils/api/members'
export default {
    name:"Peoples",
    components:{
        PeopleCard
    },
    data() {
      return {
        dataList:[]
      }
    },
    async created(){
      const res=await getMembersListAPI()
      if (res&&res.code==200){
        this.dataList=res.data
      }else{
        this.dataList=[]
      }
    }
}
</script>

<style lang="less" scoped>
.clear{
  clear: both;
}
.peoples-container{
  width: 100%;
  height: 100%;
  justify-content: space-between;
  grid-template-columns: repeat(auto-fill,420px);
  display: grid;
  .peo_item{
    width: 420px;
  }
  .peo_item:nth-child(3n + 3) {
    margin-right: 0px;
  }

}
@media only screen and (max-width: 1000px) {
  .peoples-container{
    width: 100%;
    height: 100%;
    justify-content:center;
    align-items: center;
    flex-direction: column;
    display: flex;
  }
  .peo_item{
    width: 100% !important;
    margin-right: 0px !important;
    float: none !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
  }
}
</style>