---
sidebar_key: "cli-reference/interface/ethernet/switch/rule/index"
sidebar_position: 22
title: "rule"
sidebar_label: 'rule'
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/rule
captured_at: '2026-11-01T21:27:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
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
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: enum
 }" syscap="!crs_prestera"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="super { address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-header" typ="enum (not-present | present)"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { address: ipAddr
, [mask] /alt { bitmask: ipAddr
, netmask: num [ .. 32]
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { address: ipAddr
, [mask] /alt { bitmask: ipAddr
, netmask: num [ .. 32]
 }
 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { protocol-name: enum ()
, protocol-number: num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="range"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="range"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { address: ip6Addr
, [mask] /alt { bitmask: ip6Addr
, netmask: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { address: ip6Addr
, [mask] /alt { bitmask: ip6Addr
, netmask: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="flow-label" typ="num"></ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirror" typ="bool" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="new-dst-ports" typ="multi { array-id, port: alt { port: enum
, bond: iface_enum
 }
 }">將 new-dst-ports 設定為空字串，以在硬體層面丟棄封包</ArgTableRow>
<ArgTableRow arg="mirror-ports" typ="multi { array-id, port: enum
 }" syscap="switch-mv88e6xxx"></ArgTableRow>
<ArgTableRow arg="new-qos-profile" typ="enum" syscap="crs_prestera">為匹配的封包分配 QoS 配置檔案</ArgTableRow>
<ArgTableRow arg="keep-qos-fields" typ="bool" syscap="crs_prestera">保留原始 QoS 欄位（PCP、DSCP），還是從 QoS 配置檔案中替換它們？</ArgTableRow>
<ArgTableRow arg="new-vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="new-vlan-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="new-vrf" typ="enum" syscap="crs_prestera">為匹配的封包分配 VRF</ArgTableRow>
<ArgTableRow arg="rate" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="internal-priority" typ="num"></ArgTableRow>
</ArgTable>
