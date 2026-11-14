---
title: "文件更新 - 2026年7月14日"
date: 2026-07-14
slug: /changelog-2026-07-14
source: https://manual.mikrotik.com/changelog/changelog-2026-07-14
captured_at: '2026-11-04T06:08:13+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 14 日文件變更摘要。

## 橋接與交換 {#bridging--switching}

- **[L3 硬體解除安裝](/docs/bridging-and-switching/l3-hardware-offloading)**：記錄了硬體解除安裝的 VRF 支援。新增的 “Hardware-Offloaded VRF” 章節列出了哪些交換晶片支援該功能（98DX8xxx、98DX4xxx、98DX325x、98CX8410、98DX7xxx），哪些不支援（98DX3xxx、98DX2xxx），每顆晶片的 VRF 表數量上限（512 或 1024），介面關聯規則，以及透過 /interface/ethernet/switch/rule 中的 new-vrf 選項對入向流量進行 VRF 分配。Marvell Prestera 交換晶片功能頁面新增了與之對應的 VRF 條目。
- **[網橋](/docs/bridging-and-switching)**：新增了 “DHCP Snooping 繫結表” 章節，描述構建在 /interface/bridge/host 之上的 DHCPv4 snooping 繫結資料庫，包括 dhcpv4-status、dhcpv4-ip、dhcpv4-server-id 和 dhcpv4-expires-after 欄位，VLAN filtering 下基於 MAC–VLAN 的識別，以及 WinBox/控制檯截圖。

## 容器 {#containers}

- **[容器](/docs/containers)**：統一了屬性表中型別/預設值的格式，修復了渲染不正確的有序列表縮排，並修正了細微的語法問題。
