# Contributing

Thanks for considering a contribution! This skill is evidence-driven — every claim about a model's behavior should be traceable to either an official doc, a community post (link the source), or a reproducible test.

## What's most valuable to add

1. **New `automation/site-profiles/<platform>.md`** — for platforms currently marked ⏳ (unverified)
2. **Model-version updates** — when a platform ships a new version, the signature token list often shifts
3. **Better presets** in `templates/preset-packs.md`
4. **Counter-examples** — if a "rule" in this skill produces bad output on your task, file an issue with the prompt + screenshot

## How to update `community-prompt-patterns.md`

This is the cross-platform research consolidation. When adding a model, include:

- Structure formula (`Subject + Action + ...`)
- Length sweet spot (token / character count)
- Signature tokens (positive list)
- Taboos / known-bad patterns (negative list)
- Source links (3+ independent sources preferred)

## Style

- Markdown. No fancy HTML.
- Code blocks for prompts and CLI commands.
- Tables for per-model comparisons.
- Cite sources inline where the claim originated.
- Trad. Chinese OR English in body text is fine — but prompt examples should match the platform's native language preference (Seedance / Wan = Chinese; MJ / Flux / Sora 2 = English).

## What we won't accept

- Prompts that copy copyrighted lyrics / scripts
- Prompts targeting deepfakes of real people without context
- "Workaround" instructions for bypassing a platform's safety filters
- Personally identifiable information from any platform (account names, workspace UUIDs, payment info)

<!-- freedom-repository-guide:start -->
## 自由工坊：從一個成果到一個 PR

行銷與媒體公會的 AI 影像、影片、音樂提示詞與執行知識來源。 保留上游 Skill、平台能力檔、提示詞 templates、automation profiles 與 eval 案例。

先看[本倉 Issues](https://github.com/FreeTWAI/ai-media-generator/issues)與[現有 PR](https://github.com/FreeTWAI/ai-media-generator/pulls)。提出問題、這一輪範圍、完成條件與可投入時間，在 Issue 認領並協調重疊工作；維護者已直接派工時不必重複等待，將約定連回交接即可。使用自己的 fork／分支，PR 送到 **FreeTWAI/ai-media-generator:main**。

交給 Agent 前先讓它讀 [AGENTS.md](AGENTS.md)。PR 寫明變更用途、使用者可見結果、驗證命令、限制與原 Issue；附上可公開的合成案例或重現方式。Issue／PR 是程式協作的記錄，平台名片與公會身分不取代 repo 維護者的審查。

Skill 是使用者自己的工具；訂閱、provider 授權與本人操作不轉移到中央平台。平台只保存技能書來源／公開成果 ref，不接收私人 prompts、登入憑證或未授权媒體。

### 這個模組怎麼驗證

選擇與修改範圍相符的既有入口：

```sh
git diff --check
```

命令列在這裡不表示本輪已執行。先核對依賴與環境，再記錄實際結果；缺工具、桌面、媒體或授權時寫 `not_run` 與原因，不能補造成功。純文件修改以連結／路徑核對與 `git diff --check` 為主。 本 repo 沒有統一可執行測試；變更 Skill 時依 evals 的案例檢查並記錄，生成／發布實證另依本人授權。

### 署名與上游

工坊 Fork：上游產品／授權來源為 [Hao0321/ai-media-generator](https://github.com/Hao0321/ai-media-generator)；本次協作的 Issue／PR 送到 **FreeTWAI/ai-media-generator**，不是自動送往上游。 保留原作者與授權檔，另列真正完成文件、測試、設計、程式或協作的人。使用 AI 時如實交代協作範圍；只有實際 GitHub PR／review／合併紀錄可以作為對應貢獻證據，不能靠自填帳號推定。

自願貢獻不保證案源、XP、收益或雇用。若產生付費合作，由當事人另定條款與 Seller 外部收款；平台不代收。秘密、客戶資料、真實交易單據與未授權素材不進公開 Issue／PR。
<!-- freedom-repository-guide:end -->
