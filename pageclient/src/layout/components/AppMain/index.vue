<template>
    
        <div class="app-main">
            <v-parallax height="auto" :src="ColorBG">
                <div class="about-area">
                    <router-view :key="key"></router-view>
                </div>
            </v-parallax>
        </div>
    </v-parallax>
</template>

<script>
import ColorBG from '@/assets/images/bg_01.png'
export default {
    name: 'AppMain',
    computed: {
        key() {
            return this.$route.path
        }
    },
    data() {
        return {
            ColorBG: ColorBG
        }
    },
}
</script>

<style></style>