<template>
  <main class="v3-main people-v3">
    <section class="v3-container v3-page-head people-v3__intro">
      <h1 class="v3-title">人员介绍</h1>
      <p class="v3-lede">
        OpenNLG小组依托于苏州大学自然语言处理实验室，主要是研究语言建模与生成。在张民老师等资深教授的支持下，成立于2020年8月。主要研究方向包括长上下文建模理解；推理生成；通用奖励评估；高效部署，团队已在“资源建设-建模技术-建模理论-系统级优化”的研究具备成熟体系。
      </p>
    </section>
    <section
      v-for="(group, index) in groups"
      :key="group.ctType"
      class="people-v3__group"
      :class="{ 'people-v3__group--wash': index % 2 }"
    >
      <div class="v3-container">
        <header v-if="group.ctType === 'teacher' || group.ctType === 'graduate'">
          <h2>{{ group.ctZhName }}</h2>
          <i></i>
        </header>
        <div v-if="group.ctType === 'teacher'" class="people-v3__teachers">
          <article v-for="item in group.children" :key="item.memberId">
            <div class="people-v3__teacher-portrait">
              <a
                v-if="item.outsideUrl"
                class="people-v3__person-link people-v3__person-link--avatar"
                :href="item.outsideUrl"
                target="_blank"
                rel="noopener"
                ><img :src="item.avatarUrl" :alt="item.cnName"
              /></a>
              <router-link
                v-else-if="item.insideUrl"
                class="people-v3__person-link people-v3__person-link--avatar"
                :to="item.insideUrl"
                ><img :src="item.avatarUrl" :alt="item.cnName"
              /></router-link>
              <img v-else :src="item.avatarUrl" :alt="item.cnName" />
            </div>
            <div class="people-v3__teacher-body">
              <div class="people-v3__teacher-identity">
                <h3>
                  <a
                    v-if="item.outsideUrl"
                    class="people-v3__person-link"
                    :href="item.outsideUrl"
                    target="_blank"
                    rel="noopener"
                    >{{ item.cnName }}</a
                  ><router-link
                    v-else-if="item.insideUrl"
                    class="people-v3__person-link"
                    :to="item.insideUrl"
                    >{{ item.cnName }}</router-link
                  ><template v-else>{{ item.cnName }}</template>
                </h3>
                <p v-if="item.profession" class="people-v3__teacher-role">{{ item.profession }}</p>
              </div>
              <div class="people-v3__teacher-research">
                <dl v-if="item.direction || item.email" class="people-v3__teacher-facts">
                  <div v-if="item.direction">
                    <dt>研究方向</dt>
                    <dd>{{ item.direction }}</dd>
                  </div>
                  <div v-if="item.email">
                    <dt>电子邮箱</dt>
                    <dd><a :href="'mailto:' + item.email">{{ item.email }}</a></dd>
                  </div>
                </dl>
                <p v-if="item.memberDesc" class="people-v3__teacher-bio">{{ item.memberDesc }}</p>
              </div>
            </div>
          </article>
        </div>
        <div v-else-if="group.ctType === 'graduate'" class="people-v3__alumni v3-alumni-cards">
          <article v-for="item in group.children" :key="item.memberId">
            <span class="v3-kicker">{{ alumniMeta(item) }}</span>
            <h3>
              <a
                v-if="item.outsideUrl"
                class="people-v3__person-link"
                :href="item.outsideUrl"
                target="_blank"
                rel="noopener"
                >{{ item.cnName }}</a
              ><router-link
                v-else-if="item.insideUrl"
                class="people-v3__person-link"
                :to="item.insideUrl"
                >{{ item.cnName }}</router-link
              ><template v-else>{{ item.cnName }}</template>
            </h3>
            <p v-if="item.graduationDestination"><b>毕业去向</b>{{ item.graduationDestination }}</p>
          </article>
        </div>
        <div v-else class="people-v3__original-students">
          <div class="clazz-name">
            <span>{{ group.ctZhName }}</span>
          </div>
          <el-row>
            <el-col
              v-for="item in visibleChildren(group)"
              :key="item.memberId"
              :sm="12"
              :md="12"
              :lg="8"
            >
              <div class="student-container">
                <div class="img">
                  <a
                    v-if="item.outsideUrl"
                    class="people-v3__person-link"
                    :href="item.outsideUrl"
                    target="_blank"
                    rel="noopener"
                    ><img :src="item.avatarUrl" :alt="item.cnName" @error="markAvatarFailed(item.memberId)"
                  /></a>
                  <router-link
                    v-else-if="item.insideUrl"
                    class="people-v3__person-link"
                    :to="item.insideUrl"
                    ><img :src="item.avatarUrl" :alt="item.cnName" @error="markAvatarFailed(item.memberId)"
                  /></router-link>
                  <img v-else :src="item.avatarUrl" :alt="item.cnName" @error="markAvatarFailed(item.memberId)" />
                </div>
                <div class="desc">
                  <div class="name">
                    <a
                      v-if="item.outsideUrl"
                      class="people-v3__person-link"
                      :href="item.outsideUrl"
                      target="_blank"
                      rel="noopener"
                      >{{ item.cnName }}</a
                    ><router-link
                      v-else-if="item.insideUrl"
                      class="people-v3__person-link"
                      :to="item.insideUrl"
                      >{{ item.cnName }}</router-link
                    ><template v-else>{{ item.cnName }}</template>
                  </div>
                </div>
                <div v-if="studentMeta(item)" class="cohort">{{ studentMeta(item) }}</div>
                <div v-if="item.direction" class="direction">研究方向：{{ item.direction }}</div>
                <div v-if="group.ctType === 'phd' && item.graduationDestination" class="destination">去向：{{ item.graduationDestination }}</div>
                <div v-if="item.email" class="email">
                  <a :href="'mailto:' + item.email">{{ item.email }}</a>
                </div>
              </div>
            </el-col>
          </el-row>
          <router-link
            v-if="isStudentGroup(group) && group.children.length > studentPreviewLimit"
            class="people-v3__all-students"
            :to="{ path: '/ryjs/students', query: { type: studentType(group) } }"
          >查看全部{{ group.ctZhName }}<i>↗</i></router-link>
        </div>
        <router-link v-if="group.ctType === 'graduate'" class="people-v3__all-students" :to="{ path: '/ryjs/students', query: { type: 'alumni' } }">查看全部毕业生<i>↗</i></router-link>
      </div>
    </section>
    <section v-if="!groups.length" class="v3-container">
      <div class="v3-state">正在加载成员信息…</div>
    </section>
  </main>
</template>
<script>
import { getCoverMembersListAPI } from "@/utils/api/members";
export default {
  data: () => ({ groups: [], studentPreviewLimit: 6, failedAvatars: {} }),
  created() {
    getCoverMembersListAPI().then((r) => {
      if (r && r.code === 200) this.groups = r.data || [];
    });
  },
  methods: {
    isStudentGroup(group) {
      return group.ctType === "phd" || group.ctType === "graduate_student";
    },
    studentType(group) {
      return group.ctType === "phd" ? "phd" : "master";
    },
    visibleChildren(group) {
      const children = group.children || [];
      return this.isStudentGroup(group)
        ? children.filter((item) => this.hasStudentAvatar(item)).slice(0, this.studentPreviewLimit)
        : children;
    },
    hasStudentAvatar(item) {
      return Boolean(item.avatarUrl) && !this.failedAvatars[item.memberId];
    },
    markAvatarFailed(memberId) {
      this.$set(this.failedAvatars, memberId, true);
    },
    studentMeta(item) {
      if (!item.cohortYear) return "";
      return `${item.cohortYear}级${item.programType ? " · " + item.programType : ""}`;
    },
    alumniMeta(item) {
      const degree = item.degreeType === "bachelor" ? "本科" : item.degreeType === "phd" ? "博士" : "硕士";
      return item.cohortYear ? `${item.cohortYear}级 · ${degree}` : `毕业生 · ${degree}`;
    },
  },
};
</script>
<style lang="less" scoped>
.people-v3__intro .v3-lede {
  max-width: 1120px;
  margin: 20px 0 0;
}
.people-v3__group {
  padding: 74px 0;
  border-bottom: 1px solid var(--v3-line);
}
.people-v3__group--wash {
  background: rgba(234, 241, 249, 0.46);
}
.people-v3 header {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 18px;
  align-items: center;
  margin-bottom: 30px;
}
.people-v3 header h2,
.people-v3 h3 {
  margin: 0;
  font-family: var(--v3-display);
}
.people-v3 header h2 {
  font-size: 37px;
}
.people-v3 header i {
  height: 1px;
  background: var(--v3-line);
}
.people-v3__teachers {
  display: grid;
  border-bottom: 1px solid var(--v3-line);
}
.people-v3__teachers article {
  display: grid;
  grid-template-columns: 168px minmax(0, 1fr);
  gap: 32px;
  align-items: start;
  padding: 30px 18px 30px 10px;
  border-top: 1px solid var(--v3-line);
  background: linear-gradient(90deg, rgba(230, 238, 247, 0.52) 0, rgba(230, 238, 247, 0.52) 232px, transparent 232px);
}
.people-v3__teacher-portrait {
  position: relative;
  padding: 10px 0 0 10px;
}
.people-v3__teacher-portrait::before {
  position: absolute;
  top: 0;
  left: 0;
  width: 148px;
  height: 186px;
  background: rgba(164, 185, 205, 0.62);
  content: "";
}
.people-v3__teachers img {
  position: relative;
  display: block;
  width: 100%;
  height: 210px;
  object-fit: cover;
  object-position: center top;
  transition: filter 0.2s ease;
}
.people-v3__person-link--avatar:hover img {
  filter: brightness(0.94);
}
.people-v3__teacher-body {
  display: grid;
  grid-template-columns: minmax(175px, 0.58fr) minmax(0, 1.42fr);
  gap: 30px;
  min-width: 0;
}
.people-v3__teacher-identity {
  min-width: 0;
  padding-top: 4px;
}
.people-v3__teacher-role {
  margin: 9px 0 0;
  color: var(--v3-ink-soft);
  font-size: 15px;
  line-height: 1.65;
}
.people-v3__teachers h3 {
  margin: 0;
  color: var(--v3-ink);
  font-size: 34px;
  line-height: 1.25;
}
.people-v3__teachers h3::after {
  display: block;
  width: 34px;
  height: 1px;
  margin-top: 15px;
  background: var(--v3-gold);
  content: "";
}
.people-v3__teacher-research {
  min-width: 0;
  padding-left: 30px;
  border-left: 1px solid var(--v3-line);
}
.people-v3__teacher-facts {
  display: grid;
  gap: 15px;
  margin: 0;
  font-size: 15px;
  line-height: 1.6;
}
.people-v3__teacher-facts > div {
  min-width: 0;
}
.people-v3__teacher-facts dt {
  color: var(--v3-ink-soft);
  font-size: 13px;
  letter-spacing: 0.07em;
}
.people-v3__teacher-facts dd {
  min-width: 0;
  margin: 4px 0 0;
  color: var(--v3-ink);
  overflow-wrap: anywhere;
}
.people-v3__teacher-facts a {
  color: inherit;
  text-decoration-color: rgba(155, 88, 18, 0.35);
  text-underline-offset: 3px;
}
.people-v3__teacher-facts a:hover {
  color: var(--v3-gold-deep);
}
.people-v3__teacher-bio {
  max-width: 760px;
  margin: 22px 0 0;
  color: var(--v3-ink-soft);
  font-size: 15px;
  line-height: 1.88;
}
.people-v3__original-students .clazz-name {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 10px;
  padding: 24px 0;
  color: #475168;
  font: 300 30px/1.2 var(--v3-display);
  text-align: center;
}
.people-v3__original-students .el-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.people-v3__original-students .el-col {
  display: flex;
  float: none;
  flex: 0 0 100%;
  max-width: 100%;
  align-items: center;
  justify-content: center;
}
.people-v3__original-students .student-container {
  display: flex;
  width: 100%;
  min-height: 278px;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  margin-bottom: 10px;
  color: #777;
  text-align: center;
}
.people-v3__original-students .img img {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  transition: box-shadow 0.22s, transform 0.22s;
}
.people-v3__original-students .img a:hover img {
  box-shadow: 0 10px 22px rgba(38, 56, 77, 0.12);
  transform: scale(1.04);
}
.people-v3__original-students .student-container > div {
  margin-bottom: 10px;
  font: 14px/1.55 "Times New Roman", "Microsoft YaHei", sans-serif;
}
.people-v3__original-students .desc .name {
  margin-bottom: 5px;
  color: var(--v3-ink);
  font: 18px/1.35 var(--v3-sans);
}
.people-v3__original-students .direction,
.people-v3__original-students .email,
.people-v3__original-students .destination {
  width: min(100%, 310px);
  padding: 0 8px;
  box-sizing: border-box;
  overflow-wrap: anywhere;
}
.people-v3__original-students .cohort {
  color: var(--v3-gold-deep);
  font-weight: 700;
}
.people-v3__original-students .destination {
  color: var(--v3-ink-soft);
}
.people-v3__original-students .email a {
  color: inherit;
  text-decoration: none;
}
.people-v3__original-students .email a:hover,
.people-v3__original-students .desc .name a:hover {
  color: var(--v3-gold-deep);
}
.people-v3__all-students {
  display: table;
  margin: 12px auto 0;
  padding: 9px 3px;
  border-bottom: 1px solid var(--v3-gold);
  color: var(--v3-ink);
  text-decoration: none;
  font: 700 15px var(--v3-sans);
}
.people-v3__all-students:hover {
  color: var(--v3-gold-deep);
}
.people-v3__all-students i {
  margin-left: 8px;
  color: var(--v3-gold-deep);
  font-style: normal;
}
.people-v3__alumni {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.people-v3__alumni article {
  min-height: 164px;
  padding: 20px;
  border-left: 3px solid var(--v3-gold);
  background: var(--v3-surface);
  transition: box-shadow 0.22s, transform 0.22s;
}
.people-v3__alumni article:hover {
  box-shadow: 0 8px 18px rgba(38, 56, 77, 0.06);
  transform: translateY(-2px);
}
.people-v3__alumni h3 {
  margin: 8px 0;
  font-size: 23px;
}
.people-v3__alumni p,
.people-v3__alumni div {
  margin: 9px 0 0;
  color: var(--v3-ink-soft);
  font-size: 14px;
}
.people-v3__alumni b {
  display: block;
  color: var(--v3-ink);
  font-size: 12px;
}
.people-v3__person-link {
  color: inherit;
  text-decoration: none;
}
.people-v3__person-link:not(.people-v3__person-link--avatar):hover {
  color: var(--v3-gold-deep);
}
.people-v3__person-link--avatar {
  display: block;
}
@media (min-width: 768px) {
  .people-v3__original-students .el-col {
    flex-basis: 50%;
    max-width: 50%;
  }
}
@media (min-width: 1200px) {
  .people-v3__original-students .el-col {
    flex-basis: 33.333333%;
    max-width: 33.333333%;
  }
}
@media (max-width: 900px) {
  .people-v3__teachers article {
    grid-template-columns: 164px minmax(0, 1fr);
    gap: 27px;
    padding: 23px 25px 23px 23px;
  }
  .people-v3__teachers img {
    height: 205px;
  }
  .people-v3__teachers h3 {
    font-size: 30px;
  }
  .people-v3__teacher-facts {
    gap: 12px;
  }
  .people-v3__alumni {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 739px) {
  .people-v3__group {
    padding: 55px 0;
  }
  .people-v3 header h2 {
    font-size: 30px;
  }
  .people-v3__teachers article {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 21px 20px 24px;
  }
  .people-v3__teacher-portrait {
    width: 148px;
    margin: 0 auto;
  }
  .people-v3__teachers img {
    height: 185px;
  }
  .people-v3__teacher-body {
    grid-template-columns: 1fr;
    gap: 22px;
  }
  .people-v3__teacher-identity {
    text-align: center;
  }
  .people-v3__teachers h3::after {
    margin-right: auto;
    margin-left: auto;
  }
  .people-v3__teachers h3 {
    font-size: 28px;
  }
  .people-v3__teacher-research {
    padding-top: 20px;
    padding-left: 0;
    border-top: 1px solid var(--v3-line);
    border-left: 0;
  }
  .people-v3__teacher-facts {
    gap: 13px;
  }
  .people-v3__alumni {
    grid-template-columns: 1fr;
  }
  .people-v3__alumni article {
    min-height: 0;
  }
}
</style>
