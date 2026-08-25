import { getRequest, postRequest } from "../api";

// 第一个参数是data 第二个是param
export const getTeamCultureListAPI=(param)=>{
    return getRequest('/team-culture/list',null,param)
}

export const getTeamCultureItemAPI=(param)=>{
    return getRequest('/team-culture/item',null,param)
}

export const createTeamCultureAPI=(data)=>{
    return postRequest('/team-culture/create',data)
}

export const deleteTeamCultureAPI=(id)=>{
    return postRequest(`/team-culture/delete/${id}`)
}

export const updateTeamCultureAPI=(data)=>{
    return postRequest('/team-culture/update',data)
}

