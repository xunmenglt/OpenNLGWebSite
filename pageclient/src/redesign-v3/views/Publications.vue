<template>
  <main class="v3-main publications-v3">
    <section class="v3-container v3-page-head"><h1 class="v3-title">发表论文</h1></section>
    <section class="v3-container publications-v3__body">
      <form class="publications-v3__filters" @submit.prevent="search">
        <label class="publications-v3__field publications-v3__field--keyword"><span>关键词</span><input v-model.trim="filters.keyword" type="search" placeholder="检索论文标题或作者" /></label>
        <label class="publications-v3__field"><span>年份</span><select v-model="filters.year"><option value="">全部年份</option><option v-for="item in options.years" :key="item" :value="item">{{ item }}</option></select></label>
        <label class="publications-v3__field"><span>类型</span><select v-model="filters.type"><option value="">全部类型</option><option v-for="item in typeOptions" :key="item.value" :value="item.value">{{ item.label }}</option></select></label>
        <label class="publications-v3__field"><span>会议 / 期刊</span><select v-model="filters.venue"><option value="">全部来源</option><option v-for="item in venueOptions" :key="item" :value="item">{{ item }}</option></select></label>
        <div class="publications-v3__filter-actions"><button type="button" class="publications-v3__reset" @click="reset">重置</button><button type="submit" class="publications-v3__search">检索</button></div>
      </form>
      <div class="publications-v3__result-bar" aria-live="polite"><span v-if="!loading">共 {{ query.total }} 篇</span><div v-if="activeFilters.length" class="publications-v3__active"><button v-for="item in activeFilters" :key="item.key" type="button" @click="clearFilter(item.key)">{{ item.label }}<i>×</i></button></div></div>
      <div v-if="loading" class="v3-state">正在加载论文库…</div>
      <div v-else-if="error" class="v3-state">内容暂时无法加载。<button @click="load">重试</button></div>
      <div v-else-if="yearGroups.length" class="publications-v3__layout">
        <nav class="publications-v3__years" aria-label="按年份浏览"><a v-for="yearGroup in yearGroups" :key="yearGroup.year" :href="`#publication-year-${yearGroup.year}`">{{ yearGroup.year }}</a></nav>
        <div class="publications-v3__catalogue">
          <section v-for="yearGroup in yearGroups" :id="`publication-year-${yearGroup.year}`" :key="yearGroup.year" class="publications-v3__year">
            <h2>{{ yearGroup.year }}</h2>
            <section v-for="typeGroup in yearGroup.types" :key="typeGroup.key" class="publications-v3__type">
              <header><h3>{{ typeLabel(typeGroup.key) }}</h3><span>{{ typeGroup.count }} 篇</span></header>
              <section v-for="venue in typeGroup.venues" :key="venue.key" class="publications-v3__venue">
                <h4>{{ venue.label }} <small>· {{ venue.items.length }} 篇</small></h4>
                <ol><li v-for="paper in venue.items" :key="paper.reserarchId"><h5>{{ paper.reserarchTitle }}</h5><p>{{ paper.reserarchAuthor }}</p><div class="publications-v3__links"><a v-if="paper.pdfUrl" :href="paper.pdfUrl" target="_blank" rel="noopener">PDF ↗</a><a v-else-if="publicationLink(paper)" :href="publicationLink(paper)" target="_blank" rel="noopener">出版页 ↗</a><span v-else>PDF 待补充</span></div></li></ol>
              </section>
            </section>
          </section>
        </div>
      </div>
      <div v-else class="v3-state">没有符合当前条件的论文</div>
    </section>
  </main>
</template>

<script>
import { getReserarchListAPI, getReserarchOptionsAPI } from "@/utils/api/reserarch";

const emptyFilters = () => ({ keyword: "", year: "", type: "", venue: "" });
const typeLabels = { conference: "会议论文", journal: "期刊论文", preprint: "预印本", book: "著作" };

export default {
  data: () => ({ query: { size: 200, total: 0 }, filters: emptyFilters(), options: { years: [], types: [], venues: [] }, papers: [], loading: true, error: false }),
  computed: {
    typeOptions() { return (this.options.types || []).filter(Boolean).map((value) => ({ value, label: this.typeLabel(value) })); },
    venueOptions() { return (this.options.venues || []).filter(Boolean); },
    activeFilters() {
      const labels = { keyword: "关键词", year: "年份", type: "类型", venue: "来源" };
      return Object.keys(this.filters).filter((key) => this.filters[key] !== "").map((key) => ({ key, label: `${labels[key]}：${key === "type" ? this.typeLabel(this.filters[key]) : this.filters[key]}` }));
    },
    yearGroups() {
      const years = {};
      this.papers.forEach((paper) => {
        const year = String(this.publicationYear(paper) || "未标注年份"); const type = paper.publicationType || "other"; const venue = this.venueName(paper);
        if (!years[year]) years[year] = {}; if (!years[year][type]) years[year][type] = {}; if (!years[year][type][venue]) years[year][type][venue] = []; years[year][type][venue].push(paper);
      });
      return Object.keys(years).sort((a, b) => Number(b) - Number(a)).map((year) => ({ year, types: Object.keys(years[year]).sort((a, b) => this.typeOrder(a) - this.typeOrder(b)).map((type) => ({ key: type, count: Object.values(years[year][type]).reduce((total, items) => total + items.length, 0), venues: Object.keys(years[year][type]).sort().map((venue) => ({ key: venue, label: venue, items: years[year][type][venue] })) })) }));
    },
  },
  created() { Object.keys(this.filters).forEach((key) => { if (this.$route.query[key] != null) this.filters[key] = String(this.$route.query[key]); }); this.loadOptions(); this.load(); },
  methods: {
    async loadOptions() { try { const response = await getReserarchOptionsAPI(); if (response && response.code === 200 && response.data) this.options = Object.assign({}, this.options, response.data); } catch (e) {} },
    async load() { this.loading = true; this.error = false; try { const response = await getReserarchListAPI(Object.assign({}, this.filters, { currentPage: 1, size: this.query.size })); if (response && response.code === 200) { this.papers = response.data.data || []; this.query.total = response.data.total || 0; this.syncRoute(); } else this.error = true; } catch (e) { this.error = true; } finally { this.loading = false; } },
    search() { this.load(); }, reset() { this.filters = emptyFilters(); this.load(); }, clearFilter(key) { this.filters[key] = ""; this.load(); },
    syncRoute() { const query = {}; Object.keys(this.filters).forEach((key) => { if (this.filters[key] !== "") query[key] = this.filters[key]; }); const navigation = this.$router.replace({ path: "/fblw", query }); if (navigation && navigation.catch) navigation.catch(() => {}); },
    publicationYear(paper) { return paper.publicationYear || (paper.createTime ? String(paper.createTime).slice(0, 4) : ""); }, venueName(paper) { return paper.venueShortName || paper.reserarchSource || "未标注来源"; }, typeLabel(type) { return typeLabels[type] || "其他发表"; }, typeOrder(type) { const index = ["conference", "journal", "book", "preprint", "other"].indexOf(type); return index < 0 ? 99 : index; }, publicationLink(paper) { return paper.doiUrl || paper.outsideUrl || paper.insideUrl || ""; },
  },
};
</script>

<style lang="less" scoped>
.publications-v3__body { padding: 48px 0 104px; }
.publications-v3__filters { display: grid; grid-template-columns: minmax(240px, 1.8fr) repeat(3, minmax(130px, .8fr)) auto auto; align-items: end; gap: 12px; padding: 18px 20px 20px; border-top: 3px solid var(--v3-gold); border-bottom: 1px solid var(--v3-line); background: rgba(255,255,255,.66); box-shadow: 0 12px 28px rgba(38,56,77,.05); }
.publications-v3__field { display: grid; min-width: 0; gap: 6px; }.publications-v3__field span { color: var(--v3-ink); font: 700 12px/1.2 var(--v3-sans); letter-spacing: .025em; }.publications-v3__field input,.publications-v3__field select { width: 100%; height: 40px; box-sizing: border-box; padding: 0 10px; border: 1px solid var(--v3-line); border-radius: 0; outline: none; color: var(--v3-ink); background: rgba(248,251,255,.92); font: 14px var(--v3-sans); }.publications-v3__field input:focus,.publications-v3__field select:focus { border-color: var(--v3-gold); box-shadow: 0 0 0 3px rgba(214,138,36,.11); }
.publications-v3__filter-actions { display: contents; }.publications-v3__filter-actions button { height: 40px; min-width: 56px; padding: 0 13px; border: 1px solid var(--v3-ink); cursor: pointer; font: 700 13px var(--v3-sans); }.publications-v3__reset { color: var(--v3-ink); background: transparent; }.publications-v3__search { color: #fff; background: var(--v3-ink); }
.publications-v3__result-bar { display: flex; align-items: center; justify-content: space-between; gap: 16px; min-height: 48px; padding-top: 14px; color: var(--v3-ink-soft); font: 700 13px var(--v3-mono); }.publications-v3__active { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 7px; }.publications-v3__active button { padding: 5px 8px 5px 10px; border: 1px solid rgba(155,88,18,.3); color: var(--v3-gold-deep); background: rgba(255,250,239,.7); cursor: pointer; font: 600 12px var(--v3-sans); }.publications-v3__active i { margin-left: 7px; font-style: normal; }
.publications-v3__layout { display: grid; grid-template-columns: 94px minmax(0,1fr); gap: 44px; margin-top: 34px; }.publications-v3__years { position: sticky; top: 114px; display: flex; flex-direction: column; align-self: start; border-left: 1px solid var(--v3-line); }.publications-v3__years a { padding: 7px 0 7px 13px; color: var(--v3-ink-soft); font: 700 14px/1 var(--v3-mono); text-decoration: none; }.publications-v3__years a:hover { color: var(--v3-gold-deep); }
.publications-v3__year + .publications-v3__year { margin-top: 80px; }.publications-v3__year > h2 { margin: 0 0 29px; padding-bottom: 13px; border-bottom: 1px solid var(--v3-ink); font: 700 40px/1 var(--v3-display); }.publications-v3__type + .publications-v3__type { margin-top: 42px; }.publications-v3__type > header { display: flex; align-items: baseline; justify-content: space-between; padding-bottom: 10px; border-bottom: 1px solid var(--v3-line); }.publications-v3__type h3 { margin: 0; color: var(--v3-ink); font: 700 19px/1.3 var(--v3-sans); }.publications-v3__type header span { color: var(--v3-gold-deep); font: 700 12px var(--v3-mono); }
.publications-v3__venue { margin-top: 24px; }.publications-v3__venue h4 { margin: 0 0 6px; color: var(--v3-gold-deep); font: 700 15px/1.45 var(--v3-sans); letter-spacing: .01em; }.publications-v3__venue h4 small { color: var(--v3-ink-soft); font: 600 12px var(--v3-mono); }.publications-v3__venue ol { margin: 0; padding: 0; list-style: none; }.publications-v3__venue li { position: relative; padding: 15px 104px 15px 18px; border-bottom: 1px solid rgba(207,218,231,.78); }.publications-v3__venue li::before { position: absolute; top: 25px; left: 0; width: 5px; height: 5px; border-radius: 50%; background: var(--v3-gold); content: ""; }.publications-v3__venue h5 { margin: 0; color: var(--v3-ink); font: 700 17px/1.55 var(--v3-sans); }.publications-v3__venue p { margin: 5px 0 0; color: var(--v3-ink-soft); font: 14px/1.65 var(--v3-sans); }.publications-v3__links { position: absolute; top: 19px; right: 0; white-space: nowrap; }.publications-v3__links a,.publications-v3__links span { color: var(--v3-gold-deep); font: 700 12px var(--v3-mono); text-decoration: none; }.publications-v3__links a:hover { text-decoration: underline; }.publications-v3__links span { color: var(--v3-ink-soft); font-weight: 500; }.publications-v3 .v3-state { margin-top: 34px; }
@media (max-width:1080px) { .publications-v3__filters { grid-template-columns: minmax(210px,1.5fr) repeat(3,1fr); }.publications-v3__filter-actions { display: flex; grid-column: 3 / -1; gap: 10px; }.publications-v3__filter-actions button { flex: 1; } }
@media (max-width:739px) { .publications-v3__body { padding-top: 36px; }.publications-v3__filters { grid-template-columns: 1fr 1fr; padding: 17px; }.publications-v3__field--keyword { grid-column: 1 / -1; }.publications-v3__filter-actions { grid-column: 1 / -1; }.publications-v3__result-bar { display: block; }.publications-v3__active { justify-content: flex-start; margin-top: 11px; }.publications-v3__layout { display: block; margin-top: 28px; }.publications-v3__years { position: static; flex-direction: row; overflow-x: auto; margin-bottom: 30px; border-top: 1px solid var(--v3-line); border-left: 0; }.publications-v3__years a { padding: 11px 14px; }.publications-v3__year + .publications-v3__year { margin-top: 58px; }.publications-v3__year > h2 { margin-bottom: 22px; font-size: 33px; }.publications-v3__type + .publications-v3__type { margin-top: 32px; }.publications-v3__venue li { padding: 13px 0 42px 15px; }.publications-v3__venue li::before { top: 22px; }.publications-v3__venue h5 { font-size: 16px; }.publications-v3__venue p { font-size: 13px; }.publications-v3__links { top: auto; right: auto; bottom: 14px; left: 15px; } }
</style>
