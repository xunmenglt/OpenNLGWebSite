import { postRequest } from "../api";

export const loginApi=(data)=>{
    return postRequest('/auth/login',data)
}