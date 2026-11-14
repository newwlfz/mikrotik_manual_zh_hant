---
sidebar_key: "cli-reference/interface/ethernet/switch/rule/index"
sidebar_position: 1
title: "rule"
sidebar_label: 'rule'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/rule
captured_at: '2026-11-01T21:22:41+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/rule {#interfaceethernetswitchrule}
**系統能力：** rbswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum" mandatory="1">匹配該規則將應用的交換器組。</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: enum
 }" syscap="!crs_prestera">匹配規則將對入站流量生效的交換器介面。可選擇多個埠以及[硬體解除安裝 bonding](../../../../../bridging-and-switching/l3-hardware-offloading.md#l3hw-feature-support) 介面。請注意，不能選擇 `switch1-cpu` 埠。如果 `ports` 屬性留空，則規則將應用於所有交換器介面。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { address: macAddr
, [mask] /macAddr
 }">匹配源 MAC 地址和掩碼。</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="super { address: macAddr
, [mask] /macAddr
 }">匹配目標 MAC 地址和掩碼。</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }">匹配由協定名稱或編號指定的特定 MAC 協定（如果有 VLAN 標籤則跳過）。</ArgTableRow>
<ArgTableRow arg="vlan-header" typ="enum (not-present | present)">匹配 VLAN 頭，即 VLAN 頭是否存在。需要 `vlan-filtering=yes`。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">匹配 VLAN ID。需要 `vlan-filtering=yes`。</ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="num">匹配 VLAN 優先順序（優先順序程式碼點）。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { address: ipAddr
, [mask] /alt { bitmask: ipAddr
, netmask: num [ .. 32]
 }
 }">匹配源 IPv4 地址和掩碼。如果指定了 `mac-protocol=arp`，則匹配 ARP 封包中的源 IP。若未指定 `mac-protocol`，則僅匹配 IPv4 封包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { address: ipAddr
, [mask] /alt { bitmask: ipAddr
, netmask: num [ .. 32]
 }
 }">匹配目標 IPv4 地址和掩碼。如果指定了 `mac-protocol=arp`，則匹配 ARP 封包中的目標 IP。若未指定 `mac-protocol`，則僅匹配 IPv4 封包。</ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { protocol-name: enum ()
, protocol-number: num [ .. 255]
 }">匹配由協定名稱或編號指定的特定 IP 協定。僅在未指定 `mac-protocol` 時適用於 IPv4 封包。要匹配某些 IPv6 協定，請使用 `mac-protocol=ipv6` 設定。</ArgTableRow>
<ArgTableRow arg="src-port" typ="range">匹配源協定埠號（若未指定 `mac-protocol`，則適用於 IPv4 和 IPv6 封包）。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="range">匹配目標協定埠號或埠範圍（若未指定 mac-protocol，則適用於 IPv4 和 IPv6 封包）。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">匹配封包的 DSCP 欄位（僅適用於 IPv4 封包）。</ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { address: ip6Addr
, [mask] /alt { bitmask: ip6Addr
, netmask: num
 }
 }">匹配源 IPv6 地址和掩碼。</ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { address: ip6Addr
, [mask] /alt { bitmask: ip6Addr
, netmask: num
 }
 }">匹配目標 IPv6 地址和掩碼。</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num">匹配 IPv6 流量類別。</ArgTableRow>
<ArgTableRow arg="flow-label" typ="num">匹配 IPv6 流標籤。</ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool">克隆匹配的封包並將其傳送到 CPU。</ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool">將匹配封包的目標埠更改為交換器 CPU。</ArgTableRow>
<ArgTableRow arg="mirror" typ="bool" syscap="switch-mirror-prestera">克隆匹配的封包並將其傳送到 `mirror-target` 埠。</ArgTableRow>
<ArgTableRow arg="new-dst-ports" typ="multi { array-id, port: alt { port: enum
, bond: iface_enum
 }
 }">
按指定方式更改目標埠，允許指定多個埠，包括交換器 CPU 埠。
- 如果該設定留空（例如 `new-dst-ports=""`），則封包將被丟棄；
- 如果指定了埠或[硬體解除安裝 bonding](../../../../../bridging-and-switching/marvell-prestera-switch-chip-features.md#bonding) 介面，則封包將被重定向到該埠。僅支援單個埠或 bond 介面；
- 如果使用 `all` 引數，則允許封包透過並進入出站處理，而不會被丟棄；
- 如果不使用此引數，則封包將按原樣被接受。
</ArgTableRow>
<ArgTableRow arg="mirror-ports" typ="multi { array-id, port: enum
 }" syscap="switch-mv88e6xxx">選擇多個映象目標埠，僅在 **88E6393X** 交換器晶片上可用。ACL 規則中匹配的封包將被複制併發送到所選埠。</ArgTableRow>
<ArgTableRow arg="new-qos-profile" typ="enum" syscap="crs_prestera">要分配給匹配封包的 QoS 配置檔名稱。</ArgTableRow>
<ArgTableRow arg="keep-qos-fields" typ="bool" syscap="crs_prestera">應保留 QoS 欄位（PCP、DSCP）的原始值（`yes`），還是將其替換為所分配 QoS 配置檔案中的值（`no`）？僅在設定了 `new-qos-profile` 時才有意義。</ArgTableRow>
<ArgTableRow arg="new-vlan-id" typ="num">將 VLAN ID 更改為指定的值。需要 `vlan-filtering=yes`。</ArgTableRow>
<ArgTableRow arg="new-vlan-priority" typ="num">更改 VLAN 優先順序（優先順序程式碼點）。需要 `vlan-filtering=yes`。</ArgTableRow>
<ArgTableRow arg="new-vrf" typ="enum" syscap="crs_prestera">將入站流量分配到指定的 VRF。需要交換器晶片支援[硬體解除安裝 VRF](../../../../../bridging-and-switching/l3-hardware-offloading.md#l3hw-feature-support)。在不感知 VRF 的交換器（98DX3xxx 和 98DX2xxx 系列）上，將 `new-vrf` 設定為 `main` 以外的任何值都將被視為 `redirect-to-cpu=yes`。</ArgTableRow>
<ArgTableRow arg="rate" typ="num">為匹配的流量設定入站流量限制（位元每秒）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="packets" typ="num" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="internal-priority" typ="num"></ArgTableRow>
</ArgTable>
