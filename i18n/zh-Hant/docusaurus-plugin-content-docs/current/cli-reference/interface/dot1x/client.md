---
sidebar_key: "cli-reference/interface/dot1x/client"
sidebar_position: 1
title: "client"
sidebar_label: 'client'
source: https://manual.mikrotik.com/docs/cli-reference/interface/dot1x/client
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/dot1x/client {#interfacedot1xclient}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { method: enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2) { eap-tls:13, eap-ttls:21, eap-peap:25, eap-mschapv2:26 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="identity" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="anon-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
