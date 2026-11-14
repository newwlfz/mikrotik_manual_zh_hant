---
sidebar_key: "cli-reference/disk/btrfs/subvolume"
sidebar_position: 2
title: "subvolume"
sidebar_label: 'subvolume'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/disk/btrfs/subvolume
captured_at: '2026-11-01T21:22:09+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/subvolume {#diskbtrfssubvolume}
**條件：** !smips
**系統能力：** storage
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">該條目是檔案系統的根子卷，顯示為 `<FS_ROOT>`；它會隨檔案系統自動建立。</ArgTableRow>
<ArgTableRow arg="S" typ="snapshot">該子卷是快照，使用 `parent` 引數建立。</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">該子卷為只讀。</ArgTableRow>
<ArgTableRow arg="D" typ="dead">該子卷處於 dead 狀態，例如正在被移除。</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">該子卷已掛載（`mount=yes`）到其 `mountpoint` 下。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="fs" typ="enum" mandatory="1">子卷所屬 Btrfs 檔案系統的標籤，如 [`filesystem`](./filesystem/index.md) 中所示。</ArgTableRow>
<ArgTableRow arg="parent" typ="enum">新子卷建立時所基於的子卷。使用 `parent` 時，新子卷會成為父卷的快照，並共享建立時的內容。參見 [Btrfs 子卷和快照](../../../storage/btrfs/snapshots.md)。</ArgTableRow>
<ArgTableRow arg="name" typ="string">子卷的名稱。類似路徑的名稱（例如 `Snapshots/backup-10`）會將子卷置於另一個子卷內；此時 `top-level` 會顯示包含它的子卷。</ArgTableRow>
<ArgTableRow arg="read-only" typ="bool">子卷是否為只讀（`r - READ-ONLY` 標誌）。預設：否。</ArgTableRow>
<ArgTableRow arg="mount" typ="bool">子卷是否掛載到其 `mountpoint` 下（`M - MOUNTED` 標誌）。預設：否。</ArgTableRow>
<ArgTableRow arg="mountpoint" typ="string">子卷掛載到的掛載點，相對於檔案系統掛載點。預設為子卷的名稱。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="top-level" typ="enum">子卷所在的頂層子卷，例如 `Snapshots`；當子卷直接位於檔案系統根目錄下時為 `<FS_ROOT>`。</ArgTableRow>
<ArgTableRow arg="fullname" typ="string">子卷在檔案系統中的完整路徑，例如 `Snapshots/backup-10`。</ArgTableRow>
<ArgTableRow arg="uuid" typ="string">子卷的 UUID。</ArgTableRow>
<ArgTableRow arg="received-uuid" typ="string">透過 Btrfs [`transfer`](./transfer.md) 接收子卷時，傳送端上該子卷的 UUID；對於本地建立的子卷為空。</ArgTableRow>
<ArgTableRow arg="creation-time" typ="date">子卷的建立日期和時間。</ArgTableRow>
<ArgTableRow arg="subvolume-id" typ="num">子卷的 Btrfs ID 編號。</ArgTableRow>
<ArgTableRow arg="generation" typ="num">子卷的 Btrfs 事務 generation。</ArgTableRow>
<ArgTableRow arg="dead" typ="bool">子卷是否處於 dead 狀態（`D - DEAD` 標誌）。</ArgTableRow>
<ArgTableRow arg="snapshot" typ="bool">子卷是否為快照（`S - SNAPSHOT` 標誌）。</ArgTableRow>
<ArgTableRow arg="send-trans-id" typ="num">子卷參與的最後一次 send 的 Btrfs 事務 ID。</ArgTableRow>
<ArgTableRow arg="send-time" typ="date">子卷最後一次透過 Btrfs transfer 傳送的時間。</ArgTableRow>
<ArgTableRow arg="recv-trans-id" typ="num">建立該子卷的 receive 的 Btrfs 事務 ID。</ArgTableRow>
<ArgTableRow arg="recv-time" typ="date">子卷透過 Btrfs transfer 接收的時間。</ArgTableRow>
<ArgTableRow arg="snapshots" typ="multi { array-id, snapshot: enum
 }">從該子卷建立的快照。</ArgTableRow>
<ArgTableRow arg="path" typ="string">透過 Btrfs [`transfer`](./transfer.md) 接收到的路徑（接收端的 `file=`）；對於本地建立的子卷為空。</ArgTableRow>
</ArgTable>
