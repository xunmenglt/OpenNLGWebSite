export default{
    //开启命名空间
	namespaced: true,
    // state 数据
	state: () => ({
        toPath:''
    }),
    //方法
    mutations:{
        setToPath(state,data){
            state.toPath=data
        },
        clearToPath(state){
            state.toPath=''
        },
        changeMeetingStatus(state,data){
            state.meetingStatus=data
        },
    },
    // 数据包装器
    getters: {
        
    }
}