<template>
    <div class="rjfx-container opennlg-container">
          <div class="section-title">
            <div class="title h22">发表论文</div>
            <div class="clear"></div>
            <p>Publication</p>
          </div>
          <div class="table-container">
            <el-table
              :data="paperDataList"
              :show-header="false"
              :row-class-name="tableRowClassName"
              style="width: 100%">
              <el-table-column
                prop="createTime"
                label="发表时间"
                width="180">
                <template slot-scope="scope">
                  {{ scope.row.createTime.split(" ")[0] }}
                </template>
              </el-table-column>
              <el-table-column
                prop="reserarchTitle"
                label="标题">
                <template slot-scope="scope">
                  <div class="zlwz-title">
                    {{ scope.row.reserarchTitle }}
                    <div v-if="scope.row.isNew===1" class="is-new">⭐</div>
                  </div>
                </template>
              </el-table-column>
              <el-table-column
                prop="reserarchSource"
                label="类别"
                width="200">
              </el-table-column>
              <el-table-column
                fixed="right"
                label="操作"
                width="100">
                <template slot-scope="scope">
                  <div @click="goTarget(scope.row.outsideUrl||scope.row.insideUrl)">
                    论文详情
                  </div>
                </template>
              </el-table-column>
            </el-table>
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
import { getReserarchListAPI } from '@/utils/api/reserarch'
export default{
  data() {
    return {
      queryParams:{
        currentPage:1,
        size:10,
        total:0,
      },
      paperDataList:[]
    }
  },
  created(){
    this.flashDataList()
  },
  methods:{
    tableRowClassName({row, rowIndex}){
      return 'table-row'
    },
    async flashDataList(){
      let res=await getReserarchListAPI(this.queryParams)
      if (res && res.code && res.code===200){
        this.paperDataList=res.data.data
        this.queryParams.currentPage=res.data.currentPage
        this.queryParams.size=res.data.size
        this.queryParams.total=res.data.total
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
    },
  }
}
</script>

<style lang="less" scoped>
.pagination-container{
  margin-top: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.title{
  font-size: 28px !important;
  line-height: 28px;
}
.section-title{
  padding: 50px 0;
}
/deep/ .el-table tr,.el-table {
  background-color:#ffffff00 !important;
}
/deep/ .table-row{
  font-size: 14px;
  line-height: 26px;
  font-weight: 600;
  color: #848484;
  text-transform: capitalize;
  transition: all 0.5s ease;
  font-family: 'Roboto', sans-serif;
  border-bottom: 1px solid #f41c1c;
  transition: all 0.5s ease;
}
/deep/ .table-row:hover {
  
  border-bottom: 1px solid #4c83f8;
  transition: all 0.5s ease;
}
/deep/ .el-table tr:hover{
  td{
    padding-left: 10px !important;
    transition: all 0.5s ease;
    color: rgb(255,159,25);
    cursor: pointer;
  }
}
.zlwz-title{
  display: flex;
  align-items: center;
  justify-content: start;
  .is-new{
    color: #f41c1c;
    font-size: 12px;
    vertical-align:text-top;
    margin-left: 5px;
  }
}
</style>