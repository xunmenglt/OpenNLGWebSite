<template>
  <div>
    <NavBar></NavBar>
    <AppMain></AppMain>
  </div>
</template>

<script>
import {AppMain,NavBar,FootBar} from './components'
export default {
    components:{AppMain,NavBar,FootBar},
    data() {
      return {
        drawer:true
      }
    },
}
</script>

<style>

</style>./components/index.js