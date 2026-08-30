<template>
  <div class="v3-page">
    <header class="v3-header" :class="{ 'is-scrolled': scrolled }">
      <div class="v3-container v3-header__inner">
        <router-link class="v3-brand" to="/index" aria-label="OpenNLG 首页"
          ><img :src="logo" alt="OpenNLG" /><b>OpenNLG</b></router-link
        >
        <nav class="v3-nav" aria-label="主导航">
          <router-link v-for="item in nav" :key="item.path" :to="item.path">{{
            item.label
          }}</router-link>
        </nav>
        <button
          class="v3-menu"
          :class="{ 'is-open': open }"
          type="button"
          :aria-label="open ? '关闭导航菜单' : '打开导航菜单'"
          :aria-expanded="String(open)"
          @click="open = !open"
        >
          <i></i><i></i>
        </button>
      </div>
      <nav v-if="open" class="v3-mobile-nav" aria-label="移动端主导航">
        <router-link
          v-for="item in nav"
          :key="item.path"
          :to="item.path"
          @click.native="open = false"
          >{{ item.label }}</router-link
        >
      </nav>
    </header>
    <router-view />
    <footer class="v3-footer">
      <div class="v3-container v3-footer__inner">
        <nav class="v3-footer__nav" aria-label="页脚导航">
          <router-link v-for="item in nav" :key="item.path" :to="item.path">{{
            item.label
          }}</router-link>
        </nav>
        <div class="v3-footer__meta">
          <a href="mailto:ljt@suda.edu.cn">ljt@suda.edu.cn</a
          ><small
            >Copyright {{ new Date().getFullYear() }}. All Rights Reserved By
            OpenNLG.</small
          ><a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener"
            >苏ICP备2023034280号-1</a
          >
        </div>
      </div>
    </footer>
  </div>
</template>
<script>
import logo from "@/assets/logo.jpg";
export default {
  data: () => ({
    logo,
    open: false,
    scrolled: false,
    nav: [
      { label: "首页", path: "/index" },
      { label: "人员介绍", path: "/ryjs" },
      { label: "研究方向", path: "/yjfx" },
      { label: "发表论文", path: "/fblw" },
      { label: "小组文化", path: "/tjhd" },
      { label: "联系我们", path: "/lxwm" },
    ],
  }),
  mounted() {
    window.addEventListener("keydown", this.escape);
    window.addEventListener("scroll", this.updateScroll, { passive: true });
    this.updateScroll();
  },
  beforeDestroy() {
    window.removeEventListener("keydown", this.escape);
    window.removeEventListener("scroll", this.updateScroll);
  },
  methods: {
    escape(e) {
      if (e.key === "Escape") this.open = false;
    },
    updateScroll() {
      this.scrolled = window.scrollY > 12;
    },
  },
};
</script>
