<template>
  <div class="article-list-container">
    <div class="top box">
        <v-btn rounded color="black" dark outlined @click="toCreate">
            <v-icon left>
                mdi-pencil-plus-outline
            </v-icon>
            CREATE ARTICLE
        </v-btn>
    </div>
    <div class="mid box">
        <span v-for="(item) in tableData" :key="item.id">
            <ArticleCard 
                :articleId="item.articleId" 
                :title="item.articleTitle" 
                :readTimes="item.articleReadTimes" 
                :time="item.createTime"/>
        </span>
    </div>
    <div class="btm box">
        <template>
            <div class="text-center">
              <v-pagination
                v-model="footBarParams.currentPage"
                :length="pageLength"
                :total-visible="5"
                @input="optionsChanged"
              ></v-pagination>
            </div>
        </template>
    </div>
  </div>
</template>

<script>
import {getArticleListAPI} from '@/utils/api/article'
import ArticleCard from '@/components/article-card'
export default {
    components:{
        ArticleCard
    },
    data() {
        return {
            tableIsLoading:false,
            tableData:[],
            footBarParams:{
                currentPage:1,
                size:6,
                total:0
            },
        }
    },
    created(){
        this.initialize()
        this.$bus.$on('deleteArticleHandler',this.deleteArticleHandler)
    },
    computed:{
        pageLength(){
            return Math.ceil(this.footBarParams.total/this.footBarParams.size)
        }
    },
    methods:{
        // 刷新数据
        async flashTable(){
            this.tableIsLoading=true
            try{
                const res = await getArticleListAPI({currentPage:this.footBarParams.currentPage,size:this.footBarParams.size})
                if(res.code==200){
                    this.tableData=res.data.data
                    this.footBarParams.total=res.data.total
                }else{
                    showTextMessage('warning',res.message)
                }
            } finally{
                this.tableIsLoading=false
            }

        },
        initialize() {
            this.flashTable()
        },
        optionsChanged(e){
            this.footBarParams.currentPage=e
            this.flashTable()
        },
        deleteArticleHandler(flag){
            if(flag){
                this.flashTable()
            }
        },
        
        toCreate(){
            this.$router.push({
                path:'/dashboard/articles/editor',
            })   
        }
    },
}
</script>

<style scoped>
.article-list-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}
.top{
    padding: 10px;
}
.box{
    width: 100%;
}
.mid {
    flex: 1;
    overflow: hidden;
    overflow-y: scroll;
    border-bottom: 1px solid #cecece;
    border-top: 1px solid #cecece;
    padding: 10px;
}

</style>