<template>
    <div class="pub_item" @click="toDesc(outsideUrl,insideUrl)" data-type="2" data-link="" data-linkurl="2023/TwinTex" data-id="804">
        <p><img class="pub_img" :src="publicationCover"></p>
        <div class="pub_min">
            <p>{{publicationTitle}}</p>
            <p>{{publicationDesc}}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PublictionCard',
    props:{
        publicationId:{
            type:Number,
            default:0,
            require:false
        },
        publicationCover:{
            type:String,
            default:'',
            require:false
        },
        publicationTitle:{
            type:String,
            default:'',
            require:false
        },
        publicationDesc:{
            type:String,
            default:'',
            require:false
        },
        insideUrl:{
            type:String,
            default:'',
            require:false
        },
        outsideUrl:{
            type:String,
            default:'',
            require:false
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

.pub_item {
    cursor: pointer;
    background: #ffffff;
    padding: 10px;
    border: 1px solid #e2e9f5;
    margin-bottom: 40px;
    box-shadow: 1px 4px 6px 0px rgb(226 233 245 / 25%);
}
.pub_item > p:nth-child(1) img {
    width: 290px;
    height: 150px;
}
img {
    vertical-align: middle;
}
.pub_item .pub_min > p:nth-child(1) {
    font-size: 14px;
    margin: 10px 0px;
    font-weight: 700;
    text-align: center;
    color: #000000;
    line-height: 20px;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    height: 32px;
    overflow: hidden;
}
.pub_item .pub_min > p:nth-child(2) {
    margin: 0px 0px 20px 0px;
    font-size: 14px;
    font-weight: 300;
    text-align: LEFT;
    color: #545762;
    line-height: 20px;
    height: 40px;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
}
@media only screen and (max-width: 1000px){
  .pub_img{
    width: 100% !important;
    height: auto !important;
  }
}
</style>