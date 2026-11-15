---
title: "文件更新 - 2026年11月2日"
date: 2026-11-02T00:00:00.000Z
slug: /changelog-2026-11-02
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026年11月2日 {#documentation-updates---november-2-2026}

November 2, 2026

2026年11月2日所做文件變更的摘要。

## 無線 {#wireless}

-   **[WiFi CAPsMAN](/docs/wireless/wifi/capsman)**：針對 Wi-Fi 7 CAP 的新 MLO 指南。組成 MLD 的所有介面必須使用相同的 SSID；新增示例透過 `multi-link-mode=auto` 配置射頻（或使用 `master` 使虛擬介面保持非 MLO），而 MLO CAP 需要在 `/interface/wifi/cap` 下設定 `mld-datapath=capdp`。對於帶 VLAN 的 MLO，僅啟用 `wpa3-psk`，在 provisioning 規則中匹配 Wi-Fi 7 頻段（或對所有頻段使用一條規則），並設定 `multi-link-mode`。CAPsMAN 轉發（`traffic-processing=on-capsman`）尚不支援 MLO，[Wi-Fi](/docs/wireless/wifi) 的 `traffic-processing` 說明中也提到了這一點。CAP 示例涵蓋 `wifi-qcom` 和 `wifi-mediatek` 兩個軟體包。

## VPN {#vpn}

-   **[IPsec](/docs/virtual-private-networks/ipsec#route-based-ipsec-with-xfrm-interfaces)**：新增“使用 XFRM 介面的基於路由的 IPsec”章節。XFRM 介面繫結到 IPsec 策略組，流量被路由到該介面中，而不是僅由策略選擇器匹配，因此動態路由協定可以在隧道上執行，路由標記或 VRF 可以將流量引導到該介面。一個雙路由器示例涵蓋了兩端的配置以及如何驗證。參考文件描述了標誌和引數（`mtu` 預設為 `1400`）。同樣收錄於 7.25 手冊中。

## 硬體 {#hardware}

-   **[NetMetal ax](/hardware/netmetal-ax)**：修正了供電說明：乙太網埠接受被動 PoE（18–28 V），而非 802.3af/at。新增規格表（IPQ-5010 CPU、256 MB RAM、128 MB NAND、2.4 和 5 GHz 802.11ax 射頻、一個 2.5G SFP 埠、miniPCIe 和一個 Nano SIM 插槽，工作溫度 −40 °C 至 +70 °C）。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
