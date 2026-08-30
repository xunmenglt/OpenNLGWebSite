<template>
  <main class="v3-main contact-v3">
    <section class="v3-container v3-page-head">
      <h1 class="v3-title">联系我们</h1>
    </section>
    <section class="v3-container contact-v3__grid">
      <div>
        <div class="contact-v3__letter">
          <section>
            <p>
              OpenNLG小组依托苏州大学人工智能学院自然语言处理实验室，聚焦语言建模与生成研究。团队成立于2020年8月，在张民老师等资深教授的指导与支持下，面向长上下文建模理解、推理生成、通用奖励评估与高效部署等方向持续攻关，已形成“资源建设—建模技术—建模理论—系统级优化”的完整研究体系。
            </p>
          </section>
          <section>
            <p>
              对OpenNLG团队感兴趣的同学，可以通过邮箱（<b>ljt@suda.edu.cn</b>）与我们取得联系。科研之路虽然充满挑战，但你的收获将远远超出你的付出；选择可能令人犹豫，但加入我们，你将发现这是一段值得的旅程。
            </p>
          </section>
          <section>
            <p>
              如果你读过《哈利·波特》系列，你可能会记得这样的魔法世界充满了未知和惊喜。生活的魅力在于它的不可预知性，而这种不可预知性正是由我们对未来无限的憧憬和期待所塑造的。我们热爱人工智能，崇尚科研探索，相信学习的过程就像是一个充满神秘的宝箱，它将为你带来无尽的精彩和发现。
            </p>
          </section>
          <section>
            <p>
              我们寻找的伙伴：对自然语言处理有浓厚兴趣的研究生或本科生。拥有良好的编程能力和数学基础。具有团队合作精神，愿意与他人共同学习和进步。对科研有热情，愿意接受挑战，追求卓越。
            </p>
          </section>
        </div>
      </div>
      <aside>
        <a href="mailto:ljt@suda.edu.cn">ljt@suda.edu.cn</a>
        <small>欢迎通过邮件联系 OpenNLG 小组。</small>
      </aside>
    </section>
  </main>
</template>
<script>
export default {};
</script>
<style lang="less" scoped>
.contact-v3__grid {
  display: grid;
  grid-template-columns: 1.45fr 0.62fr;
  gap: 82px;
  padding: 56px 0 92px;
}
.contact-v3__letter section {
  padding: 27px 0;
  border-bottom: 1px solid var(--v3-line);
}
.contact-v3__letter section:last-child {
  border-bottom: 0;
}
.contact-v3__letter p {
  margin: 0;
  color: var(--v3-ink-soft);
  font-size: 17px;
  line-height: 1.85;
}
.contact-v3__letter b {
  color: var(--v3-gold-deep);
}
.contact-v3 aside {
  position: sticky;
  top: 118px;
  align-self: start;
  padding: 38px 30px;
  border: 1px solid var(--v3-line);
  border-top: 3px solid var(--v3-gold);
  background: linear-gradient(145deg, #ffffff 0%, #edf4fa 100%);
  box-shadow: 0 7px 20px rgba(38, 56, 77, 0.05);
  color: var(--v3-ink);
}
.contact-v3 aside .v3-kicker {
  color: var(--v3-gold-deep);
}
.contact-v3 aside a {
  display: block;
  margin-top: 10px;
  color: inherit;
  font: 700 23px/1.3 var(--v3-display);
  overflow-wrap: anywhere;
  text-decoration: none;
}
.contact-v3 aside small {
  display: block;
  margin-top: 12px;
  color: var(--v3-ink-soft);
  font-size: 14px;
}
@media (max-width: 900px) {
  .contact-v3__grid {
    grid-template-columns: 1fr;
    gap: 38px;
    padding-bottom: 72px;
  }
  .contact-v3 aside a {
    font-size: 20px;
  }
  .contact-v3 aside {
    position: static;
    width: 100%;
    box-sizing: border-box;
  }
}
@media (max-width: 739px) {
  .contact-v3__grid {
    gap: 40px;
    padding-bottom: 62px;
  }
  .contact-v3__letter p {
    font-size: 15px;
  }
  .contact-v3 aside {
    position: static;
    margin-top: 0;
    min-height: 0;
  }
}
</style>
