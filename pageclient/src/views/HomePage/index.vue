<template>
  <v-parallax height="auto" src="../../assets/images/bg_01.png">
    
    <div style="height:40px"></div>
    <div>
      <div class="main-split-container" id="home">
        <Carousels />
        <div style="height:50px"></div>

      </div>
      <v-divider></v-divider>
      <div class="main-split-container">
        <div class="m_width">
          <div class="section-title">
            <div class="title">研究方向</div>
            <div class="clear"></div>
            <p>Research Interests</p>
          </div>
          <div class="group-desc">
            <carouseComp/>
          </div>
          <div class="motto">
            <!-- Lab Motto: We put the fun in funicular! -->
          </div>
        </div>
        <div style="height:50px"></div>
      </div>
      <v-divider></v-divider>
      <div class="main-split-container">
        <div class="m_width">
          <div class="section-title">
            <div class="title">最新消息</div>
            <div class="clear"></div>
            <p>Latest News</p>
          </div>
          <div class="group-desc">
            <LastNews/>
          </div>
          <div class="motto">
            <!-- Lab Motto: We put the fun in funicular! -->
          </div>
        </div>
        <div style="height:50px"></div>
      </div>

      <v-divider></v-divider>
      <div class="main-split-container">
        <div class="m_width">
          <div class="section-title">
            <div class="title">团队印象</div>
            <div class="clear"></div>
            <p>Team Impression</p>
          </div>
          <div class="group-desc">
            <LatestPhotos/>
          </div>
          <div class="motto">
            <!-- Lab Motto: We put the fun in funicular! -->
          </div>
        </div>
        <div style="height:50px"></div>
      </div>

    </div>
    <div class="invitation-container" style="height:100px;color:black">
      
      <div class="one item">
        <span class="h22">欢迎加入OpenNLG</span>
      </div>
      <div class="two item">
        欢迎对我们小组感兴趣的同学通过 ljt@suda.edu.cn 联系我们
      </div>
    </div>
  </v-parallax>
</template>

<script>
import Carousels from '@/components/carousels'
import Peoples from '@/components/peoples'
import Publication from '@/components/publication'
import News from '@/components/news'
import Papers from '@/components/papers'
import carouseComp from '@/components/carousel';
import LastNews from '@/components/last-news'
import LatestPhotos from '@/components/latest-photos'
export default {
  components: {
    Carousels,
    Peoples,
    Publication,
    News,
    Papers,
    carouseComp,
    LastNews,
    LatestPhotos
  },
  data() {
    return {
      tab: 0,
      block_home: 0,
      block_news: 0,
      block_reserarch: 0,
      block_people: 0,
      block_publication: 0,
      bodyHeight: 0,
      isActive: 0
    }
  },
  methods: {
    windowScroll() {
      this.bodyHeight = document.documentElement.scrollTop || document.body.scrollTop
    },
  },
  destroyed() {
    //销毁上面监听的滚动事件
    // window.removeEventListener("scroll", this.windowScroll);
  },
  mounted() {
    // window.addEventListener("scroll", this.windowScroll);
    //先获取右侧内容区域每个模块的高度
    // setTimeout(() => {
    //   this.block_home = document.getElementById('home').offsetTop
    //   this.block_news = document.getElementById('news').offsetTop
    //   this.block_reserarch = document.getElementById('reserarch').offsetTop
    //   this.block_people = document.getElementById('people').offsetTop
    //   this.block_publication = document.getElementById('publication').offsetTop
    // }, 500)
  },
  watch: {
    bodyHeight: {
      handler(newVal) {
        // console.log(newVal,this.block_home,this.block_news,this.block_reserarch,this.block_people,this.block_publication)
        if (newVal == 0) return
        if (newVal >= this.block_home) {
          this.tab = 0
        }
        if (newVal >= this.block_news) {
          this.tab = 1
        }
        if (newVal >= this.block_reserarch) {
          this.tab = 2
        }
        if (newVal >= this.block_people) {
          this.tab = 3
        }
        if (newVal >= this.block_publication) {
          this.tab = 4
        }
      },
      immediate: true,
      deep: true
    }
  },
}
</script>

<style lang="less" scoped>
.invitation-container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  .one{
    font-size: 28px;
    line-height: 28px;
    margin-bottom: 10px;
  }
  .item{
    color: #848484;
  }
}
.main-split-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.home-title {
  font-size: 84px;
  color: #D3D3D3;
  font-weight: 700;
  text-align: center;
}

.m_width {
  width: 1300px;
  margin: 0 auto;
}

@media only screen and (max-width: 1000px) {
  .m_width {
    width: 100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding: 0 10px;

  }
  .home-title{
    font-size: 50px !important;
  }
  .peo_item {
    width: 100%;
    margin-right: 0;
  }

  .pb_ct {
    padding: 5px 0;
    width: 100%;
    float: left;
    margin-left: 0;
  }

  .pub_item {
    padding-bottom: 20px;
    margin-bottom: 10px;
    overflow: hidden;
  }

  .pub_item>p:nth-child(1) img {
    width: 100%;
    height: auto;
  }

  .pub_item .pub_min {
    width: 100%;
  }

  .pub_item .pub_min>p:nth-child(1) {
    font-size: 14px;
    margin: 5px 0px;
    font-weight: 700;
    text-align: left;
    color: #000000;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
    line-height: 30px;
    height: 35px;
    text-align: center;
    border-bottom: 1px dashed #eee;
  }

  .pub_item .pub_min>p:nth-child(2) {
    margin: 15px 0px 5px 0;
    font-size: 12px;
    font-weight: 400;
    text-align: left;
    color: #616161;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
    line-height: 15px;
    height: 30px;
    text-align: center;
  }
}

.group-desc {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 18px;
  width: 100%;
  text-align: center;
  color: #333;

  .action {
    color: #FF6600;
  }
}

.motto {
  width: 100%;
  text-align: center;
  color: #ffd54b;
}

/deep/ .v-parallax__content {
  display: block !important;

}

.news-container {
  width: 100%;
  box-sizing: border-box;
  padding-left: 5%;
  padding-right: 5%;
}

.papers-container {
  width: 80%;
}
</style>