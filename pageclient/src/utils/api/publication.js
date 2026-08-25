import { getRequest, postRequest } from "../api";

// 第一个参数是data 第二个是param
export const getPublicationListAPI=(param)=>{
    return getRequest('/publication/list',null,param)
}

export const getPublicationItemAPI=(param)=>{
    return getRequest('/publication/item',null,param)
}

export const createPublicationAPI=(data)=>{
    return postRequest('/publication/create',data)
}

export const deletePublicationAPI=(id)=>{
    return postRequest(`/publication/delete/${id}`)
}

export const updatePublicationAPI=(data)=>{
    return postRequest('/publication/update',data)
}

