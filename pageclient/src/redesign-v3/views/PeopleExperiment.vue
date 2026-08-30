<template>
  <main class="v3-main people-exp">
    <section class="v3-container v3-page-head people-exp__intro">
      <h1 class="v3-title">人员介绍1</h1>
      <p class="v3-lede">
        OpenNLG小组依托于苏州大学自然语言处理实验室，主要是研究语言建模与生成。在张民老师等资深教授的支持下，成立于2020年8月。主要研究方向包括长上下文建模理解；推理生成；通用奖励评估；高效部署，团队已在“资源建设-建模技术-建模理论-系统级优化”的研究具备成熟体系。
      </p>
    </section>

    <section
      v-for="(group, index) in groups"
      :key="group.ctType"
      class="people-exp__group"
      :class="{ 'people-exp__group--wash': index % 2 }"
    >
      <div class="v3-container">
        <header>
          <h2>{{ group.ctZhName }}</h2>
          <i></i>
        </header>

        <div v-if="group.ctType === 'teacher'" class="people-exp__teachers">
          <article v-for="item in group.children" :key="item.memberId">
            <a v-if="item.outsideUrl" :href="item.outsideUrl" target="_blank" rel="noopener">
              <img :src="item.avatarUrl" :alt="item.cnName" />
            </a>
            <router-link v-else-if="item.insideUrl" :to="item.insideUrl">
              <img :src="item.avatarUrl" :alt="item.cnName" />
            </router-link>
            <img v-else :src="item.avatarUrl" :alt="item.cnName" />
            <div>
              <p class="v3-kicker">{{ item.profession }}</p>
              <h3>
                <a v-if="item.outsideUrl" :href="item.outsideUrl" target="_blank" rel="noopener">{{ item.cnName }}</a>
                <router-link v-else-if="item.insideUrl" :to="item.insideUrl">{{ item.cnName }}</router-link>
                <template v-else>{{ item.cnName }}</template>
              </h3>
              <dl>
                <dt>研究方向</dt><dd>{{ item.direction }}</dd>
                <dt>电子邮箱</dt><dd><a v-if="item.email" :href="'mailto:' + item.email">{{ item.email }}</a></dd>
              </dl>
              <p>{{ item.memberDesc }}</p>
            </div>
          </article>
        </div>

        <div v-else-if="group.ctType === 'graduate'" class="people-exp__alumni">
          <article v-for="item in group.children" :key="item.memberId" class="people-exp__member-card">
            <span class="v3-kicker">ALUMNI</span>
            <h3>
              <a v-if="item.outsideUrl" :href="item.outsideUrl" target="_blank" rel="noopener">{{ item.cnName }}</a>
              <router-link v-else-if="item.insideUrl" :to="item.insideUrl">{{ item.cnName }}</router-link>
              <template v-else>{{ item.cnName }}</template>
            </h3>
            <p><b>毕业去向</b>{{ item.direction }}</p>
            <div v-html="item.memberDesc"></div>
          </article>
        </div>

        <div v-else class="people-exp__students">
          <article v-for="item in group.children" :key="item.memberId" class="people-exp__member-card people-exp__student-card">
            <div class="people-exp__portrait">
              <a v-if="hasAvatar(item) && item.outsideUrl" :href="item.outsideUrl" target="_blank" rel="noopener">
                <img :src="item.avatarUrl" :alt="item.cnName" @error="markAvatarFailed(item.memberId)" />
              </a>
              <router-link v-else-if="hasAvatar(item) && item.insideUrl" :to="item.insideUrl">
                <img :src="item.avatarUrl" :alt="item.cnName" @error="markAvatarFailed(item.memberId)" />
              </router-link>
              <img v-else-if="hasAvatar(item)" :src="item.avatarUrl" :alt="item.cnName" @error="markAvatarFailed(item.memberId)" />
              <div v-else class="people-exp__placeholder" :aria-label="item.cnName + '暂无照片'">{{ initials(item) }}</div>
            </div>
            <div class="people-exp__student-copy">
              <h3>
                <a v-if="item.outsideUrl" :href="item.outsideUrl" target="_blank" rel="noopener">{{ item.cnName }}</a>
                <router-link v-else-if="item.insideUrl" :to="item.insideUrl">{{ item.cnName }}</router-link>
                <template v-else>{{ item.cnName }}</template>
              </h3>
              <p v-if="item.enName" class="people-exp__en-name">{{ item.enName }}</p>
              <p v-if="item.direction" class="people-exp__direction">{{ item.direction }}</p>
              <a v-if="item.email" class="people-exp__email" :href="'mailto:' + item.email">{{ item.email }}</a>
            </div>
          </article>
        </div>
      </div>
    </section>
    <section v-if="!groups.length" class="v3-container"><div class="v3-state">正在加载成员信息…</div></section>
  </main>
</template>

<script>
import { getCoverMembersListAPI } from "@/utils/api/members";

export default {
  data: () => ({ groups: [], failedAvatars: {} }),
  created() {
    getCoverMembersListAPI().then((response) => {
      if (response && response.code === 200) this.groups = response.data || [];
    });
  },
  methods: {
    hasAvatar(item) {
      return Boolean(item.avatarUrl) && !this.failedAvatars[item.memberId];
    },
    markAvatarFailed(memberId) {
      this.$set(this.failedAvatars, memberId, true);
    },
    initials(item) {
      if (item.cnName) return item.cnName.slice(0, 1);
      return (item.enName || "O").split(/\s+/).map((part) => part.slice(0, 1)).join("").slice(0, 2).toUpperCase();
    },
  },
};
</script>

<style lang="less" scoped>
.people-exp__intro .v3-lede { max-width: 980px; margin: 20px 0 0; }
.people-exp__group { padding: 74px 0; border-bottom: 1px solid var(--v3-line); }
.people-exp__group--wash { background: rgba(234, 241, 249, 0.46); }
.people-exp header { display: grid; grid-template-columns: auto 1fr; gap: 18px; align-items: center; margin-bottom: 30px; }
.people-exp header h2,
.people-exp h3 { margin: 0; font-family: var(--v3-display); }
.people-exp header h2 { font-size: 37px; }
.people-exp header i { height: 1px; background: var(--v3-line); }
.people-exp a { color: inherit; text-decoration: none; }
.people-exp a:hover { color: var(--v3-gold-deep); }
.people-exp__teachers { display: grid; gap: 20px; }
.people-exp__teachers article { display: grid; grid-template-columns: 236px 1fr; gap: 34px; padding: 20px; border: 1px solid var(--v3-line); background: var(--v3-surface); }
.people-exp__teachers article > a { display: block; }
.people-exp__teachers img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: center top; }
.people-exp__teachers h3 { margin: 4px 0; font-size: 32px; }
.people-exp__teachers dl { display: grid; grid-template-columns: 84px 1fr; gap: 5px 15px; margin: 18px 0; font-size: 15px; }
.people-exp__teachers dd { margin: 0; }
.people-exp__teachers dt,
.people-exp__teachers article > div > p { color: var(--v3-ink-soft); }
.people-exp__alumni,
.people-exp__students { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; align-items: stretch; }
.people-exp__member-card { min-height: 164px; box-sizing: border-box; border-left: 3px solid var(--v3-gold); background: var(--v3-surface); transition: border-color 0.2s, background-color 0.2s; }
.people-exp__member-card:hover { border-left-color: var(--v3-gold-deep); background: rgba(255, 255, 255, 0.92); }
.people-exp__alumni article { padding: 20px; }
.people-exp__alumni h3 { margin: 8px 0; font-size: 23px; }
.people-exp__alumni p,
.people-exp__alumni div { margin: 9px 0 0; color: var(--v3-ink-soft); font-size: 14px; }
.people-exp__alumni b { display: block; color: var(--v3-ink); font-size: 12px; }
.people-exp__student-card { display: grid; grid-template-columns: 68px minmax(0, 1fr); gap: 14px; align-items: center; padding: 16px; }
.people-exp__portrait { width: 68px; height: 82px; overflow: hidden; background: #e6edf4; }
.people-exp__portrait a { display: block; width: 100%; height: 100%; }
.people-exp__portrait img { display: block; width: 100%; height: 100%; object-fit: cover; object-position: center top; filter: saturate(0.92) contrast(0.98); transition: filter 0.2s; }
.people-exp__portrait a:hover img { filter: saturate(1.04) contrast(1); }
.people-exp__placeholder { display: grid; width: 100%; height: 100%; place-items: center; color: #6b7e91; background: #e6edf4; font: 700 24px/1 var(--v3-display); }
.people-exp__student-copy { display: flex; min-width: 0; min-height: 122px; flex-direction: column; align-items: flex-start; justify-content: center; }
.people-exp__student-copy h3 { color: var(--v3-ink); font-size: 22px; line-height: 1.18; transition: color 0.2s; }
.people-exp__student-card:hover h3 { color: var(--v3-gold-deep); }
.people-exp__en-name { max-width: 100%; margin: 3px 0 8px; overflow: hidden; color: #718295; font: 10px/1.3 var(--v3-mono); text-overflow: ellipsis; white-space: nowrap; }
.people-exp__direction { display: -webkit-box; margin: 0; overflow: hidden; color: var(--v3-ink-soft); font-size: 13px; line-height: 1.5; -webkit-box-orient: vertical; -webkit-line-clamp: 2; }
.people-exp__email { display: block; max-width: 100%; overflow: hidden; margin-top: auto; padding-top: 7px; color: #607286; font: 11px/1.35 var(--v3-mono); text-overflow: ellipsis; white-space: nowrap; }
@media (max-width: 1040px) {
  .people-exp__alumni,
  .people-exp__students { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 739px) {
  .people-exp__group { padding: 55px 0; }
  .people-exp header h2 { font-size: 30px; }
  .people-exp__teachers article { grid-template-columns: 1fr; padding: 16px; }
  .people-exp__teachers img { width: 170px; }
  .people-exp__alumni,
  .people-exp__students { grid-template-columns: 1fr; }
  .people-exp__alumni article { min-height: 0; }
  .people-exp__student-card { grid-template-columns: 64px minmax(0, 1fr); gap: 14px; min-height: 146px; padding: 15px; }
  .people-exp__portrait { width: 64px; height: 78px; }
  .people-exp__student-copy { min-height: 114px; }
  .people-exp__student-copy h3 { font-size: 21px; }
  .people-exp__en-name { margin-bottom: 6px; }
  .people-exp__direction { font-size: 13px; }
  .people-exp__email { padding-top: 6px; font-size: 11px; }
}
</style>
