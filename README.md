# Business Card — Kanare Kodera

個人名刺のデザインファイル。技術イベント（AWS Summit、JAWS UG など）での配布用。

## デザイン

- **コンセプト:** ミニマル・ダーク（[kanare.dev](https://kanare.dev) と統一）
- **サイズ:** 91mm × 55mm（縦型・両面）
- **印刷:** CMYK 想定、塗り足し 3mm 考慮
- **フォント:** IBM Plex Sans JP（名前・肩書き）/ JetBrains Mono（技術タグ・連絡先）
- **アイコン:** Tabler Icons（統一ストロークスタイル）

## ファイル構成

```
my-business-card/
├── assets/
│   ├── avatar.png       # プロフィール画像
│   └── qr-code.svg      # QR コード（kanare.dev）
├── dist/
│   ├── front.pdf        # 印刷用 PDF（表面）61mm × 97mm
│   └── back.pdf         # 印刷用 PDF（裏面）61mm × 97mm
├── src/
│   ├── styles.css       # 共通スタイル（CSS Variables・コンポーネント）
│   ├── partials/
│   │   ├── front.html   # 表面カードの HTML フラグメント
│   │   └── back.html    # 裏面カードの HTML フラグメント
│   └── templates/
│       ├── index.html       # プレビュー用テンプレート
│       ├── print-front.html # 印刷用テンプレート（表面）
│       └── print-back.html  # 印刷用テンプレート（裏面）
├── build.py         # ビルドスクリプト
├── index.html       # 生成物 — プレビュー用
├── print-front.html # 生成物 — 印刷用（表面）
└── print-back.html  # 生成物 — 印刷用（裏面）
```

> **編集するのは `src/` 以下のみ。** `index.html` / `print-*.html` は生成物なので直接編集しない。

## ビルド

```bash
python3 build.py         # HTML 生成 + PDF 生成（dist/）
python3 build.py --html  # HTML 生成のみ
```

PDF 生成には Google Chrome（macOS）が必要です。

## プレビュー

```bash
python3 -m http.server 8080
# → http://localhost:8080/
```

`index.html` を直接ブラウザで開くことも可能ですが、ローカルサーバー経由の方がフォントの読み込みが安定します。

塗り足しガイド（金色のアウトライン）はプレビュー時のみ表示され、印刷時は自動で非表示になります。

## カスタマイズ

`src/styles.css` の `:root` 内の CSS Variables を変更するだけでデザインを調整できます。

```css
:root {
  --color-bg:    #131210;  /* 背景色 */
  --color-accent: #d8aa00; /* アクセントカラー */
  --fs-name:     9.5mm;    /* 名前フォントサイズ */
  /* ... */
}
```

変更後は `python3 build.py` で再ビルド。

## 印刷（ラクスル）

1. `python3 build.py` で `dist/front.pdf` / `dist/back.pdf` を生成
2. ラクスルで「標準名刺」「両面」を選択
3. `dist/front.pdf`（表面）・`dist/back.pdf`（裏面）をアップロード

PDF はラクスル指定の仕上がりサイズ（91mm × 55mm）+ 塗り足し 3mm = **61mm × 97mm** で出力されます。
