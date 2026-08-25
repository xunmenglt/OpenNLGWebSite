<template>
  <div class="teammembers-container">
    <div class="top box">
      <v-btn rounded color="black" dark outlined @click="toCreate">
          <v-icon left>
              mdi-pencil-plus-outline
          </v-icon>
          CREATE MEMBER
      </v-btn>
  </div>
    <div class="btm box">
        <MemberCard v-for="(item) in tableData" :key="item.memberId" :id="item.memberId" 
                    :avatarUrl="item.avatarUrl" 
                    :enName="item.enName" 
                    :cnName="item.cnName" 
                    :memberDesc="item.memberDesc" 
                    :serialNum="item.serialNum"
                    :profession="item.profession"
                    :direction="item.direction"
                    :email="item.email"
                    :ctType="item.ctType"
                    @hanldEditMemberInfo="hanldEditMemberInfo"
                    @hanldDeleteMemberInfo="hanldDeleteMemberInfo"/>
    </div>


    <!-- 删除弹出窗 -->
    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <!-- 添加弹窗 -->
    <v-dialog v-model="addDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="text-h5">New Member</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="9">
                <v-list-item-avatar tile size="80" color="grey">
                  <v-img  :src="createParam.avatarUrl"></v-img>
                </v-list-item-avatar>
                <v-list-item-subtitle>
                  <v-text-field auto-grow :row-height="3" label="头像地址" v-model="createParam.avatarUrl"></v-text-field>
                </v-list-item-subtitle>
              </v-col>
              <v-col cols="3">
                <v-btn
                small
                color="blue-grey"
                class="white--text"
                @click="dialogCropper=true"
              >
                Upload
                <v-icon
                  right
                  dark
                >
                  mdi-cloud-upload
                </v-icon>
              </v-btn>
              </v-col>
              <v-col cols="4">
                <v-text-field label="中文名" v-model="createParam.cnName">
                </v-text-field>
              </v-col>
              <v-col cols="4">
                <v-text-field label="英文名" v-model="createParam.enName">
                </v-text-field>
              </v-col>
              <v-col cols="4">
                <v-text-field type="number" label="序号" v-model="createParam.serialNum">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea outlined auto-grow :row-height="15" label="简介" v-model="createParam.memberDesc" counter="500"></v-textarea>
              </v-col>
              <v-col cols="12">
                <v-text-field label="职业" v-model="createParam.profession">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="研究方向" v-model="createParam.direction">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="邮箱" v-model="createParam.email">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-combobox
                  v-model="createParam.ctType"
                  label="类别"
                  :items='membersCategories'
                  :filter-keys="['ctType']"
                  :item-text="'ctZhName'"
                  :item-value="'ctType'"
                  :return-object="false"
                ></v-combobox>
              </v-col>
              <v-col cols="6">
                <v-text-field label="外链" v-model="createParam.outsideUrl">
                </v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field label="内链" v-model="createParam.insideUrl">
                </v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="createClose">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="doCreate">
            Create
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 编辑弹窗 -->
    <v-dialog v-model="updateDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Edit Member</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="9">
                <v-list-item-avatar tile size="80" color="grey">
                  <v-img  :src="updateParam.avatarUrl"></v-img>
                </v-list-item-avatar>
                <v-list-item-subtitle>
                  <v-text-field auto-grow :row-height="3" label="avatar url" v-model="updateParam.avatarUrl"></v-text-field>
                </v-list-item-subtitle>
              </v-col>
              <v-col cols="3">
                <v-btn
                small
                color="blue-grey"
                class="white--text"
                @click="dialogCropper=true"
              >
                Upload
                <v-icon
                  right
                  dark
                >
                
                  mdi-cloud-upload
                </v-icon>
              </v-btn>
              </v-col>
              <v-col cols="4">
                <v-text-field label="中文名" v-model="updateParam.cnName">
                </v-text-field>
              </v-col>
              <v-col cols="4">
                <v-text-field label="英文名" v-model="updateParam.enName">
                </v-text-field>
              </v-col>
              <v-col cols="4">
                <v-text-field type="number" label="序号" v-model="updateParam.serialNum">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea outlined auto-grow :row-height="15" label="简介" v-model="updateParam.memberDesc" counter="500"></v-textarea>
              </v-col>
              <v-col cols="12">
                <v-text-field label="职业" v-model="updateParam.profession">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="研究方向" v-model="updateParam.direction">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="邮箱" v-model="updateParam.email">
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-combobox
                  v-model="updateParam.ctType"
                  label="类别"
                  :items='membersCategories'
                  :filter-keys="['ctType']"
                  :item-text="'ctZhName'"
                  :item-value="'ctType'"
                  :return-object="false"
                ></v-combobox>
              </v-col>
              <v-col cols="6">
                <v-text-field label="外链" v-model="updateParam.outsideUrl">
                </v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field label="内链" v-model="updateParam.insideUrl">
                </v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="updateClose">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="doUpdate">
            Update
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogCropper">
      <PicCropper @cropperCancel="cropperCancelChange" @cropperConfirm="cropperConfirmChange"></PicCropper>
    </v-dialog>
  </div>
</template>

<script>
import {createMembersAPI, deleteMembersAPI, getMembersItemAPI, getMembersListAPI, updateMembersAPI} from '@/utils/api/members'
import MemberCard from '@/components/member-card'
import PicCropper from '@/components/pic-cropper'
import { uploadFileAPI } from '@/utils/api/file'
import {getMembersCategoryListAPI} from '@/utils/api/membersCategory'
export default {
  components:{
    MemberCard,
    PicCropper
  },
  data() {
    return {
      tableData:[],
      membersCategories:[],
      dialogDelete: false,
      tableIsLoading:false,
      dialogCropper:false,
      addDialog:false,
      updateDialog:false,
      deleteItem:null,
      defaultParam:{  
        "avatarUrl": "",  
        "cnName": "", 
        "enName": ""  ,
        "memberDesc": "", 
        "serialNum":"",
        "outsideUrl":"",
        "insideUrl":"",
        "profession":"",
        "direction":"",
        "email":"",
        "ctType":""
      },
      createParam:{
        "avatarUrl": "",  
        "cnName": "", 
        "enName": ""  ,
        "memberDesc": "", 
        "serialNum":"",
        "outsideUrl":"",
        "insideUrl":"",
        "profession":"",
        "direction":"",
        "email":"",
        "ctType":""
      },
      updateParam:{
        "avatarUrl": "",  
        "cnName": "", 
        "enName": ""  ,
        "memberDesc": "", 
        "serialNum":"",
        "outsideUrl":"",
        "insideUrl":"",
        "profession":"",
        "direction":"",
        "email":"",
        "ctType":""
      }
    }
  },
  created(){
    this.initialize()
  },
  methods:{
    initMembersCategories(){
      getMembersCategoryListAPI().then((res)=>{
        this.membersCategories=res.data
      })
    },
    async hanldEditMemberInfo(e){
      if (e){
        const res=await getMembersItemAPI({"membersId":e})
        if(res&&res.code&&res.code===200){
          this.updateDialog=true
          this.updateParam=Object.assign({}, res.data)
        }
      }      
    },
    async doUpdate(){
      const res = await updateMembersAPI(this.updateParam)
      if(res&&res.code&&res.code===200){
        this.flashTable()
        this.updateClose()
      }
    },
    updateClose(){
      this.updateDialog = false
      this.$nextTick(() => {
        this.updateParam = Object.assign({}, this.defaultParam)
      })
    },

    hanldDeleteMemberInfo(e){
      this.dialogDelete = true
      this.deleteItem=e
    },

    async deleteItemConfirm() {
      if(this.deleteItem){
        const res=await deleteMembersAPI(this.deleteItem)
        if (res&&res.code&&res.code===200){
          this.flashTable()
        }
      }
      this.closeDelete()
    },
    closeDelete() {
      this.dialogDelete = false
      this.deleteItem=null
    },


    // 刷新数据
    async flashTable(){
      this.tableIsLoading=true
      try{
        const res = await getMembersListAPI()

        if(res.code==200){
          this.tableData=res.data
        }else{
          showTextMessage('warning',res.message)
        }
      } finally{
        this.tableIsLoading=false
      }

    },
    
    initialize() {
      this.flashTable()  
      this.initMembersCategories()
    },
    toCreate(){
      this.addDialog=true
      this.createParam.serialNum=this.tableData.length+1
    },
    async doCreate(){
      const res = await createMembersAPI(this.createParam)
      if(res&&res.code&&res.code===200){
        this.flashTable()
        this.createClose()
      }
    },
    createClose() {
      this.addDialog = false
      this.$nextTick(() => {
        this.createParam = Object.assign({}, this.defaultParam)
      })
    },
    cropperCancelChange(){
      this.dialogCropper=false
    },
    async cropperConfirmChange(e){
      if(e){
          const formData = new FormData();
          formData.append('file', e);
          const res =await uploadFileAPI(formData)
          if(res&&res.code&&res.code===200){
            this.createParam.avatarUrl=res.data

            this.updateParam.avatarUrl=res.data

          }
      }
      this.dialogCropper=false
    }
  }
}
</script>

<style lang="less" scoped>
.teammembers-container{
  height: 100%;
  width: 100%; 
  display: flex;
  flex-direction: column;
}
.box{
  width: 100%;
}
.btm{
  flex: 1;
  overflow: hidden;
  overflow-y: auto;
  flex-wrap: wrap;
  display: flex;
  padding: 10px;
}
.top{
  padding: 10px;
  border-bottom: 1px solid #c4c4c4;
}
</style>