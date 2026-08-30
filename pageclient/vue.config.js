const { defineConfig } = require('@vue/cli-service')
const isOfflineBundle = process.env.OPENNLG_OFFLINE === '1'
module.exports = defineConfig({
  pages:{
    index:{
      entry: isOfflineBundle ? 'src/offline-main.js' : 'src/main.js',
      title:'OpenNLG Group'
    }
  },
  
  transpileDependencies: [
    'vuetify'
  ],
  publicPath:'./'
})
