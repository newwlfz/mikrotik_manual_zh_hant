---
sidebar_key: "system-information-and-utilities/neighbor-discovery"
sidebar_position: 8
title: "鄰居發現"
sidebar_label: "鄰居發現"
description: "鄰居發現使用 MNDP、CDP 和 LLDP 在二層網路上發現 MikroTik 及第三方裝置：鄰居列表、各協定設定、介面參與、LLDP TLV 以及 LLDP-MED 語音 VLAN 示例。"
tags:
  - 'neighbor-discovery'
  - 'lldp'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/neighbor-discovery
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

鄰居發現協定允許你在二層廣播域中查詢相容 MNDP（MikroTik Neighbor Discovery Protocol）、CDP（Cisco Discovery Protocol）或 LLDP（Link Layer Discovery Protocol）的裝置。它們可用於繪製你的網路拓撲。

`/ip/neighbor` 列出所有發現的鄰居，無論它們是由哪個協定通告的（`discovered-by` 值顯示是哪個協定），並帶有通用摘要欄位。只讀的 [`/ip/neighbor/lldp`](../cli-reference/ip/neighbor/lldp.md) 選單僅顯示由 LLDP 發現的條目以及 LLDP 專用欄位，這些欄位按 LLDP 標準命名。`/ip/neighbor` 的只讀引數在其 [`/ip/neighbor`](../cli-reference/ip/neighbor/index.md) CLI 參考中描述：

```ros
[admin@MikroTik] > /ip/neighbor/print where identity="Router-A"
Columns: INTERFACE, ADDRESS4, ADDRESS6, MAC-ADDRESS
#  INTERFACE  ADDRESS4       ADDRESS6                   MAC-ADDRESS
0  ether2     192.168.88.24  fe80::de2c:6eff:fee7:106a  DC:2C:6E:E7:10:6B
   bridge
```

只要裝置持續通告自身，鄰居列表就保留條目。裝置每 30 秒通告一次其存在（預設的 `discover-interval`）；當通告停止時，條目在超時老化後被刪除。`lldpRemTable` SNMP 表包含與 `/ip/neighbor/lldp` 相同的 LLDP 發現條目；僅由 CDP 或 MNDP 發現的條目不屬於 SNMP LLDP-MIB。

## 在 WinBox 中檢視和配置發現 {#view-and-configure-discovery-in-winbox}

開啟 **IP > Neighbors** 檢視已發現的裝置以及發現它們時所經過的介面。選擇 **LLDP** 標籤頁可檢視僅限 LLDP 的條目。要配置發現，請在右側面板中選擇 **Discovery Settings**：

1. 在 **Interface** 中選擇介面列表。這對應於 `discover-interface-list`；請選擇一個包含應參與發現的介面的列表。
2. 勾選所需的 **Protocol** 複選框，並檢查 **Mode**，它控制發現是傳送、接收還是兩者兼有。選擇 **OK** 儲存設定。

![WinBox Discovery Settings dialog with interface list, protocol, and mode controls](/img/2c85b54d0d8cc634.webp)

截圖展示的是一個已有配置。請為你的網路選擇合適的介面列表，而不是照搬其中的選擇。

## 選擇參與發現的介面 {#choose-which-interfaces-participate}

發現設定在 [`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings.md) 選單中配置：

```ros
/ip/neighbor/discovery-settings/print
```

發現功能執行在 `discover-interface-list` [介面列表](../cli-reference/interface/list/index.md)（預設為 `static`）中的介面上。列表中的介面既通告路由器（傳送發現報文），也接受在其上監聽到的鄰居。從列表中移除某個介面會在兩個方向上停用該介面的發現功能：路由器不再在該介面上通告自身，並停止接受在其上監聽到的鄰居。將列表設定為 `none` 會完全關閉發現功能：通告停止（在其他裝置上，本路由器的條目會老化消失——其 `age` 值持續增長，直到條目消失），並且本路由器自身的鄰居列表會清空。若只想停止通告但保留檢視鄰居（例如在 WAN 上），請設定 `mode=rx-only`。

鄰居發現可在各個從介面上獨立工作。當主介面（bonding 或 bridge）被包含在發現介面列表中時，其所有從介面會自動參與。鄰居列表同時顯示主介面和通告到達的從介面（參見上例中的 `ether2` + `bridge` 條目）。若只允許在某些從介面上進行鄰居發現，請僅在列表中包含這些從介面，並確保不包含主介面：

```ros
/interface/bonding add name=bond1 slaves=ether5,ether6
/interface/list add name=only-ether5
/interface/list/member add interface=ether5 list=only-ether5
/ip/neighbor/discovery-settings set discover-interface-list=only-ether5
```

## LLDP-MED 網路策略 VLAN 示例 {#lldp-med-network-policy-vlan-example}

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

有關橋接 VLAN 配置的更多詳細資訊，請參閱 [橋接 VLAN 過濾](../bridging-and-switching/index.md#bridge-vlan-filtering)。

## LLDP {#lldp}

根據 RouterOS 配置，可以在 LLDP 訊息中傳送不同的型別-長度-值（TLV）。這包括：

- 機箱 ID（MAC 地址）。
- 埠 ID（介面名稱）。
- 生存時間。
- 系統名稱（system identity）。
- 系統描述（平臺 - MikroTik，軟體版本 - RouterOS 版本，硬體名稱 - RouterBoard 名稱）。
- 管理地址（埠上配置的所有 IP 地址）。
- 系統能力（已啟用的系統能力，例如 bridge 或 router）。
- 埠描述（如果傳送介面是 bridge 或 bond 的一部分，則為“bridge/ether1”這樣的組合介面名稱，否則為與埠 ID 相同的介面名稱）。
- IEEE 802.1 埠 VLAN ID。
- IEEE 802.1 埠和協定 VLAN ID。
- IEEE 802.1 VLAN 名稱。
- IEEE 802.3 MAC/PHY 配置/狀態。
- IEEE 802.3 透過 MDI 供電。
- IEEE 802.3 最大幀大小。
- LLDP-MED 媒體能力（MED 能力列表）。
- LLDP-MED 網路策略（為語音流量分配的 VLAN ID）。
- LLDP-MED 透過 MDI 擴充套件供電。
- LLDPDU 結束。

## 技術細節 {#technical-details}

- 裝置每隔 `discover-interval`（預設 30 秒）通告一次；在接收端，如果未及時收到通告，則刪除相應條目。CDP 和 LLDP 通告攜帶的 TTL 為 `(discover-interval * 4) + 1`。
- 通告內容和可選 TLV 由 [`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings.md) 引數控制，包括 PoE TLV（`lldp-poe-power`、`lldp-poe-in-power`）和 DCBX（`lldp-dcbx`）。
- `dying-gasp` 會在正常重啟、關機或升級之前傳送 TTL=0 的發現數據包，以便鄰居立即刪除相應條目。
- `add-dns-entries` 會根據 identity 為發現的鄰居建立動態 DNS 條目；請參閱 [DNS](../network-management/dns.md)。

有關所有引數和只讀值，請參閱 [`/ip/neighbor`](../cli-reference/ip/neighbor/index.md)、[`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings.md) 和 [`/ip/neighbor/lldp`](../cli-reference/ip/neighbor/lldp.md) CLI 參考頁面。
