<template>
    <!-- <v-carousel
      cycle
      height="500"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item
        v-for="(slide) in slides"
        :key="slide.id"
        :src="slide.src"
      >
      </v-carousel-item>
    </v-carousel> -->
    <div class="home-container">
        <div class="desc">
            <div class="move-font">
                {{ showText }}
                <span class="typed-cursor">❘</span>
            </div>
            <div class="fu">
                Gather the knowledge of the world and create wonderful strokes
            </div>
        </div>
        <div class="slot-img">
            <img src="../../assets/images/homepage.png">
        </div>
    </div>
</template>

<script>

export default {
    name: 'Carousels',
    data() {
        return {
            content: "Welcome to OpenNLG",
            showText:""
        }
    },
    mounted(){
        this.appear(this.content)
    },
    methods: {
        appear(content) {
            const _this = this;

            this.showText = "";
            clearTimeout(this.timer);

            var speed = 200; //设置定时的速度 越来越快
            var count = 1;

            function changeContent() {
                _this.showText = content.substring(0, count); //截取字符串
                count++;
                if (count != content.length + 1) {
                    speed -= 1;
                    if (speed < 5) speed = 5;

                    _this.timer = setTimeout(changeContent, speed);
                }
            }
            changeContent();
        },
    }
}
</script>

<style lang="less" scoped>
.home-container {
    --height_full: 100vh;
    height: calc(var(--height_full) - 100px);
    width: 100%;
    position: relative;

    .slot-img {
        height: 100%;
        position: absolute;
        right: 0;

        img {
            height: 100%;
        }
    }
}

.desc {
    position: absolute;
    color: #000;
    font-size: 72px;
    font-weight: 600;
    top: 25%;
    left: 5%;

    .fu {
        font-size: 20px;
    }
}
@media only screen and (max-width: 1000px) {
    .move-font{
        font-size: 50px;
        text-align: center;
    }
}
@keyframes typedjsBlink{
    0%{
        opacity: 1;
    }
    100%{
        opacity: 0;
    }
}
.typed-cursor{
    color: rgb(0, 0, 0);
    animation:typedjsBlink 1s infinite;
}

</style>