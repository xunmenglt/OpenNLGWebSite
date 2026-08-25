<template>
    <v-container class="h-100  d-flex align-center justify-center">
      <v-card class="login-card">
        <v-card-title>User Login</v-card-title>
          <v-card-text class="pa-8">
            <v-form ref="form">
               <v-text-field variant="underlined" v-model="username" required
                          label="username"
              ></v-text-field>
               <v-text-field variant="underlined" v-model="password" required
                          label="password"
                          type="password"
              ></v-text-field>
              <v-row class="mt-5 d-flex justify-space-around">
                <v-btn class="ml-5" @click="handleCancel">CANCEL</v-btn>
                <v-btn class="ml-5" @click="handleLogin">LOGIN</v-btn>
              </v-row>
            </v-form>
          </v-card-text>
      </v-card>
    </v-container>
  </template>
  

<script>

import {loginApi} from '@/utils/api/auth'

import {mapState,mapMutations,mapGetters} from 'vuex'

import { showTextMessage } from '@/plugins/toastification'
//  username:'OpenNLG',password:'88888888'
export default {
    name:"Login",
    data() {
        return {
            username:'',
            password:''
        }
    },
    computed:{
      ...mapState("m_path",['toPath']),
    },
    methods:{
        ...mapMutations("m_path",['clearToPath']),
        handleCancel(){
            this.$emit('handleCancel',true)
        },
        async handleLogin(){
            // todo handle login
            if(this.username===''||this.username===undefined||this.username===null){
              showTextMessage('warning','用户名不能为空')
              return
            }
            if(this.password===''||this.password===undefined||this.password===null){
              showTextMessage('warning','密码不能为空')
              return
            }
            await this.doLogin({username:this.username,password:this.password})
            this.$router.push('/dashboard')
            this.$emit('handleCancel',true)
        },
        async doLogin(data){
            
            const res = await loginApi(data)
            console.log(res)
            if (res && res.code===200){
              // 保存token
              const token=res.data.tokenHead+res.data.token
              window.localStorage.setItem('og_token',token)
              // 判断之前是否从其他跳转过来的界面
              if(this.toPath!='/' && this.toPath!='/index'){
                const path=this.toPath+''
                this.clearToPath()
                this.$router.replace(path)
              }
            }
        }
    }
}
</script>

<style lang="less" scoped>
.login-card{
  width: 500px;
}
@media only screen and (max-width: 1000px) {
  .login-card{
    width: 300px;
  }
}

</style>