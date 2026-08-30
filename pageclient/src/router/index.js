import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "layout",
    redirect: "index",
    component: () => import("@/redesign-v3/PublicLayout.vue"),
    meta: { redesign: true },
    children: [
      {
        path: "index",
        component: () => import("@/redesign-v3/views/Home.vue"),
        meta: {
          title: "欢迎访问 OpenNLG 小组",
        },
      },
      {
        path: "ryjs",
        component: () => import("@/redesign-v3/views/People.vue"),
        meta: {
          title: "人员介绍",
        },
      },
      {
        path: "ryjs1",
        redirect: "/ryjs",
      },
      {
        path: "ryjs/students",
        component: () => import("@/redesign-v3/views/Students.vue"),
        meta: {
          title: "学生名录",
        },
      },
      {
        path: "yjfx",
        component: () => import("@/redesign-v3/views/Research.vue"),
        meta: {
          title: "研究方向",
        },
      },
      {
        path: "fblw",
        component: () => import("@/redesign-v3/views/Publications.vue"),
        meta: {
          title: "发表论文",
        },
      },
      {
        path: "zlwz",
        component: () => import("@/redesign-v3/views/Columns.vue"),
        meta: {
          title: "专栏文章",
        },
      },
      {
        path: "tjhd",
        component: () => import("@/redesign-v3/views/Culture.vue"),
        meta: {
          title: "小组文化",
        },
      },
      {
        path: "lxwm",
        component: () => import("@/redesign-v3/views/Contact.vue"),
        meta: {
          title: "联系我们",
        },
      },
    ],
  },
  {
    path: "/dashboard/login",
    name: "dashboard",
    component: () => import("@/views/dashboard/login.vue"),
    meta: {
      title: "控制台·登录",
    },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    redirect: "/dashboard/index",
    component: () => import("@/views/dashboard/index.vue"),
    children: [
      {
        path: "index",
        name: "index",
        component: () => import("@/views/dashboard/sidebars/welcome.vue"),
        meta: {
          title: "欢迎使用OpenNLG 控制台",
        },
      },
      {
        path: "teammembers",
        name: "teammembers",
        component: () => import("../views/dashboard/sidebars/teammembers.vue"),
        meta: {
          title: "控制台·团队成员",
        },
      },
      {
        path: "news",
        name: "news",
        component: () => import("../views/dashboard/sidebars/news.vue"),
        meta: {
          title: "控制台·团队新闻",
        },
      },
      {
        path: "reserarch",
        name: "reserarch",
        component: () => import("../views/dashboard/sidebars/reserarch.vue"),
        meta: {
          title: "控制台·发表论文",
        },
      },
      {
        path: "publication",
        name: "publication",
        component: () => import("../views/dashboard/sidebars/publication.vue"),
        meta: {
          title: "控制台·小组产品",
        },
      },
      {
        path: "teamculture",
        name: "teamculture",
        component: () => import("@/views/dashboard/sidebars/teamculture.vue"),
        meta: {
          title: "控制台·小组文化",
        },
      },
      {
        path: "articles",
        name: "articles",
        redirect: "/dashboard/articles/list",
        component: () => import("@/views/dashboard/sidebars/articles.vue"),
        meta: {
          title: "控制台·文章管理",
        },
        children: [
          {
            path: "list",
            name: "list",
            component: () =>
              import("@/views/dashboard/sidebars/article/list.vue"),
            meta: {
              title: "控制台·文章管理",
            },
          },
          {
            path: "editor",
            name: "editor",
            component: () =>
              import("@/views/dashboard/sidebars/article/editor.vue"),
            meta: {
              title: "控制台·文章编辑",
            },
          },
        ],
      },

      {
        path: "resources",
        name: "resources",
        component: () => import("@/views/dashboard/sidebars/resources.vue"),
        meta: {
          title: "控制台·小组资源",
        },
      },
    ],
  },
];

const router = new VueRouter({
  // mode:'history',
  routes,
});
router.beforeEach((to, from, next) => {
  if (to.meta) {
    document.title = to.meta.title;
  }
  if (window.localStorage.getItem("og_token")) {
    next();
  } else {
    if (
      to.fullPath.indexOf("dashboard") === -1 ||
      to.fullPath.indexOf("/dashboard/login") !== -1
    ) {
      next();
    } else {
      //保存用户想要访问的路径
      store.commit("m_path/setToPath", to.fullPath);
      next("/dashboard/login");
    }
  }
});
export default router;
