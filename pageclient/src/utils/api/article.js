import { getRequest, postRequest } from "../api";

// 第一个参数是data 第二个是param
export const getArticleListAPI=(param)=>{
    return getRequest('/article/list',null,param)
}

export const getArticleItemAPI=(param)=>{
    return getRequest('/article/item',null,param)
}

export const createArticleAPI=(data)=>{
    return postRequest('/article/create',data)
}

export const deleteArticleAPI=(id)=>{
    return postRequest(`/article/delete/${id}`)
}

export const updateArticleAPI=(data)=>{
    return postRequest('/article/update',data)
}

