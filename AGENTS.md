# AGENTS.md — 健康ブログ「健康の窓口／脳の健康」(torapon-kenkou.com)

## ユーザーについて
- 理学療法士・非エンジニア。専門用語を避けた平易な日本語で説明する。
- 迷ったら勝手に進めず確認する。リスクは先回りして指摘する。

## このリポジトリ
- Hugo + Cloudflare Pages。GitHub: masatoshi-nakahama5/my-blog（Private厳守）。
- 記事: `content/posts/<slug>/index.md` + `images/`。front matter に title/date/categories/weight。
- **公開は自動**: main へ push すると自動ビルド＆公開（毎時0分にもcron実行）。未来日付=予約公開。
- **push 前に必ずユーザーへ「GitHubへ送ってOK？」と確認する。**
- ⚠️ GitHubのcronは2〜3時間飛ぶことがある（実測: 02:44→05:46→08:05）。**X投稿の予定時刻の6時間以上前**に
  公開時刻を置く。急ぐときは `gh workflow run "Daily deploy"` で手動起動。
- 手動デプロイ（通常不要）: `hugo` → `npx wrangler pages deploy public --project-name my-blog`

## 記事の約束
- 一覧の並びは weight で制御（小さいほど上）。同テーマは近い weight で隣接させる。
- 吹き出し会話（読者→Torapon）を1記事3〜5か所。
- 太字の罠: `**` を「」（）や句読点に密着させない。NG=`**「〜」**` / OK=`「**〜**」`。書いたらレンダリング後に生の `**` が残っていないか確認。
- 表現はマイルドに（例:「頭の回転が遅い」→「考えるスピードがゆっくりめ」）。
- 医療的断定をしない。ワクチン・薬の記事は接種/入手を勧めない（かかりつけ医相談を促す）。
- 記事プレビューが404のときは date が未来になっていないか確認。
- カバー画像はユーザーがChatGPTで生成→幅1200px JPEG (quality 88) に変換して使う。
- 図・グラフは PIL で自作（matplotlib未導入）。模式図には「イメージ図です（実測値ではありません）」を入れる。
- いらすとや画像は Blogger フィードAPIで検索: `https://www.irasutoya.com/feeds/posts/default?q=<単語>&alt=json&max-results=12`

## アフィリエイト
- もしもアフィリエイト。健康ブログのAmazonは a_id=5534074（ゴルフブログとは別ID・混同しない）。
- 広告は1記事2〜3個まで。書影は `m.media-amazon.com/images/P/{ISBN10}` が確実。

## セキュリティ
- APIキー・トークンをコードに書かない。個人情報をコミットしない。リポジトリは Private のまま。

## X告知（参考・Codexは実行不可）
- @Torapon0104（「脳の健康」）・1記事1本・公開翌日20:00。X予約はブラウザ作業のため手動またはClaudeが担当。
