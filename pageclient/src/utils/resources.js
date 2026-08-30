const devApplication={
    // 既支持本机 localhost，也支持通过局域网地址打开开发预览。
    protocol:window.location.protocol.replace(':',''),
    host:window.location.hostname || "localhost",
    prefix:'',
    port:'3000'
}
const prodApplication={
    protocol:'https',
    host:"opennlg.cn",
    prefix:'/api',
    port:'443'
}
// 开发服务器连接本机 API；生产构建仍连接线上 API。
export const applicationContext=process.env.NODE_ENV === 'development' ? devApplication : prodApplication
