---
sidebar_key: "introduction"
sidebar_position: 1
title: "簡介"
sidebar_label: "簡介"
description: "MikroTik RouterOS 是一款適用於 MikroTik 裝置的強大網路作業系統，在一個平臺中提供路由、防火牆、VPN、無線管理、QoS、自動化和監控工具，用於網路的構建與運維。"
tags:
  - 'cli-reference'
source: https://manual.mikrotik.com/docs/7.25/introduction
captured_at: '2026-11-04T11:19:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik RouterOS 是驅動 MikroTik 路由器、交換器和無線裝置的網路作業系統。它把路由、防火牆、VPN、無線管理、服務質量、自動化和監控工具彙集到單一平臺中，用於構建和運維各種規模的網路。

## 文件的組織方式 {#how-the-documentation-is-organized}

左側邊欄是這本手冊的地圖。各分類的排列順序會帶你從通用知識走向具體功能，因此從頭到尾依次閱讀的讀者，會從初次接觸裝置一路走到高階配置。

整體流程如下：

- **入門** 介紹如何訪問新裝置、首次配置、安裝、授權、升級以及基礎安全。
- 隨後的各主題章節分別聚焦系統的一個領域：管理工具、系統資訊與實用工具、診斷與監控、硬體、有線與無線連線、行動網路、橋接與交換、網路服務、路由協定、防火牆與服務質量、虛擬專用網路、使用者管理、高可用性、物聯網、儲存以及容器。
- **開發者指南** 面向為 RouterOS 編寫自動化程式的人員，介紹指令碼和程式設計介面。
- **CLI 參考** 位於最後，屬於查閱型內容，而非從頭讀到尾的章節。

如果裝置對你是全新的，請從入門開始。基礎系統就緒後，再轉到與你任務相符的主題章節。把 CLI 參考當作工作中隨時查閱的字典，而不是從前讀到後的章節。

## 查詢資訊 {#finding-information}

有幾種方式可以定位內容：

- **搜尋。** 搜尋框會為每個頁面的全文建立索引。當你知道關鍵字、命令或屬性名時，這是最快的途徑。
- **側邊欄和麵包屑。** 瀏覽側邊欄以探索某個主題，並檢視每個頁面頂部的麵包屑導航，瞭解自己處於結構的哪個位置。
- **頁內目錄。** 頁面右側的列表連結到該頁面的各個標題，因此在較長的文章中可以直接跳到所需的部分。
- **版本選擇器。** 當釋出了多個版本文件時，頂部導航中的版本下拉選單可讓你選擇要閱讀的文件版本。

## CLI 參考 {#the-cli-reference}

[CLI 參考](./cli-reference/index.md) 按控制檯路徑記錄 RouterOS 的命令選單和屬性。透過選單查詢功能，例如 `/ip/address` 或 `/routing/bgp`，即可找到可用的命令、配置物件，以及每個屬性及其型別和預設值。

這一部分由 RouterOS 系統本身自動生成，而非人工編寫。選單、命令和引數型別都從軟體中提取，因此該參考與系統實際暴露的內容保持同步。每個引數都會列出引數型別，解釋這些型別的圖例位於 CLI 參考的起始頁面。由於該部分是自動生成的，請按控制檯路徑查閱並依賴搜尋，不要指望每個主題都有一篇手工編輯的文章。

## 發行說明與文件更新 {#release-notes-and-documentation-updates}

有兩個獨立的部分記錄事物如何隨時間變化：

- **[文件變更](/changelog/)** — 按日期彙總手冊中的改動，並附有受影響頁面的連結。在你上次訪問之後新增、更正或重新組織的內容，都可以在這裡檢視。
- **[產品新聞](/blog/)** — MikroTik 的產品公告和新聞簡報。

## 報告錯誤與提出改進建議 {#reporting-mistakes-and-suggesting-improvements}

如果你發現錯誤、過時的說明或頁面中的缺漏，請告訴我們。請傳送電子郵件至 [support@mikrotik.com](mailto:support@mikrotik.com)，說明頁面地址並簡要描述問題。如果方便，請附上你期望看到的準確措辭，這樣可以加快更正的進度。針對單個頁面的清晰報告，是為所有人改進手冊的最有效方式。

## 面向 AI 工具的機器可讀訪問 {#machine-readable-access-for-ai-tools}

整本手冊都以純文字格式釋出，因此不僅能在瀏覽器中閱讀，也能被檢索流水線、助手和其他自動化工具讀取。

可用的端點如下：

| 端點 | 用途 |
| --- | --- |
| [`/llms.txt`](pathname:///llms.txt) | 包含每個頁面的索引，附有簡短描述和連結。它遵循 [llms.txt 約定](https://llmstxt.org)，旨在作為工具首先讀取的入口，用於發現有哪些內容存在。 |
| [`/llms-full.txt`](pathname:///llms-full.txt) | 將整本手冊拼接成單個純文字檔案，適用於批次攝取或載入完整的本地副本。 |
| 每頁 Markdown | 任意頁面的原始原始檔。在文件地址後追加 `.md`，例如 [`/docs/introduction.md`](pathname:///docs/introduction.md)，即可獲取其背後的 Markdown。 |
| [`/sitemap.xml`](pathname:///sitemap.xml) | 標準站點地圖，為爬蟲和索引器列出每個頁面。站點的 `robots.txt` 允許標準爬蟲和 AI 爬蟲訪問。 |

常見做法是先讀取 `/llms.txt` 找到相關頁面，然後按需獲取各個 `.md` 頁面以瞭解細節。如果你希望一次性獲得完整語料，則改為載入 `/llms-full.txt`。這些檔案在每次構建時都會重新生成，因此始終與已釋出的頁面保持一致。
