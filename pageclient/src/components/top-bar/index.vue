<template>
    <v-app-bar class="bar" app color="white" fixed elevate-on-scroll :min-height="100">
        <div class="logo-container" @click="toIndex">
            <img src="../../assets/logo.png" alt="logo">
        </div>
        <v-tabs class="d-none d-sm-flex"  v-model="tab" light color="#000000" align-with-title>
            <v-tab :tabindex="0" @click="scrollIndex('home')" class="tab">HOME</v-tab>
            <v-tab :tabindex="1" @click="scrollIndex('news')" class="tab">News</v-tab>
            <v-tab :tabindex="2" @click="scrollIndex('reserarch')" class="tab">RESERARCH</v-tab>
            <v-tab :tabindex="3" @click="scrollIndex('people')" class="tab">PEOPLE</v-tab>
            <v-tab :tabindex="4" @click="scrollIndex('publication')" class="tab">PUBLICATION</v-tab>
        </v-tabs>
        <v-spacer></v-spacer>
        <v-btn class="ma-2" v-if="isLogin" outlined @click="toDashboard"> 
            Dashboard  
            <v-icon right >
                mdi-monitor-dashboard
            </v-icon>
        </v-btn>
        <v-btn class="ma-2" v-else outlined @click="toLogin"> Login </v-btn>
    </v-app-bar>
</template>

<script>
import {mapState} from 'vuex'
export default {
    name: "TopBar",
    props: {
        selectBar: {
            type: Number,
            default: 0,
            require:false
        },
    },
    computed:{
        ...mapState("m_user",['og_token']),
        isLogin(){
            // console.log(this.og_token)
            if (this.og_token===''||this.og_token===undefined||this.og_token===null){
                return false
            }else{
                return true
            }
        }
    },
    data() {
        return {
            tab:0,
        }
    },
    methods: {
        scrollIndex(id) {
            // 获取当前路径
            const currentPath=this.$route.path
            if(currentPath!='/'||currentPath!='/index'){
                this.$router.push('/index')
            }
            setTimeout(()=>{                
                this.$nextTick(() => {
                    let targetbox = document.getElementById(id)
                    let height = targetbox.offsetTop
                    document.documentElement.scrollTop = height
                })
            },200)
        },
        toLogin(){
            this.$bus.$emit('toLogin',true)
        },
        toDashboard(){
            if (this.og_token===''||this.og_token===undefined||this.og_token===null){
                return 
            }else{
                this.$router.push('/dashboard')
            }
        },
        toIndex(){
            this.$router.push('/index')
        }
    },
    watch:{
        selectBar(newVal){
            this.tab=newVal
        },
    }
}
</script>

<style lang="less" scoped>
.logo-container{
    height: 100%;
    border-radius: 5px;
    box-sizing: border-box;
    padding-top: 15px;
    cursor: pointer;
    img{
        border-radius: 10px;
        height: 80%; 
    }
}
/deep/ .v-toolbar__content{
    height: 100% !important;
    padding-left: 5%;
}
.tab{
    margin-left: 5%;
    font-size: 16px;
    color: #333;
    font-weight: 700;
}
/deep/ .v-item-group{
    width: 100% !important;
}
.bar{
    z-index: 9999;
}
</style>