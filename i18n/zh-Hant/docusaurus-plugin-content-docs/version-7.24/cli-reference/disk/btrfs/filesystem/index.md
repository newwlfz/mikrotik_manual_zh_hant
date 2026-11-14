---
sidebar_key: "cli-reference/disk/btrfs/filesystem/index"
sidebar_position: 4
title: "filesystem"
sidebar_label: "filesystem"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/disk/btrfs/filesystem
captured_at: '2026-11-01T21:26:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/filesystem {#diskbtrfsfilesystem}
**條件：** !smips
**系統能力：** storage
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="missing-devs">missing-devs</ArgTableRow>
<ArgTableRow arg="b" typ="balancing">balancing</ArgTableRow>
<ArgTableRow arg="r" typ="replacing">replacing</ArgTableRow>
<ArgTableRow arg="s" typ="scrubbing">scrubbing</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="label" typ="string"></ArgTableRow>
<ArgTableRow arg="default-subvolume" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="total-devs" typ="num"></ArgTableRow>
<ArgTableRow arg="dev-ids" typ="multi { array-id, devid: num
 }"></ArgTableRow>
<ArgTableRow arg="devs" typ="multi { array-id, dev: enum
 }"></ArgTableRow>
<ArgTableRow arg="spaces" typ="multi { array-id, space: string
 }"></ArgTableRow>
<ArgTableRow arg="balance-status" typ="string"></ArgTableRow>
<ArgTableRow arg="replace-status" typ="string"></ArgTableRow>
<ArgTableRow arg="scrub-status" typ="string"></ArgTableRow>
<ArgTableRow arg="write-errors" typ="multi { snapshot: num
 }"></ArgTableRow>
<ArgTableRow arg="read-errors" typ="multi { snapshot: num
 }"></ArgTableRow>
<ArgTableRow arg="flush-errors" typ="multi { snapshot: num
 }"></ArgTableRow>
<ArgTableRow arg="corruption-errors" typ="multi { snapshot: num
 }"></ArgTableRow>
<ArgTableRow arg="generation-errors" typ="multi { snapshot: num
 }"></ArgTableRow>
</ArgTable>
