# Business Card — Kanare Kodera

個人名刺のデザインファイル。技術イベント（AWS Summit、JAWS UG など）での配布用。

## デザイン

- **コンセプト:** ミニマル・上質・静かなデザイン（Apple / MUJI 系）
- **サイズ:** 91mm × 55mm（縦型・両面）
- **印刷:** CMYK 想定、塗り足し 3mm 考慮
- **フォント:** Inter（名前・肩書き）/ JetBrains Mono（技術タグ・ラベル）

## ファイル構成

```
my-business-card/
├── index.html   # HTML/CSS 実装（ブラウザプレビュー・印刷用）
└── prompt.md    # デザイン仕様・要件定義
```

## プレビューの確認方法

### ブラウザで開く（最速）

```bash
open index.html
```

または VS Code の拡張機能「Live Server」を使うと、コード変更をリアルタイムで確認できます。

### 印刷プレビュー

ブラウザで `index.html` を開き、`Cmd + P` → 「印刷」で印刷プレビューを確認できます。  
`@media print` スタイルが適用され、プレビュー UI（ラベル・塗り足しガイド）は非表示になります。

### カスタマイズ

`index.html` 冒頭の `:root` 内の CSS Variables を変更するだけでデザインを調整できます。

```css
:root {
  --color-bg:           #0B0B0B;   /* 背景色 */
  --color-text-primary: #FFFFFF;   /* 主テキスト */
  --fs-name:            9.5mm;     /* 名前フォントサイズ */
  /* ... */
}
```

## Figma

デザインの Figma ファイルはこちら:

🔗 **[Business Card — Kanare Kodera](https://www.figma.com/design/WoKecPvSgTHemnVCIW4pFt)**

| 面 | 内容 |
|---|---|
| 表面 | 名前（Inter Extra Light）/ Cloud Engineer / 技術タグ |
| 裏面 | QR コードプレースホルダー / 連絡先 / 背景モノグラム "K" |

> **QR コードについて:** Figma・HTML ともに現在はプレースホルダーです。印刷前に実際の URL（例: `kanare.dev`）の QR コード画像を差し替えてください。

## 印刷（ラクスル）

1. `index.html` をブラウザで開く
2. `Cmd + P` → 用紙サイズを **91 × 55mm**（縦）に設定
3. 「背景のグラフィックを印刷する」を有効にする
4. PDF として保存 → ラクスルへアップロード

塗り足しガイド（赤い半透明のアウトライン）は印刷時に自動で非表示になります。
