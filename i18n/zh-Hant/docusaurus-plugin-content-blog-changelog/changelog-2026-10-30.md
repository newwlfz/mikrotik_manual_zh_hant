---
title: "文件更新 - 2026年10月30日"
date: 2026-10-30T00:00:00.000Z
slug: /changelog-2026-10-30
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026年10月30日 {#documentation-updates---october-30-2026}

October 30, 2026

2026年10月30日所做的文件更改摘要。

## 橋接與交換 {#bridging--switching}

-   **[L3 硬體解除安裝](/docs/bridging-and-switching/l3-hardware-offloading)**：更正了 ECMP 雜湊說明。啟用 L3 硬體解除安裝後，硬體轉發的 ECMP 使用交換晶片自身的雜湊掩碼，其中包含 TCP/UDP 埠，並忽略配置的雜湊策略；FastTrack 解除安裝的連線遵循核心 FIB 查詢，可能選擇不同的 nexthop。新增警告指出，同一流中混合硬體轉發與 FastTrack/CPU 轉發的封包可能導致非對稱路由和連線重設。[RouterOS 中的封包流](/docs/firewall-and-quality-of-service/packet-flow-in-routeros) 說明 FastPath 按目標地址快取路由，因此 `l4` 和 `l3-inner` 策略不會按流分散 FastPath 快取的流量；[路由決策](/docs/user-guides/routing-and-networking-protocols/routing-decision) 以及 [`/ip/settings`](/docs/cli-reference/ip/settings) 和 [`/ipv6/settings`](/docs/cli-reference/ipv6/settings) 參考文件與之相符。7.25 和 7.24 手冊中也有此說明。

## 高可用性解決方案 {#high-availability-solutions}

-   **[VRRP](/docs/high-availability-solutions/vrrp#hardware-offloading)**：新增“硬體解除安裝”一節。啟用 L3 硬體解除安裝後，處於 master 狀態的 VRRP 例項會被解除安裝：交換晶片對發往虛擬 MAC 地址的幀進行路由，並將其用作被路由流量的源 MAC 地址，且該例項顯示 `H`（`hw-offloaded`）標誌，該標誌在 [`/interface/vrrp`](/docs/cli-reference/interface/vrrp) 參考文件中描述。[L3 硬體解除安裝](/docs/bridging-and-switching/l3-hardware-offloading) 和 [Marvell Prestera 交換晶片特性](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 將 VRRP 列為可解除安裝，但 98DX3236、98DX224S、98DX226S 和 98DX2528 交換晶片除外。

## 使用者指南 {#user-guides}

-   **[路由選擇與過濾](/docs/user-guides/routing-and-networking-protocols/route-selection-and-filtering#community-regexp-matching)**：更多 community regexp 細節：反斜槓轉義一個字面字元（`\d` 匹配字母 `d`，因此數字請使用 `[0-9]`），匹配區分大小寫且不錨定。[`community-list`](/docs/cli-reference/routing/filter/community-list)、[`community-ext-list`](/docs/cli-reference/routing/filter/community-ext-list) 和 [`community-large-list`](/docs/cli-reference/routing/filter/community-large-list) 中的 `regexp` 描述說明，regexp 條目用於匹配以及由 `delete`/`filter` 使用，而 `append`/`set` 只使用具體值。

## 診斷與監控 {#diagnostics--monitoring}

-   **[Netwatch](/docs/diagnostics-monitoring-and-troubleshooting/netwatch)**、**[介面統計與 monitor-traffic](/docs/diagnostics-monitoring-and-troubleshooting/interface-stats-and-monitor-traffic)**：新增警告，說明指令碼策略：Netwatch 指令碼以 `read`、`write`、`test` 和 `reboot` 執行，`/tool/traffic-monitor` 指令碼以 `ftp`、`reboot`、`read`、`write` 和 `test` 執行。兩者都連結到 Scripting 頁面的指令碼許可權部分。Netwatch 警告也出現在 7.25 和 7.24 手冊中。

## CLI 參考 {#cli-reference}

-   **[`/routing/pimsm/interface-template`](/docs/cli-reference/routing/pimsm/interface-template)**、**[`/routing/pimsm/igmp-interface-template`](/docs/cli-reference/routing/pimsm/igmp-interface-template)**：這兩個選單分別配置：`interface-template` 僅啟用 PIM，`igmp-interface-template` 執行 IGMP/MLD 查詢器，因此一個介面可以執行 PIM、IGMP/MLD，或兩者同時執行。
-   **[CLI 參考](/docs/cli-reference#standard-list-entry-properties)**：`comment` 屬性限制為 16 KB。

## 物聯網 {#internet-of-things}

-   **[TG-LR 設定](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide)**：根據 TG-LR 源手冊重新生成。裝置命令描述詳細得多，配置感測器與資料規則已移至遙測下，磁開關與已知問題部分已擴充。頁面連結到上行鏈路負載解碼器指令碼以及出廠預設配置命令的下載；TG-LRX2 工具現在從 PyPI 安裝（`pip install tg-lrx2-utils`），而不是捆綁歸檔。

## 硬體 {#hardware}

-   **[FTC21-ups](/hardware/ftc21-ups)**：新的防風雨光纖轉銅纜轉換器手冊，帶 2.5G SFP 埠、兩個千兆乙太網埠（Ether2 上的 PoE-out）以及整合電池，可在短暫斷電期間維持執行。
-   **[KNOT Gateway LR8](/hardware/l14g-2ax-bt5-lr8-and-eg800k)**、**[KNOT Gateway HL9](/hardware/l14g-2ax-bt5-hl9-and-eg800q)**：新手冊，包含規格、快速入門、壁掛和抱杆安裝、供電、蜂窩調變解調器配置以及重設按鈕部分。HL9 是一款 IP66 IoT 閘道器，具有 BLE 5.1、915 MHz Wi-Fi HaLow、Wi-Fi、千兆乙太網、LTE Cat 1 bis 和 GNSS。
-   **[IAQM-THC2PV-W 和 IAQM-THC2PV-G](/hardware/iaqm-thc2pv-w-and-iaqm-thc2pv-g)**：安全螺絲使用 T9 Torx 批頭，而不是 TA23 三角批頭。
-   **[CRS326-24G-2S+RM](/hardware/crs326-24g-2s-plus-rm)**、**[CRS317-1G-16S+RM](/hardware/crs317-1g-16s-plus-rm)**、**[CRS309-1G-8S+IN](/hardware/crs309-1g-8s-plus-in)** 以及其他 11 個 CRS 交換器頁面：已按硬體頁面模板對齊：一個連結到產品頁面的標題、以列表形式呈現的安全警告、連結到“安裝”和“供電”部分的快速入門步驟、其中 12 個頁面上的新規格表，以及缺少時的重設按鈕部分。RouterOS/SwOS 啟動說明和 Marvell Prestera 特性參考現在格式化為步驟和連結。
-   **[RouterBOARD](/docs/hardware/routerboard)**：由 Mode 或 Reset 按鈕啟動的指令碼以 `ftp`、`reboot`、`read`、`write`、`test` 和 `romon` 策略執行。7.25 和 7.24 手冊中也有此說明。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
