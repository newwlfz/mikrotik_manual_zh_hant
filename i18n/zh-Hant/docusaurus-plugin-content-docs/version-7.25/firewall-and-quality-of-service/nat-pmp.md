---
sidebar_key: "firewall-and-quality-of-service/nat-pmp"
sidebar_position: 6
title: "NAT-PMP"
sidebar_label: "NAT-PMP"
description: "NAT-PMP 讓區域網路用戶端獲知路由器的外部 IPv4 地址並請求埠對映，從而使應用程式在 NAT 後方無需手動埠轉發即可接受入站連線。內容涵蓋啟用 RouterOS NAT-PMP 服務以及分配外部和內部介面。"
tags:
  - 'nat-pmp'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/nat-pmp
captured_at: '2026-11-04T11:15:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

NAT 埠對映協定（NAT-PMP，[RFC 6886](https://www.rfc-editor.org/rfc/rfc6886)）讓區域網路中的應用程式能夠獲知路由器的外部 IPv4 地址並請求埠對映，因此需要接受傳入連線的應用程式（例如遊戲、點對點用戶端以及語音或視訊通話）無需手動配置埠轉發即可在 NAT 後正常工作。NAT-PMP 在 Apple 裝置上很常見。RouterOS 還支援 [UPnP](./upnp.md)，這是一種用途相同的替代協定。

用戶端透過 UDP 埠 5351 向路由器傳送請求，每個對映都有一個有限的生命週期，由用戶端進行續期。生命週期到期後，該對映會被刪除。NAT-PMP 服務預設處於停用狀態。

對映僅對請求發出的源地址生效：用戶端無法為其他裝置建立對映，因此只能把可信網路連線為 internal 介面。該協定沒有身份驗證機制。

## 配置示例 {#configuration-example}

![Network diagram: the router connects to the Internet on ether1 (10.0.0.1/24) and to a LAN switch on ether2 (192.168.88.1/24); two computers, PC1 (192.168.88.10/24) and PC2 (192.168.88.11/24), are on the 192.168.88.0/24 LAN](/img/a8f12d6db929635a.webp)

前提條件：LAN 已對外部介面做 masquerade，例如：

```ros
/ip/firewall/nat/add action=masquerade chain=srcnat out-interface=ether1
```

啟用該服務，並把面向 Internet 的介面標記為 external、把面向用戶端的介面標記為 internal：

```ros
/ip/nat-pmp/set enabled=yes
/ip/nat-pmp/interfaces/add interface=ether1 type=external
/ip/nat-pmp/interfaces/add interface=ether2 type=internal
```

此時內部介面上的用戶端就可以請求自己的外部地址和埠映射了。只能指定一個外部介面；再新增第二個時會被拒絕，並返回 `failure: only one external interface can be added to the list`。如果外部介面有多個地址，請在介面條目上設定 `forced-ip`，以選擇向用戶端報告哪個地址。

:::warning
在使用 VLAN 的環境中，請將 VLAN 介面本身指定為 internal 介面：用戶端流量正是從該介面進入的。
:::

## 技術細節 {#technical-details}

### 服務埠與通告 {#service-ports-and-announcements}

服務在內部介面的 UDP 埠 5351 上監聽用戶端請求；在服務啟用期間，該埠會以動態 `natpmp` 條目的形式顯示在 `/ip/service` 中。用戶端自行選擇其請求的源埠。

當路由器的外部地址發生變化時，路由器會按照 RFC 6886 的描述，從每個內部介面向 `224.0.0.1` 的 UDP 埠 5350 組播免費的外部地址通告。需要接收這些通告的用戶端應在 UDP 埠 5350 上監聽。

### 對映生命週期 {#mapping-lifetime}

根據 RFC 6886：用戶端請求對映時會指定以秒為單位的生命週期（推薦值為兩小時），閘道器可以授予更短的生命週期，用戶端會在對映到期前一半的時間點進行續期。生命週期已過期的對映會被自動刪除，而傳送生命週期為 0 的請求會立即刪除該用戶端的對映。

關於所有屬性，請參閱 CLI 參考中的 [`/ip/nat-pmp`](../cli-reference/ip/nat-pmp/index.md) 和 [`/ip/nat-pmp/interfaces`](../cli-reference/ip/nat-pmp/interfaces.md)。
