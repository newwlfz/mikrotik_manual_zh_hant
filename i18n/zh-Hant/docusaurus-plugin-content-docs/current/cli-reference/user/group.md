---
sidebar_key: "cli-reference/user/group"
sidebar_position: 4
title: "group"
sidebar_label: 'group'
source: https://manual.mikrotik.com/docs/cli-reference/user/group
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/group {#usergroup}
**型別：**目錄

使用者組定義授予組成員的許可權（策略）。內建組 `read`、`write` 和 `full` 無法刪除。完整指南請參閱 [使用者](../../authentication-authorization-accounting/user.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">組名稱。</ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, array-id, policy: super { !
, policy: enum
 }
 }">
授予組成員的許可權。在策略前加上 `!` 可撤銷該策略。`add` 會撤銷其未列出的所有策略，而未使用 `policy` 建立的新組會將所有策略取反（無許可權）。`set` 僅更改其列出的策略：對具有 `api` 的組執行 `set policy=read,rest-api` 會保留 `api`；`policy=!api` 會撤銷它。預設值：none.
- `local` - 在本地控制檯登入。
- `telnet` - 透過 Telnet 登入。
- `ssh` - 透過 SSH 登入。
- `ftp` - 透過 FTP 登入；允許讀取、寫入和刪除檔案（與 `read` 和 `write` 一起使用）。
- `reboot` - 重啟路由器。
- `read` - 對路由器配置的讀取許可權。
- `write` - 對配置的寫入許可權（使用者管理除外）；不包含 `read`。
- `policy` - 使用者管理許可權（與 `write` 一起使用）；還允許檢視其他使用者建立的指令碼變數（需要 `test`）以及設計 WebFig 皮膚（需要 `sensitive`）。
- `test` - 執行 ping、traceroute、bandwidth-test、wireless scan 和 snooper、fetch、email 及其他測試工具。
- `winbox` - 透過 WinBox 登入並使用 bandwidth-test 身份驗證。
- `password` - 使用 `/password` 更改使用者自己的密碼。
- `web` - 透過 WebFig 登入。
- `sniff` - 使用封包嗅探器、torch 和流量生成器。
- `sensitive` - 檢視和更改敏感資訊。
- `api` - 透過 API 訪問路由器。
- `romon` - 連線到 RoMON 伺服器。
- `rest-api` - 透過 REST API 訪問路由器。
</ArgTableRow>
<ArgTableRow arg="skin" typ="enum">應用於透過 WebFig 登入的組成員的 WebFig 皮膚。預設值：default。</ArgTableRow>
</ArgTable>
