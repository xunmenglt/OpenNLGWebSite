import Vue from 'vue'
import Vuex from 'vuex'

import module_user from './user'
import module_path from './path'
Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    m_user:module_user,
    m_path:module_path
  }
})
