---
sidebar_key: "cli-reference/interface/ovpn-server/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ovpn-server/monitor
captured_at: '2026-11-01T21:22:54+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-server/monitor {#interfaceovpn-servermonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">當前連線狀態。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線執行時間。</ArgTableRow>
<ArgTableRow arg="user" typ="string">已認證使用者名稱。</ArgTableRow>
<ArgTableRow arg="caller-id" typ="string">已連線用戶端的 Caller ID。</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">使用的加密編碼。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">連線的當前 MTU。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">連線的本地 IP 地址。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">連線的遠端 IP 地址。</ArgTableRow>
</ArgTable>
