# OpenNLG 数据库

此目录只保存可公开的结构和迁移脚本，不保存真实成员资料、账号密码、上传文件或导出的生产数据。

## 新环境

使用具备建库权限的 MySQL 8 账号创建空库后执行：

```bash
mysql -u root -p -e "CREATE DATABASE opennlg CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p opennlg < database/schema.sql
```

然后通过 `scripts/import_student_directory.py`、论文导入脚本或管理后台导入已审核的数据。上传文件应同步到 `OPENNLG_FILE_PATH` 指定目录。

## 已有环境升级

先完整备份数据库，再按文件名顺序执行 `pageserver/src/main/resources/db/migration/` 下的脚本。每个脚本只能在对应结构尚未升级的数据库上执行一次；执行记录与备份时间应写入部署记录。

不要将 `学生数据.xlsx`、Google Scholar 导出文件、数据库转储、账号密码或上传图片提交到 Git。
