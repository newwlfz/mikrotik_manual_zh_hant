---
title: "文件更新 - 2026年5月27日"
date: 2026-05-27
slug: /changelog-2026-05-27
source: https://manual.mikrotik.com/changelog/changelog-2026-05-27
captured_at: '2026-11-04T06:07:46+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年5月27日文件變更摘要。

## 擴充套件功能 {#extended-features}

- **[Container Apps](/docs/containers/apps)**：新增 network-outgoing-access 引數，用於控制容器應用是否具有出站網路訪問許可權。當該引數設定為 no 時，系統會自動建立一條 mangle drop 規則，以阻止該特定容器的出站流量。

## 入門 {#getting-started}

- **[Backup](/docs/getting-started/configuration-management/backup)**：澄清了引言部分的描述——備份功能會將路由器配置儲存到二進位制檔案中（此前描述為“克隆”），使措辭更加準確。
