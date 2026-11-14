---
sidebar_key: "cli-reference/app/network"
sidebar_position: 2
title: "network"
sidebar_label: 'network'
source: https://manual.mikrotik.com/docs/cli-reference/app/network
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## app/network {#appnetwork}
**系統能力：** app
**軟體包：** container
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="e" typ="external">該網路是現有橋或 LAN 橋。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">網路配置無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">網路名稱。`internal` 是應用建立的網路；外部網路使用橋名稱和 `lan` 別名。</ArgTableRow>
<ArgTableRow arg="allow-outgoing-access" typ="bool">網路上的應用是否可以訪問網路外部的目標。預設值：yes。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="network" typ="ipAddr">應用建立的內部網路的網路地址。</ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr">路由器在該網路上的 IP 地址。</ArgTableRow>
<ArgTableRow arg="status" typ="string">當前網路狀態，例如 `ready`。</ArgTableRow>
<ArgTableRow arg="used-ips" typ="multi { array-id, array-id, ip-and-name: composite { ip: ipAddr
, name: string
 }
 }">該網路上已分配的 IP 地址以及使用每個地址的應用或主機。</ArgTableRow>
<ArgTableRow arg="bridge-interface" typ="iface_enum { none }">承載網路的網橋介面。</ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { cmd: string
 }">RouterOS 用於建立網路的命令。</ArgTableRow>
</ArgTable>
