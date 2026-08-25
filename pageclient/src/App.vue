<template>
  <v-app class="app-container">
    <v-main class="main-container">
      <router-view/>
    </v-main>
    <Foot/>
  </v-app>
</template>

<script>
import Foot from '@/components/foot'
export default {
  name: 'App',
  components:{
    Foot
  },
}
</script>
<style>
</style>