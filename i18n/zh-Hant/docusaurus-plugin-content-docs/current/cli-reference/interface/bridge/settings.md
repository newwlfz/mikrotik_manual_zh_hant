---
sidebar_key: "cli-reference/interface/bridge/settings"
sidebar_position: 9
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/settings {#interfacebridgesettings}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="use-ip-firewall" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-ip-firewall-for-vlan" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-ip-firewall-for-pppoe" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bridge-fast-path-active" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge-fast-path-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-fast-path-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-fast-forward-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-fast-forward-bytes" typ="num"></ArgTableRow>
</ArgTable>
