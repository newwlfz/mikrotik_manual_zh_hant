---
title: "無線 VLAN Trunk"
description: "本頁說明如何使用 bridge VLAN filtering 在 MikroTik RouterOS 上設定 Wireless VLAN Trunking，讓特定 VLAN 可透過無線 PtP 連線選擇性轉送，同時封鎖其他 VLAN。內容涵蓋 bridge 設定、VLAN 表設定、介面存取控制，以及硬體卸載的 VLAN 處理。"
tags:
  - 'bridge-vlan-filtering'
  - 'vlan'
  - 'wireless'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/wireless-vlan-trunk
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

常見的工作是只透過 Wireless Point-to-Point（PtP）鏈路轉送特定一組 VLAN。這可以使用 bridge VLAN filtering 完成，且應取代任何其他方法（包括橋接 VLAN 介面）。假設我們需要透過 Wireless 鏈路轉送 2 個不同的 VLAN，並捨棄所有其他 VLAN ID。VLAN 10 將作為 Internet 流量，而 VLAN 99 將作為管理流量。以下是網路拓撲：

![Wireless VLAN Trunk](/img/663b80723f6ff040.webp)

## 設定 {#configuration}

先在 **AP** 與 **ST** 上建立新的 bridge，並將 **ether1** 與 **wlan1** 埠加入其中：

```ros
/interface/bridge
add name=bridge protocol-mode=none
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=wlan1
```

:::info
如有需要，可以啟用 RSTP，但一般來說，PtP 鏈路不需要 RSTP，因為不應該有任何可能發生迴圈的路徑。
:::

基於安全性考量，你應該啟用 ingress-filtering，因為你預期只會有 tagged 流量。接著可以設定 bridge 過濾所有 untagged 流量。在 **AP** 與 **ST** 上執行下列操作：

```ros
/interface/bridge/port
set [find where interface=ether1 or interface=wlan1] frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

設定 bridge VLAN 表。由於 VLAN99 將作為管理流量，因此需要允許這個 VLAN ID 存取 bridge 介面，否則當你嘗試存取設備時，流量就會被捨棄。VLAN10 不需要存取 bridge，因為它只打算轉送到另一端。若要達成此功能，請在 **AP** 與 **ST** 的 bridge VLAN 表中加入這些項目：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,wlan1 vlan-ids=10
add bridge=bridge tagged=ether1,wlan1,bridge vlan-ids=99
```

:::info Interface Access Control
你可以依介面限制設備的管理存取。若想防止從特定介面（例如 `wlan1`）存取，只要從對應的 bridge VLAN 項目中移除該介面即可。
:::

:::warning Handling Wireless & HW-Offloaded VLANs
對於同時支援硬體卸載 VLAN filtering 與 wireless 的設備（例如 RB4011、LtAP），請特別小心。若未明確允許該 VLAN 存取 CPU，從 HW-offloaded 埠流向 wireless 介面的封包可能會被捨棄。

若要允許特定 VLAN 存取 CPU：

* **加入 bridge 介面**作為該 VLAN 的成員（請參閱 VLAN99 範例）。
* **或者，在受影響的 bridge 埠上停用 HW offloading**。
:::

所有設備（**R1**、**R2**、**AP** 與 **ST**）都需要建立 VLAN 介面，才能透過特定 VLAN ID 存取設備。針對 **AP** 與 **ST**，在 bridge 介面上建立 VLAN 介面，並指派 IP 位址：

```ros
/interface/vlan
add interface=bridge name=MGMT vlan-id=99
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

針對 **R1** 與 **R2**，執行相同動作，但用來建立 VLAN 介面的介面可能會依你的設定而有所不同：

```ros
/interface/vlan
add interface=ether1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

:::info
若要允許轉送更多 VLAN，只要在 bridge VLAN 表中指定更多 VLAN ID 即可。你可以指定以逗號分隔的多個 VLAN，甚至指定 VLAN 範圍。
:::

### 設定 **AP** 上的無線鏈路 {#setup-the-wireless-link-on-ap}

```ros
/interface/wireless/security-profiles
add authentication-types=wpa2-psk mode=dynamic-keys name=wlan_sec wpa2-pre-shared-key=use_a_long_password_here
/interface/wireless
set wlan1 band=5ghz-a/n/ac channel-width=20/40/80mhz-Ceee disabled=no mode=bridge scan-list=5180 security-profile=wlan_sec ssid=ptp_test
```

### 設定 **ST** 上的無線鏈路 {#setup-the-wireless-link-on-st}

```ros
/interface/wireless/security-profiles
add authentication-types=wpa2-psk mode=dynamic-keys name=wlan_sec wpa2-pre-shared-key=use_a_long_password_here
/interface/wireless
set wlan1 band=5ghz-a/n/ac channel-width=20/40/80mhz-Ceee disabled=no mode=station-bridge scan-list=5180 security-profile=wlan_sec ssid=ptp_test
```

:::info
不同類型的設定有不同的需求。PtP 鏈路通常會使用 NV2 無線協定。你可以在 [NV2 Manual](/docs/wireless/abgn/nv2) 頁面閱讀更多關於 NV2 的資訊。
:::

當鏈路設定完成後，你可以在 **AP** 與 **ST** 上啟用 bridge VLAN filtering：

```ros
/interface/bridge
set bridge vlan-filtering=yes
```

:::danger
啟用 VLAN filtering 前，請再次確認 bridge VLAN 表。bridge VLAN 表設定錯誤可能導致無法存取設備，並可能需要重設設定。
:::
