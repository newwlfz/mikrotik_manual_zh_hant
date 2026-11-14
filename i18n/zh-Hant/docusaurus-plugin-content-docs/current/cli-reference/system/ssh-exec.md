---
sidebar_key: "cli-reference/system/ssh-exec"
sidebar_position: 31
title: "ssh-exec"
sidebar_label: 'ssh-exec'
source: https://manual.mikrotik.com/docs/cli-reference/system/ssh-exec
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ssh-exec {#systemssh-exec}
**型別：** 命令

[`ssh-exec`](../../management-tools/ssh.md#run-remote-commands-from-scripts) 命令是一種非互動式 SSH 命令，允許你透過指令碼和 scheduler 在裝置上遠端執行命令。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ipv6-address: composite { ip6: ip6Addr
, interface: [ iface_enum]
 }
 }">遠端主機的 IPv4 或 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="command" typ="string">要執行的遠端命令。</ArgTableRow>
<ArgTableRow arg="user" typ="string">遠端主機的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">遠端主機的密碼。應使用 SSH PKI 身份驗證，而不是純文字密碼。</ArgTableRow>
<ArgTableRow arg="port" typ="num">SSH 伺服器監聽的 TCP 埠。預設：22。</ArgTableRow>
<ArgTableRow arg="known-hosts-ignore" typ="bool">跳過主機金鑰驗證</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">連線時使用的源地址。支援 IPv4 和 IPv6。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">用於執行該命令的 VRF；連線會在該路由表內建立。</ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">將輸出寫入檔案，而不是 'output' 變數。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="exit-code" typ="num">遠端命令 shell 報告的退出碼；命令執行時為 `0`。連線或身份驗證失敗會中止 `ssh-exec` 本身，而不是返回。</ArgTableRow>
<ArgTableRow arg="output" typ="string">返回遠端執行命令的輸出。</ArgTableRow>
</ArgTable>
