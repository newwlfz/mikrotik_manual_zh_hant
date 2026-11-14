---
sidebar_key: "cli-reference/disk/btrfs/filesystem"
title: "filesystem"
sidebar_label: 'filesystem'
source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/filesystem
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/filesystem {#diskbtrfsfilesystem}
**條件：** !smips
**系統能力：** storage
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="missing-devs">檔案系統的一個或多個裝置缺失，因此檔案系統處於降級狀態。</ArgTableRow>
<ArgTableRow arg="b" typ="balancing">檔案系統正在執行 balance 操作。</ArgTableRow>
<ArgTableRow arg="r" typ="replacing">檔案系統正在執行裝置 replace 操作。</ArgTableRow>
<ArgTableRow arg="s" typ="scrubbing">檔案系統正在執行 scrub 操作。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="label" typ="string">Btrfs 檔案系統的標籤，用於在 btrfs 選單中定址該檔案系統，例如 `btrfsdisk`。</ArgTableRow>
<ArgTableRow arg="default-subvolume" typ="enum">在 `/file` 中作為檔案系統根資料夾呈現的子卷。`<FS_ROOT>`（預設）是 Btrfs 檔案系統本身的根。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="uuid" typ="string">Btrfs 檔案系統的 UUID。</ArgTableRow>
<ArgTableRow arg="total-devs" typ="num">檔案系統中的裝置數量。</ArgTableRow>
<ArgTableRow arg="dev-ids" typ="multi { array-id, devid: num
 }">檔案系統中裝置的數字裝置 ID；當裝置缺失時，[`replace-device`](./replace-device.md) 需要這些 ID。</ArgTableRow>
<ArgTableRow arg="devs" typ="multi { array-id, dev: enum
 }">檔案系統中裝置的磁碟槽位，例如 `nvme8,nvme9`。</ArgTableRow>
<ArgTableRow arg="spaces" typ="multi { array-id, space: string
 }">檔案系統的空間分配，按裝置和儲存配置檔案（`data`、`system`、`meta`、`global-reserve`）劃分，例如 `data,raid1:1.07GB nvme8:1.07GB nvme9:1.07GB, used:1%`。</ArgTableRow>
<ArgTableRow arg="balance-status" typ="string">balance 操作的狀態，例如 `done`，或錯誤訊息，例如 `BTRFS_IOC_BALANCE_V2 failed: ...`。</ArgTableRow>
<ArgTableRow arg="replace-status" typ="string">replace 或裝置移除操作的狀態，例如 `done`，或錯誤訊息，例如 `BTRFS_IOC_DEV_REPLACE failed: File exists` 或 `BTRFS_IOC_RM_DEV_V2 failed: Resource temporarily unavailable`。</ArgTableRow>
<ArgTableRow arg="scrub-status" typ="string">scrub 操作的狀態，例如 `done`。</ArgTableRow>
<ArgTableRow arg="write-errors" typ="multi { snapshot: num
 }">寫入錯誤計數器，檔案系統中每個裝置一個值。使用 [`reset-counters`](./reset-counters.md) 重設。</ArgTableRow>
<ArgTableRow arg="read-errors" typ="multi { snapshot: num
 }">讀取錯誤計數器，每個裝置一個值。</ArgTableRow>
<ArgTableRow arg="flush-errors" typ="multi { snapshot: num
 }">重新整理錯誤計數器，每個裝置一個值。</ArgTableRow>
<ArgTableRow arg="corruption-errors" typ="multi { snapshot: num
 }">資料損壞錯誤計數器，每個裝置一個值。</ArgTableRow>
<ArgTableRow arg="generation-errors" typ="multi { snapshot: num
 }">generation 不匹配錯誤計數器，每個裝置一個值。</ArgTableRow>
</ArgTable>
