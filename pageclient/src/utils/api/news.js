import { getRequest, postRequest } from "../api";

// 第一个参数是data 第二个是param
export const getNewsListAPI=(param)=>{
    return getRequest('/news/list',null,param)
}

export const getNewsItemAPI=(param)=>{
    return getRequest('/news/item',null,param)
}

export const createNewsAPI=(data)=>{
    return postRequest('/news/create',data)
}

export const deleteNewsAPI=(id)=>{
    return postRequest(`/news/delete/${id}`)
}

export const updateNewsAPI=(data)=>{
    return postRequest('/news/update',data)
}

