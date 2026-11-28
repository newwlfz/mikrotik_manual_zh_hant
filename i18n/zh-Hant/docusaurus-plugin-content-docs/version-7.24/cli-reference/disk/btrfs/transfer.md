---
title: "transfer"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/disk/btrfs/transfer
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## disk/btrfs/transfer 
**條件：** !smips
**Syscap：** storage
**類型：** 目錄

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (receive | send)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="fs" typ="enum"></ArgTableRow>
<ArgTableRow arg="send-parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="send-subvolumes" typ="multi { array-id, subvolume: enum
 }"></ArgTableRow>
<ArgTableRow arg="file" typ="file"></ArgTableRow>
<ArgTableRow arg="ssh-address" typ="string"></ArgTableRow>
<ArgTableRow arg="ssh-receive-mount" typ="string"></ArgTableRow>
<ArgTableRow arg="ssh-port" typ="num"></ArgTableRow>
<ArgTableRow arg="ssh-user" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
