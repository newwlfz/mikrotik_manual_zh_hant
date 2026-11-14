---
title: "文件更新 - 2026年7月6日"
date: 2026-07-06
slug: /changelog-2026-07-06
source: https://manual.mikrotik.com/changelog/changelog-2026-07-06
captured_at: '2026-11-04T06:08:09+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年7月6日所做的文件變更摘要。

## 橋接與交換 {#bridging--switching}

- **[Bridge](/docs/bridging-and-switching)**：記錄了 STP/MSTP 優先順序欄位的有效值步進規則。Bridge 和 MSTI 優先順序必須以 4096（0x1000）為步長設定——最低的 12 位會被忽略——並給出了完整的有效十六進位制/十進位制值列表；bridge port 和 MST-override port 優先順序必須以 16（0x10）為步長設定，並且現在使用顯式的 0x00–0xf0 值集合。此外還修復了在遷移過程中損壞的 port-cost-mode path-cost 參考表，將其呈現為同時包含 Long 和 Short 兩列的正確可摺疊表格。
- **[Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol)**：將相同的優先順序步進規則和有效值細節應用到了 CIST/MSTI/埠優先順序的說明中。

## 系統 {#system}

- **[Neighbor discovery](/docs/system-information-and-utilities/neighbor-discovery)**：新增了 "LLDP neighbors" 一節，記錄了只讀的 /ip/neighbor/lldp 選單，該選單僅針對透過 LLDP 發現的鄰居顯示詳細的 LLDP TLV（chassis ID、port ID、system name/description），並附有示例輸出，以及一條說明：lldpRemTable SNMP 表會排除僅由 CDP/MNDP 發現的條目。
