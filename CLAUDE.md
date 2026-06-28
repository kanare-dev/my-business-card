# Claude Code — プロジェクト方針

## 券面内容を変更したらビルドする

`src/` 以下のファイル（partials、templates、styles.css）を変更した後は、必ず以下を実行して生成物を更新する：

```bash
python3 build.py
```

これにより `build/`（HTML）、`dist/`（PDF）、`preview/`（PNG）がすべて更新される。

生成物（`dist/`、`preview/`）はGit管理対象なので、commit/push時には変更されたソースファイルと一緒に含める。

## 編集対象は `src/` のみ

| ディレクトリ | 役割 | 編集 |
|---|---|---|
| `src/partials/` | 表裏カードのHTMLフラグメント（単一ソース） | ✅ |
| `src/templates/` | プレビュー・印刷用テンプレート | ✅ |
| `src/styles.css` | 全共通スタイル・CSS Variables | ✅ |
| `assets/` | 画像・QRコード | ✅ |
| `build/` | 中間生成物（gitignore） | ❌ |
| `dist/` | 最終PDF（生成物） | ❌ |
| `preview/` | PNG プレビュー（生成物） | ❌ |

## インクルード構造

テンプレートは `<!-- include: partials/back.html -->` マーカーで partial を展開する仕組み。`build.py` がビルド時に展開する。partial を直接ブラウザで開いても動作しない。

## アセットパスは `../` 始まり

生成HTMLは `build/` に出力されるため、partial・テンプレート内のパスはすべて `../` を付ける：

- `../src/styles.css`
- `../assets/avatar.png`
- `../assets/qr-code.svg`

## 印刷仕様

- **仕上がり:** 55mm × 91mm（縦型）
- **塗り足し（bleed）:** 3mm → PDFサイズ 61mm × 97mm
- **セーフエリア:** 上下 8mm（`--safe-h`）、左右 7mm（`--safe-v`）
- **PDF生成:** Chrome headless（`--print-to-pdf`）、ローカルHTTPサーバー経由
- **入稿先:** ラクスル「標準名刺・両面」

## 裏面QRの上下均等配置について

`card__inner` は `top: bleed + safe-h` で配置されるため、カード上端から内側エリアまで視覚的に 8mm の余白がある。QR を単純センタリングすると上が広く見える。

**補正:** `src/templates/print-back.html` の `.card__qr-section` に `padding-bottom: var(--safe-h)` を設定することで上下の視覚的余白を均等にしている。

- bleed は裁断で消えるため補正値は `safe-h`（8mm）のみ。`bleed + safe-h` にすると過補正になる。
- プレビュー（`src/templates/index.html`）も同じく `padding-bottom: var(--safe-h)` を設定済み。

## デザイントークン（主要変数）

```css
--safe-h: 8mm;   /* 上下セーフエリア — QR補正値と連動 */
--safe-v: 7mm;   /* 左右セーフエリア */
--bleed:  3mm;   /* 塗り足し */
--color-accent: #d8aa00;  /* アクセントカラー */
--fs-name: 9.5mm;         /* 名前フォントサイズ（変更不要） */
```

`--safe-h` を変更した場合、QR補正の `padding-bottom` は変数参照のため自動追従する。
