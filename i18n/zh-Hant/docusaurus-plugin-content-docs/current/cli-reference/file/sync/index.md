---
sidebar_key: "cli-reference/file/sync"
title: "sync"
sidebar_label: 'sync'
source: https://manual.mikrotik.com/docs/cli-reference/file/sync
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## file/sync {#filesync}
**軟體包：** rose-storage
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該同步條目已被停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">該條目無效，例如它引用了不存在或不可用的路徑。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該條目是自動建立的。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="remote-address" typ="multi { array-id, address: string
 }" mandatory="1">要與之同步的遠端 RouterOS 裝置的 IP 地址。遠端裝置必須已啟用 rsync 守護程式（[`rsync-daemon`](../rsync-daemon.md)）。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (upload | download)" mandatory="1">
同步方向：
- `upload` - 將 `local-path` 檔案或資料夾傳送到遠端裝置。
- `download` - 從遠端裝置獲取 `remote-path` 到本路由器。
</ArgTableRow>
<ArgTableRow arg="local-path" typ="file">本路由器上的檔案或資料夾路徑；在 `mode=upload` 時為源，在 `mode=download` 時為目標。</ArgTableRow>
<ArgTableRow arg="remote-path" typ="string">遠端裝置上的檔案或資料夾路徑。</ArgTableRow>
<ArgTableRow arg="user" typ="string">用於在遠端裝置上進行身份驗證的 RouterOS 使用者。</ArgTableRow>
<ArgTableRow arg="password" typ="string">遠端裝置上該使用者的密碼。設定後，傳輸會自動透過建立的 IPsec 進行。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">同步狀態，例如 `in sync`、`making control connection to <ip>` 或 `initializing transfer`。</ArgTableRow>
</ArgTable>
