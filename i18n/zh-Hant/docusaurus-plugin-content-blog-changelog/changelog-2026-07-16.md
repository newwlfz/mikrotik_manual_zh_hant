---
title: "文件更新 - 2026年7月16日"
date: 2026-07-16
slug: /changelog-2026-07-16
source: https://manual.mikrotik.com/changelog/changelog-2026-07-16
captured_at: '2026-11-04T06:08:13+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 16 日文件變更摘要。

## 認證與 AAA {#authentication--aaa}

- **[Certificates](/docs/authentication-authorization-accounting/certificates)**：新增了內建根證書頒發機構的完整列表，並列出每個機構的組織、通用名稱和主題 ID —— 涵蓋 Amazon、DigiCert、GlobalSign、Go Daddy、Sectigo、USERTrust 和 ISRG 根證書。另有一張表記錄了 SMIPS 裝置上縮減後的信任儲存（DigiCert Global Root G2、ISRG Root X1/X2、ISRG Root YE/YR）。同時註明該列表可在 /certificate/builtin/ 訪問。

## 系統 {#system}

- **[Scheduler](/docs/system-information-and-utilities/scheduler)**：記錄了 days 引數，該引數可將任務限制在一週中的特定日期（mon,wed,fri 或 always）。屬性列表已轉換為規範的表格，並新增了 policy 引數；start-time=startup 現已在 start-time 行中說明；新增的示例展示了一個僅在工作日執行的任務。同時還闡明瞭 days、start-time 和 interval 之間的互動方式。

## 硬體 {#hardware}

- **[RouterBOARD](/docs/hardware/routerboard)**：新增說明：Mode、Reset 和 WPS 按鈕的 on-event 指令碼以 read,write,reboot,ftp,romon,test 許可權執行。

## 網路管理 {#network-management}

- **[DHCP](/docs/network-management/dhcp)**：補全了此前為空的屬性說明，涉及 DHCP 用戶端（custom-source-mac-address、custom-hostname-suffix、caps-managers）和 DHCP 伺服器（address-lists、use-reconfigure）。擴充了 add-dns-entries 和 add-dns-entries-suffix 的說明，解釋 FQDN 如何根據用戶端主機名構建，並新增說明：父 DNS 區域必須已存在 —— DHCP 伺服器不會建立它。

## 快速入門 {#getting-started}

- **[x86 授權](/docs/getting-started/routeros-licensing/x86)**：新增了一條常見問題解答，說明如何更正已購買金鑰上輸錯的 Software ID，並提供了 mikrotik.com 賬戶中 "Fix Software ID" 選項的分步操作說明。
- **[RouterOS 授權](/docs/getting-started/routeros-licensing)**：各授權頁面之間的內部連結現已改用 Docusaurus 路由。

## 硬體指南 {#hardware-guides}

- **[硬體指南](/hardware/)**：修復了 80 個交換器和無線系統頁面中的失效 URL、標題層級和表格單元格標題，並將剩餘的 Confluence 幫助連結替換為 Docusaurus 路由。
