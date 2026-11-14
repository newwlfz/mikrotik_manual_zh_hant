---
title: "文件更新 - 2026年6月19日"
date: 2026-06-19
slug: /changelog-2026-06-19
source: https://manual.mikrotik.com/changelog/changelog-2026-06-19
captured_at: '2026-11-04T06:08:03+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年6月19日文件變更摘要。

## 管理工具 {#management-tools}

- **[WebFig](/docs/management-tools/webfig#enable-https)**：圍繞僅限區域網路使用的場景重構了“啟用 HTTPS”章節。現在該章節首先介紹自簽名證書（當透過路由器的私有區域網路 IP 訪問路由器時，這是預設方式，因為公共 CA 無法為私有地址簽發證書），並說明如何透過信任路由器的根 CA 來消除瀏覽器警告。Let's Encrypt/ACME 方式現在被明確定位為適用於透過真實公網域名訪問的路由器的選項，並註明了私有 IP、名稱匹配和分離 DNS 方面的注意事項，以及不開放 WAN 埠的 DNS-01 挑戰。

## 身份驗證與 AAA {#authentication--aaa}

- **[證書](/docs/authentication-authorization-accounting/certificates#acme-client)**：清理了 Let's Encrypt/ACME、CRL 和 Settings 章節。命令和引數引用（a 標誌、crl-use、crl-download、/certificate/settings）現在格式化為內聯程式碼，而不再是損壞的斜體/引號標記；IP Cloud DNS-01 那句話已透過指向 IP Cloud DDNS 頁面的連結加以澄清，並且第一個 add-acme 示例使用了具體的域名。

## 入門 {#getting-started}

- **[首次配置](/docs/getting-started/first-time-configuration)**：新增了一個無線設定影片，現以規範的 &lt;video&gt; 播放器嵌入，影片片段來自 static/videos/。
