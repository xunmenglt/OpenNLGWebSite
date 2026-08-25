const devApplication={
    protocol:'http',
    host:"localhost",
    prefix:'',
    port:'3000'
}
const prodApplication={
    protocol:'https',
    host:"opennlg.cn",
    prefix:'/api',
    port:'443'
}
export const applicationContext=prodApplication