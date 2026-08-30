# OpenNLG 会议论文导入流程

该工具以 Google Scholar 个人主页为候选发现入口，但不会自动请求 Google Scholar。请在浏览器中打开目标个人主页，点击“显示更多”直到 2025 年及之后的条目都加载完成，然后使用“另存为”保存完整网页（HTML）。

## 1. 提取候选项

```bash
python3 scripts/publications/extract_scholar.py \
  --input /absolute/path/to/scholar-profile.html \
  --output-dir runs/publications/2026-08-28
```

脚本只保留 2025 年至运行当天年份内、来源匹配 `venues.json` 白名单的候选项。它会产生 `candidates.json`、`rejected.json` 与 `review.csv`。

## 2. 补全元数据

```bash
python3 scripts/publications/enrich_publications.py \
  --input runs/publications/2026-08-28/candidates.json \
  --output-dir runs/publications/2026-08-28
```

补全优先使用 DBLP，失败后使用 Crossref。请检查 `review.csv`：Google Scholar 可能截断作者，且“出现在 Scholar”不等于“已被会议录取”。

将确认需要展示的记录修改为：

```text
decision=include
acceptance_confirmed=yes
```

并确保 `authors` 是完整作者序列。未确认或预印本论文保持空白，不会导入。

## 3. 预览导入（默认，不写数据库）

```bash
python3 scripts/publications/import_publications.py \
  --input runs/publications/2026-08-28/review.csv \
  --output runs/publications/2026-08-28/import-preview.json
```

## 4. 经人工确认后写入数据库

先设置短期 JWT，不要把它写入文件或命令历史：

```bash
read -rs OPENNLG_API_TOKEN
export OPENNLG_API_TOKEN
python3 scripts/publications/import_publications.py \
  --input runs/publications/2026-08-28/review.csv \
  --output runs/publications/2026-08-28/import-result.json \
  --api-base https://opennlg.cn/api \
  --apply
unset OPENNLG_API_TOKEN
```

写入前脚本会按“标准化标题 + 正式年份”读取现有论文并去重。导入使用现有受保护的 `/reserarch/create` 接口，不会连接 MySQL 或保存数据库凭据。

## 5. 重新复核快照中的所有近期论文

当 Scholar 的来源仍显示 arXiv、但论文可能已被会议录取时，使用以下命令重新提取快照中全部 2025 年至当前年份的标题，并逐篇查询 DBLP 与 Crossref：

```bash
python3 scripts/publications/verify_all_titles.py \
  --input /absolute/path/to/scholar-profile.mhtml \
  --output-dir runs/publications/full-audit
```

输出的 `verification-results.json` 会保留每篇的 Scholar 原始来源和 DBLP/Crossref 证据；`review-all.csv` 是供人工确认的合并审核表。只有外部会议元数据命中 `venues.json` 白名单时，状态才会是 `verified_conference`。

传入 `--reuse-from <旧 verification-results.json>` 可复用此前已经取得的 DBLP/Crossref 证据。OpenAlex 与 Semantic Scholar 仅作为二次/三次检索来源，尝试补全开放 PDF，不参与会议准入判断。`verified-conferences.json` 与 `verified-conferences.csv` 只包含“DBLP/Crossref 独立确认会议且已有 PDF 链接”的最终记录；已确认但未找到 PDF 的记录单列在 `verified-missing-pdf.json`。

若 Semantic Scholar 首次查询被限流，可仅对缺 PDF 的已确认会议论文低频重试：

```bash
python3 scripts/publications/backfill_pdfs.py \
  --input runs/publications/final-audit-2024/verification-results.json \
  --output-dir runs/publications/final-audit-2024
```

若仍缺 PDF，可按 DBLP 的公开 `ee` 链接定向解析 ACL Anthology、OpenReview、PMLR、NeurIPS 等官方论文库：

```bash
python3 scripts/publications/resolve_official_pdfs.py \
  --input runs/publications/final-audit-2024/verification-results.json \
  --output-dir runs/publications/final-audit-2024
```

脚本还会生成严格最终输出 `verified-conferences.json` 与 `verified-conferences.csv`，其中只保留 DBLP 或 Crossref 独立确认、并命中白名单会议的记录。

## 6. 会议与期刊的包容性复核

若展示范围需要覆盖所有已正式发表的会议和期刊论文（不受 `venues.json` 白名单限制），在严格会议审计完成后运行：

```bash
python3 scripts/publications/audit_formal_publications.py \
  --input runs/publications/final-audit-2024/verification-results.json \
  --overrides scripts/publications/formal_publication_overrides.json \
  --output-dir runs/publications/inclusive-audit-2024
```

该步骤生成 `confirmed-publications.json`（有 DBLP/Crossref 元数据或官方 proceedings 证据的正式发表记录）及 `needs-official-confirmation.json`（预印本或尚缺正式证据的记录）。它不会覆盖严格会议结果，也不会写入网站数据库。
