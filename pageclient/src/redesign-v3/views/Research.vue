<template>
  <main class="v3-main research-v3">
    <section class="v3-container v3-page-head">
      <h1 class="v3-title">研究方向</h1>
    </section>
    <section>
      <article
        v-for="item in rjfx_list"
        :key="item.title"
        class="research-v3__chapter"
      >
        <div class="v3-container research-v3__body">
          <div>
            <h2>{{ item.title }}</h2>
            <p>{{ item.desc }}</p>
          </div>
          <figure><img :src="item.image" :alt="item.title" /></figure>
        </div>
      </article>
    </section>
    <section v-if="!rjfx_list.length" class="v3-container">
      <div class="v3-state">暂无可展示的研究方向信息。</div>
    </section>
  </main>
</template>
<script>
// Kept with the active V3 page so the retired legacy public view is no longer
// part of the production dependency graph.
export default {
  data: () => ({
    rjfx_list: [
      {
        id: 1,
        title: "大语言模型",
        desc: "以ChatGPT和GPT-4为代表的大型语言模型成为最具影响力的技术革新之一。这些模型以其卓越的语言处理和推理能力，为实现通用人工智能的宏伟目标提供了希望的曙光。OpenNLG小组正专注于深入研究这些大型语言模型的潜在局限和能力边界，同时致力于推动这些模型的能力向更高层次发展。",
        image: "https://t10.baidu.com/it/u=979229777,200087834&fm=30&app=106&f=JPEG?w=640&h=461&s=0012EC33118E44E846F41CCA0200B0B2",
      },
      {
        id: 2,
        title: "自然语言处理",
        desc: "自然语言处理（NLP）领域专注于计算机与人类语言的互动，旨在让计算机不仅能够解读自然语言的深层含义，还能使用自然语言来清晰地传达特定的意图和思想。OpenNLG团队正致力于一系列具有挑战性的NLP研究领域，包括文本的自动生成、知识的深度整合与逻辑推理、文档的高效检索以及模型的优化压缩等，致力于将这些NLP技术与实际应用紧密相连。",
        image: "https://img1.baidu.com/it/u=2033602622,521439758&fm=253&fmt=auto&app=138&f=JPEG?w=683&h=461",
      },
    ],
  }),
};
</script>
<style lang="less" scoped>
.research-v3__chapter {
  padding: 80px 0;
  border-bottom: 1px solid var(--v3-line);
}
.research-v3__chapter:nth-child(even) {
  background: rgba(234, 241, 249, 0.46);
}
.research-v3__body {
  display: grid;
  grid-template-columns: 1fr 0.92fr;
  gap: 88px;
  align-items: start;
}
.research-v3__chapter:nth-child(even) .research-v3__body {
  direction: rtl;
}
.research-v3__chapter:nth-child(even) .research-v3__body > * {
  direction: ltr;
}
.research-v3__body h2 {
  margin: 2px 0 18px;
  font: 700 43px/1.2 var(--v3-display);
}
.research-v3__body p:last-child {
  margin: 0;
  color: var(--v3-ink-soft);
  font-size: 17px;
  line-height: 1.82;
}
.research-v3__body figure {
  display: flex;
  min-height: 290px;
  margin: 0;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--v3-line);
  background: linear-gradient(145deg, #eaf1f9, #f9fbfd);
  padding: 24px;
  box-sizing: border-box;
}
.research-v3__body img {
  display: block;
  max-width: calc(100% - 8px);
  max-height: 242px;
  object-fit: contain;
}
@media (max-width: 1023px) {
  .research-v3__body {
    gap: 40px;
  }
  .research-v3__body h2 {
    font-size: 35px;
  }
}
@media (max-width: 739px) {
  .research-v3__chapter {
    padding: 58px 0;
  }
  .research-v3__body {
    grid-template-columns: 1fr;
    gap: 28px;
  }
  .research-v3__chapter:nth-child(even) .research-v3__body {
    direction: ltr;
  }
  .research-v3__body h2 {
    font-size: 33px;
  }
  .research-v3__body p:last-child {
    font-size: 15px;
  }
  .research-v3__body figure {
    min-height: 220px;
    padding: 18px;
  }
  .research-v3__body img {
    max-height: 184px;
  }
}
</style>
