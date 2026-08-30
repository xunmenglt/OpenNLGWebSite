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
        <v-toolbar-title>Lab Reserarch</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>

        <v-dialog v-model="dialog" max-width="880px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on" @click="toAddItem">
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
                      <v-img :src="editedItem.reserarchCover"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-subtitle>
                      <v-text-field auto-grow :row-height="3" label="cover url" v-model="editedItem.reserarchCover"></v-text-field>
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
                    <v-text-field label="reserarch title" v-model="editedItem.reserarchTitle">
                    </v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field label="reserarch source" v-model="editedItem.reserarchSource">
                    </v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field label="authors" v-model="editedItem.reserarchAuthor">
                    </v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="publication year" type="number" v-model.number="editedItem.publicationYear"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select label="publication type" :items="publicationTypes" v-model="editedItem.publicationType"></v-select>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="research direction" v-model="editedItem.researchDirection"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="venue short name" v-model="editedItem.venueShortName"></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <span>item is new?</span>
                    <v-radio-group row v-model="editedItem.isNew">

                      <v-radio :value="1" :label="'YES'">

                      </v-radio>
                      
                      <v-radio :value="0" :label="'NO'">

                      </v-radio>
                      
                    </v-radio-group>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field label="outside url" v-model="editedItem.outsideUrl">
                    </v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field label="inside url" v-model="editedItem.insideUrl">
                    </v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="PDF url" v-model="editedItem.pdfUrl"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="DOI url" v-model="editedItem.doiUrl"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="code url" v-model="editedItem.codeUrl"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="project url" v-model="editedItem.projectUrl"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-menu ref="menuCreate" v-model="menuCreate" :close-on-content-click="false" :return-value.sync="dateCreate"
                      transition="scale-transition" offset-y min-width="auto">
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field v-model="dateCreate" label="create Time" prepend-icon="mdi-calendar" readonly
                          v-bind="attrs" v-on="on"></v-text-field>
                      </template>
                      <v-date-picker v-model="dateCreate" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menuCreate = false">
                          Cancel
                        </v-btn>
                        <v-btn text color="primary" @click="selectCreateTime(dateCreate)">
                          OK
                        </v-btn>
                      </v-date-picker>
                    </v-menu>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-menu ref="menuUpdate" v-model="menuUpdate" :close-on-content-click="false" :return-value.sync="dateUpdate"
                      transition="scale-transition" offset-y min-width="auto">
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field v-model="dateUpdate" label="update Time" prepend-icon="mdi-calendar" readonly
                          v-bind="attrs" v-on="on"></v-text-field>
                      </template>
                      <v-date-picker v-model="dateUpdate" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menuUpdate = false">
                          Cancel
                        </v-btn>
                        <v-btn text color="primary" @click="selectUpdateTime(dateUpdate)">
                          OK
                        </v-btn>
                      </v-date-picker>
                    </v-menu>
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
    <template v-slot:item.reserarchCover="{ item }">
      <div class="img-con">
        <img style="width:100px" :src="item.reserarchCover"/>
      </div>
    </template>
    <template v-slot:item.reserarchTitle="{ item }">
      <Cell :content="item.reserarchTitle" :width="'150px'" :lines="2"/>
    </template>
    <template v-slot:item.reserarchSource="{ item }">
      <Cell :content="item.reserarchSource" :width="'150px'" :lines="2"/>
    </template>
    <template v-slot:item.reserarchAuthor="{ item }">
      <Cell :content="item.reserarchAuthor" :width="'150px'" :lines="2"/>
    </template>
    <template v-slot:item.isNew="{ item }">
      <span v-if="item.isNew">YES</span>
      <span v-else>NO</span>
    </template>
    <template v-slot:item.outsideUrl="{ item }">
      <Cell :content="item.outsideUrl" :width="'100px'"/>
    </template>
    <template v-slot:item.insideUrl="{ item }">
      <Cell :content="item.insideUrl" :width="'100px'"/>
    </template>
    <template v-slot:item.updateTime="{ item }">
      <Cell :content="item.updateTime" :width="'150px'"/>
    </template>

  </v-data-table>
</template>

<script>
import { showTextMessage } from '@/plugins/toastification'
import Cell from '@/components/cell'
import PicCropper from '@/components/pic-cropper'
import { createReserarchAPI, deleteReserarchAPI, getReserarchListAPI, updateReserarchAPI } from '@/utils/api/reserarch'
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
    // date pickers like news.vue
    dateCreate: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    dateUpdate: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    menuCreate: false,
    menuUpdate: false,
    publicationTypes: [
      { text: 'Conference Papers', value: 'conference' },
      { text: 'Journal Articles', value: 'journal' },
      { text: 'Preprint Articles', value: 'preprint' },
      { text: 'Books', value: 'book' },
    ],
    headers: [
      {text: 'id',value: 'reserarchId'},
      {text:"cover",value:"reserarchCover",sortable:false},
      { text: 'title', value: 'reserarchTitle',sortable: false },
      { text: 'source', value: 'reserarchSource',sortable: false },
      { text: 'authors', value: 'reserarchAuthor',align:"center" },
      { text: 'year', value: 'publicationYear', sortable: false },
      { text: 'type', value: 'publicationType', sortable: false },
      { text: 'direction', value: 'researchDirection', sortable: false },
      { text: 'venue', value: 'venueShortName', sortable: false },
      { text: 'isNew', value: 'isNew', sortable: false },
      { text: 'outside url', value: 'outsideUrl',sortable: false },
      { text: 'inside url', value: 'insideUrl',sortable: false },
      { text: 'create time', value: 'createTime' },
      { text: 'update time', value: 'updateTime' },
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
      "isNew": 1,
      "outsideUrl": "",
      "publicationYear": null,
      "publicationType": "conference",
      "researchDirection": "",
      "venueShortName": "",
      "pdfUrl": "",
      "doiUrl": "",
      "codeUrl": "",
      "projectUrl": "",
      "reserarchAuthor": "",
      "reserarchCover": "",
      "reserarchId": 0,
      "reserarchSource": "",
      "reserarchTitle": "",
      "updateTime": ""
    },
    defaultItem: {
      "createTime": "",
      "insideUrl": "",
      "isNew": 1,
      "outsideUrl": "",
      "publicationYear": null,
      "publicationType": "conference",
      "researchDirection": "",
      "venueShortName": "",
      "pdfUrl": "",
      "doiUrl": "",
      "codeUrl": "",
      "projectUrl": "",
      "reserarchAuthor": "",
      "reserarchCover": "",
      "reserarchId": 0,
      "reserarchSource": "",
      "reserarchTitle": "",
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
        const res = await getReserarchListAPI({currentPage:this.footBarParams.currentPage,size:this.footBarParams.size})
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
      await createReserarchAPI(data)
    },

    async updateItem(data){
      await updateReserarchAPI(data)
    },

    initialize() {
      this.flashTable()  
    },

    toAddItem(){
      // reset date pickers to today on creating
      const today = (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)
      this.dateCreate = today
      this.dateUpdate = today
    },

    editItem(item) {
      this.editedIndex=item.reserarchId
      this.editedItem = Object.assign({}, item)
      // align with news.vue: convert to yyyy-mm-dd if needed
      this.dateCreate = (item.createTime || '').replace(/\//g,'-') || this.dateCreate
      this.dateUpdate = (item.updateTime || this.dateCreate).replace(/\//g,'-')
      this.dialog = true
    },

    deleteItem(item) {
      this.editedIndex = this.tableData.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    async deleteItemConfirm() {
      await deleteReserarchAPI(this.editedItem.reserarchId)
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
        await this.updateItem({
          reserarchId: this.editedItem.reserarchId,
          reserarchTitle: this.editedItem.reserarchTitle,
          reserarchSource: this.editedItem.reserarchSource,
          reserarchAuthor: this.editedItem.reserarchAuthor,
          publicationYear: this.editedItem.publicationYear,
          publicationType: this.editedItem.publicationType,
          researchDirection: this.editedItem.researchDirection,
          venueShortName: this.editedItem.venueShortName,
          pdfUrl: this.editedItem.pdfUrl,
          doiUrl: this.editedItem.doiUrl,
          codeUrl: this.editedItem.codeUrl,
          projectUrl: this.editedItem.projectUrl,
          reserarchCover: this.editedItem.reserarchCover,
          isNew: this.editedItem.isNew,
          outsideUrl: this.editedItem.outsideUrl,
          insideUrl: this.editedItem.insideUrl,
          createTime: this.dateCreate,
          updateTime: this.dateUpdate,
        })
      } else {
        // 添加
        await this.addItem({
          reserarchId: null,
          reserarchTitle: this.editedItem.reserarchTitle,
          reserarchSource: this.editedItem.reserarchSource,
          reserarchAuthor: this.editedItem.reserarchAuthor,
          publicationYear: this.editedItem.publicationYear,
          publicationType: this.editedItem.publicationType,
          researchDirection: this.editedItem.researchDirection,
          venueShortName: this.editedItem.venueShortName,
          pdfUrl: this.editedItem.pdfUrl,
          doiUrl: this.editedItem.doiUrl,
          codeUrl: this.editedItem.codeUrl,
          projectUrl: this.editedItem.projectUrl,
          reserarchCover: this.editedItem.reserarchCover,
          isNew: this.editedItem.isNew,
          outsideUrl: this.editedItem.outsideUrl,
          insideUrl: this.editedItem.insideUrl,
          createTime: this.dateCreate,
          updateTime: this.dateUpdate,
        })
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
            this.editedItem.reserarchCover=res.data
          }
      }
      this.dialogCropper=false
    },
    selectCreateTime(date){
      this.editedItem.createTime=date
      this.$refs.menuCreate && this.$refs.menuCreate.save && this.$refs.menuCreate.save(date)
    },
    selectUpdateTime(date){
      this.editedItem.updateTime=date
      this.$refs.menuUpdate && this.$refs.menuUpdate.save && this.$refs.menuUpdate.save(date)
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
