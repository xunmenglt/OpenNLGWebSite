<template>
  <div class="dashbord-container">
    <v-row class="row" no-gutters style="height: 100%;">
        <v-col  cols="2" class="left-col">
            <v-card elevation="0" height="100%" class="left-card">
                <v-navigation-drawer permanent >
                  <template v-slot:prepend>
                    <v-list-item two-line>
                      <v-list-item-avatar @click="toIndex" class="logo">
                        <img src="../../assets/logo.png">
                      </v-list-item-avatar>
            
                      <v-list-item-content>
                        <v-list-item-title><b>OpenNLG 小组</b></v-list-item-title>
                        <v-list-item-subtitle>Dashboard</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </template>
            
                  <v-divider></v-divider>
            
                  <v-list dense nav>
                    <v-list-item
                      v-for="item in navigation_items"
                      :key="item.title"
                      link
                      :class="active_id==item.id?'item-active':''"
                      @click="changeRoute(item.id,item.path)"
                    >
                      <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                      </v-list-item-icon>
            
                      <v-list-item-content>
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-navigation-drawer>
              </v-card>
        </v-col>
        <v-col cols="10" class="right-col">
          <router-view/>
        </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
    name:'Dashboard',
    data() {
        return {
            navigation_items: [
                { id:1,title: '团队成员', icon: 'mdi-account-group-outline',path:'/dashboard/teammembers'},
                { id:2,title: '小组新闻', icon: 'mdi-newspaper-variant-outline' ,path:'/dashboard/news'},
                { id:3,title: '发表论文', icon: 'mdi-book-open-page-variant-outline' ,path:'/dashboard/reserarch'},
                { id:4,title: '小组产品', icon: 'mdi-shape-plus-outline' ,path:'/dashboard/publication'},
                { id:5,title: '小组文化', icon: 'mdi-image-multiple-outline' ,path:'/dashboard/teamculture'},
                { id:6,title: '站内文章', icon: 'mdi-language-markdown' ,path:'/dashboard/articles'},
                { id:7,title: '小组资源', icon: 'mdi-folder-file-outline' ,path:'/dashboard/resources'},
            ],
            active_id:0
        }
    },
    mounted(){
      document.documentElement.scrollTop =0 
      document.body.scrollTop=0
    },
    methods:{
        toIndex(){
            this.$router.push('/index')
        },
        changeRoute(id,path){
            if (this.active_id==id) return
            this.active_id=id
            this.$router.push(path)
        }
    }
}
</script>

<style lang="less" scoped>
.dashbord-container{
    height: 100vh;
}
.row{

}
.left-col{
}
.right-col{
  padding: 15px !important;
  box-sizing: border-box !important;
  height: 100vh;
}
.logo{
    cursor: pointer;
    
}
.left-card{
    background: #fff;
}
.item-active{
    background: #808080;
}
</style>