import { getCoverMembersListAPI } from '@/utils/api/members'
export default{
    data() {
        return {
            team_member_info:[]
        }
    },
    created() {
        this.initTeamMemberInfo()
    },
    methods: {
        initTeamMemberInfo(){
            getCoverMembersListAPI().then(res=>{
                if (res && res.code && res.code===200){
                    this.team_member_info=res.data
                }
            })
        }
    },
}