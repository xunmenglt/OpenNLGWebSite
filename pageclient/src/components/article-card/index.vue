<template>
  <div class="article-card-container">
    <v-row>
        <v-col cols="10">
            <v-row>
                <div class="title" @click="preview">{{title}}</div>
            </v-row>
            <v-row>
                <div class="tip-container">
                    <v-chip small outlined color="#BDBDBD">
                        <v-icon left>
                            mdi-eye
                        </v-icon>
                        <span>{{readTimes}}</span>
                    </v-chip>
                    <v-divider class="mx-4" vertical></v-divider>
                    <v-chip small outlined color="#BDBDBD">
                        <v-icon left>
                            mdi-clock-time-eight
                        </v-icon>
                        <span>{{time}}</span>
                    </v-chip>
                    <v-divider class="mx-4" vertical></v-divider>
                    <v-chip small outlined color="teal darken-2" @click="doCopy(`/article/view?id=${articleId}`)">
                        <v-icon left>
                            mdi-multicast
                        </v-icon>
                        <span>/article/view?id={{articleId}}</span>
                    </v-chip>
                </div>
            </v-row>
        </v-col>
        <v-col cols="2">
            <div class="options-container">
                
                <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-icon class="mr-2" v-on="on" v-bind="attrs" @click="editItem">
                            mdi-pencil
                        </v-icon>
                    </template>
                    <span>editing</span>
                </v-tooltip>
                <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-icon class="mr-2" v-on="on" v-bind="attrs" @click="deleteItem">
                            mdi-delete
                        </v-icon>
                    </template>
                    <span>delete</span>
                </v-tooltip>
                <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-icon class="mr-2" v-on="on" v-bind="attrs" @click="preview">
                            mdi-eye-arrow-right
                        </v-icon>
                    </template>
                    <span>preview</span>
                </v-tooltip>
            </div>
        </v-col>
    </v-row>
    <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
          <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
  </div>
</template>

<script>
import { showTextMessage } from '@/plugins/toastification'
import { deleteArticleAPI } from '@/utils/api/article'
export default {
    props:{
        articleId:{
            type:String,
            default:'',
            require:false
        },
        title:{
            type:String,
            default:'',
            require:false
        },
        readTimes:{
            type:Number,
            default:0,
            require:false
        },
        time:{
            type:String,
            default:'',
            require:false
        }
    },
    data() {
        return {
            dialogDelete:false
        }
    },
    methods:{
        doCopy(content){
            navigator.clipboard.writeText(content).then(()=>{
                showTextMessage('success','复制成功')
            }).catch(()=>{
                showTextMessage('error','复制失败')
            })
        },
        async deleteItem(){
            this.dialogDelete = true
        },
        async deleteItemConfirm() {
            if (this.articleId){
                const res=await deleteArticleAPI(this.articleId)
                if (res.code==200){
                    this.$bus.$emit('deleteArticleHandler',true)
                }
            }
            this.closeDelete()
        },
        closeDelete() {
            this.dialogDelete = false
        },
        editItem(){
            if(this.articleId){
                this.$router.push({
                    path:'/dashboard/articles/editor',
                    query:{
                        id:this.articleId
                    }
                })
            }
        },
        preview(){
            if(this.articleId){
                this.$router.push({
                    path:'/article/view',
                    query:{
                        id:this.articleId
                    }
                })
            }
        }
    }
}
</script>

<style lang="less" scoped>
.article-card-container{
    width: 100%;
    padding: 15px;
    border-radius: 5px;
    box-sizing: border-box;
    margin-bottom: 10px;
    border: 1px solid #eaeaea;
}
.title{
    color: #000;
    font-size: 18px !important;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}
.title:hover{
    color: #ff890a;
    cursor: pointer;
}
.tip-container{
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 10px;
}
.options-container{
    display: flex;
    width: 100%;
    justify-content: space-around;
    align-content: center;
    height: 100%;
    padding: 20px;
}
</style>