<template>
    <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
            <div class="cell-container" v-bind="attrs"
                                        v-on="on" 
                                        :style="{'width':width,'-webkit-line-clamp':lines}">
                {{ content }}
            </div>
        </template>
        <span>{{ content }}</span>
    </v-tooltip>
</template>

<script>

export default {
    name:'Cell',
    props:{
        content:{
            type:[String,Number,Object],
            default:''
        },
        width:{
            type:String,
            default:"100%"
        },
        lines:{
            type:Number,
            default:1
        }
    }
}
</script>

<style>
.cell-container{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
}
</style>