<template>
  <main class="v3-main columns-v3">
    <section class="v3-container v3-page-head">
      <h1 class="v3-title">专栏文章</h1>
    </section>
    <section class="v3-container columns-v3__body">
      <div v-if="loading" class="v3-state">正在加载文章…</div>
      <div v-else-if="error" class="v3-state">
        内容暂时无法加载。<button @click="load">重试</button>
      </div>
      <template v-else-if="articles.length">
        <a
          v-if="isFirstPage"
          class="columns-v3__lead"
          :href="href(articles[0])"
          :target="target(articles[0])"
          :rel="rel(articles[0])"
          ><h2>{{ articles[0].newsTitle }}</h2>
          <p>{{ articles[0].newsSummary }}</p>
          <footer>
            <time>{{ date(articles[0].createTime) }}</time
            ><b>阅读全文 ↗</b>
          </footer></a
        >
        <div
          class="columns-v3__index"
          :class="{ 'columns-v3__index--all': !isFirstPage }"
        >
          <a
            v-for="article in indexedArticles"
            :key="article.newsId"
            :href="href(article)"
            :target="target(article)"
            :rel="rel(article)"
            ><time>{{ date(article.createTime) }}</time>
            <div>
              <h3>
                {{ article.newsTitle }}<b v-if="article.isNew === 1">NEW</b>
              </h3>
              <p v-if="article.newsSummary">{{ article.newsSummary }}</p>
            </div>
            <i>↗</i></a
          >
        </div>
      </template>
      <div v-else class="v3-state">暂无文章</div>
      <div class="v3-pager">
        <el-pagination
          @size-change="size"
          @current-change="page"
          :current-page="query.currentPage"
          :page-sizes="[10, 20, 30, 40]"
          :page-size="query.size"
          :pager-count="5"
          layout="total, sizes, prev, pager, next, jumper"
          :total="query.total"
          prev-text="上一页"
          next-text="下一页"
        />
      </div>
    </section>
  </main>
</template>
<script>
import { getNewsListAPI } from "@/utils/api/news";
export default {
  data: () => ({
    query: { currentPage: 1, size: 10, total: 0 },
    articles: [],
    loading: true,
    error: false,
  }),
  created() {
    this.load();
  },
  computed: {
    isFirstPage() {
      return this.query.currentPage === 1;
    },
    indexedArticles() {
      return this.isFirstPage ? this.articles.slice(1) : this.articles;
    },
  },
  methods: {
    async load() {
      this.loading = true;
      this.error = false;
      try {
        const r = await getNewsListAPI(this.query);
        if (r && r.code === 200) {
          this.articles = r.data.data || [];
          Object.assign(this.query, {
            currentPage: r.data.currentPage,
            size: r.data.size,
            total: r.data.total,
          });
        } else this.error = true;
      } catch (e) {
        this.error = true;
      } finally {
        this.loading = false;
      }
    },
    size(v) {
      this.query.size = v;
      this.load();
    },
    page(v) {
      this.query.currentPage = v;
      this.load();
    },
    date: (v) => (v ? v.split(" ")[0] : ""),
    href: (x) => x.outsideUrl || x.insideUrl || undefined,
    target: (x) => (x.outsideUrl ? "_blank" : null),
    rel: (x) => (x.outsideUrl ? "noopener" : null),
  },
};
</script>
<style lang="less" scoped>
.columns-v3__body {
  padding: 56px 0 94px;
}
.columns-v3__lead {
  display: block;
  padding: 40px 48px 32px;
  border: 1px solid var(--v3-line);
  border-top: 3px solid var(--v3-gold);
  background: linear-gradient(120deg, #ffffff 0%, #f5f9fd 66%, #e9f1f9 100%);
  box-shadow: 0 5px 16px rgba(38, 56, 77, 0.05);
  color: var(--v3-ink);
  text-decoration: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.columns-v3__lead:hover {
  border-color: rgba(155, 88, 18, 0.58);
  box-shadow: 0 10px 24px rgba(38, 56, 77, 0.1);
}
.columns-v3__lead h2 {
  max-width: 760px;
  margin: 0 0 15px;
  font: 700 40px/1.28 var(--v3-display);
}
.columns-v3__lead p {
  max-width: 630px;
  margin: 0;
  color: var(--v3-ink-soft);
  font-size: 16px;
}
.columns-v3__lead footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 20px;
  margin-top: 28px;
}
.columns-v3__lead time,
.columns-v3__lead footer b {
  color: var(--v3-gold-deep);
  font: 700 13px/1.4 var(--v3-mono);
}
.columns-v3__lead footer b {
  font-size: 14px;
}
.columns-v3__index {
  margin-top: 34px;
  border-top: 1px solid var(--v3-line);
}
.columns-v3__index--all {
  margin-top: 0;
}
.columns-v3__index a {
  display: grid;
  grid-template-columns: clamp(92px, 11vw, 126px) 1fr 24px;
  gap: 24px;
  padding: 25px 4px;
  border-bottom: 1px solid var(--v3-line);
  color: inherit;
  text-decoration: none;
}
.columns-v3__index a:hover h3 {
  color: var(--v3-gold-deep);
}
.columns-v3__index a:hover i {
  transform: translate(3px, -3px);
}
.columns-v3__index time,
.columns-v3__index h3 b {
  color: var(--v3-gold-deep);
  font: 700 13px/1.4 var(--v3-mono);
}
.columns-v3__index h3 {
  margin: 0;
  font: 700 20px/1.45 var(--v3-sans);
}
.columns-v3__index h3 b {
  margin-left: 8px;
}
.columns-v3__index p {
  margin: 7px 0 0;
  color: var(--v3-ink-soft);
  font-size: 15px;
}
.columns-v3__index i {
  align-self: center;
  color: var(--v3-gold-deep);
  font-size: 21px;
  font-style: normal;
  transition: transform 0.2s;
}
@media (max-width: 739px) {
  .columns-v3__body {
    padding-top: 38px;
  }
  .columns-v3__lead {
    padding: 32px 24px;
  }
  .columns-v3__lead h2 {
    font-size: 31px;
  }
  .columns-v3__lead footer {
    justify-content: space-between;
    gap: 12px;
  }
  .columns-v3__index a {
    grid-template-columns: 1fr 22px;
    gap: 7px;
  }
  .columns-v3__index time {
    grid-column: 1/-1;
  }
  .columns-v3__index h3 {
    font-size: 18px;
  }
}
</style>
