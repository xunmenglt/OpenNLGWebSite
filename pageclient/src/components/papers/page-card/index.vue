<template>
    <div class="se_item">
        <div class="se_img">
            <img :src="reserarchCover">
        </div>
        <div class="se_intro">
            <p class="title">
                <a href="javascript:void(0)" @click="toInSide">
                    {{ reserarchTitle }}
                </a>
                <span v-if="isNew" class="newIcon">N</span> 
            </p>
            <p class="origin">
                {{ reserarchSource }}
            </p>
            <p class="authers">
                {{ reserarchAuthor }}
            </p>
            <a href="javascript:void(0)" @click="toOutSide">
                <div class="check-page">
                    <div></div>
                    <div style="display: flex;justify-content: center;align-items: center;">
                        <div class="icon_text">Project Page </div> <img class="right_icon" src="../../../assets/images/m_icon.png">
                    </div>
                </div>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "PageCard",
    props:{
        reserarchId:{
            type:Number,
            default:0,
            require:false   
        },
        reserarchTitle:{
            type:String,
            default:'',
            require:false 
        },
        reserarchSource:{
            type:String,
            default:'',
            require:false 
        },
        reserarchCover:{
            type:String,
            default:'',
            require:false 
        },
        reserarchAuthor:{
            type:String,
            default:'',
            require:false 
        },
        outsideUrl:{
            type:String,
            default:'',
            require:false 
        },
        insideUrl:{
            type:String,
            default:'',
            require:false 
        },
        isNew:{
            type:Number,
            default:0,
            require:false   
        }
    },
    methods:{
        toInSide(){
            if(this.insideUrl){
                    
                this.$router.push(this.insideUrl)
            }
        },
        toOutSide(){
            if(this.outsideUrl){    
                this.$router.push(this.outsideUrl)
            }
        }
    }
}
</script>

<style lang="less" scoped>
.se_item {
    display: flex;
    justify-content: start;
    align-items: start;
    margin-bottom: 30px;
    padding-bottom: 20px;
    border-bottom: 1px solid #e2e6ec;
    position: relative;
}
.se_img {
    width: 293px;
    height: 152px;
    margin-right: 20px;
    text-align: center;
    img{
        width: 100%;
        border-style: none;
    }
}
.se_intro {
    width: calc(100% - 313px);
}
a {
    text-decoration: none;
}
.newIcon {
    color: #fff;
    background-color: #6ec7ff;
    font-style: normal;
    padding: 0px 3px;
    border-radius: 3px;
    margin-left: 5px;
    vertical-align: middle;
}
.title{
    color: #333;
    a{
        color: #333;
    }
}
.origin{
    font-size: 16px;
    line-height: 30px;
    font-weight: 400;
    text-align: LEFT;
    color: #616161;
}
.authers{
    font-size: 14px;
    line-height: 30px;
    font-weight: 300;
    text-align: LEFT;
    color: #72757c;
}
.check-page{
    
    display: flex;
    justify-content: space-between;
    align-items: center;

}
.icon_text{
    font-size: 12px;
    color: #930040;
}
.right_icon {
    width: 18px;
    height: 18px;
    margin-left: 2px;
}
@media only screen and (max-width: 1000px) {
    .se_item {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        margin-bottom: 30px;
        text-align: center;
    }
    .se_intro {
        width: 100%;
    }
    .se_img {
        width: 293px;
        height: 152px;
        margin-right: 20px;
        text-align: center;
        margin-bottom: 10px;
        border:1px solid #e2e6ec;
        img{
            width: 100%;
            border-style: none;
        }
    }
}
</style>