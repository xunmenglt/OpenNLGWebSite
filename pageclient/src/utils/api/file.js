import { uploadFile } from "../api"

export const uploadFileAPI=(formData)=>{
    return uploadFile('/file/upload',formData)
}