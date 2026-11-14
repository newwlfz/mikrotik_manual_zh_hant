---
title: "文件更新 - 2026年8月11日"
date: 2026-08-11
slug: /changelog-2026-08-11
source: https://manual.mikrotik.com/changelog/changelog-2026-08-11
captured_at: '2026-11-04T06:08:26+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年8月11日所做的文件變更摘要。

## VPN {#vpn}

- **[GRE/EoIP](/docs/virtual-private-networks/eoip)**、**[OpenVPN](/docs/virtual-private-networks/openvpn)**、**[L2TP](/docs/virtual-private-networks/l2tp)**、**[ZeroTier](/docs/virtual-private-networks/zerotier)**、**[WireGuard](/docs/virtual-private-networks/wireguard)**、**[IPsec](/docs/virtual-private-networks/ipsec)**、**[SSTP](/docs/virtual-private-networks/sstp)**、**[PPTP](/docs/virtual-private-networks/pptp)**、**[PPPoE](/docs/virtual-private-networks/pppoe)**、**[6to4](/docs/virtual-private-networks/6to4)** 和 **[IPIP](/docs/virtual-private-networks/ipip)**：已將 CLI 引數表移入 CLI Reference，並改寫了相關說明文字（同時將 IPsec 頁面從 .mdx 轉換為 .md）。

## 高可用性解決方案 {#high-availability-solutions}

- **[Bonding](/docs/high-availability-solutions/bonding)**、**[VRRP](/docs/high-availability-solutions/vrrp)** 和 **[MLAG](/docs/high-availability-solutions/multi-chassis-link-aggregation-group)**：已將 CLI 引數移入 CLI Reference。

## 橋接與交換 {#bridging--switching}

- **[服務質量](/docs/bridging-and-switching/quality-of-service)**：已將交換器 QoS 引數移入 CLI Reference。

## 網路管理 {#network-management}

- **[ARP](/docs/cli-reference/ip/arp)**：刪除了重複的 ARP 文章，並將其引數說明合併到 CLI Reference 中。
- **[DNS](/docs/network-management/dns)**：澄清了 DNS-over-HTTPS（DoH）服務的相容性——已將 Control D 加入相容列表，並改寫了“不相容”列表的措辭，以反映這些服務僅在 ARM64、x86 和 CHR 裝置上可用。

## 容器 {#containers}

- **[Container Mosquitto MQTT Server](/docs/containers/user-guides/container-mosquitto-mqtt-server)**：修復了一個失效連結。

## 系統 {#system}

- **[裝置模式](/docs/system-information-and-utilities/device-mode)**：修復了一個失效連結。
