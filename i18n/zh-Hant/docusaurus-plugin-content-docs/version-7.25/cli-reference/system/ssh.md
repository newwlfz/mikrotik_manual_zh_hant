---
sidebar_key: "cli-reference/system/ssh"
sidebar_position: 31
title: "ssh"
sidebar_label: 'ssh'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ssh
captured_at: '2026-11-01T21:25:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ssh {#systemssh}
**型別：** 命令

[SSH 用戶端](../../management-tools/ssh.md#ssh-client) 用於連線遠端主機。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ipv6-address: composite { ip6: ip6Addr
, interface: [ iface_enum]
 }
 }">遠端主機的 IPv4 或 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="command" typ="string">要執行的遠端命令。</ArgTableRow>
<ArgTableRow arg="user" typ="string">遠端主機的使用者名稱。預設為當前登入的使用者。</ArgTableRow>
<ArgTableRow arg="port" typ="num">SSH 伺服器監聽的 TCP 埠。預設：22。</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">連線時使用的源地址。支援 IPv4 和 IPv6。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">在哪個 VRF 中建立連線。僅在該路由表內匹配遠端主機。</ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">將輸出寫入檔案而不是終端。不接受密碼輸入，請使用金鑰認證。</ArgTableRow>
</ArgTable>
