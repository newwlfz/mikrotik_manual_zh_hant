---
sidebar_key: "cli-reference/interface/ppp-client/firmware-upgrade"
sidebar_position: 2
title: "firmware-upgrade"
sidebar_label: 'firmware-upgrade'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ppp-client/firmware-upgrade
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ppp-client/firmware-upgrade {#interfaceppp-clientfirmware-upgrade}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="upgrade" typ="bool">執行升級或僅檢查</ArgTableRow>
<ArgTableRow arg="firmware-file" typ="file">升級映象的路徑或 URL</ArgTableRow>
<ArgTableRow arg="update-channel" typ="enum (stable | testing)">韌體更新通道</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="installed" typ="string"></ArgTableRow>
<ArgTableRow arg="latest" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="note" typ="string"></ArgTableRow>
</ArgTable>
