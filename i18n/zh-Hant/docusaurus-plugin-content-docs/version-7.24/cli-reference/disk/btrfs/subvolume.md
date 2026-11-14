---
sidebar_key: "cli-reference/disk/btrfs/subvolume"
sidebar_position: 2
title: "subvolume"
sidebar_label: "subvolume"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/disk/btrfs/subvolume
captured_at: '2026-11-01T21:26:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/subvolume {#diskbtrfssubvolume}
**條件：** !smips
**系統能力：** storage
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="S" typ="snapshot">snapshot</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">read-only</ArgTableRow>
<ArgTableRow arg="D" typ="dead">dead</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">mounted</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="fs" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="mount" typ="bool"></ArgTableRow>
<ArgTableRow arg="mountpoint" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="top-level" typ="enum"></ArgTableRow>
<ArgTableRow arg="fullname" typ="string"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="received-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="creation-time" typ="date"></ArgTableRow>
<ArgTableRow arg="subvolume-id" typ="num"></ArgTableRow>
<ArgTableRow arg="generation" typ="num"></ArgTableRow>
<ArgTableRow arg="dead" typ="bool"></ArgTableRow>
<ArgTableRow arg="snapshot" typ="bool"></ArgTableRow>
<ArgTableRow arg="send-trans-id" typ="num"></ArgTableRow>
<ArgTableRow arg="send-time" typ="date"></ArgTableRow>
<ArgTableRow arg="recv-trans-id" typ="num"></ArgTableRow>
<ArgTableRow arg="recv-time" typ="date"></ArgTableRow>
<ArgTableRow arg="snapshots" typ="multi { array-id, snapshot: enum
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string"></ArgTableRow>
</ArgTable>
