---
title: "文件更新 - 2026年7月2日"
date: 2026-07-02
slug: /changelog-2026-07-02
source: https://manual.mikrotik.com/changelog/changelog-2026-07-02
captured_at: '2026-11-04T06:08:07+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 2 日文件變更摘要。

## 認證與 AAA {#authentication--aaa}

- **[Certificates](/docs/authentication-authorization-accounting/certificates)**：新增了“手動 ACME 續期”一節，記錄了 /certificate/acme-renew 命令並附帶用法示例。同時明確了 PKCS12 匯出使用 AES 加密，以及 PKCS12 匯入同時支援 AES 和 3DES 解密。

## 系統 {#system}

- **[Wake on LAN](/docs/system-information-and-utilities/wake-on-lan)**：重構了頁面 —— 屬性表已替換為指向 CLI 參考的連結，措辭更加精煉，並新增了一張 Wake on LAN 工具的 WinBox 截圖。interface 和 mac 引數現在在 CLI 參考中說明。

## 診斷與監控 {#diagnostics--monitoring}

- **[Ping](/docs/diagnostics-monitoring-and-troubleshooting/ping)**：新增了指向 CLI 參考的交叉連結，其中每個 ping 引數現在都有說明 —— address、interval、size、ttl、dscp、do-not-fragment、src-address、arp-ping、count、interface 和 vrf，以及所有隻讀結果欄位，例如 packet-loss、min-rtt、avg-rtt 和 max-rtt。
