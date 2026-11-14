---
title: "文件更新 - 2026年6月15日"
date: 2026-06-15
slug: /changelog-2026-06-15
source: https://manual.mikrotik.com/changelog/changelog-2026-06-15
captured_at: '2026-11-04T06:07:59+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 15 日文件變更摘要。

## 認證與 AAA {#authentication--aaa}

- **[Certificates](/docs/authentication-authorization-accounting/certificates)**：澄清了證書屬性描述——現在將 digest-algorithm 描述為用於對證書進行簽名的雜湊演算法，將 invalid-before/invalid-after 描述為有效期的開始日期和到期日期；同時修正了 key-usage 值的格式。這屬於對 dot1x、PPP AAA、RADIUS 和 User Manager 頁面進行更廣泛措辭修正的一部分。
- **[HotSpot Customisation](/docs/authentication-authorization-accounting/hotspot-captive-portal/hotspot-customisation)**：對 HotSpot 自定義指南進行了小幅修正。

## 橋接與交換 {#bridging--switching}

- **[Cannot upgrade SwOS](/docs/bridging-and-switching/swos/troubleshooting)**：新增了一份故障排除指南，涵蓋 SwOS 升級失敗後的恢復。其中包括針對僅執行 SwOS 的裝置（CSS106、CSS326、CSS610）使用硬體復位以引導進入備份韌體的分步操作流程，以及雙啟動裝置（CRS3xx）的序列埠控制檯恢復、透過 /system swos upgrade 進行的 RouterOS CLI 升級，以及 RouterOS 7.17+ 中的 device-mode 限制。
- **[CRS1xx/2xx series switches](/docs/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples)**：修正了單播 FDB 容量的表述（最多 16k 條 MAC 表項）以及巨型幀的數值。相關修正還涉及 L3 Hardware Offloading（預設值、lpm-usage 表述）、MACsec 示例以及 VLAN（disabled 屬性描述）頁面。
- **[Bridging & Switching Case Studies](/docs/bridging-and-switching/user-guides/bridge-igmp-mld-snooping)**：展開了 SDVoE 這一縮寫（Software Defined Video over Ethernet），並修正了 IGMP/MLD 偵聽及相關案例示例中的 VLAN 優先順序值。

## 容器 {#containers}

- **[Container Apps](/docs/containers/apps/available-apps)**：修正了可用應用列表中的若干應用描述（conduit、mediamanager、prowlarr、webtop），並澄清了 network-outgoing-access 引數——當其設為 no 時會建立一條 mangle drop 規則。此外還對 HAProxy、Home Assistant、Matrix Synapse、Mosquitto、ThingsBoard 和 FreeRADIUS 示例進行了小幅格式修正。
- **[Mosquitto MQTT Server](/docs/containers/user-guides/container-mosquitto-mqtt-server)**：修復了一個失效的防火牆文件連結。

## 物聯網 {#internet-of-things}

- **[The Things Stack](/docs/internet-of-things/lora/user-guides/the-things-stack)**：為傳統 UDP 場景和現代 LNS/CUPS（LoRa Basics Station）場景新增了網關注冊步驟，包括相應的 RouterOS 配置以及關於為 lora 服務使用內建信任儲存的說明。

## 無線 {#wireless}

- **[Wireless](/docs/wireless)**：按產品/技術系列重新組織了無線章節——拆分為 Wi-Fi 6/6E (802.11ax)、Wi-Fi 5 (802.11ac) 和 802.11 a/b/g/n 三個獨立部分——並在概覽頁面上提供了裝置分流指南、統一的章節簡介、入門連結、CAPsMAN 相互交叉引用，同時移除了過時的版本說明。
- **[Wi-Fi 5 (802.11ac)](/docs/wireless/wifi-ac)**：新增了一條警告，指出 wifi-qcom-ac 驅動佔用資源較多，建議 802.11ac 裝置使用原有的輕量級無線驅動。
