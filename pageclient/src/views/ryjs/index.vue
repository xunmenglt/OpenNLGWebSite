<template>
  <div class="opennlg-container">
    <div class="group-intro">
      OpenNLG小组依托于苏州大学自然语言处理实验室，主要是研究语言建模与生成。在张民老师等资深教授的支持下，成立于2020年8月。主要研究方向包括长上下文建模理解；推理生成；通用奖励评估；高效部署，团队已在“资源建设-建模技术-建模理论-系统级优化”的研究具备成熟体系。
    </div>
    <div class="ryjs-container">
      <div class="ryjs-item" v-for="(item,index) in team_member_info" :key="index">
        <div class="teacher-item" v-if="item.ctType==='teacher'">
          <el-row v-for="(teacher,index) in item.children" :key="index">
            <el-col class="right" :xs="24" :md="24" :lg="6">
              <div class="image" @click="goTarget(teacher.outsideUrl)">
                <img :src="teacher.avatarUrl">
              </div>
            </el-col>
            <el-col :xs="24" :md="24" :lg="18">
              <div class="teacher-name">
                <h3 @click="goTarget(teacher.outsideUrl)">{{teacher.cnName}}</h3>
              </div>
              <div class="zhicheng">
                <h4>{{teacher.profession}}</h4>
              </div>
              <div class="yanjiufangx">
                <p>研究方向：{{teacher.direction}}</p>
              </div>
              <div class="email">
                <p>电子邮箱: {{teacher.email}}</p>
              </div>
              <div class="desc">
                <p>{{teacher.memberDesc}}</p>
              </div>
            </el-col>
          </el-row>
        </div>

        <div class="student-item" v-else-if="item.ctType!=='graduate'&&item.ctType!=='teacher'">
          <div class="clazz-name">{{item.ctZhName}}</div>
          <el-row>
            <el-col :sm="12" :md="12" :lg="8" v-for="(student,index) in item.children" :key="index">
              <div class="student-container">
                <div class="img" @click="goTarget(student.outsideUrl)">
                  <img :src="student.avatarUrl" />
                </div>
                <div class="desc">
                  <div class="name" @click="goTarget(student.outsideUrl)">
                    {{ student.cnName }}
                  </div>
                </div>
                <div class="direction">
                  研究方向：{{ student.direction }}
                </div>
                <div class="email">
                  电子邮箱：{{ student.email }}
                </div>
              </div>
            </el-col>
          </el-row>
        </div>

        <div class="student-item graduate-item" v-else-if="item.ctType==='graduate'">
          <div class="clazz-name">{{item.ctZhName}}</div>
          <el-row>
            <el-col :sm="12" :md="12" :lg="8" v-for="(student,index) in item.children" :key="index">
              <div class="student-container">
                <div class="desc">
                  <div class="name" @click="goTarget(student.outsideUrl)">
                    {{ student.cnName }}
                  </div>
                </div>
                <div class="direction">
                  毕业去向：{{ student.direction }}
                </div>
              </div>
              <div v-html="student.memberDesc" class="tip">
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import indexJS from './index.js'
export default{
  ...indexJS,
  methods: {
    ...(indexJS.methods || {}),
    goTarget(url){
      if(!url){ return }
      if(/^https?:\/\//i.test(url)){
        window.open(url)
      }else{
        this.$router && this.$router.push(url)
      }
    }
  }
}
</script>

<style lang="less" scoped>
@import url('./index.less');
</style>