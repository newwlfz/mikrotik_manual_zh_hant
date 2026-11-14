---
sidebar_key: "cli-reference/system/ssh"
sidebar_position: 31
title: "ssh"
sidebar_label: "ssh"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/ssh
captured_at: '2026-11-01T21:30:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ssh {#systemssh}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ipv6-address: composite { ip6: ip6Addr
, interface: [ iface_enum]
 }
 }"></ArgTableRow>
<ArgTableRow arg="command" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">此輸出方法不接受密碼輸入，請使用金鑰認證</ArgTableRow>
</ArgTable>
