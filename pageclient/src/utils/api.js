import axios from "axios";
import router from "@/router";
import {applicationContext} from '@/utils/resources.js'
import { showTextMessage } from "@/plugins/toastification";

const offlineData =
  typeof window !== "undefined" ? window.__OPENNLG_OFFLINE_DATA__ : null;

const value = (item, key) => String(item[key] == null ? "" : item[key]).toLowerCase();
const page = (items, params = {}) => {
  const currentPage = Math.max(1, Number(params.currentPage) || 1);
  const size = Math.max(1, Number(params.size) || 10);
  return { currentPage, size, total: items.length, data: items.slice((currentPage - 1) * size, currentPage * size) };
};
const success = (data) => Promise.resolve({ code: 200, message: "SUCCESS", data });
const offlineGet = (url, params = {}) => {
  if (!offlineData) return null;
  const data = offlineData;
  if (url === "/members/coverlist" || url === "/members/list") return success(data.members || []);
  if (url === "/news/list") return success(page(data.news || [], params));
  if (url === "/team-culture/list") return success(page(data.culture || [], params));
  if (url === "/reserarch/options") return success(data.researchOptions || {});
  if (url === "/reserarch/list") {
    const result = (data.research || []).filter((item) => {
      const year = String(item.publicationYear || value(item, "createTime").slice(0, 4));
      const keyword = value(params, "keyword");
      return (!params.direction || item.researchDirection === params.direction) &&
        (!params.year || year === String(params.year)) &&
        (!params.type || item.publicationType === params.type) &&
        (!params.resource || value(item, "reserarchSource").includes(value(params, "resource"))) &&
        (!params.venue || item.venueShortName === params.venue) &&
        (!params.author || value(item, "reserarchAuthor").includes(value(params, "author"))) &&
        (!params.title || value(item, "reserarchTitle").includes(value(params, "title"))) &&
        (!keyword || value(item, "reserarchTitle").includes(keyword) || value(item, "reserarchAuthor").includes(keyword));
    });
    return success(page(result, params));
  }
  return Promise.resolve({ code: 404, message: "离线包不包含此接口" });
};

//设置基路径
// axios.defaults.baseURL = "http://"+endIp+"/businc/v1/api"
axios.defaults.baseURL = applicationContext.protocol+"://"+applicationContext.host+':'+applicationContext.port+applicationContext.prefix

// 设置请求拦截器，对请求操作进行拦截
axios.interceptors.request.use(config=>{
    //如果存在token，那么请求就携带该token
    const token=window.localStorage.getItem('og_token')
    
    if(token){
        config.headers['Authorization']=token
    }
    
    return config
},
error=>{
    showTextMessage('error','请求拦截未知错误')
})

// 设置响应拦截器，对响应结果进行拦截
axios.interceptors.response.use(
  (success) => {
    //业务逻辑处理
    if (
      success.data.code == 500 ||
      success.data.code == 401 ||
      success.data.code == 403
    ) {
      if (success.config && success.config.skipAuthRedirect) {
        return Promise.reject(new Error(success.data.message || "请求未完成"));
      }
      showTextMessage("error", success.data.message);
      if (success.data.code == 401) {
        window.localStorage.removeItem("og_token");
        router.replace("/index");
      }
      return;
    }
    if (success.data.message && success.data.message != "SUCCESS") {
      showTextMessage("success", success.data.message);
    }
    return success.data;
  },
  (error) => {
    if (error.config && error.config.skipAuthRedirect) {
      return Promise.reject(error);
    }
    if (error.response) {
      if (error.response.status == 504 || error.response.status == 404) {
        showTextMessage("error", "服务器被吃了＞︿＜");
      } else if (error.response.status == 403) {
        showTextMessage("error", "权限不足，请联系管理员");
      } else if (error.response.status == 401) {
        showTextMessage("error", error.response.data.message);
        window.localStorage.removeItem("og_token");
        router.replace("/index");
      } else {
        if (error.response.data.message) {
          showTextMessage("error", error.response.data.message);
        } else {
          showTextMessage("error", "未知错误≡(▔﹏▔)≡");
        }
      }
    } else {
      showTextMessage("error", "请稍后重试，服务器更新中");
    }
    return;
  }
);

let base=''

//传送json格式的post请求
export const postRequest=(url,data,params)=>{
    return axios({
        method:'post',
        url:`${base}${url}`,
        data,
        params
    })
}

//传送json格式的get请求
export const getRequest=(url,data,params,options={})=>{
    const response = offlineGet(url, params);
    if (response) return response;
    return axios({
        ...options,
        method:'get',
        url:`${base}${url}`,
        data:data,
        params:params
    })
}


//传送json格式的delete请求
export const deleteRequest=(url,data,params)=>{
    return axios({
        method:'delete',
        url:`${base}${url}`,
        data,
        params
    })
}

//传送json格式的put请求
export const putRequest=(url,params)=>{
    return axios({
        method:'put',
        url:`${base}${url}`,
        data:params
    })
}

export const uploadFile=(url,formData)=>{
    return axios({
      url: `${base}${url}`,
      method: 'post',
      data: formData,
      headers: { 'Content-Type': 'multipart/form-data' },
    })
}
