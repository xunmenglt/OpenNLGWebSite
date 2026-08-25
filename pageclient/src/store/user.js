import router from '../router'
import { getRequest } from '@/utils/api'
import { showTextMessage } from '@/plugins/toastification'
export default{
	//开启命名空间
	namespaced: true,
	// state 数据
	state: () => ({
	  	// 登录成功之后的 token 字符串
		og_token: window.localStorage.getItem('og_token') || '',
		// 用户的基本信息
		userinfo: JSON.parse(window.localStorage.getItem('userinfo') || '{}'),
		//重定页面object 对象 { openType, from }
	}),
	//方法
	mutations:{
		// 更新用户的基本信息
		updateUserInfo(state, userinfo) {
            if(userinfo){
                state.userinfo = userinfo
                // 通过 this.commit() 方法，调用 m_user 模块下的 saveUserInfoToStorage 方法，将 userinfo 对象持久化存储到本地
                this.commit('m_user/saveUserInfoToStorage')
                // console.log(userinfo)
            }else{
                getRequest('/auth/user/info').then(res=>{
                    state.userinfo=res.data
                    this.commit('m_user/saveUserInfoToStorage')
                }).catch(error=>{
					showTextMessage('error','获取用户信息失败，请稍后重试')
                    window.localStorage.removeItem('og_token')
                    router.replace('/')
                })
            }
            
		},
        //清除用户信息
        clearUserInfo(state){
            state.userinfo={},
            window.localStorage.removeItem('userinfo')
            window.localStorage.removeItem('og_token')
        },
		// 将 userinfo 持久化存储到本地
		saveUserInfoToStorage(state) {
			window.localStorage.setItem('userinfo', JSON.stringify(state.userinfo))
		},
		// 更新 token 字符串
		updateToken(state, token) {
			state.token = token
		    // 通过 this.commit() 方法，调用 m_user 模块下的 saveTokenToStorage 方法，将 token 字符串持久化存储到本地
		    this.commit('m_user/saveTokenToStorage')
		},
		// 将 token 字符串持久化存储到本地
		saveTokenToStorage(state) {
		    window.localStorage.setItem('og_token', state.token)
		},
	},
    // 数据包装器
    getters: {
        
    }

}