---
sidebar_key: "cli-reference/interface/pppoe-client/scan"
sidebar_position: 2
title: "scan"
sidebar_label: 'scan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/pppoe-client/scan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pppoe-client/scan {#interfacepppoe-clientscan}
**型別：** 命令

PPPoE Scanner 允許掃描二層廣播域中的所有活動 PPPoE 伺服器。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">用於掃描 PPPoE 伺服器的介面。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="service" typ="string">伺服器上配置的服務名稱。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">檢測到的伺服器的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="ac-name" typ="string">Access Concentrator 的名稱。</ArgTableRow>
</ArgTable>
