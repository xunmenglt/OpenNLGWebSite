<template>
  <v-data-table :headers="headers" :items="tableData" :loading="tableIsLoading" :server-items-length="footBarParams.total"
    @update:options="optionsChanged" height="70%" class="elevation-1">
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Lab NEWS</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>

        <v-dialog v-model="dialog" max-width="500px">
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
                  <v-col cols="12">
                    <v-textarea auto-grow :row-height="3" label="news title" v-model="editedItem.newsTitle"></v-textarea>
                  </v-col>
                  <v-col cols="12">
                    <v-textarea outlined auto-grow :row-height="15" label="news content"
                      v-model="editedItem.newsSummary"></v-textarea>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field label="outside url" v-model="editedItem.outsideUrl">
                    </v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field label="inside url" v-model="editedItem.insideUrl">
                    </v-text-field>
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
                  <v-col cols="12" sm="6" md="4">
                    <v-menu ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="date"
                      transition="scale-transition" offset-y min-width="auto">
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field v-model="date" label="create Time" prepend-icon="mdi-calendar" readonly
                          v-bind="attrs" v-on="on"></v-text-field>
                      </template>
                      <v-date-picker v-model="date" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu = false">
                          Cancel
                        </v-btn>
                        <v-btn text color="primary" @click="selectCreateTime(date)">
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
    <template v-slot:item.newsTitle="{ item }">
      <Cell :content="item.newsTitle" :width="'150px'" />
    </template>
    <template v-slot:item.newsSummary="{ item }">
      <Cell :content="item.newsSummary" :width="'250px'" :lines="2" />
    </template>
    <template v-slot:item.outsideUrl="{ item }">
      <Cell :content="item.outsideUrl" :width="'100px'" />
    </template>
    <template v-slot:item.insideUrl="{ item }">
      <Cell :content="item.insideUrl" :width="'100px'" />
    </template>

  </v-data-table>
</template>

<script>
import { createNewsAPI, deleteNewsAPI, getNewsListAPI, updateNewsAPI } from '@/utils/api/news'
import { showTextMessage } from '@/plugins/toastification'
import Cell from '@/components/cell'
export default {
  components: {
    Cell
  },
  data: () => ({
    dialog: false,
    dialogDelete: false,
    tableIsLoading: false,
    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    menu: false,
    headers: [
      { text: 'id', value: 'newsId' },
      { text: 'title', value: 'newsTitle', sortable: false },
      { text: 'summary', value: 'newsSummary', sortable: false },
      { text: 'read times', value: 'newsReadTimes', align: "center" },
      { text: 'outside url', value: 'outsideUrl', sortable: false },
      { text: 'inside url', value: 'insideUrl', sortable: false },
      { text: 'create time', value: 'createTime' },
      { text: 'actions', value: 'actions', sortable: false },
    ],
    footBarParams: {
      currentPage: 1,
      size: 10,
      total: 0
    },
    tableData: [],
    editedIndex: -1,
    editedItem: {
      "newsTitle": '',
      "newsSummary": '',
      "outsideUrl": '',
      "insideUrl": '',
      "createTime": '',
      'isNew':0
    },
    defaultItem: {
      "newsTitle": '',
      "newsSummary": '',
      "outsideUrl": '',
      "insideUrl": '',
      "createTime": '',
      'isNew':0
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
    async flashTable() {
      this.tableIsLoading = true
      try {
        const res = await getNewsListAPI({ currentPage: this.footBarParams.currentPage, size: this.footBarParams.size })
        if (res.code == 200) {
          this.tableData = res.data.data
          this.footBarParams.size = res.data.size
          this.footBarParams.currentPage = res.data.currentPage
          this.footBarParams.total = res.data.total
        } else {
          showTextMessage('warning', res.message)
        }
      } finally {
        this.tableIsLoading = false
      }

    },
    toAddItem(){
      this.date=(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)
    },
    async addItem(data) {
      await createNewsAPI(data)
    },

    async updateItem(data) {
      await updateNewsAPI(data)
    },

    initialize() {
      this.flashTable()
    },

    editItem(item) {
      this.editedIndex = item.newsId
      this.date=item.createTime.replaceAll('/','-')
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item) {
      this.editedIndex = this.tableData.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    async deleteItemConfirm() {
      await deleteNewsAPI(this.editedItem.newsId)
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
          newsId: this.editedItem.newsId,
          insideUrl: this.editedItem.insideUrl,
          newsSummary: this.editedItem.newsSummary,
          newsTitle: this.editedItem.newsTitle,
          outsideUrl: this.editedItem.outsideUrl,
          createTime:this.date,
          isNew:this.editedItem.isNew
        })
      } else {
        // 添加
        await this.addItem({
          insideUrl: this.editedItem.insideUrl,
          newsSummary: this.editedItem.newsSummary,
          newsTitle: this.editedItem.newsTitle,
          outsideUrl: this.editedItem.outsideUrl,
          createTime:this.date,
          isNew:this.editedItem.isNew
        })
      }
      this.close()
    },
    optionsChanged(e) {
      this.footBarParams.currentPage = e.page
      this.footBarParams.size = e.itemsPerPage
      this.flashTable()
    },
    selectCreateTime(date){
      this.editedItem.createTime=date
      this.$refs.menu.save(date)
    }
  },
}
</script>

<style lang="less" scoped>
.outsideUrl-cell {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100px;
}

.insideUrl-cell {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100px;
}

.v-data-table {
  height: 98%;
}
</style>