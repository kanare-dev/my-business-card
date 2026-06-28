# Claude Code — プロジェクト方針

## 券面内容を変更したらビルドする

`src/` 以下のファイル（partials、templates、styles.css）を変更した後は、必ず以下を実行して生成物を更新する：

```bash
python3 build.py
```

これにより `build/`（HTML）、`dist/`（PDF）、`preview/`（PNG）がすべて更新される。

生成物（`dist/`、`preview/`）はGit管理対象なので、commit/push時には変更されたソースファイルと一緒に含める。
