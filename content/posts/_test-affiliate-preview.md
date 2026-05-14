---
title: "（動作確認用）アフィリエイト表示プレビュー"
date: 2026-05-05
draft: true
affiliate: true
categories: ["テスト"]
tags: ["test"]
build:
  list: never
  render: always
---

これは shortcode の動作確認用の下書きです。本番には公開されません（`draft: true` と `build.list: never` を指定）。

front matter で `affiliate: true` を指定しているので、この記事の冒頭には自動で「PR表記」が挿入されているはずです（タイトルのすぐ下）。

## 商品カードの表示テスト

以下は `{{</* affiliate */>}}` shortcode の表示例です。

{{< affiliate
    title="オムロン 上腕式血圧計 HEM-7281T"
    image="/images/tiger.png"
    amazon="https://example.com/amazon-link"
    rakuten="https://example.com/rakuten-link"
    description="現場でもよく使われている定番モデル。Bluetooth でスマホアプリと連携して測定値を自動記録できます。" >}}

## 画像なし・Amazonのみのパターン

{{< affiliate
    title="リハビリの王道"
    amazon="https://example.com/amazon-link"
    description="理学療法士が読んで参考になった本。" >}}

## PR表記を本文中に手動で入れたいとき

下記のように `{{</* pr-notice */>}}` を書くと、本文中の好きな位置に PR 表記を挿入できます。

{{< pr-notice >}}

以上、動作確認用ページです。
