<template>
  <div class="article-view-container">
    <TopBar/>
    <div style="height:40px"></div>
    <div v-if="article" class="view-container">
        <div class="tilte">{{article.articleTitle}}</div>
        <div class="auther">
            <v-icon>mdi-account-group</v-icon>
            <span class="auther-text">OpenNLG</span>
        </div>

        <v-row :justify="'end'">
            <v-col md="3" xs="6" sm="6">
                <div class="other-info">
                    <div>    
                        <v-icon>mdi-eye</v-icon>
                        <span class="auther-text inf">{{article.articleReadTimes}}</span>
                    </div>
                    <div style="width:15%"></div>
                    <div>    
                        <v-icon>mdi-clock-time-eight</v-icon>
                        <span class="auther-text inf">{{article.createTime}}</span>
                    </div>
                </div>
            </v-col>
        </v-row>
        <v-divider></v-divider>
        <div class="text-container markdown-body">
            <mavon-editor
              class="md"
              boxShadowStyle="0px"
              :value="article.articleContent"
              :subfield="false"
              :defaultOpen="'preview'"
              :toolbarsFlag="false"
              :editable="false"
              :scrollStyle="true"
              :ishljs="true"
            />
        </div>
    </div>
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import {getArticleItemAPI} from '@/utils/api/article'
import TopBar from '@/components/top-bar'
export default {
    name:'ArticleView',
    components: {
        mavonEditor,
        TopBar
    },
    data() {
        return {
            article:null
        }
    },
    async created(){
        const id=this.$route.query.id;
        if (id){
            const res=await getArticleItemAPI({articleId:id})
            if(res&&res.code&&res.code===200){
                this.article=res.data
            }
        }
    }
}
</script>

<style lang="less" scoped>
.tilte{
    font-size: 40px;
    font-weight: 900px;
    text-align: center;
}
.article-view-container{
    background: #fff;
}
/deep/ .v-show-content{
    background: #fff !important;
}
.view-container{
    padding: 10px;
    z-index: 0;
}
.auther{
    display: flex;
    justify-content: center;
    align-items: center;

}
.auther-text{
    padding-left: 10px;
}
.other-info{
    display: flex;
    align-items: center;
    justify-content: center;
}
.inf{
    color: #a0a0a0;
}
.text-container{
    width: 100%;
}
</style>