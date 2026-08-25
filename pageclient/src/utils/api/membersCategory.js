import { getRequest, postRequest } from "../api";

// 第一个参数是data 第二个是param
export const getMembersCategoryListAPI=()=>{
    return getRequest('/members-category/list')
}

