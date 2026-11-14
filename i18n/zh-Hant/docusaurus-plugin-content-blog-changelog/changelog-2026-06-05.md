---
title: "文件更新 - 2026 年 6 月 5 日"
date: 2026-06-05
slug: /changelog-2026-06-05
source: https://manual.mikrotik.com/changelog/changelog-2026-06-05
captured_at: '2026-11-04T06:07:52+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 5 日文件變更摘要。

## CLI 參考 {#cli-reference}

- **[BGP](/docs/cli-reference/routing/bgp)**：修正了 vrf 引數說明中的語法錯誤（"connections operates" → "connections operate"），更正了 input.last-notification 中的拼寫錯誤（"notificatin" → "notification"），並清理了 input.affinity 說明中重複的 HTML。修正了 output.no-early-cut 說明中的 "NPLRI" → "NLRI"。將 EVPN rd 引數中的 "RDs form" 更正為 "RDs from"。
- **[OSPF](/docs/cli-reference/routing/ospf/interface-template)**：將 ptp 介面的預設網路型別說明從 "point-to-point" 更正為正確的 "ptp" 值，並補上了動作說明中缺失的句號。
- **[RIP](/docs/cli-reference/routing/rip/instance)**：修正了 route-timeout 與 update-interval 之間被互換的說明——超時說明此前被錯誤地分配給了 update-interval 引數。補上了 originate-default 中缺失的句號。
- **[Routing Filter](/docs/cli-reference/routing/filter/rule)**：從 communities 引數說明中移除了無用的 "ask Google" 提示。
- **[Router ID](/docs/cli-reference/routing/id)**：在 Router ID 選擇文件中補上了缺失的 only-static 選項，該選項只選取靜態配置的地址。
- **[Fantasy Routing](/docs/cli-reference/routing/fantasy)**：修正了 prefix-length 引數說明中的 "refix length" 拼寫錯誤 → "Prefix length"。
- **[PIM-SM](/docs/cli-reference/routing/pimsm)**：將此前位置不當的 spt-bit 標誌說明整合進正確的 ArgTableRow，使其能與其他標誌一起正確渲染，而不再作為純文字單獨懸掛。

## 開發者指南 {#developer-guides}

- **[Scripting](/docs/developer-guides/scripting)**：修正了換頁跳脫字元的十六進位制值（\f 此前被錯誤列為 0xFF，現更正為 0x0C）。修正了 :resolve 命令示例（port= → server-port=）。清理了各程式碼示例中的行尾空白和不一致的縮排。
- **[API](/docs/developer-guides/api)**：修正了長度編碼規範（最大值由 0x7FFFFFFFFF 改為 0xFFFFFFFFF）。更正了 VLAN 介面查詢示例（type=ether → type=vlan）。修正了 .proplist 文件中的 "high-performance penalty" → "high performance penalty"。
- **[REST API](/docs/developer-guides/rest-api)**：修正了 GET 過濾示例的說明過濾器（"valid addresses" → "dynamic addresses"）。更正了 POST 文件，說明命令字編碼在 URL 中（而非請求頭中）。修正了 .proplist 示例（此前錯誤地使用了 _proplist）。修正了多個示例呼叫，使其使用 HTTPS，並更正了 LTE 韌體升級示例中 number → numbers 的引數拼寫錯誤。修正了 REST API 索引說明，移除了冗餘的 "Developer guides cover" 字首。
- **[Python3 API Example](/docs/developer-guides/api/python3-example)**：修正了 "Becasue" → "Because" 及 "pasword" → "password" 的拼寫錯誤。修復了引數解析程式碼中被破壞的縮排。

## 容器 {#containers}

- **[Available Apps](/docs/containers/apps/available-apps)**：新增頁面，列出 100 多個可從 RouterOS App 選單部署的可用容器應用，涵蓋家庭自動化、媒體伺服器、檔案共享、網路監控和開發工具等類別。
- **[Apps](/docs/containers/apps)**：重新組織了 Containers 目錄結構——將已棄用的 apps.rb 頁面移入 Apps/ 目錄，並刪除了導致導航衝突的重複 Containers/ 資料夾。

## 入門 {#getting-started}

- **[Netinstall](/docs/getting-started/installation-and-upgrade/netinstall)**：修復了 Netinstall 頁面從 getting-started/ 移至 getting-started/installation-and-upgrade/ 後，5 個檔案中損壞的相對連結和絕對連結。更新了 Configuration Management、RouterOS Licensing、Device Mode 以及 5 月 29 日變更日誌條目中的入站連結。
