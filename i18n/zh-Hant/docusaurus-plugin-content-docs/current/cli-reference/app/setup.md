---
sidebar_key: "cli-reference/app/setup"
sidebar_position: 6
title: "setup"
sidebar_label: 'setup'
source: https://manual.mikrotik.com/docs/cli-reference/app/setup
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## app/setup {#appsetup}
**系統能力：** app
**軟體包：** container
**型別：** 命令

啟動互動式設定嚮導。它會選擇應用磁碟、LAN 網橋，以及用於應用 URL 和埠轉發的路由器 IP 地址。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="disk" typ="enum (none)">用於安裝應用程式的選定儲存磁碟</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">用於容器網路的選定 LAN 網橋介面</ArgTableRow>
<ArgTableRow arg="router-ip-alt" typ="alt { router-ip-enum: enum
, router-ip: ipAddr
 }">用於手動覆蓋 RouterOS 裝置的 IP 地址</ArgTableRow>
</ArgTable>
