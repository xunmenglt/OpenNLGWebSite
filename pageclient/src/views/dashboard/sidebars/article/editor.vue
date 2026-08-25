<template>
    <div class="editor-container">
        <div class="top box">
            <v-row>
                <v-col cols="9">
                    <v-text-field v-model="title" :readonly="!titleIsEditing"
                        :hint="!titleIsEditing ? 'Click the icon to edit' : 'Click the icon to save'"
                        :label="`State — ${titleIsEditing ? 'Editable' : 'Readonly'}`" persistent-hint
                        prepend-icon="mdi-format-title" placeholder="please enter a title">
                        <template v-slot:append-outer>
                            <v-slide-x-reverse-transition mode="out-in">
                                <v-icon :key="`icon-${titleIsEditing}`" :color="titleIsEditing ? 'success' : 'info'"
                                    @click="titleIsEditing = !titleIsEditing"
                                    v-text="titleIsEditing ? 'mdi-check-outline' : 'mdi-circle-edit-outline'"></v-icon>
                            </v-slide-x-reverse-transition>
                        </template>
                    </v-text-field>
                </v-col>
                <v-col>
                    <div class="option-button-container">
                        <v-btn rounded color="error" dark outlined @click="saveArtcicle">
                            <v-icon left>
                                mdi-content-save-edit
                            </v-icon>
                            SAVE
                        </v-btn>
                        <v-btn rounded color="black" dark outlined @click="backToList">
                            <v-icon left>
                                mdi-arrow-left-circle
                            </v-icon>
                            BACK
                        </v-btn>
                    </div>
                </v-col>
            </v-row>
        </div>
        <div class="mid box">
        </div>
        <div class="btm box">
            <mavon-editor ref="md" v-model="content" boxShadowStyle="0px" @imgAdd="imgAdd" @save="saveArtcicle"/>
        </div>
    </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import {uploadFileAPI} from '@/utils/api/file'
import { createArticleAPI, getArticleItemAPI, updateArticleAPI } from '@/utils/api/article'
export default {
    name:'Editor',
    components: {
        mavonEditor
    },
    data() {
        return {
            title: '',
            content: '',
            summary: null,
            articleId: null,
            titleIsEditing: false,
            defaultItem:{
                articleContent:'',
                articleId: null,
                articleTitle: '',
            },
            isCanSave:true,
        }
    },
    async created(){        
        const id=this.$route.query.id;
        if (id){
            this.articleId=id
            const res=await getArticleItemAPI({articleId:id})
            if(res&&res.code&&res.code===200){
                this.title=res.data.articleTitle
                this.content=res.data.articleContent
            }
        }else{
            this.articleId=null
        }
    },
    methods: {
        async imgAdd(pos, $file) {
            let $vm = this.$refs.md
            const formData = new FormData();
            formData.append('file', $file);
            const res= await uploadFileAPI(formData)
            if (res.code==200){
                $vm.$img2Url(pos, res.data);
            }
        },
        // 保存文章
        async saveArtcicle(){
            if(this.isCanSave){
                this.isCanSave=false
                if (this.articleId){// 更新文字
                    await updateArticleAPI({
                        articleContent:this.content,
                        articleId: this.articleId,
                        articleTitle: this.title,
                    })
                }else{// 新增文章
                    const res=await createArticleAPI({
                        articleContent:this.content,
                        articleTitle: this.title,
                    })
                    if(res&&res.code&&res.code===200){
                        this.articleId=res.data
                    }
                }
                setTimeout(()=>{
                    this.isCanSave=true
                },3000)
            }
            
        },
        backToList(){
            this.$router.replace('/dashboard/articles/list')
        }
    }
}
</script>

<style lang="less" scoped>
.editor-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.box {
    width: 100%;
}

.option-button-container {
    height: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.mid {
    height: 20px;
    border-bottom: 1px solid #cecece;
}

.btm {
    flex: 1;
    overflow: hidden;
}

/deep/ .v-note-wrapper {
    height: 100% !important;
}
</style>