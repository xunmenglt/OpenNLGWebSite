<template>
  <div class="article-container">
    <router-view />
  </div>
</template>

<script>

import Editor from '@/views/dashboard/sidebars/article/editor.vue'

export default {
  components:{
    Editor
  }
}
</script>

<style scoped>
.article-container{
  height: 100%;
}
</style>