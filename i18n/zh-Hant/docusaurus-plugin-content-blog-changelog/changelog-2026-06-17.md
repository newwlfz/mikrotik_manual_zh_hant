---
title: "文件更新 - 2026年6月17日"
date: 2026-06-17
slug: /changelog-2026-06-17
source: https://manual.mikrotik.com/changelog/changelog-2026-06-17
captured_at: '2026-11-04T06:08:00+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 17 日文件變更摘要。

## 認證與 AAA {#authentication--aaa}

- **[Certificates](/docs/authentication-authorization-accounting/certificates#crl)**：新增專門的 CRL（證書吊銷列表）章節，說明 RouterOS 如何根據證書的 CRL 驗證證書。說明如何啟用 crl-use=yes 和 crl-download=yes，以及如何透過 URL 手動新增 CRL，或從證書的 CRL 分發點動態新增 CRL。包含 /certificate/crl 選單的屬性表（akid、cert、dynamic、expired、fingerprint、last-update、next-update、num、removed、signature、url）。

## 管理工具 {#management-tools}

- **[WebFig](/docs/management-tools/webfig)**：重寫並更新了 WebFig 頁面，措辭更清晰，並更換了新截圖。HTTPS 設定步驟經過修訂，改為使用終端實體證書和 www-ssl 服務；Terminal 章節已整理；**Design Skin** 章節已重構，對每項操作（隱藏選單/子選單/標籤頁、重新命名、備註、只讀、標誌）進行了更清晰的描述，並增加了 numeric-interval（1..10）和 prefix（station$）欄位限制的示例。
