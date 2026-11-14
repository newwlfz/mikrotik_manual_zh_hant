---
title: "文件更新 - 2026年7月20日"
date: 2026-07-20
slug: /changelog-2026-07-20
source: https://manual.mikrotik.com/changelog/changelog-2026-07-20
captured_at: '2026-11-04T06:08:16+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 20 日文件變更摘要。

## 站點 {#site}

- **文件版本控制**：當前文件已凍結為版本 **7.24**，現在可以從版本下拉選單中選擇。凍結版本不會被搜尋引擎索引，對於當前文件中仍然存在的頁面，站點搜尋也不再返回來自凍結版本的重複結果。

## 身份驗證與 AAA {#authentication--aaa}

- **[證書](/docs/authentication-authorization-accounting/certificates)**：文件中每個證書屬性現在都會連結回證書儲存。受影響的頁面包括 [RADIUS](/docs/authentication-authorization-accounting/radius)、[User Manager](/docs/authentication-authorization-accounting/user-manager)、[Container apps](/docs/containers/apps)、[LoRa](/docs/internet-of-things/lora/general-properties)、[MQTT](/docs/internet-of-things/mqtt)、[Wiliot](/docs/internet-of-things/wiliot)、[TR-069](/docs/management-tools/tr-069)、[OpenFlow](/docs/network-management/openflow)、[Fetch](/docs/system-information-and-utilities/fetch)、[IPsec](/docs/virtual-private-networks/ipsec)、[OpenVPN](/docs/virtual-private-networks/openvpn) 和 [SSTP](/docs/virtual-private-networks/sstp)。

## 無線 {#wireless}

- **[WiFi](/docs/wireless/wifi)**：澄清了 Network 部分——不帶標籤的 /interface/wifi/network 條目會應用於所有介面，並且示例現在標註為 network 和 radio 預設。MLO 示例增加了一個 security.passphrase 值。
