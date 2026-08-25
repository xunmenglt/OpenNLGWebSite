import { getRequest, postRequest } from "../api";

// 第一个参数是data 第二个是param
export const getReserarchListAPI=(param)=>{
    return getRequest('/reserarch/list',null,param)
}

export const getReserarchItemAPI=(param)=>{
    return getRequest('/reserarch/item',null,param)
}

export const createReserarchAPI=(data)=>{
    return postRequest('/reserarch/create',data)
}

export const deleteReserarchAPI=(id)=>{
    return postRequest(`/reserarch/delete/${id}`)
}

export const updateReserarchAPI=(data)=>{
    return postRequest('/reserarch/update',data)
}

