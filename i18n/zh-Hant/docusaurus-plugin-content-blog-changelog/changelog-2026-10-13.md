---
title: "文件更新 - 2026年10月13日"
date: 2026-10-13T00:00:00.000Z
slug: /changelog-2026-10-13
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026 年 10 月 13 日 {#documentation-updates---october-13-2026}

October 13, 2026

2026 年 10 月 13 日文件變更摘要。

## 使用者指南 {#user-guides}

-   **[路由選擇與過濾](/docs/user-guides/routing-and-networking-protocols/route-selection-and-filtering#community-regexp-matching)**：新增“Community 正則表示式匹配”部分。一個 community 列表項包含具體的 `communities` 或一個 `regexp`，同一個列表可以混合使用兩者。正則表示式會與每個 community 的輸出形式進行匹配：標準 community 為 `asn:value` 或熟知名稱，擴充套件 community 為帶型別的 `rt:`/`soo:` 形式，large community 為三個十進位制欄位。示例按 large community 的管理域刪除或拒絕路由。另外新增：對於沒有 community 屬性的路由，“any” 匹配器返回 false，“subset” 匹配器返回 true，因此使用 `bgp-communities-empty`（或 extended 和 large 變體）來測試屬性是否為空；帶列表的 `delete` 還會刪除與其 regexp 條目匹配的 community，而 `append` 和 `set` 僅使用具體值。

## 入門 {#getting-started}

-   **[IPv6 鄰居發現](/docs/getting-started/networking-fundamentals/ipv6-neighbor-discovery)**：對於介面 `all` 的 `/ipv6/nd` 條目，其優先順序低於為特定介面配置的條目。

## 管理工具 {#management-tools}

-   **[CMR](/docs/management-tools/cmr#run-script-permissions)**：run-script 許可權部分將 `/system backup save`、`/system reset-configuration` 和 `/file copy` 列為被拒絕的命令。`/export` 可用並返回用戶端配置，因此 `run-script` 可以從整個裝置群收集配置匯出；敏感值仍保持隱藏（`/export` 會省略它們，`show-sensitive` 不會顯示它們，而 `get` 會將它們顯示為 `*`）。

## 硬體 {#hardware}

-   **[KNOT LR8G kit](/hardware/knot-lr8g-kit)**、**[KNOT LR9G kit](/hardware/knot-lr9g-kit)**：已針對 G 套件更正：GPS 模組位於 LoRa 卡上（不支援 GLONASS、BeiDou 或 Galileo），microUSB 埠僅用於外設，不能用於供電。GNSS 配置部分現在為 GPS 配置，並連結到 GPS 指南；BG77 AT 命令說明已替換為兩項天線檢查（從 LoRa 卡到 SMA 埠的 U.FL 轉接線，以及標有 GNSS 的 SMA 埠上的外部天線）。已連結 Modbus 配置指南。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
