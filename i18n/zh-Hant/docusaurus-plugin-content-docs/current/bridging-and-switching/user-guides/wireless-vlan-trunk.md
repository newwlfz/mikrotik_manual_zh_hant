---
sidebar_key: "bridging-and-switching/user-guides/wireless-vlan-trunk"
sidebar_position: 8
title: "無線 VLAN 中繼"
sidebar_label: "無線 VLAN 中繼"
description: "本頁說明如何在 MikroTik RouterOS 上使用 bridge VLAN filtering 配置 Wireless VLAN Trunking，從而允許在無線 PtP 鏈路上選擇性地轉發特定 VLAN，同時阻止其他 VLAN。內容涵蓋 bridge 設定、VLAN 表配置、介面訪問控制以及硬體解除安裝的 VLAN 處理。"
tags:
  - 'bridge-vlan-filtering'
  - 'vlan'
  - 'wireless'
source: https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/wireless-vlan-trunk
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

一項非常常見的任務是透過無線點對點（PtP）鏈路僅轉發特定的一組 VLAN。這可以透過 bridge VLAN filtering 實現，並且應當使用它，而不要使用任何其他方法（包括橋接 VLAN 介面）。假設我們需要透過無線鏈路轉發 2 個不同的 VLAN，其他所有 VLAN ID 都應被丟棄。VLAN 10 將用於我們的網際網路流量，而 VLAN 99 將用於我們的管理流量。下面是網路拓撲：

![Wireless VLAN Trunk](/img/663b80723f6ff040.webp)

## 配置 {#configuration}

首先在 **AP** 和 **ST** 上建立一個新的 bridge，並向其中新增 **ether1** 和 **wlan1** 埠：

```ros
/interface/bridge
add name=bridge protocol-mode=none
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=wlan1
```

:::info
如有需要，你可以啟用 RSTP，但通常 PtP 鏈路並不需要 RSTP，因為不應存在任何可能形成環路的情況。
:::

出於安全考慮，你應當啟用 ingress-filtering，因為你只期望接收帶標籤的流量。然後你可以將 bridge 設定為過濾掉所有未打標籤的流量。在 **AP** 和 **ST** 上執行以下操作：

```ros
/interface/bridge/port
set [find where interface=ether1 or interface=wlan1] frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

設定 bridge VLAN 表。由於 VLAN99 將用於我們的管理流量，因此我們需要允許該 VLAN ID 訪問 bridge 介面，否則一旦你嘗試訪問裝置，流量就會被丟棄。VLAN10 不需要訪問 bridge，因為它只用於轉發到另一端。要實現這樣的功能，請在 **AP** 和 **ST** 上的 bridge VLAN 表中新增以下條目：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,wlan1 vlan-ids=10
add bridge=bridge tagged=ether1,wlan1,bridge vlan-ids=99
```

:::info 介面訪問控制
你可以按介面限制對裝置的管理訪問。如果你希望阻止從某個特定介面（例如 `wlan1`）進行訪問，只需從相應的 bridge VLAN 條目中移除該介面即可。
:::

:::warning 處理無線與硬體解除安裝 VLAN
對於同時支援硬體解除安裝 VLAN filtering 和無線功能的裝置（例如 RB4011、LtAP），需要謹慎操作。如果未顯式允許該 VLAN 的 CPU 訪問，從硬體解除安裝埠流向無線介面的封包可能會被丟棄。

要允許特定 VLAN 的 CPU 訪問：

* **將 bridge 介面**新增為該 VLAN 的成員（參見 VLAN99 示例）。
* **或者，在受影響的 bridge 埠上停用硬體解除安裝**。
:::

所有裝置（**R1**、**R2**、**AP** 和 **ST**）都需要建立一個 VLAN 介面，以便能夠透過特定的 VLAN ID 訪問裝置。對於 **AP** 和 **ST**，在 bridge 介面之上建立 VLAN 介面併為其分配 IP 地址：

```ros
/interface/vlan
add interface=bridge name=MGMT vlan-id=99
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

對於 **R1** 和 **R2**，做同樣的操作，但需要在其上建立 VLAN 介面的介面可能會因你的具體設定而不同：

```ros
/interface/vlan
add interface=ether1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

:::info
要允許轉發更多 VLAN，你只需在 bridge VLAN 表中指定更多 VLAN ID，可以用逗號分隔指定多個 VLAN，甚至可以使用 VLAN 範圍。
:::

### 在 **AP** 上配置無線鏈路 {#setup-the-wireless-link-on-ap}

```ros
/interface/wireless/security-profiles
add authentication-types=wpa2-psk mode=dynamic-keys name=wlan_sec wpa2-pre-shared-key=use_a_long_password_here
/interface/wireless
set wlan1 band=5ghz-a/n/ac channel-width=20/40/80mhz-Ceee disabled=no mode=bridge scan-list=5180 security-profile=wlan_sec ssid=ptp_test
```

### 在 **ST** 上配置無線鏈路 {#setup-the-wireless-link-on-st}

```ros
/interface/wireless/security-profiles
add authentication-types=wpa2-psk mode=dynamic-keys name=wlan_sec wpa2-pre-shared-key=use_a_long_password_here
/interface/wireless
set wlan1 band=5ghz-a/n/ac channel-width=20/40/80mhz-Ceee disabled=no mode=station-bridge scan-list=5180 security-profile=wlan_sec ssid=ptp_test
```

:::info
每種型別的設定都有不同的要求。對於 PtP 鏈路，通常使用 NV2 無線協定。你可以在  [NV2 手冊](../../wireless/abgn/nv2.md)  頁面閱讀有關 NV2 的更多資訊。
:::

鏈路建立完成後，你可以在 **AP** 和 **ST** 上啟用 bridge VLAN filtering：

```ros
/interface/bridge
set bridge vlan-filtering=yes
```

:::danger
在啟用 VLAN filtering 之前，請仔細檢查 bridge VLAN 表。bridge VLAN 表配置錯誤可能導致裝置無法訪問，並且可能需要重設配置。
:::
