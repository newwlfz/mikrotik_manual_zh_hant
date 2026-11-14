---
sidebar_key: "system-information-and-utilities/neighbor-discovery"
sidebar_position: 8
title: "鄰居發現"
sidebar_label: "鄰居發現"
description: "鄰居發現協定可在二層域中使用 MNDP、CDP 或 LLDP 檢測裝置，並顯示已連線鄰居的 IP/MAC 地址和介面。配置選項包括協定選擇、發現間隔調整，以及用於共享 QoS 和 VLAN 的 LLDP TLV。"
tags:
  - 'neighbor-discovery'
  - 'lldp'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/neighbor-discovery
captured_at: '2026-11-04T11:22:07+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

鄰居發現協定允許你在二層廣播域中查詢相容 MNDP（MikroTik Neighbor Discovery Protocol）、CDP（Cisco Discovery Protocol）或 LLDP（Link Layer Discovery Protocol）的裝置。它們可用於繪製你的網路拓撲。

所有隻讀的鄰居引數均記錄在 [`/ip/neighbor`](../cli-reference/ip/neighbor/index.md) CLI 參考中。

透過 LLDP 發現的鄰居顯示在 [`/ip/neighbor/lldp`](../cli-reference/ip/neighbor/lldp.md) 中單獨的只讀選單裡。

與彙總來自所有發現協定（MNDP、CDP 和 LLDP）的鄰居的常規 `/ip/neighbor` 選單不同，`/ip/neighbor/lldp` 僅顯示透過 LLDP 發現的條目。

`lldpRemTable` SNMP 表僅報告透過 LLDP 發現的鄰居。僅由 CDP 或 MNDP 發現的條目不會出現在 SNMP LLDP-MIB 中。

## 在 WinBox 中檢視和配置發現 {#view-and-configure-discovery-in-winbox}

開啟 **IP > Neighbors** 檢視已發現的裝置以及發現它們時所經過的介面。選擇 **LLDP** 標籤頁可檢視僅限 LLDP 的條目。要配置發現，請在右側面板中選擇 **Discovery Settings**：

1. 在 **Interface** 中選擇介面列表。這對應於 `discover-interface-list`；請選擇一個包含應參與發現的介面的列表。
2. 勾選所需的 **Protocol** 複選框，並檢查 **Mode**，它控制發現是傳送、接收還是兩者兼有。選擇 **OK** 儲存設定。

![WinBox Discovery Settings dialog with interface list, protocol, and mode controls](/img/2c85b54d0d8cc634.webp)

截圖展示的是一個已有配置。請為你的網路選擇合適的介面列表，而不是照搬其中的選擇。

發現設定在 [`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings.md) 選單中配置。

你可以透過使用[介面列表](../cli-reference/interface/list/index.md)來更改某個介面是否參與鄰居發現。如果該介面包含在發現介面列表中，它將傳送有關係統的基本資訊，並處理在二層網路中廣播收到的發現數據包。將介面從介面列表中移除，將同時停用該介面上的鄰居發現，以及在該介面上發現本裝置本身的可能性。

鄰居發現作用於各個從介面。當主介面（例如 bonding 或 bridge）被包含在發現介面列表中時，其所有從介面都將自動參與鄰居發現。若只希望在某些從介面上啟用鄰居發現，請將特定的從介面加入列表，並確保主介面未被包含。

```ros
/interface/bonding
add name=bond1 slaves=ether5,ether6
/interface/list
add name=only-ether5
/interface/list/member
add interface=ether5 list=only-ether5
/ip/neighbor/discovery-settings
set discover-interface-list=only-ether5
```

現在鄰居列表會顯示主介面，以及實際接收到發現訊息的從介面：

```ros
[admin@R2] > ip neighbor print
 # INTERFACE ADDRESS                                           MAC-ADDRESS       IDENTITY   VERSION    BOARD         
 0 ether5    192.168.88.1                                      CC:2D:E0:11:22:33 R1         6.45.4 ... CCR1036-8G-2S+
    bond1    
```

### LLDP-MED 網路策略 VLAN 示例 {#lldp-med-network-policy-vlan-example}

此示例為串聯了一臺 PC 的 VoIP 電話配置交換器埠。電話透過 LLDP-MED Network Policy TLV 分配的帶標籤流量傳輸語音。PC 使用無標籤流量，由橋接埠的 PVID 分配到另一個 VLAN。

在此設定中：

- **ether1** 是上游 trunk 埠，以帶標籤方式承載所有 VLAN 至路由器。
- **ether2** 是電話埠。VoIP 電話直接連線，PC 透過電話連線。
  - 語音流量使用 **VLAN 100**（帶標籤），透過 `lldp-med-net-policy-vlan` 通告。
  - 來自 PC 的資料流量使用 **VLAN 200**（在電話埠上無標籤），由橋接埠的 `pvid` 分配。

建立橋接並新增埠：

```ros
/interface/bridge
add name=bridge1 frame-types=admit-only-vlan-tagged

/interface/bridge/port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=200
```

建立橋接 VLAN 表。trunk 埠以帶標籤方式承載兩個 VLAN。電話埠以帶標籤方式承載語音 VLAN。PC 的資料 VLAN 由橋接埠的 `pvid` 分配，它會動態新增無標籤成員關係——無需顯式指定 `untagged=ether2`：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2 vlan-ids=100
add bridge=bridge1 tagged=ether1 vlan-ids=200
```

啟用 LLDP-MED 並設定語音 VLAN。停用 CDP 以避免干擾 LLDP-MED：

```ros
/ip/neighbor/discovery-settings
set lldp-med=yes lldp-med-net-policy-vlan=100 protocol=lldp,mndp
```

在橋接上啟用 VLAN 過濾：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::note
LLDP-MED Network Policy TLV 僅在發現到支援 LLDP-MED 裝置的介面上傳送。它不會在未發現支援 MED 鄰居的介面上廣播。
:::

:::info
有關橋接 VLAN 配置的更多詳細資訊，請參閱[橋接 VLAN 過濾](../bridging-and-switching/index.md#bridge-vlan-filtering)。
:::

## LLDP {#lldp}

根據 RouterOS 配置，可以在 LLDP 訊息中傳送不同的型別-長度-值（TLV）。這包括：

- Chassis ID（MAC 地址）。
- Port ID（介面名稱）。
- Time To Live。
- System Name（系統標識）。
- System Description（平臺 - MikroTik，軟體版本 - RouterOS 版本，硬體名稱 - RouterBoard 名稱）。
- Management Address（埠上配置的所有 IP 地址）。
- System Capabilities（已啟用的系統能力，例如 bridge 或 router）。
- Port Description（如果傳送介面是 bridge 或 bond 的一部分，則為組合介面名稱，如 "bridge/ether1"，否則與 Port ID 相同的介面名稱）。
- IEEE 802.1 Port VLAN ID。
- IEEE 802.1 Port And Protocol VLAN ID。
- IEEE 802.1 VLAN Name。
- IEEE 802.3 MAC/PHY Configuration/Status。
- IEEE 802.3 Power Via MDI。
- IEEE 802.3 Maximum Frame Size。
- LLDP-MED Media Capabilities（MED 能力列表）。
- LLDP-MED Network Policy（為語音流量分配的 VLAN ID）。
- LLDP-MED Extended Power via MDI。
- End of LLDPDU。
