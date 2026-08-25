<template>
  <div class="tjhd-container opennlg-container">
        <div class="section-title">
          <div class="title h22">小组文化</div>
          <div class="clear"></div>
          <p>Publication</p>
        </div>
        <div class="image-container">
          <el-row :gutter="10">
            <el-col :xl="24" :sm="12" :md="8" :lg="6" class="tjhd-item" v-for="(item,index) in tjhdDataList" :key="index">
              <div class="item">
                <div class="image-container" @click="goTarget(item.outsideUrl||item.insideUrl)">
                  <img :src="item.image">
                </div>
                <div class="title">
                  {{ item.title }}
                </div>
              </div>
            </el-col>
          </el-row>
        </div>
        <div class="pagination-container">
          <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="queryParams.currentPage"
          :page-sizes="[10, 20, 30, 40]"
          :page-size="queryParams.size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="queryParams.total"
          prev-text="上一页"
          next-text="下一页">
        </el-pagination>
        </div>
  </div>
</template>

<script>
import { getTeamCultureListAPI } from '@/utils/api/teamculture'

export default{
data() {
  return {
    queryParams:{
        currentPage:1,
        size:10,
        total:0,
    },
    tjhdDataList:[
    ]
  }
},
created(){
  this.flashDataList()
},
methods:{
  async flashDataList(){
      let res=await getTeamCultureListAPI(this.queryParams)
      if (res && res.code && res.code===200){
        this.tjhdDataList=res.data.data
        this.queryParams.currentPage=res.data.currentPage
        this.queryParams.size=res.data.size
        this.queryParams.total=res.data.total
        console.log(res.data)
      }else{
        this.dataList=[]
      }
    },
    handleSizeChange(size){
      this.queryParams.size=size
      this.flashDataList()
    },
    handleCurrentChange(page){
      this.queryParams.currentPage=page
      this.flashDataList()
    },
    goTarget(href) {
      window.open(href, "_blank");
    }
}
}
</script>

<style lang="less" scoped>
.tjhd-item{
  .item{
    width: 100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-bottom: 10px;
    .image-container{
      width: 100%;
      height: 205px;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      img{
        height: 100%;
        width: auto;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
      }
    }
    .title{
      width: 100%;
      height: 40px;
      background: #ebf9ff;
      font-family: var(--font-name) !important;
      font-weight: 800;
      --wght:500;
      --BEVL:100;
      font-variation-settings: "wght" var(--wght),"BEVL" var(--BEVL);
      line-height: 40px;
      text-align: center;
    }
  }
}
.pagination-container{
  margin-top: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>