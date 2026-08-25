<template>
  <div class="lxwm-container opennlg-container">
    <p>
      OpenNLG小组依托苏州大学人工智能学院自然语言处理实验室，聚焦语言建模与生成研究。团队成立于2020年8月，在张民老师等资深教授的指导与支持下，面向长上下文建模理解、推理生成、通用奖励评估与高效部署等方向持续攻关，已形成“资源建设—建模技术—建模理论—系统级优化”的完整研究体系。
    </p>
    <p>
      对OpenNLG团队感兴趣的同学，可以通过邮箱（<span class="strong">ljt@suda.edu.cn</span>）与我们取得联系。科研之路虽然充满挑战，但你的收获将远远超出你的付出；选择可能令人犹豫，但加入我们，你将发现这是一段值得的旅程。
    </p>
    <p>
      如果你读过《哈利·波特》系列，你可能会记得这样的魔法世界充满了未知和惊喜。生活的魅力在于它的不可预知性，而这种不可预知性正是由我们对未来无限的憧憬和期待所塑造的。我们热爱人工智能，崇尚科研探索，相信学习的过程就像是一个充满神秘的宝箱，它将为你带来无尽的精彩和发现。
    </p>
    <p>
      我们寻找的伙伴：对自然语言处理有浓厚兴趣的研究生或本科生。拥有良好的编程能力和数学基础。具有团队合作精神，愿意与他人共同学习和进步。对科研有热情，愿意接受挑战，追求卓越。
    </p>
    <!-- <div class="lxwm-image-container">
      <img :src="require('@/assets/images/lxwm/01.jpg')">
    </div> -->
    <div class="lxwm-anim" aria-hidden="true">
      <span v-for="n in 12" :key="n"></span>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.lxwm-container{
  font-size: 18px;
  p{
    color: rgb(121, 121, 121);
    text-indent: 36px;
    font-family: var(--font-name);
  }
}
.strong{
  color:#ff9f19;
  &:hover{
    color: blue;
  }
}
.lxwm-image-container{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  img{
    width: 50%;
  }
}

/* Decorative floating bubbles to fill empty space */
.lxwm-anim{
  position: relative;
  height: 260px;
  margin: 24px 0 8px;
  overflow: hidden;
  border-radius: 12px;
}
.lxwm-anim span{
  position: absolute;
  bottom: -40px;
  display: block;
  width: 10px; height: 10px;
  border-radius: 50%;
  opacity: .18;
  background: radial-gradient(circle at 30% 30%, var(--title-color, #366092), rgb(225, 138, 38));
  animation: rise 14s linear infinite;
}
.lxwm-anim span:nth-child(1){ left: 6%;  width: 10px; height: 10px; animation-delay: 0s; }
.lxwm-anim span:nth-child(2){ left: 14%; width: 12px; height: 12px; animation-delay: 1.2s; }
.lxwm-anim span:nth-child(3){ left: 22%; width: 8px;  height: 8px;  animation-delay: 2.4s; }
.lxwm-anim span:nth-child(4){ left: 30%; width: 14px; height: 14px; animation-delay: .6s; }
.lxwm-anim span:nth-child(5){ left: 38%; width: 9px;  height: 9px;  animation-delay: 3.1s; }
.lxwm-anim span:nth-child(6){ left: 46%; width: 11px; height: 11px; animation-delay: 1.8s; }
.lxwm-anim span:nth-child(7){ left: 54%; width: 13px; height: 13px; animation-delay: .9s; }
.lxwm-anim span:nth-child(8){ left: 62%; width: 10px; height: 10px; animation-delay: 2.8s; }
.lxwm-anim span:nth-child(9){ left: 70%; width: 12px; height: 12px; animation-delay: 1.4s; }
.lxwm-anim span:nth-child(10){ left: 78%; width: 8px;  height: 8px;  animation-delay: 2.1s; }
.lxwm-anim span:nth-child(11){ left: 86%; width: 11px; height: 11px; animation-delay: .4s; }
.lxwm-anim span:nth-child(12){ left: 94%; width: 9px;  height: 9px;  animation-delay: 3.6s; }

@keyframes rise{
  0%{ transform: translateY(0) scale(1); opacity: 0; }
  10%{ opacity: .35; }
  90%{ opacity: .12; }
  100%{ transform: translateY(-320px) scale(.92); opacity: 0; }
}
</style>