---
title: "文件更新 - 2026年9月28日"
date: 2026-09-28
slug: /changelog-2026-09-28
source: https://manual.mikrotik.com/changelog/changelog-2026-09-28
captured_at: '2026-11-04T06:08:52+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年9月28日文件變更摘要。

## 開發者指南 {#developer-guides}

- **[REST API](/docs/developer-guides/rest-api)**：已在 RouterOS 7.25 上重寫並驗證，每個示例都重新執行，每個輸出都重新捕獲。新增章節涵蓋：使用自己的證書頒發機構配置 HTTPS、最小許可權的 REST 使用者、限制訪問、讀取和修改記錄、執行命令，以及構建儀表盤或整合，其中包括一個由 AI 助手編寫的示例。頁面現在說明：REST 使用者需要同時具備 rest-api 和 api 策略，並且請求體需要 Content-Type: application/json。頁面還說明：PATCH 僅對記錄有效（設定選單使用 POST .../set）、60 秒限制以及如何在其範圍內操作，以及同一使用者的請求會逐個執行。其他新增內容：10 分鐘登入快取、路由器不傳送 CORS 頭，以及一張列出狀態碼和錯誤詳情的問題排查表。修正了舊的錯誤示例（應為 400，而非 406）、帶引號數字的解析方式，以及設定選單的回覆結構。僅適用於 LTE 的示例已替換為可在任何路由器上執行的示例：將一個地址封禁一天、把配置儲存到伺服器，以及一個 Python 流量讀取器。

## 防火牆與 QoS {#firewall--qos}

- **[UPnP](/docs/firewall-and-quality-of-service/upnp)**：已重寫，並針對 RouterOS 7.25 進行了驗證。修正了 allow-disable-external-interface 的預設值（為 no），將 forced-external-ip 重新命名為 forced-ip，刪除了啟用新介面條目的過時步驟（新條目建立時即為啟用狀態），並說明多個外部介面可以並行提供對映，每個介面都作為獨立的 WAN 連線裝置通告。補充了技術細節：服務埠（SSDP 使用 UDP 1900，控制使用內部介面地址的 TCP 2828）、僅接受永久對映，以及任何設定變更都會移除所有動態埠對映。
- **[NAT-PMP](/docs/firewall-and-quality-of-service/nat-pmp)**：按照 RFC 6886 重寫。修正了埠說明（服務監聽 UDP 5351，用戶端監聽 UDP 5350 上的外部地址通告），說明只接受一個外部介面，並將示例輸出替換為文字（舊的埠對映註釋不可能來自 NAT-PMP 請求，因為該請求不攜帶描述欄位）。
- **[SSH 暴力破解防護](/docs/firewall-and-quality-of-service/user-guides/bruteforce-prevention)**：改用可在預設防火牆中正常工作的規則集重寫；舊規則被放在預設 drop 規則之後，且自身沒有 drop 規則。新增了受信任地址、解除封禁，以及這些規則仍允許多少次密碼嘗試的說明。
- **[埠敲門](/docs/firewall-and-quality-of-service/user-guides/port-knocking)**：敲門規則現在位於預設 drop 規則之前，損壞的口令（layer 7）示例已用可正常工作的用戶端重新構建。
- **[DDoS 防護](/docs/firewall-and-quality-of-service/user-guides/ddos-protection)**：說明了檢測的工作原理以及它在哪些情況下不再有效。刪除了從未匹配的 SYN-ACK 規則，以及會留下 0.0.0.0 條目的列表建立行。

## 入門 {#getting-started}

- **[保護你的路由器](/docs/getting-started/securing-your-router)**：修正了命令和說法：示例密碼中包含一個非拉丁字母，密碼中的 $ 必須轉義，WAN 防火牆示例現在可在預設配置下正常工作，available-from 取代了已棄用的 address，並且 strong-crypto 的說明有誤。

## 高可用性解決方案 {#high-availability-solutions}

- **[MLAG](/docs/high-availability-solutions/multi-chassis-link-aggregation-group)**：描述了 mlag-state 的各個取值。

## 系統 {#system}

- **[服務](/docs/system-information-and-utilities/services)**：/ip/service 和 Web 伺服器屬性表已移至 CLI Reference。頁面保留了適用於各引數的通用內容，包括 available-from 會讓埠仍然可見，因此仍需使用防火牆來抵禦不受信任的網路。

## CLI 參考 {#cli-reference}

- **[/ip/service](/docs/cli-reference/ip/service)、[/ip/service/webserver](/docs/cli-reference/ip/service/webserver)**：補齊了所有引數的說明：

- tls-version 所接受的 TLS 版本。
- 未配置證書時 www-ssl 僅提供匿名加密套件。
- available-from 如何拒絕用戶端。
- 埠已被佔用時出現的 invalid 標誌。
- 每個 Web 伺服器元件（rest-plain、webfig-secure 及其他）在關閉時都會返回 403 Forbidden，以及 index-* 何時生效。

- **[/user/group](/docs/cli-reference/user/group)**：策略說明現在指出，set 會保留其未列出的策略，因此要撤銷某項策略需使用 !。
- **[/ip/upnp](/docs/cli-reference/ip/upnp)、[/ip/upnp/interfaces](/docs/cli-reference/ip/upnp/interfaces)、[/ip/nat-pmp](/docs/cli-reference/ip/nat-pmp)、[/ip/nat-pmp/interfaces](/docs/cli-reference/ip/nat-pmp/interfaces)**：補齊了所有引數的說明，包括預設值、forced-ip 的作用，以及 allow-disable-external-interface 的 ForceTermination 行為。
- **[CLI 參考](/docs/cli-reference)**：從約 40 個命令頁面中刪除了 RouterOS 已不再擁有的引數，例如 /disk、/system/health 和 /lcd 中的引數，並標記了已棄用的引數。
