---
sidebar_key: "cli-reference/compare-versions"
sidebar_position: 1
title: "CLI 參考版本對比"
description: "比較兩個 RouterOS CLI 參考版本之間的引數。"
source: https://manual.mikrotik.com/docs/cli-reference/compare-versions
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

每個 RouterOS 版本都會帶來新的 CLI 參考：隨著功能演進，命令和引數會被新增、重新命名和刪除。在下方選擇兩個版本，以檢視它們之間添加了哪些引數以及刪除了哪些引數。

<CliCompare />

## 比較的工作原理 {#how-the-comparison-works}

- 資料由此倉庫中帶版本號的 CLI 參考頁面（`versioned_docs/version-*/cli-reference`）生成，因此它反映的是已釋出的頁面，而不是 RouterOS 原始碼本身。
- **引數** 是命令或選單的引數，包括只讀引數。**標誌** 是條目的屬性，例如 `disabled`、`running` 和 `invalid`。
- 當整個頁面在另一個版本中缺失時，命令或選單會被列在 *新增命令* 或 *刪除命令* 下。
- 目錄頁面（例如 `ip/firewall`）會列出該選單下每個條目的引數，因此在那裡被移除的引數實際上可能已移動到某個子選單頁面中。
