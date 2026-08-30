# OpenNLG V3 维护说明

本文件补充根目录 `README.md` 的原始项目说明，面向 OpenNLG V3 网站的日常维护者。原 `README.md` 保留为项目基础安装与部署参考；两者不互相替代。

## 1. 系统边界

OpenNLG 由以下部分组成：

- 公开网站：`pageclient/src/redesign-v3/`，当前唯一维护的公开视觉版本；
- 管理后台：`/dashboard`，用于维护人员、新闻、研究方向、论文、产品、文化影像、文章和资源；
- API 服务：`pageserver/`，默认监听 `3000` 端口；
- MySQL 数据库：保存网站内容及后台账号；
- 上传文件目录：由 `OPENNLG_FILE_PATH` 指定，不属于 Git 仓库；
- 离线导出：由 `scripts/build_offline_html.py` 生成，仅包含公开页面与当次数据库快照。

`pageclient/src/redesign-v2/` 和更早公开页面已不在当前维护范围，也不应重新作为公开路由入口。管理后台不是 V3 视觉页面的一部分，但仍是 V3 数据的维护入口。

## 2. 代码与数据目录

```text
pageclient/
  src/redesign-v3/               # V3 公开页面、布局和样式
  src/views/dashboard/           # 管理后台
  src/router/index.js             # 公开站与后台路由
  src/utils/resources.js          # 开发/生产 API 地址选择

pageserver/
  src/main/resources/application-*.yml
  src/main/resources/mapper/      # MyBatis 查询与写入逻辑
  src/main/resources/db/migration/# V3 数据库迁移

database/
  schema.sql                      # 新环境空数据库基线，不含真实资料

scripts/
  import_student_directory.py     # 人员目录导入
  sync_public_content_mysql.py    # 内容同步工具
  publications/                   # 论文提取、核验、PDF 补全与导入
  build_offline_html.py           # 单文件离线站点导出
```

下列内容必须保留在本机或受控存储中，不能提交到 Git：本地 `application-local.yml`、`.env`、数据库转储、真实人员 Excel、Scholar/MHTML 存档、上传文件目录、`runs/` 核验输出、`exports/` 离线导出。

## 3. 本地开发

### 3.1 前置条件

- JDK 8；本项目的旧版 Lombok 不保证可在高版本 JDK 下编译；
- Maven 3.6+；
- Node.js 16 或 18、npm 8+；
- MySQL 8。

后端的默认 Profile 是 `prod`。本地开发必须显式激活 `local`，否则会读取生产环境变量配置。

### 3.2 初始化空数据库

以下命令只创建结构和基础分类，不含真实网站内容：

```bash
mysql -uroot -p -e "CREATE DATABASE IF NOT EXISTS opennlg DEFAULT CHARACTER SET utf8mb4;"
mysql -uroot -p opennlg < database/schema.sql
```

已有数据库升级前必须备份。数据库迁移目前由人工执行，并非 Flyway/Liquibase 自动迁移；按文件名顺序执行 `pageserver/src/main/resources/db/migration/V3_*.sql`，并记录已执行的版本。

### 3.3 启动后端

```bash
cp pageserver/src/main/resources/application-local.example.yml \
  pageserver/src/main/resources/application-local.yml

export OPENNLG_DB_PASSWORD='本地数据库密码'
export SPRING_PROFILES_ACTIVE=local
cd pageserver
mvn spring-boot:run
```

本地 API 为 `http://localhost:3000`，开发环境 Swagger 通常位于 `http://localhost:3000/doc.html`。配置文件中的 `OPENNLG_FILE_PATH` 必须指向存在且可写的本地目录。

### 3.4 启动前端

```bash
cd pageclient
npm ci
npm run serve
```

开发服务器通常在 `http://localhost:8080`。开发模式自动访问本机 API；普通生产构建访问 `https://opennlg.cn/api`，由 `pageclient/src/utils/resources.js` 控制。

### 3.5 构建检查

```bash
cd pageclient && npm run build
cd ../pageserver && mvn -DskipTests compile
python3 ../scripts/publications/verify_all_titles.py --help
```

`mvn test` 和论文脚本测试可在依赖已下载的环境执行；不要将因网络下载失败误判为代码测试失败。

## 4. V3 页面与路由

公开路由由 `pageclient/src/router/index.js` 定义，页面源文件均位于 `pageclient/src/redesign-v3/views/`：

| 页面 | 路由 | 数据来源 |
| --- | --- | --- |
| 首页 | `/` | 新闻、研究方向、团队成员、文化影像 |
| 人员介绍 | `/ryjs` | 成员分类、人员关系、教育信息 |
| 学生名录 | `/ryjs/students` | 博士生、硕士生、毕业生完整列表 |
| 研究方向 | `/yjfx` | 研究方向 |
| 发表论文 | `/fblw` | 论文库 |
| 专栏文章 | `/zlwz` | 文章 |
| 团队印象 | `/tjhd` | 团队文化影像 |
| 联系我们 | `/lxwm` | 静态联系信息 |

管理后台入口为 `/dashboard/login`。公开站的内容变更应优先通过后台或受控导入脚本写入数据库，避免直接修改前端文案以绕开数据来源。

## 5. 人员目录维护

### 5.1 数据模型

人员基础资料保存在 `og_members`，分类关系保存在 `og_member_category_rel`，培养和年级资料保存在 `og_member_education`。V3 主要使用以下分类：

- `teacher`：教师；
- `phd`：博士生；
- `graduate_student`：硕士生；
- `graduate`：毕业生。

人员维护时应保证每名公开展示人员都有一个可见的主分类关系；学生还应填写适用的年级、学位类型和培养类型。毕业生及有明确去向的博士生可填写去向。

### 5.2 字段规则

| 字段 | 用途 | 维护规则 |
| --- | --- | --- |
| 姓名 | 公开名称 | 数据库已有姓名优先；变更前先核对是否会产生重复人员 |
| 年级 | 例如 `2022` | 页面显示为 `2022级`；统一使用“级”，不写“届” |
| 学位类型 | `bachelor`、`master`、`phd` | 用于学生和毕业生说明 |
| 培养类型 | 例如 `直博` | 仅在确有信息时填写 |
| 毕业去向 | 单位/学校等 | 仅填写已确认公开的信息 |
| 邮箱、研究方向、头像 | 可为空 | 不应以虚构占位资料替代空值 |

有头像和无头像学生在 V3 中分别排布：公开人员页优先展示有头像成员；学生名录会在有头像列表后另列无头像成员。头像上传后应确认 `avatarUrl` 可从公开站访问。

### 5.3 Excel 导入

人员 Excel 为敏感源数据，不纳入版本库。导入前先运行脚本的预览模式并人工核对姓名映射、类别和年级；写库前应备份目标数据库。具体参数以脚本帮助为准：

```bash
python3 scripts/import_student_directory.py --help
```

导入后在 `/ryjs` 和 `/ryjs/students` 检查分类、年级、去向与头像展示，不只检查数据库行数。

## 6. 论文维护

论文页面按年份、会议/期刊分组，条目展示标题、作者序列和 PDF 链接。`og_reserarch` 是当前论文数据表；会议/期刊名称、年份、作者和 PDF 均应以已核验信息为准。

论文工具位于 `scripts/publications/`，标准流程为：

1. 从 Scholar 存档提取候选标题；
2. 用外部元数据补全；
3. 预览导入结果；
4. 人工确认后再写入本地数据库或线上 API；
5. 补全和复核 PDF 链接。

完整命令与核验约束见 [scripts/publications/README.md](scripts/publications/README.md)。不得把未确认的预印本、无法确认的会议归属或猜测的 PDF 链接直接公开。

## 7. 其他公开内容与管理后台

管理后台目前维护以下内容：

- 团队成员；
- 小组新闻；
- 发表论文；
- 小组产品；
- 团队文化；
- 站内文章；
- 小组资源。

研究方向、新闻、文化影像和论文发生变更后，至少验证对应公开页面、首页摘要和后台列表三处是否一致。图片上传、删除或替换还要验证文件目录和公开文件 URL。

## 8. Docker 与生产部署

生产部署沿用根目录 `README.md` 的 Docker Compose 流程。部署前：

1. 将 `.env.example` 复制为 `.env`，替换全部示例密码、JWT 密钥、数据库地址和文件域名；
2. 根据实际域名更新 `dockerscript/caddy/Caddyfile`、前端生产 API 地址和 `OPENNLG_FILE_DOMAIN`；
3. 构建后端 JAR 与前端 `dist/`，复制到 `dockerscript/` 的相应目录；
4. 启动容器、等待 MySQL 健康，再导入 `database/schema.sql` 或已审核的数据库备份；
5. 恢复上传文件并验证 API、登录、文件访问和公开页面。

生产环境必须从环境变量读取数据库密码和 JWT 密钥。禁止重新把凭据写回 `application-prod.yml`、Docker Compose、提交记录或文档示例。

## 9. 离线 HTML 与 GitHub Pages

以下命令会读取当前本地数据库，构建 V3 公开页面并生成单个 HTML：

```bash
python3 scripts/build_offline_html.py
```

默认输出为 `exports/opennlg-public-offline.html`。该文件会嵌入当次可公开的数据和可嵌入的媒体，因此：

- 它适合离线预览、归档或经审核后的静态托管；
- 生成前必须核对人员、邮箱、图片、论文和新闻的公开授权；
- 不要把它、`exports/` 或数据库快照直接提交到默认开发分支；
- GitHub Pages 应使用专用发布分支或 Actions 工件，且只在完成公开数据审核后发布；
- 离线包不包含管理后台、登录功能或实时数据库写入能力。

## 10. 协作与交付检查

日常修改在 `develop` 分支进行，完成后创建 Pull Request 合并到 `main`。推送 `develop` 不会覆盖 `main`；只有合并或直接向 `main` 推送才会改变主分支。

提交前至少完成：

```bash
cd pageclient && npm run build
cd ../pageserver && mvn -DskipTests compile
cd .. && python3 -m unittest discover -s scripts/publications/tests -p 'test_*.py'
git diff --check
git status
```

提交前再核对：

- 未提交 `.env`、`application-local.yml`、数据库转储、Excel、MHTML、上传文件、`runs/` 或 `exports/`；
- 新增/修改的公开人员和论文均有来源与公开授权；
- 本地数据库迁移已记录、可复现；
- V3 公开页面、后台编辑和目标数据一致；
- 若涉及发布，完成独立的域名、HTTPS、数据公开范围检查。

## 11. 相关文档

- 原项目安装和 Docker 说明：[README.md](README.md)
- 数据库基线与迁移：[database/README.md](database/README.md)
- 论文核验和导入：[scripts/publications/README.md](scripts/publications/README.md)
- V3 视觉设计基线：[frontend-design.md](frontend-design.md)
