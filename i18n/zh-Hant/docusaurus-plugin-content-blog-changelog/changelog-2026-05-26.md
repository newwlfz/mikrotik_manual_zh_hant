---
title: "文件更新 - 2026年5月26日"
date: 2026-05-26
slug: /changelog-2026-05-26
source: https://manual.mikrotik.com/changelog/changelog-2026-05-26
captured_at: '2026-11-04T06:07:46+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 5 月 26 日文件變更摘要。

## 無線 {#wireless}

- **[WiFi](/docs/wireless/wifi)：Wi-Fi 7 MLO 引數已加入文件** — 新增的 mld-interface 和 mld-name 引數可在 Wi-Fi 7 (802.11be) 硬體上啟用多鏈路操作（Multi-Link Operation）。CAPsMAN 配置新增 multi-link-mode 和 supported-hw-caps。supported-bands 擴充套件支援 6ghz-ax、6ghz-be、2ghz-be。
- **[IS-IS](/docs/user-guides/routing-and-networking-protocols/unicast/is-is) 文件已更新** — 對 IS-IS 路由協定頁面進行了全文更正、補充和語法改進。

## 認證與 AAA {#authentication--aaa}

- **[RADIUS](/docs/authentication-authorization-accounting/radius)：RadSec 行為已澄清** — RADIUS 伺服器必須使用 radsec 作為共享金鑰；啟用 RadSec 後，RouterOS 會同時覆蓋共享金鑰和埠（改為 TCP 2083），無論手動設定如何。

## 網路管理 {#network-management}

- **[SOCKS](/docs/network-management/socks)：使用者認證已寫入文件** — /socks/users 選單現已完整記錄（此前為“Work in Progress”）。涵蓋啟用基於密碼的認證（auth-method=password）以及管理憑據。
- **[VRF](/docs/user-guides/routing-and-networking-protocols/vrf) 文件已更新** — VRF 頁面經過大幅修訂，結構更完善並補充了交叉引用連結。

## IP 服務 {#ip-services}

- **[DNS](/docs/network-management/dhcp)：新增引數已寫入文件** — 在 DHCP 和 IPv6 鄰居發現頁面中新增了 add-dns-entries 和 add-dns-entries-suffix。

## 行動網路 {#mobile-networking}

- **[LTE](/docs/mobile-networking/lte-5g)：兩個引數已寫入文件** — esim-channel（用於 eSIM 的自動/AT 控制通道）和 link-recovery-timer（LTE 介面未執行時，重新配置前等待的秒數）。已移除未釋出功能的佔位條目。

## 入門 {#getting-started}

- **[入門](/docs/getting-started) 章節已重組** — 移動了圖片、修復了失效連結，並在整個入門章節中添加了交叉引用。

## CLI 參考 {#cli-reference}

- **新增 IPv4/IPv6 地址與鄰居引數** — [/ip/address](/docs/cli-reference/ip/address)、[/ipv6/address](/docs/cli-reference/ipv6/address)、[/ipv6/nd](/docs/cli-reference/ipv6/nd) 以及 /ipv6/pool 現在在 CLI 參考中都有完整的引數說明。
- **路由文章：已新增 CLI 交叉引用連結** — 所有路由文件頁面現在都連結到相應的 CLI 參考條目。
