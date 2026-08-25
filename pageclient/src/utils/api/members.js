import { getRequest, postRequest } from "../api";

// 第一个参数是data 第二个是param
export const getMembersListAPI=()=>{
    return getRequest('/members/list')
}

export const getCoverMembersListAPI=()=>{
    return getRequest('/members/coverlist')
}

export const getMembersItemAPI=(param)=>{
    return getRequest('/members/item',null,param)
}

export const createMembersAPI=(data)=>{
    return postRequest('/members/create',data)
}

export const deleteMembersAPI=(id)=>{
    return postRequest(`/members/delete/${id}`)
}

export const updateMembersAPI=(data)=>{
    return postRequest('/members/update',data)
}

