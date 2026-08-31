import Vue from "vue";
import VueRouter from "vue-router";
import PublicLayout from "@/redesign-v3/PublicLayout.vue";
import Home from "@/redesign-v3/views/Home.vue";
import People from "@/redesign-v3/views/People.vue";
import Students from "@/redesign-v3/views/Students.vue";
import Research from "@/redesign-v3/views/Research.vue";
import Publications from "@/redesign-v3/views/Publications.vue";
import Columns from "@/redesign-v3/views/Columns.vue";
import Culture from "@/redesign-v3/views/Culture.vue";
import Contact from "@/redesign-v3/views/Contact.vue";

Vue.use(VueRouter);

// The offline bundle intentionally contains public pages only.  Static imports
// keep Vue CLI from emitting route chunks that a standalone HTML cannot load.
export default new VueRouter({
  mode: "hash",
  scrollBehavior(to, from, savedPosition) {
    // Keep offline preview navigation consistent with the normal V3 site.
    if (savedPosition) return savedPosition;
    if (to.path === from.path) return false;
    return { x: 0, y: 0 };
  },
  routes: [
    {
      path: "/",
      component: PublicLayout,
      meta: { redesign: true },
      redirect: "/index",
      children: [
        { path: "index", component: Home, meta: { title: "欢迎访问 OpenNLG 小组" } },
        { path: "ryjs", component: People, meta: { title: "人员介绍" } },
        { path: "ryjs1", redirect: "/ryjs" },
        { path: "ryjs/students", component: Students, meta: { title: "学生名录" } },
        { path: "yjfx", component: Research, meta: { title: "研究方向" } },
        { path: "fblw", component: Publications, meta: { title: "发表论文" } },
        { path: "zlwz", component: Columns, meta: { title: "专栏文章" } },
        { path: "tjhd", component: Culture, meta: { title: "小组文化" } },
        { path: "lxwm", component: Contact, meta: { title: "联系我们" } },
      ],
    },
  ],
});
