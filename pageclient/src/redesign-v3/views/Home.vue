<template>
  <main class="v3-main home-v3">
    <section class="v3-container home-v3__hero">
      <div>
        <h1 aria-label="Welcome to OpenNLG.">
          <span>{{ typedSegment(0, 7) }}</span><br />
          <span>{{ typedSegment(8, 3) }}<i>{{ typedSegment(11, 8) }}</i></span
          ><b aria-hidden="true">|</b>
        </h1>
        <p>Gather the knowledge of the world and create wonderful strokes</p>
        <router-link class="v3-link" to="/yjfx">阅读研究方向</router-link>
      </div>
      <figure><img :src="hero" alt="OpenNLG 首页插画" /></figure>
    </section>
    <section class="v3-section v3-section--wash">
      <div class="v3-container">
        <header class="home-v3__head">
          <div>
            <h2>研究方向</h2>
            <span>RESEARCH DIRECTIONS</span>
          </div>
          <router-link class="v3-link" to="/yjfx">全部方向</router-link>
        </header>
        <el-carousel
          class="home-v3__carousel"
          :type="carouselType"
          :height="researchHeight"
          :autoplay="false"
          indicator-position="outside"
          aria-label="研究方向轮播"
          ><el-carousel-item v-for="item in directions" :key="item.title"
            ><router-link class="home-v3__gallery-card" to="/yjfx"
              ><span><img :src="item.image" :alt="item.title" /></span
              ><b>{{ item.title }}</b></router-link
            ></el-carousel-item
          ></el-carousel
        >
      </div>
    </section>
    <section class="v3-section">
      <div class="v3-container">
        <header class="home-v3__head">
          <div>
            <h2>最新消息</h2>
            <span>LATEST NEWS</span>
          </div>
          <router-link class="v3-link" to="/zlwz">文章索引</router-link>
        </header>
        <div v-if="news.length" class="home-v3__news">
          <a :href="href(news[0])" :target="target(news[0])" :rel="rel(news[0])"
            ><time>{{ date(news[0].createTime) }}</time>
            <h3>{{ news[0].newsTitle }}</h3>
            <p>{{ news[0].newsSummary }}</p>
            <b>阅读全文 ↗</b></a
          >
          <div>
            <a
              v-for="item in news.slice(1, 5)"
              :key="item.newsId"
              :href="href(item)"
              :target="target(item)"
              :rel="rel(item)"
              ><time>{{ date(item.createTime) }}</time
              ><b>{{ item.newsTitle }}</b
              ><i>↗</i></a
            >
          </div>
        </div>
        <div v-else class="v3-state">
          {{ newsError ? "最新消息暂时无法加载。" : "正在加载最新消息…" }}
          <button v-if="newsError" @click="loadNews">重试</button>
        </div>
      </div>
    </section>
    <section class="v3-section v3-section--wash">
      <div class="v3-container">
        <header class="home-v3__head">
          <div>
            <h2>团队印象</h2>
            <span>TEAM IMPRESSION</span>
          </div>
          <router-link class="v3-link" to="/tjhd">影像档案</router-link>
        </header>
        <el-carousel
          v-if="culture.length"
          class="home-v3__carousel home-v3__carousel--culture"
          :type="carouselType"
          :height="cultureHeight"
          :autoplay="false"
          indicator-position="outside"
          aria-label="团队印象轮播"
          ><el-carousel-item v-for="item in culture.slice(0, 6)" :key="item.id"
            ><a
              class="home-v3__gallery-card"
              :href="href(item)"
              :target="target(item)"
              :rel="rel(item)"
              ><span><img :src="item.image" :alt="item.title" /></span
              ><b>{{ item.title }}</b></a
            ></el-carousel-item
          ></el-carousel
        >
        <div v-else class="v3-state">
          {{ cultureError ? "团队影像暂时无法加载。" : "正在加载团队影像…" }}
          <button v-if="cultureError" @click="loadCulture">重试</button>
        </div>
      </div>
    </section>
    <section class="home-v3__call">
      <div class="v3-container">
        <div>
          <h2>欢迎加入 OpenNLG</h2>
          <p>欢迎对我们小组感兴趣的同学通过 ljt@suda.edu.cn 联系我们</p>
        </div>
        <router-link to="/lxwm">联系我们 ↗</router-link>
      </div>
    </section>
  </main>
</template>
<script>
import hero from "@/assets/images/homepage.png";
import { getNewsListAPI } from "@/utils/api/news";
import { getTeamCultureListAPI } from "@/utils/api/teamculture";
export default {
  data: () => ({
    hero,
    fullTitle: "Welcome\nto OpenNLG.",
    typedTitle: "",
    typingTimer: null,
    news: [],
    culture: [],
    newsError: false,
    cultureError: false,
    compact: false,
    directions: [
      {
        title: "大语言模型",
        image:
          "https://img2.baidu.com/it/u=664406207,2507014690&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=500",
      },
      {
        title: "自然语言处理",
        image:
          "https://img1.baidu.com/it/u=2033602622,521439758&fm=253&fmt=auto&app=138&f=JPEG?w=683&h=461",
      },
      {
        title: "文本生成",
        image:
          "https://img0.baidu.com/it/u=3326062826,4294308451&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=500",
      },
      {
        title: "大模型应用",
        image:
          "https://img1.baidu.com/it/u=1847612787,2202854552&fm=253&fmt=auto&app=138&f=JPEG?w=666&h=500",
      },
    ],
  }),
  computed: {
    carouselType() {
      return this.compact ? "" : "card";
    },
    researchHeight() {
      if (window.innerWidth < 740) return "302px";
      return this.compact ? "326px" : "354px";
    },
    cultureHeight() {
      if (window.innerWidth < 740) return "238px";
      return this.compact ? "254px" : "278px";
    },
  },
  created() {
    this.loadNews();
    this.loadCulture();
  },
  mounted() {
    this.resize();
    window.addEventListener("resize", this.resize);
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      this.typedTitle = this.fullTitle;
      return;
    }
    let index = 0;
    this.typingTimer = window.setInterval(() => {
      this.typedTitle = this.fullTitle.slice(0, ++index);
      if (index >= this.fullTitle.length) window.clearInterval(this.typingTimer);
    }, 75);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.resize);
    window.clearInterval(this.typingTimer);
  },
  methods: {
    typedSegment(start, length) {
      return this.typedTitle.slice(start, start + length);
    },
    async loadNews() {
      this.newsError = false;
      try {
        const r = await getNewsListAPI({ currentPage: 1, size: 5 });
        if (r && r.code === 200) this.news = r.data.data || [];
        else this.newsError = true;
      } catch (e) {
        this.newsError = true;
      }
    },
    async loadCulture() {
      this.cultureError = false;
      try {
        const r = await getTeamCultureListAPI({ currentPage: 1, size: 6 });
        if (r && r.code === 200) this.culture = r.data.data || [];
        else this.cultureError = true;
      } catch (e) {
        this.cultureError = true;
      }
    },
    resize() {
      this.compact = window.innerWidth < 1024;
    },
    date: (v) => (v ? v.split(" ")[0] : ""),
    href: (x) => x.outsideUrl || x.insideUrl || undefined,
    target: (x) => (x.outsideUrl ? "_blank" : null),
    rel: (x) => (x.outsideUrl ? "noopener" : null),
  },
};
</script>
<style lang="less" scoped>
.home-v3__hero {
  display: grid;
  grid-template-columns: 0.9fr 1.1fr;
  gap: 76px;
  min-height: 600px;
  align-items: center;
}
.home-v3__hero h1 {
  margin: 12px 0 18px;
  font: 700 78px/0.96 var(--v3-display);
  letter-spacing: -0.055em;
}
.home-v3__hero h1 i {
  color: var(--v3-gold-deep);
  font-style: normal;
}
.home-v3__hero h1 b {
  color: var(--v3-gold-deep);
  font-weight: 400;
  animation: home-v3-caret 1.05s steps(1, end) infinite;
}
.home-v3__hero > div > p:not(.v3-kicker) {
  max-width: 360px;
  margin: 0 0 28px;
  color: var(--v3-ink-soft);
  font-size: 17px;
}
.home-v3__hero figure {
  position: relative;
  display: flex;
  margin: 0;
  align-items: center;
  justify-content: center;
}
.home-v3__hero figure::before {
  position: absolute;
  z-index: -1;
  width: 78%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(210, 224, 240, 0.72), transparent 69%);
  content: "";
}
.home-v3__hero figure img {
  display: block;
  max-width: 100%;
  max-height: 400px;
  object-fit: contain;
}
.home-v3__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 30px;
  margin-bottom: 30px;
}
.home-v3__head h2,
.home-v3__call h2 {
  margin: 0;
  font: 700 46px/1.1 var(--v3-display);
}
.home-v3__head span {
  display: block;
  margin-top: 8px;
  color: var(--v3-gold-deep);
  font: 700 14px/1.4 var(--v3-mono);
  letter-spacing: 0.08em;
}
.home-v3__carousel {
  border-top: 1px solid var(--v3-line);
}
.home-v3__carousel ::v-deep .el-carousel__item {
  display: flex;
  justify-content: center;
  padding-top: 10px;
  box-sizing: border-box;
  background: transparent;
}
.home-v3__carousel ::v-deep .el-carousel__arrow {
  width: 38px;
  height: 38px;
  background: rgba(38, 56, 77, 0.78);
}
.home-v3__carousel ::v-deep .el-carousel__indicator button {
  width: 22px;
  height: 2px;
  background: var(--v3-line);
}
.home-v3__carousel ::v-deep .el-carousel__indicator.is-active button {
  background: var(--v3-gold-deep);
}
.home-v3__gallery-card {
  display: flex;
  flex-direction: column;
  width: 460px;
  max-width: 100%;
  height: 100%;
  padding: 10px 10px 0;
  box-sizing: border-box;
  border: 1px solid var(--v3-line);
  background: var(--v3-surface);
  color: inherit;
  text-decoration: none;
}
.home-v3__gallery-card > span {
  display: flex;
  width: 100%;
  aspect-ratio: 11/7;
  align-items: center;
  justify-content: center;
  background: #eaf1f9;
}
.home-v3__gallery-card img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
.home-v3__gallery-card > b {
  display: flex;
  flex: 1;
  align-items: center;
  padding: 0 12px;
  font: 700 22px/1.2 var(--v3-display);
}
.home-v3__carousel--culture .home-v3__gallery-card {
  width: 360px;
}
.home-v3__carousel--culture .home-v3__gallery-card > span {
  min-height: 0;
  flex: 1 1 auto;
  aspect-ratio: auto;
}
.home-v3__carousel--culture .home-v3__gallery-card > b {
  min-height: 56px;
  flex: 0 0 56px;
  box-sizing: border-box;
  font-size: 18px;
  overflow-wrap: anywhere;
}
.home-v3__news {
  display: grid;
  grid-template-columns: 1fr 1fr;
  border-top: 1px solid var(--v3-ink);
}
.home-v3__news a {
  color: inherit;
  text-decoration: none;
}
.home-v3__news a h3,
.home-v3__news a b,
.home-v3__news a i {
  transition: color 0.2s, transform 0.2s;
}
.home-v3__news a:hover h3,
.home-v3__news a:hover b {
  color: var(--v3-gold-deep);
}
.home-v3__news a:hover i {
  transform: translate(3px, -3px);
}
.home-v3__news > a {
  min-height: 240px;
  padding: 28px 42px 28px 0;
  border-right: 1px solid var(--v3-line);
}
.home-v3__news time {
  display: block;
  color: var(--v3-gold-deep);
  font: 700 13px/1.4 var(--v3-mono);
}
.home-v3__news h3 {
  margin: 14px 0 9px;
  font: 700 29px/1.35 var(--v3-display);
}
.home-v3__news p {
  margin: 0;
  color: var(--v3-ink-soft);
  font-size: 15px;
}
.home-v3__news > a > b {
  display: block;
  margin-top: 16px;
}
.home-v3__news > div a {
  display: grid;
  grid-template-columns: 96px 1fr 20px;
  gap: 14px;
  padding: 18px 0 18px 28px;
  border-bottom: 1px solid var(--v3-line);
}
.home-v3__news > div i {
  color: var(--v3-gold-deep);
  font-style: normal;
}
.home-v3__call {
  padding: 76px 0;
}
.home-v3__call .v3-container {
  display: grid;
  grid-template-columns: 1.4fr 0.45fr;
  gap: 30px;
  min-height: 168px;
  align-items: center;
  padding: 34px 44px;
  border: 1px solid var(--v3-line);
  border-left: 4px solid var(--v3-gold);
  background: linear-gradient(112deg, #ffffff 0%, #f4f8fc 58%, #f6efe5 100%);
  box-shadow: 0 8px 22px rgba(38, 56, 77, 0.05);
}
@keyframes home-v3-caret {
  50% {
    opacity: 0;
  }
}
.home-v3__call h2 {
  font-size: 38px;
}
.home-v3__call p {
  margin: 8px 0 0;
}
.home-v3__call a {
  justify-self: end;
  padding: 12px 18px;
  border: 1px solid var(--v3-ink);
  color: inherit;
  font-weight: 800;
  text-decoration: none;
  transition: background 0.2s, color 0.2s;
}
.home-v3__call a:hover {
  background: var(--v3-ink);
  color: #fff;
}
@media (max-width: 1023px) {
  .home-v3__hero {
    gap: 42px;
    min-height: 530px;
  }
  .home-v3__hero h1 {
    font-size: 60px;
  }
}
@media (max-width: 879px) {
  .home-v3__hero {
    grid-template-columns: 1fr;
    gap: 36px;
    min-height: 0;
    padding: 68px 0;
  }
  .home-v3__hero h1 {
    font-size: 56px;
  }
  .home-v3__hero figure {
    justify-content: flex-start;
  }
  .home-v3__hero figure img {
    max-height: 350px;
  }
}
@media (max-width: 739px) {
  .home-v3__hero,
  .home-v3__news {
    grid-template-columns: 1fr;
  }
  .home-v3__hero {
    gap: 38px;
    min-height: 0;
    padding: 62px 0;
  }
  .home-v3__hero h1 {
    font-size: 53px;
  }
  .home-v3__hero figure img {
    max-height: 290px;
  }
  .home-v3__head {
    align-items: flex-start;
  }
  .home-v3__head h2 {
    font-size: 35px;
  }
  .home-v3__news > a {
    padding: 24px 0;
    border-right: 0;
    border-bottom: 1px solid var(--v3-line);
  }
  .home-v3__news > div a {
    padding-left: 0;
    grid-template-columns: 84px 1fr 18px;
  }
  .home-v3__call .v3-container {
    display: block;
    min-height: 0;
    padding: 30px 24px;
  }
  .home-v3__call h2 {
    font-size: 33px;
  }
  .home-v3__call a {
    display: inline-block;
    margin-top: 24px;
  }
}
</style>
