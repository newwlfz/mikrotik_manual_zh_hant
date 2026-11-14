---
title: "文件更新 - 2026年10月27日"
date: 2026-10-27T00:00:00.000Z
slug: /changelog-2026-10-27
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026年10月27日 {#documentation-updates---october-27-2026}

October 27, 2026

2026年10月27日所做的文件變更摘要。

## 使用者指南[​](#user-guides "Direct link to User Guides") {#user-guides}

-   **[RPKI](/docs/user-guides/routing-and-networking-protocols/unicast/rpki)**：針對 ASPA 和 RTR 協定版本 2 進行了擴充套件。RouterOS 以版本 2 啟動 RTR 會話，並自動回退到版本 1；協商後的版本顯示在 [`/routing/rpki/session`](/docs/cli-reference/routing/rpki/session) 的 `version` 欄位中。新增章節涵蓋字首源驗證和 ASPA 驗證：驗證狀態、如何驗證它們，以及相關要求（支援 RTR 版本 2 併發布 ASPA 物件的驗證器、在 eBGP 連線上使用 `local.role` 設定 RFC 9234 角色集，以及在過濾鏈中使用 `rpki-aspa-verify`）。[路由選擇與過濾](/docs/user-guides/routing-and-networking-protocols/route-selection-and-filtering) 列出了 `rpki-aspa` 屬性和 `rpki-aspa-verify` 命令，且 [`/routing/route`](/docs/cli-reference/routing/route) 描述了 `rpki-aspa`。

## 橋接與交換[​](#bridging--switching "Direct link to Bridging & Switching") {#bridging--switching}

-   **[CRS3xx 和 CSS3xx (SwOS)](/docs/bridging-and-switching/swos/crs3)**、**[CSS106](/docs/bridging-and-switching/swos/css106)**、**[CSS610](/docs/bridging-and-switching/swos/css610)**、**[GPEN21](/docs/bridging-and-switching/swos/gpen21)**：描述了 `DHCP with fallback` 地址獲取及其時序。交換器每秒傳送一次 DHCP 請求，在沒有伺服器應答時使用靜態地址，在伺服器應答後 1–2 秒獲得租約，並在租約時間過半時續租。當續租無人應答時，它會在 5 秒內返回靜態地址並恢復請求。
-   **[L3 硬體解除安裝](/docs/bridging-and-switching/l3-hardware-offloading)**：在功能表中新增了關於 L3 硬體解除安裝和 FastPath 的 ECMP 雜湊策略的說明，並新增到 [RouterOS 中的封包流](/docs/firewall-and-quality-of-service/packet-flow-in-routeros)、[路由決策](/docs/user-guides/routing-and-networking-protocols/routing-decision) 以及 `/ip/settings` 和 `/ipv6/settings` 參考中。這些說明已於 10 月 30 日更正。

## CLI 參考[​](#cli-reference "Direct link to CLI Reference") {#cli-reference}

-   **[CLI 參考](/docs/cli-reference)**：基於更新的 RouterOS 7.26 測試構建重新生成。新增選單：[`/interface/wifi/easymesh`](/docs/cli-reference/interface/wifi/easymesh)（包含 `bss`、`sta`、`topology`、`dpp-trigger` 和 `wps-push-button`）；[`/system/resource/hardware`](/docs/cli-reference/system/resource/hardware) 中的 `power-cycle`、`power-reset` 和 `reset-overcurrent` 命令以及 `overcurrent` 計數器；以及 `/app/settings/remove-certificate`。新增引數包括 [`/certificate/import`](/docs/cli-reference/certificate/import) 中的 `pem`，[`/container`](/docs/cli-reference/container) 中的 `labels` 和 `image-labels`，bonding 中的 `lacp-strict`，網橋中的 `dhcp-snooping-option82-policy` 和 STP 拓撲變更計數器，網橋埠上的 `host-moves`，`forced-on-a` 和 `forced-on-bt` PoE-out 模式，以及 IPFIX 中的 `nat-src-address6`/`nat-dst-address6`。在 [`/interface/ethernet/pon`](/docs/cli-reference/interface/ethernet/pon) 中重新設計了 PON ONU 身份欄位（`ploam-password`、`loid`、`loid-password`、`vendor-id`、`serial-number`、`equipment-id` 等），並且 `/routing/stats/memory` 報告 `reserved`、`free` 和 `fragmentation`。[`/system/routerboard/settings`](/docs/cli-reference/system/routerboard/settings) 頁面已移動，並保留了其描述。7.25 和 7.24 參考在同一輪中獲得了少量修復。

## 硬體[​](#hardware "Direct link to Hardware") {#hardware}

-   **[LAMP 5G R16](/hardware/lamp-5g-r16)**：包含圖片的新安裝說明：使用 U 型螺栓進行抱杆安裝（杆徑 25–60 mm）和壁掛安裝（6 mm 孔和牆塞），並警告裝置必須垂直安裝。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
