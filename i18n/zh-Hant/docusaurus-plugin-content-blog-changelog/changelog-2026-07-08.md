---
title: "文件更新 - 2026 年 7 月 8 日"
date: 2026-07-08
slug: /changelog-2026-07-08
source: https://manual.mikrotik.com/changelog/changelog-2026-07-08
captured_at: '2026-11-04T06:08:09+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 8 日文件變更摘要。

## 管理工具 {#management-tools}

- **[Console](/docs/management-tools/console)**：將單獨的 "Command Line Interface" 頁面合併到 Console 頁面，使所有 CLI/console 相關內容集中在一處，並相應更新了 Scripting、Bluetooth 和 MQTT 頁面中的交叉引用，同時修復了 Quick Typing 部分的一個小格式問題。

## 開發者指南 {#developer-guides}

- **[Scripting](/docs/developer-guides/scripting)**：為 print 命令記錄了 order-by 引數，該引數最多可按三個屬性對輸出進行排序（在屬性前加 - 表示降序），並附有示例。

## 高可用性解決方案 {#high-availability-solutions}

- **[VRRP](/docs/high-availability-solutions/vrrp)**：新增了 v3-checksum-as-v2 設定，用於控制 VRRPv3 IPv4 校驗和是否包含 IPv4 偽首部。預設值（no）與 FRR 等基於 Linux 的實現一致；將其設為 yes 可相容 Cisco 及其他廠商。該設定僅適用於 VRRPv3 IPv4，且 Virtual Router 中的所有路由器必須使用相同的值，以避免 "bad checksum" 錯誤。
