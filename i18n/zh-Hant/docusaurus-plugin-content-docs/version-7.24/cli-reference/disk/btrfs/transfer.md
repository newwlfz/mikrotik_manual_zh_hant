---
sidebar_key: "cli-reference/disk/btrfs/transfer"
sidebar_position: 3
title: "transfer"
sidebar_label: "transfer"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/disk/btrfs/transfer
captured_at: '2026-11-01T21:26:44+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/transfer {#diskbtrfstransfer}
**條件：** !smips
**系統能力：** storage
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
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

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
