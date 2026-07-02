"""
脳ニュース毎晩リサーチ
4分野（認知/運動/栄養/睡眠 × 認知機能）の新着をWeb検索でまとめて
_archive/brain-news/YYYY-MM-DD.md に保存する。
"""
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import anthropic

MODEL = "claude-sonnet-4-6"
MAX_WEB_SEARCHES = 12

PROMPT = """以下の4分野について、本日（過去24〜36時間）の新着情報をWeb検索して、構造化Markdownでまとめてください。
すべての分野は「認知機能」を軸にしています。

**分野:**
1. 認知機能と脳（病態・診断・薬物・神経科学全般）
2. 認知機能と運動（身体活動・運動療法・リハビリ）
3. 認知機能と栄養（食事・サプリ・特定栄養素）
4. 認知機能と睡眠（睡眠の質・睡眠時間・睡眠障害）

**情報源（優先順）:**
- ケアネットニュース (carenet.com/news)
- Medical Tribune・日経メディカル
- PubMed（過去7日以内の新着）
- Nature / NEJM / Lancet の公式ニュース・プレス
- 日本神経学会・国立長寿医療研究センターなど公的機関の発表

**各分野ごとに最大3件、本当に重要な新着があれば取り上げ、なければ「特になし」と明記。**

**各記事の書式:**
- **タイトル**
- 出典 / URL
- 3〜5行の要約（一次情報重視）
- **なぜToraponが注目すべきか**（1〜2行：臨床的意義）
- **インタビューポイント**（Toraponに聞くべき質問、1〜2問）

**最後に「今夜の総括」を3行以内で。**

出力フォーマット例：

```markdown
# YYYY-MM-DD 脳科学ブリーフィング

**収集日時**: YYYY-MM-DD（朝）
**4分野（すべて「認知機能」軸）**: 脳 / 運動 / 栄養 / 睡眠

---

## ① 認知機能と脳

### 1-1. タイトル
- **出典**: 媒体名
- **URL**: https://...
- **要約**: ...
- **なぜToraponが注目すべきか**: ...
- **インタビューポイント**: ...

### 1-2. 〈特になし〉

---

## ② 認知機能と運動

（同様）

---

## ③ 認知機能と栄養

（同様）

---

## ④ 認知機能と睡眠

（同様）

---

## 今夜の総括

1. ...
2. ...
3. ...
```

Markdown本体のみ出力してください（前置き・後書き不要）。"""


def main() -> None:
    client = anthropic.Anthropic()
    today_jst = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d")

    response = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        tools=[
            {
                "type": "web_search_20250305",
                "name": "web_search",
                "max_uses": MAX_WEB_SEARCHES,
            }
        ],
        messages=[{"role": "user", "content": PROMPT.replace("YYYY-MM-DD", today_jst)}],
    )

    markdown_parts = [
        block.text for block in response.content if block.type == "text"
    ]
    markdown = "\n".join(markdown_parts).strip()

    if not markdown:
        raise SystemExit("No markdown produced from Claude response")

    output_dir = Path("_archive/brain-news")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{today_jst}.md"
    output_path.write_text(markdown + "\n", encoding="utf-8")
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
