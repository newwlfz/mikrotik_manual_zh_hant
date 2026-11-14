---
sidebar_key: "cli-reference/interface/ethernet/switch/host"
sidebar_position: 6
title: "host"
sidebar_label: 'host'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/host
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/host {#interfaceethernetswitchhost}
**系統能力：** rbswitch and oldswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum" mandatory="1">要將 MAC 地址分配到的交換器的名稱。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">主機的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: alt { port: enum
, trunk: iface_enum
 }
 }" mandatory="1">介面的名稱，一個靜態 MAC 地址可以對映到多個埠，包括交換器 CPU 埠。</ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool">是否將具有匹配 MAC 目的地址（對於 CRS3xx 系列交換器為匹配目的地址或源地址）的幀的副本傳送到交換器 CPU 埠。</ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool">是否將具有匹配 MAC 目的地址（對於 CRS3xx 系列交換器為匹配目的地址或源地址）的幀重定向到交換器 CPU 埠。</ArgTableRow>
<ArgTableRow arg="drop" typ="bool">是否丟棄在某個埠上收到的、具有匹配 MAC 源地址（對於 CRS3xx 系列交換器為匹配目的地址或源地址）的幀。</ArgTableRow>
<ArgTableRow arg="mirror" typ="bool">是否將具有匹配 MAC 目的地址（對於 CRS3xx 系列交換器為匹配目的地址或源地址）的幀的副本傳送到 `mirror-target` 埠。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">靜態新增的 MAC 地址條目的 VLAN ID。</ArgTableRow>
<ArgTableRow arg="share-vlan-learned" typ="bool">靜態主機 MAC 地址查詢是與共享 VLAN 學習（SVL）還是與獨立 VLAN 學習（IVL）配合使用。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>
