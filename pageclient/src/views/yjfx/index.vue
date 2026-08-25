<template>
    <div class="rjfx-container opennlg-container">
          <div class="card-container" v-for="(item,index) in rjfx_list" :key="index">
            <v-row :class='[index%2==0?"":"rtl"]'>
              <v-col cols="9" class="content-box">
                <div class="rjfx-title">
                  <span class="h22">
                    {{ item.title }}
                  </span>
                  <div class="clear"></div>
                </div>
                <div class="rjfx-desc">
                  {{ item.desc }}
                </div>
              </v-col>
              <v-col cols="3">
                <div class="fjfx-image">
                  <div class="image-warp">
                    <img :src="item.image" />
                  </div>
                </div>
              </v-col>
            </v-row>
            <div v-if="index!=(rjfx_list.length-1)" style="clear:both;display: block;border-bottom: 1px solid #ccc;padding-top: 3rem;margin-bottom: 5rem;"></div>
          </div>
    </div>
</template>

<script>
import indexjs from './index.js'
export default {
  ...indexjs
}
</script>

<style lang="less" scoped>
@import './index.less';
</style>