---
sidebar_key: "cli-reference/disk/btrfs/transfer"
sidebar_position: 3
title: "transfer"
sidebar_label: 'transfer'
source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/transfer
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/transfer {#diskbtrfstransfer}
**條件：** !smips
**系統能力：** storage
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (receive | send)" mandatory="1">
Btrfs 傳輸的方向：
- `receive` - 在 `file` 處接收 Btrfs 傳送流，例如兩臺 RouterOS 裝置之間快照備份的目標端。
- `send` - 透過 SSH 將檔案系統 `fs` 的子卷（快照）傳送到遠端 RouterOS 裝置。

傳輸使用 `/user/ssh-keys` 的 SSH 使用者金鑰認證。有關可用的傳送/接收示例，請參閱 [Btrfs 子卷和快照](../../../storage/btrfs/snapshots.md)。
</ArgTableRow>
<ArgTableRow arg="fs" typ="enum">傳輸所操作的 Btrfs 檔案系統的標籤，如 [`filesystem`](./filesystem/index.md) 中所示。</ArgTableRow>
<ArgTableRow arg="send-parent" typ="enum">作為增量 `send` 基礎的先前成功傳送的快照；僅傳輸自該快照以來的更改。</ArgTableRow>
<ArgTableRow arg="send-subvolumes" typ="multi { array-id, subvolume: enum
 }">要傳送的快照，用於 `send` 傳輸。快照名稱（不是路徑），如 [`subvolume`](./subvolume.md) 下所示。</ArgTableRow>
<ArgTableRow arg="file" typ="file">傳輸的目標（或源）路徑，例如儲存接收到的快照的掛載路徑 `BackupBtrfsDisk/Snapshots`。</ArgTableRow>
<ArgTableRow arg="ssh-address" typ="string">`send` 傳輸的遠端 RouterOS 裝置的地址。</ArgTableRow>
<ArgTableRow arg="ssh-receive-mount" typ="string">遠端裝置上接收快照的掛載路徑，例如 `BackupBtrfsDisk/Snapshots`。</ArgTableRow>
<ArgTableRow arg="ssh-port" typ="num">遠端裝置的 SSH 埠。預設值：22。</ArgTableRow>
<ArgTableRow arg="ssh-user" typ="string">在遠端裝置上進行身份驗證所用的 SSH 使用者；必須已在遠端裝置上為 `ssh-user` 匯入本地使用者的 SSH 金鑰。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bytes" typ="num">到目前為止已傳輸的位元組數。</ArgTableRow>
<ArgTableRow arg="status" typ="string">傳輸的狀態，例如 `done`，或錯誤訊息。</ArgTableRow>
</ArgTable>
