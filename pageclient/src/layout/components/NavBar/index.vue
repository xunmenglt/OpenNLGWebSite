<template>
  <v-app-bar class="bar" app color="white" fixed elevate-on-scroll :min-height="100">
    <div class="opennlg-container top-bar-container">
        <div class="logo-container" @click="toIndex">
            <img :src="OpenNLGLogImage" alt="logo">
        </div>
        <v-tabs class="d-none d-sm-flex" v-model="tab" light color="#000000" align-with-title>
            <v-tab :tabindex="0" @click="toNewPage('/index')" class="tab">首页</v-tab>
            <v-tab :tabindex="1" @click="toNewPage('/ryjs')" class="tab">人员介绍</v-tab>
            <v-tab :tabindex="2" @click="toNewPage('/yjfx')" class="tab">研究方向</v-tab>
            <v-tab :tabindex="3" @click="toNewPage('/fblw')" class="tab">发表论文</v-tab>
            <v-tab :tabindex="4" @click="toNewPage('/zlwz')" class="tab">专栏文章</v-tab>
            <v-tab :tabindex="5" @click="toNewPage('/tjhd')" class="tab">小组文化</v-tab>
            <v-tab :tabindex="6" @click="toNewPage('/lxwm')" class="tab">联系我们</v-tab>
        </v-tabs>
    </div>
    
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
    toNewPage(path){
      this.$router.push(path)
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
.top-bar-container{
    height: 100%;
    display: flex;
    align-items: center;
}
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