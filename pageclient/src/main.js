import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "@mdi/font/css/materialdesignicons.css";
import "./utils/communication/bus";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import OpenNLGLogImage from "@/assets/logo.jpg";
// 引入全局样式
import "@/assets/css/stype.less";
import "@/redesign-v3/style.less";

// elui
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
Vue.use(ElementUI);

Vue.prototype.OpenNLGLogImage = OpenNLGLogImage;

Vue.use(Toast, {
  transition: "Vue-Toastification__bounce",
  maxToasts: 3,
  newestOnTop: false,
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
