---
sidebar_key: "cli-reference/disk/format"
sidebar_position: 6
title: "format"
sidebar_label: 'format'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/disk/format
captured_at: '2026-11-01T21:22:08+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/format {#diskformat}
**條件：** !smips
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file-system" typ="enum (fat32 | ext4 | btrfs | xfs | wipe | wipe-quick | exfat | discard | discard-secure)">
將磁碟格式化為何種檔案系統。
- `ext4` - 使用 ext4 格式化；大多數用例的預設值。
- `fat32` - 使用 FAT32 格式化，幾乎任何裝置都可讀取。
- `exfat` - 使用 exFAT 格式化，適用於儲存卡和 USB 驅動器上的大檔案。
- `btrfs` - 使用 Btrfs 格式化（資料校驗和、快照、RAID）；需要 [儲存](../../storage/index.md) 軟體包。
- `xfs` - 使用 XFS 格式化；需要 [儲存](../../storage/index.md) 軟體包。
- `discard` - 丟棄磁碟的所有塊（相當於 `blkdiscard`），不寫入檔案系統。
- `discard-secure` - 相同，但使用安全丟棄，同時擦除底層資料。
- `wipe` - 覆蓋磁碟上的所有資料，使其無法恢復。
- `wipe-quick` - 移除檔案系統而不覆蓋資料；速度快，但資料可透過工具恢復。
</ArgTableRow>
<ArgTableRow arg="label" typ="string">檔案系統標籤。預設值：`<slot>-fs`。</ArgTableRow>
<ArgTableRow arg="mbr-partition-table" typ="bool">在格式化過程中向磁碟寫入 MBR 分割區表。若不寫入，磁碟將沒有分割區表；之後使用 `add type=partition` 建立分割區，這些分割區儲存在 GUID 分割區表中。預設值：no。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="output" typ="string">格式化的進度：`mkfs` 命令列及其輸出、進度百分比或位元組計數器，以及最後的 `format done` 行。</ArgTableRow>
</ArgTable>
