---
sidebar_key: "system-information-and-utilities/files"
sidebar_position: 5
title: "檔案"
sidebar_label: "檔案"
description: "File 選單用於管理路由器上的使用者檔案：建立、編輯、複製和刪除檔案及目錄，讀取檔案內容，以及檢視已上傳 RouterOS 軟體包的詳細資訊。"
tags:
  - 'file-management'
  - 'routeros-features'
  - 'storage'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/files
captured_at: '2026-11-04T11:21:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

`/file` 選單顯示路由器儲存上的所有使用者檔案，例如上傳的軟體包、備份、指令碼和匯出檔案。你可以建立檔案和目錄、編輯檔案內容，以及複製或刪除條目。對於上傳的 RouterOS `.npk` 軟體包，該選單還會顯示特定於軟體包的資訊，例如架構、版本和構建時間：

```ros
[admin@MikroTik] > /file/print detail
0  name=my-dir type=directory last-modified=2026-09-25 12:13:27
 
1  name=routeros-7.24.2-arm64.npk type=package size=13.3MiB
   last-modified=2026-09-25 12:13:01 package-name="system"
   package-version="7.24.2" package-build-time=2026-09-03 09:57:14
   package-architecture="arm64"
 
2  name=skins type=directory last-modified=1970-01-01 03:00:05
 
3  name=my-dir/test.txt type=.txt file size=5 last-modified=2026-09-25 12:13:27
   contents=hello
```

透過 [檔案共享](../network-management/cloud/file-share.md)（Back To Home（遠端回家））共享的檔案和目錄會帶有 `S`（共享）標誌，並顯示包含共享連結的 `url` 屬性。路由器之間的檔案同步在 `/file/sync` 選單中配置，請參閱 [Rsync](../storage/rsync.md)。

## 在 WinBox 中管理檔案 {#manage-files-in-winbox}

在左側選單中開啟 **Files**。**File** 標籤頁會列出檔名、型別、大小和修改時間：

1. 選擇 **New**，然後選擇 **Text File** 或 **Directory**，以建立條目。
2. 在右側面板中選擇 **Upload...**，將檔案從計算機複製到路由器。要將路由器上的檔案儲存到計算機，請選擇其所在行，然後選擇 **Download...**。**Remove** 會從路由器中刪除所選條目。
3. 上傳大檔案之前，請檢查視窗底部的儲存使用情況。

![WinBox Files list with file actions and storage usage](/img/f8c5e1dff7ba33c6.webp)

上傳檔案會將其儲存在路由器上；它不會自動匯入配置指令碼或恢復備份。如果你打算應用該檔案，請遵循相關的配置流程。

## 儲存詳細資訊 {#storage-details}

如果裝置的檔案列表中存在名為 **flash** 的目錄，請將所有需要在重啟或斷電後保留的檔案儲存在其中：`flash` 之外的所有內容都儲存在 RAM 磁碟中，並會在重啟時丟失。這不包括 `.npk` 升級檔案，升級過程會在 RAM 磁碟內容被丟棄之前應用這些檔案。

在帶有 NAND 快閃記憶體的多核裝置上（例如 CCR 系列路由器和 RB4011），RouterOS 使用回寫快取：檔案更改會緩衝在 RAM 中，稍後寫入快閃記憶體介質，這最多可能延遲 40 秒。這會降低 CPU 使用率和快閃記憶體磨損。但是，如果在該時間視窗內突然斷電，**可能會留下空檔案或零長度檔案**，因為更改尚未寫入快閃記憶體。

在某些裝置上，RouterOS 會壓縮儲存的檔案以佔用更少的磁碟空間。`/file` 顯示原始檔案大小，但 `/system/resource` 中的 [`free-hdd-space`](../cli-reference/system/resource/index.md#free-hdd-space) 是根據壓縮後的大小計算的，因此它可能顯示比預期更多的可用空間。

## 檔案操作 {#file-operations}

### 建立檔案或目錄 {#create-a-file-or-directory}

使用 [`/file/add`](../cli-reference/file/index.md) 命令，並指定 `type=file` 或 `type=directory`：

```ros
[admin@MikroTik] > /file/add name=my-file.txt type=file
[admin@MikroTik] > /file/add name=my-dir type=directory
```

### 讀取檔案內容 {#read-file-contents}

`get` 僅對大小略低於 60 KiB 的檔案返回 `contents` 屬性；對於更大的檔案，它不返回任何內容。要讀取更大的檔案，請使用 [`/file/read`](../cli-reference/file/read.md) 命令，該命令會以字串形式返回檔案的一個塊：

```ros
[admin@MikroTik] > :put [/file/get text.txt contents]
123456

[admin@MikroTik] > /file/read file=text.txt offset=2 chunk-size=3
  data: 345
```

### 對檔案使用 head 或 tail {#head-or-tail-a-file}

使用 [`/file/head`](../cli-reference/file/head.md) 和 [`/file/tail`](../cli-reference/file/tail.md) 列印檔案的前 `n` 行或後 `n` 行（預設 10 行）：

```ros
[admin@MikroTik] > /file/head test.txt n=3 numbered
 1: 1
 2: 2
 3: 3
```

### 複製檔案或目錄 {#copy-a-file-or-directory}

使用 [`/file/copy`](../cli-reference/file/copy.md) 命令。目錄會連同其所有內容一起遞迴複製：

```ros
[admin@MikroTik] > /file/add name=test1.txt type=file
[admin@MikroTik] > /file/add name=dir1 type=directory
[admin@MikroTik] > /file/copy test1.txt name=dir1/test1copy.txt
[admin@MikroTik] > /file/copy dir1 name=dir2
[admin@MikroTik] > /file/print
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME                TYPE       SIZE  LAST-MODIFIED
0 dir2                directory        2026-09-25 12:12:20
1 dir1                directory        2026-09-25 12:12:20
2 test1.txt           .txt file     0  2026-09-25 12:12:20
3 skins               directory        1970-01-01 03:00:05
4 dir1/test1copy.txt  .txt file     0  2026-09-25 12:12:20
5 dir2/test1copy.txt  .txt file     0  2026-09-25 12:12:20
```

所有引數都記錄在 [`/file`](../cli-reference/file/index.md) CLI 參考中。
