<template>
  <v-data-table
    :headers="headers" 
    :items="tableData" 
    :loading="tableIsLoading"
    :server-items-length="footBarParams.total"
    @update:options="optionsChanged"
    height="80%"
    class="elevation-1">
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Lab Publication</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>

        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              New Item
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="9">
                    <v-list-item-avatar tile :width="250" :height="140.5" color="grey">
                      <v-img :src="editedItem.publicationCover"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-subtitle>
                      <v-text-field auto-grow :row-height="3" label="cover url" v-model="editedItem.publicationCover"></v-text-field>
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
                  <v-col cols="12">
                    <v-text-field label="publication title" v-model="editedItem.publicationTitle">
                    </v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field label="publication desc" v-model="editedItem.publicationDesc">
                    </v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field label="outside url" v-model="editedItem.outsideUrl">
                    </v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field label="inside url" v-model="editedItem.insideUrl">
                    </v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">
                Cancel
              </v-btn>
              <v-btn color="blue darken-1" text @click="save">
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

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
      </v-toolbar>
      <v-dialog v-model="dialogCropper">
        <PicCropper :width="250" :height="140.5" @cropperCancel="cropperCancelChange" @cropperConfirm="cropperConfirmChange"></PicCropper>
      </v-dialog>
    </template>

    <template v-slot:item.actions="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)">
        mdi-pencil
      </v-icon>
      <v-icon small @click="deleteItem(item)">
        mdi-delete
      </v-icon>
    </template>

    <template v-slot:no-data>
        <v-btn icon color="green">
          <v-icon>mdi-cached</v-icon>
        </v-btn>
    </template>

    <!-- 设置单元格大小和样式 -->
    <template v-slot:item.publicationCover="{ item }">
      <div class="img-con">
        <img style="width:100px" :src="item.publicationCover"/>
      </div>
    </template>
    <template v-slot:item.publicationTitle="{ item }">
      <Cell :content="item.publicationTitle" :width="'150px'" :lines="2"/>
    </template>
    <template v-slot:item.outsideUrl="{ item }">
      <Cell :content="item.outsideUrl" :width="'100px'"/>
    </template>
    <template v-slot:item.insideUrl="{ item }">
      <Cell :content="item.insideUrl" :width="'100px'"/>
    </template>

  </v-data-table>
</template>

<script>
import { showTextMessage } from '@/plugins/toastification'
import Cell from '@/components/cell'
import PicCropper from '@/components/pic-cropper'
import { createPublicationAPI, deletePublicationAPI, getPublicationItemAPI, getPublicationListAPI, updatePublicationAPI } from '@/utils/api/publication'
import { uploadFileAPI } from '@/utils/api/file'
export default {
  components:{
    Cell,
    PicCropper
  },
  data: () => ({
    dialog: false,
    dialogDelete: false,
    tableIsLoading:false,
    dialogCropper:false,
    headers: [
      {text: 'id',value: 'publicationId'},
      {text:"cover",value:"publicationCover",sortable:false},
      { text: 'title', value: 'publicationTitle',sortable: false },
      { text: 'desc', value: 'publicationDesc',sortable: false },
      { text: 'outside url', value: 'outsideUrl',sortable: false },
      { text: 'inside url', value: 'insideUrl',sortable: false },
      { text: 'create time', value: 'createTime' },
      { text: 'actions', value: 'actions', sortable: false },
    ],
    footBarParams:{
        currentPage:1,
        size:10,
        total:0
    },
    tableData: [],
    editedIndex: -1,
    editedItem: {
      "createTime": "",
      "insideUrl": "",
      "outsideUrl": "",
      "publicationCover": "",
      "publicationDesc": "",
      "publicationId": 0,
      "publicationTitle": "",
      "updateTime": ""
    },
    defaultItem: {
      "createTime": "",
      "insideUrl": "",
      "outsideUrl": "",
      "publicationCover": "",
      "publicationDesc": "",
      "publicationId": 0,
      "publicationTitle": "",
      "updateTime": ""
    },
  }),
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },

  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },

  created() {
    // this.initialize()
  },

  methods: {
    // 刷新数据
    async flashTable(){
      this.tableIsLoading=true
      try{
        const res = await getPublicationListAPI({currentPage:this.footBarParams.currentPage,size:this.footBarParams.size})
        if(res.code==200){
          this.tableData=res.data.data
          this.footBarParams.size=res.data.size
          this.footBarParams.currentPage = res.data.currentPage
          this.footBarParams.total=res.data.total
        }else{
          showTextMessage('warning',res.message)
        }
      } finally{
        this.tableIsLoading=false
      }

    },

    async addItem(data){
      await createPublicationAPI(data)
    },

    async updateItem(data){
      await updatePublicationAPI(data)
    },

    initialize() {
      this.flashTable()  
    },

    editItem(item) {
      this.editedIndex=item.publicationId
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item) {
      this.editedIndex = this.tableData.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    async deleteItemConfirm() {
      await deletePublicationAPI(this.editedItem.publicationId)
      this.closeDelete()
    },

    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
      this.flashTable()
    },

    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
      this.flashTable()
    },

    async save() {
      if (this.editedIndex > -1) {
        // 修改
        await this.updateItem(this.editedItem)
      } else {
        // 添加
        this.editedItem.publicationId=null
        await this.addItem(this.editedItem)
      }
      this.close()
    },
    optionsChanged(e){
      this.footBarParams.currentPage=e.page
      this.footBarParams.size=e.itemsPerPage
      this.flashTable()
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
            this.editedItem.publicationCover=res.data
          }
      }
      this.dialogCropper=false
    }
  },
}
</script>

<style lang="less" scoped>

.outsideUrl-cell{
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100px;
}
.insideUrl-cell{
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100px;
}
.v-data-table{
  height: 98%;
}
.img-con{
  padding: 10px;
  img{
    box-shadow: 0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)!important;

  }
}
</style>