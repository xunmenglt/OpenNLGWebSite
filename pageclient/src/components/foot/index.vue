<template>
    <v-footer dark padless>
        
        <v-card flat tile class="lighten-1 white--text text-center">
          <div class="fg" style="width:100vw"></div>
  
          <v-card-text class="white--text">
          <strong>Copyright {{ new Date().getFullYear() }}. All Rights Reserved By OpenNLG.</strong>
          <br><a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备2023034280号-1</a>
          </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
export default {
    name:'Foot'
}
</script>
<style lang="less" scoped>
.fg{
  border-top: 10px rgb(255,159,25) solid;
}
</style>