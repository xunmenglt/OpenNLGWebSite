<template>
  <v-app class="app-container">
    <v-main class="main-container">
      <router-view />
    </v-main>
    <Foot v-if="!isRedesign" />
  </v-app>
</template>

<script>
import Foot from "@/components/foot";
export default {
  name: "App",
  components: {
    Foot,
  },
  computed: {
    isRedesign() {
      return this.$route.matched.some(function (route) {
        return route.meta.redesign;
      });
    },
  },
};
</script>
<style></style>
