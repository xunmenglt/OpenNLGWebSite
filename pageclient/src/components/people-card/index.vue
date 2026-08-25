<template>
    <div class="card-container">
        <div class="card-img">
            <img :src="avatarUrl">
        </div>
        <div class="card-intro">
            <a href="javascript:void(0)" class="card_name" @click="toDesc">{{enName}} ({{cnName}})<img class="card_icon" src="../../assets/images/m_icon.png"></a>
            <div class="card_text" v-html="memberDesc"></div>
        </div>
    </div>
</template>

<script>
export default {
    name:'PeopleCard',

    props:{
        cnName:{
            type:String,
            default:'',
            require:false
        },
        enName:{
            type:String,
            default:'',
            require:false
        },
        memberDesc:{
            type:String,
            default:'',
            require:false
        },
        avatarUrl:{
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
        }
    },
    methods:{
        toDesc(){
            if(this.outsideUrl){
                window.open(this.outsideUrl)  
            }else{
                if(this.insideUrl){
                    this.$router.push(this.insideUrl)
                }
            }
        }
    }
}
</script>

<style lang="less" scoped>
.card-container{
    display: flex;
    justify-content: space-between;
    align-items: start;
    border: 1px solid #e2e9f5;
    box-shadow: 1px 4px 6px 0px rgb(226 233 245 / 25%);
    padding: 10px;
    margin-bottom: 20px;
    .card-img{
        width: 150px;
        height: 150px;
        img{
            width: 100%;
        }
    }
    .card-intro{
        padding-left: 10px;
        width: calc(100% - 160px);
        a {
            color: #337ab7;
            text-decoration: none;
            .card_icon{
                cursor: pointer;
                position: absolute;
                top: 0;
                right: 0;
                width: 20px;
                height: 20px;
            }
        }
        .card_name{
            display: block;
            cursor: pointer;
            padding-right: 25px;
            position: relative;
            font-size: 18px;
            height: 20px;
            line-height: 20px;
            overflow: hidden;
            margin-bottom: 12px;
            font-weight: 400;
            text-align: left;
            color: #000000;
            text-shadow: 1px 4px 6px rgb(226 233 245 / 25%);
        }
        .card_text {
            position: relative;
            overflow: hidden;
            font-size: 12px;
            font-weight: 300;
            text-align: left;
            color: #545454;
            line-height: 15px;
           
            text-shadow: 1px 4px 6px 0px rgba(226, 233, 245, 0.25);
            text-overflow: -o-ellipsis-lastline;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 8;
            line-clamp: 8;
            -webkit-box-orient: vertical;
        }
    }
}
@media only screen and (max-width: 1000px) {
    .card-container{
        display: flex;
        width: 80%;
        padding: 10px;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .card-intro{
        width: 100% !important;
        padding-left: 0 !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 10px;
    }
    .card-img{
        border: 2px solid #eee;
    }
    .card_text{
        text-align: center !important;
    }
}
</style>