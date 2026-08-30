<template>
  <main class="v3-main culture-v3">
    <section class="v3-container v3-page-head">
      <h1 class="v3-title">小组文化</h1>
    </section>
    <section class="v3-container culture-v3__body">
      <div v-if="loading" class="v3-state">正在加载团队影像…</div>
      <div v-else-if="error" class="v3-state">
        内容暂时无法加载。<button @click="load">重试</button>
      </div>
      <div v-else-if="list.length" class="culture-v3__grid">
        <a
          v-for="item in list"
          :key="item.id"
          :href="href(item)"
          :target="target(item)"
          :rel="rel(item)"
          ><span><img :src="item.image" :alt="item.title" /></span
          ><b>{{ item.title }}</b></a
        >
      </div>
      <div v-else class="v3-state">暂无团队影像</div>
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
import { getTeamCultureListAPI } from "@/utils/api/teamculture";
export default {
  data: () => ({
    query: { currentPage: 1, size: 10, total: 0 },
    list: [],
    loading: true,
    error: false,
  }),
  created() {
    this.load();
  },
  methods: {
    async load() {
      this.loading = true;
      this.error = false;
      try {
        const r = await getTeamCultureListAPI(this.query);
        if (r && r.code === 200) {
          this.list = r.data.data || [];
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
    href: (x) => x.outsideUrl || x.insideUrl || undefined,
    target: (x) => (x.outsideUrl ? "_blank" : null),
    rel: (x) => (x.outsideUrl ? "noopener" : null),
  },
};
</script>
<style lang="less" scoped>
.culture-v3__body {
  padding: 56px 0 94px;
}
.culture-v3__grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
}
.culture-v3__grid a {
  display: block;
  color: inherit;
  text-decoration: none;
}
.culture-v3__grid span {
  display: flex;
  aspect-ratio: 4/3;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  border: 1px solid var(--v3-line);
  background: #eaf1f9;
  transition: border-color 0.22s, box-shadow 0.22s;
}
.culture-v3__grid img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}
.culture-v3__grid a:hover img {
  transform: scale(1.035);
}
.culture-v3__grid a:hover span {
  border-color: rgba(155, 88, 18, 0.46);
  box-shadow: 0 7px 16px rgba(38, 56, 77, 0.08);
}
.culture-v3__grid b {
  display: block;
  min-height: 59px;
  padding: 10px 2px 0;
  font: 700 18px/1.35 var(--v3-display);
}
@media (max-width: 1023px) {
  .culture-v3__grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 739px) {
  .culture-v3__body {
    padding-top: 38px;
  }
  .culture-v3__grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
  .culture-v3__grid b {
    font-size: 16px;
    min-height: 54px;
  }
}
</style>
