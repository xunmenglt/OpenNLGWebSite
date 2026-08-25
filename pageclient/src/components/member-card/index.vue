<template>
    <v-card class="mx-auto card-container" max-width="344" outlined>
        <v-list-item three-line>
            <v-list-item-avatar tile size="80" color="grey">
                <v-img v-if="avatarUrl" :src="avatarUrl"></v-img>
            </v-list-item-avatar>

            <v-list-item-content>
                <div class="text-h5">
                    {{enName}}
                </div>
                <v-list-item-title class="text-overline mb-1">
                    {{cnName}}
                </v-list-item-title>
                <v-list-item-subtitle>
                    <div class="desc">
                        {{ memberDesc }}
                    </div>
                </v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>

        <v-card-actions>
            
            <div style="width:250px">
                <v-chip
                class="ma-2"
                color="darken-3"
                outlined
                >
                <v-icon left>
                    mdi-account-outline
                </v-icon>
                {{ serialNum }}
                </v-chip>
            </div>
            <div>
                <v-btn text  x-small fab color="primary" @click="hanldEdit">
                    <v-icon >mdi-pencil</v-icon>
                </v-btn>
                
                <v-btn text  x-small fab color="warning" @click="hanldDelete">
                    <v-icon >mdi-delete</v-icon>
                </v-btn>
            </div>
        </v-card-actions>
    </v-card>
</template>
<script>
export default {
    name: "MemberCard",
    props:{
        id:{
            type:[Number,String],
            default:'',
            require:false
        },
        avatarUrl:{
            type:String,
            default:'',
            require:false
        },
        enName:{
            type:String,
            default:'',
            require:false
        },
        cnName:{
            type:String,
            default:'',
            require:false
        },
        memberDesc:{
            type:String,
            default:'',
            require:false
        },
        serialNum:{
            type:Number,
            default:0,
            require:false
        }
    },
    data() {
        return {

        }
    },
    methods:{
        hanldEdit(){
            this.$emit('hanldEditMemberInfo',this.id)
        },
        hanldDelete(){
            this.$emit('hanldDeleteMemberInfo',this.id)
        }
    }

}
</script>

<style lang="less" scoped>
.desc{
    font-size: 10px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp:2
}
.card-container{
    margin-bottom: 10px;
    height: 170px;
    box-shadow: 0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)!important;

}
.card-container:hover{
    box-shadow: 0 3px 10px -5px rgba(0,0,0,.2),0 16px 24px 2px rgba(0,0,0,.14),0 6px 30px 5px rgba(0,0,0,.12)!important;

}
</style>