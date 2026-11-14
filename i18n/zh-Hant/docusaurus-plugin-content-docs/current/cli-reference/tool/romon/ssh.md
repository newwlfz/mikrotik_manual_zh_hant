---
sidebar_key: "cli-reference/tool/romon/ssh"
sidebar_position: 4
title: "ssh"
sidebar_label: 'ssh'
source: https://manual.mikrotik.com/docs/cli-reference/tool/romon/ssh
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon/ssh {#toolromonssh}
**系統能力：** security
**型別：** 命令

透過 [RoMON](../../../management-tools/romon.md) 覆蓋網路與路由器建立 SSH 會話，無需任何 IP 連通性。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="macAddr">要連線的路由器的 RoMON ID（MAC 地址）</ArgTableRow>
<ArgTableRow arg="command" typ="string">要在遠端路由器上執行的命令，而不是互動式會話</ArgTableRow>
<ArgTableRow arg="user" typ="string">要在遠端路由器上登入的使用者賬戶</ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">將 `command` 的輸出儲存到本地路由器上的檔案中</ArgTableRow>
</ArgTable>
