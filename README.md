# OpenBA Website

OpenBA 团队网站，采用前后端分离架构：前端基于 Vue 2，后端基于 Spring Boot，数据存储使用 MySQL 8。项目支持本地开发联调，也可以通过 Docker Compose 部署。

## 技术栈

- 前端：Vue 2、Vue CLI 5、Vue Router、Vuex、Element UI、Vuetify、Axios
- 后端：Java 8、Spring Boot 2.5、Spring Security、MyBatis-Plus、JWT
- 数据库：MySQL 8
- 部署：Docker Compose、Caddy

## 项目结构

```text
OpenBAWebSite/
├── pageclient/                 # Vue 前端
├── pageserver/                 # Spring Boot 后端
├── dockerscript/               # Docker Compose、Caddy 和数据库脚本
│   ├── caddy/                  # Caddy 配置及前端部署目录
│   ├── server/                 # 后端镜像构建目录
│   ├── docker-compose.yaml
│   └── opennlg.sql             # Docker 部署使用的初始化数据
└── metarial/                   # 其他历史数据脚本
```

## 环境要求

本地开发建议安装：

- JDK 8
- Maven 3.6+
- Node.js 16 或 18
- npm 8+
- MySQL 8

后端依赖的 Lombok 版本较旧，请使用 JDK 8 构建。JDK 23 等较新版本可能导致 Lombok 未生成 getter、setter 和构造方法，从而出现大量“找不到符号”编译错误。开始前可用 `java -version` 和 `mvn -version` 确认 Maven 实际使用的 JDK。

Docker 部署需要：

- Docker Engine 20.10+
- Docker Compose v2（使用 `docker compose` 命令）

## 一、本地测试

### 1. 获取代码

```bash
git clone <仓库地址>
cd OpenBAWebSite
```

后续命令均默认在项目根目录执行。

### 2. 创建并导入数据库

启动本机 MySQL 8，然后创建数据库并导入测试数据：

```bash
mysql -uroot -p -e "CREATE DATABASE IF NOT EXISTS opennlg DEFAULT CHARACTER SET utf8mb4;"
mysql -uroot -p opennlg < dockerscript/opennlg.sql
```

数据库脚本包含建表语句和演示数据。重复导入会重建相关数据表，请先备份需要保留的数据。

### 3. 配置后端开发环境

编辑 `pageserver/src/main/resources/application-dev.yml`：

```yaml
spring:
  datasource:
    url: jdbc:mysql://127.0.0.1:3306/opennlg?serverTimezone=Asia/Shanghai&characterEncoding=utf8&useSSL=false
    username: root
    password: 你的本地数据库密码

file:
  # 修改为本机可写的绝对目录，并提前创建该目录
  path: /absolute/path/to/opennlg/files/
  resource-path: /files/**
  domain: http://localhost:3000/files/
```

不要将个人数据库密码、生产密码或新生成的 JWT 密钥提交到 Git。

运行后端测试：

```bash
cd pageserver
mvn test
```

以 `dev` Profile 启动后端：

```bash
mvn spring-boot:run -Dspring-boot.run.profiles=dev
```

后端默认监听 `http://localhost:3000`。开发环境开启了 Swagger，可访问：

```text
http://localhost:3000/doc.html
```

### 4. 配置并启动前端

项目当前在 `pageclient/src/utils/resources.js` 最后一行使用生产配置：

```js
export const applicationContext=prodApplication
```

本地联调前，将其临时改为：

```js
export const applicationContext=devApplication
```

然后安装依赖并启动开发服务器：

```bash
cd pageclient
npm ci
npm run serve
```

终端会显示前端访问地址，Vue CLI 默认通常为：

```text
http://localhost:8080
```

前端会向 `http://localhost:3000` 发送 API 请求。联调结束、构建生产版本前，请将 `resources.js` 切回 `prodApplication`。

### 5. 本地构建检查

前端没有单独的自动化测试脚本，可以用生产构建检查依赖、语法和打包流程：

```bash
cd pageclient
npm run build
```

后端打包检查：

```bash
cd pageserver
mvn clean package
```

成功后会分别生成：

- `pageclient/dist/`
- `pageserver/target/pageserver-1.0-SNAPSHOT.jar`

## 二、Docker 部署

Docker Compose 会启动以下服务：

| 服务 | 用途 | 对外端口 |
| --- | --- | --- |
| `mysql` | MySQL 8 数据库 | `9623` |
| `server` | Spring Boot API | `3000` |
| `caddy` | 前端静态站点、HTTPS、API 反向代理 | `80`、`443`、`8001` |

### 1. 配置域名

当前生产域名为 `opennlg.cn`，同时写在以下文件中：

- `pageclient/src/utils/resources.js`
- `pageserver/src/main/resources/application-prod.yml`
- `dockerscript/caddy/Caddyfile`

如果使用其他域名，请同步替换这三处域名，并将域名的 A/AAAA 记录解析到部署服务器。Caddy 申请 HTTPS 证书时，服务器的 `80` 和 `443` 端口必须可以从公网访问。

正式部署前还应修改以下生产配置：

- `dockerscript/docker-compose.yaml` 中的 MySQL root 密码
- `pageserver/src/main/resources/application-prod.yml` 中的数据库密码
- `application-prod.yml` 中的 JWT `secret`

数据库密码在 Compose 和后端配置中必须保持一致。

### 2. 构建部署文件

确认前端的 `resources.js` 已使用 `prodApplication`，然后执行：

```bash
# 构建后端
cd pageserver
mvn clean package -DskipTests
cp target/pageserver-1.0-SNAPSHOT.jar ../dockerscript/server/pageserver.jar

# 构建前端
cd ../pageclient
npm ci
npm run build
mkdir -p ../dockerscript/caddy/data/pageclient
cp -R dist/. ../dockerscript/caddy/data/pageclient/

cd ../dockerscript
```

`dockerscript/server/Dockerfile` 会把 `pageserver.jar` 打入后端镜像；Caddy 会从 `dockerscript/caddy/data/pageclient/` 提供前端静态文件。

### 3. 启动服务

在 `dockerscript` 目录运行：

```bash
docker compose up -d --build
docker compose ps
```

首次启动且数据库健康后，导入初始化数据：

```bash
docker compose exec -T mysql \
  mysql -uroot -p'opennlg' opennlg < opennlg.sql
```

如果已经修改了 MySQL 密码，请同步替换命令中的 `opennlg`。初始化脚本会删除并重建相关表，因此只应在首次部署或确认需要重置数据时执行。

### 4. 验证部署

查看容器状态和日志：

```bash
docker compose ps
docker compose logs --tail=100 mysql
docker compose logs --tail=100 server
docker compose logs --tail=100 caddy
```

验证 API：

```bash
curl http://127.0.0.1:3000/api/news/list
```

域名和 HTTPS 生效后，在浏览器访问：

```text
https://你的域名
```

Caddy 会将 `/api/*` 请求反向代理到后端的 `3000` 端口。

### 5. 更新部署

代码更新后，重新执行“构建部署文件”中的命令，再运行：

```bash
cd dockerscript
docker compose up -d --build
```

仅查看实时日志：

```bash
docker compose logs -f --tail=100
```

停止服务但保留数据库数据：

```bash
docker compose down
```

不要随意添加 `-v` 参数，否则可能删除 Compose 管理的数据卷。当前 MySQL 数据也会持久化在 `dockerscript/mysql/` 目录中，升级或重置前请先备份。

## 常见问题

### Maven 报 getter、setter 或构造方法“找不到符号”

这通常不是实体类真的缺少方法，而是当前 JDK 版本过高，旧版 Lombok 注解处理失败。请将 `JAVA_HOME` 切换到 JDK 8，再用 `mvn -version` 确认后重新构建。

### 前端仍然请求 `https://opennlg.cn`

检查 `pageclient/src/utils/resources.js`：本地开发应使用 `devApplication`，生产构建应使用正确域名的 `prodApplication`。修改后需要重新启动开发服务器或重新构建前端。

### 后端无法连接 MySQL

检查当前激活的 Spring Profile、数据库地址、端口和密码：

- 本地开发：MySQL 通常是 `127.0.0.1:3306`，启动时指定 `dev`
- Docker：后端通过 Compose 服务名 `mysql:3306` 连接数据库
- 宿主机访问 Docker MySQL：使用 `127.0.0.1:9623`

### 文件上传失败

本地开发需确保 `application-dev.yml` 的 `file.path` 是存在且可写的目录。Docker 环境会把 `dockerscript/server/files/` 挂载到容器内的 `/var/user/opennlgfiles/`。

### Caddy 无法签发 HTTPS 证书

确认域名已经解析到当前服务器、防火墙和云安全组已放行 `80`/`443`，并检查：

```bash
docker compose logs caddy
```
