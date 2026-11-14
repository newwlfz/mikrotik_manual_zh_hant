---
sidebar_key: "cli-reference/interface/ovpn-client/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-client/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-client/monitor {#interfaceovpn-clientmonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">當前連線狀態。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線正常執行時間。</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">使用的加密編碼。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">連線的當前 MTU。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">連線的本地 IP 地址。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">連線的遠端 IP 地址。</ArgTableRow>
</ArgTable>
