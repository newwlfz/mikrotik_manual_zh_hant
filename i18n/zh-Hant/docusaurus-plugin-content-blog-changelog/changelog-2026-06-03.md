---
title: "文件更新 - 2026年6月3日"
date: 2026-06-03
slug: /changelog-2026-06-03
source: https://manual.mikrotik.com/changelog/changelog-2026-06-03
captured_at: '2026-11-04T06:07:50+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 3 日所做的文件變更摘要。

## 身份驗證與 AAA {#authentication--aaa}

- **[證書](/docs/authentication-authorization-accounting/certificates)**：更新了 ACME 示例，使得在省略 directory-url 時，Let's Encrypt 證書生成會使用預設的目錄 URL。
- **[證書](/docs/authentication-authorization-accounting/certificates)**：新增了 wiliot 和 logging，作為 trust-store 與 builtin-trust-store 證書設定支援的值。

## 開發者指南 {#developer-guides}

- **[REST API](/docs/developer-guides/rest-api)**：澄清了透過 www 和 www-ssl 服務進行 HTTP 與 HTTPS 訪問的方式，並添加了指向 IP Service 和 Certificate 文件的連結。

## 行動網路 {#mobile-networking}

- **[LTE/5G](/docs/mobile-networking/lte-5g)**：新增了離線 FOTA/DFOTA 調變解調器韌體升級指南，包括適用於本地檔案和 HTTP URL 的韌體檔案示例、調變解調器相容性表格以及安全警告。

## 網路管理 {#network-management}

- **[DNS](/docs/network-management/dns)**：新增了關於使用內建證書頒發機構儲存以及在 ARM64、x86 和 CHR 裝置上進行 HTTP/2 協商的 DNS over HTTPS 說明。
