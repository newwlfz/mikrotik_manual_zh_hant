---
sidebar_key: "system-information-and-utilities/files"
sidebar_position: 5
title: "檔案"
sidebar_label: "檔案"
description: "MikroTik RouterOS 中的 File 選單允許管理使用者空間檔案，包括建立/編輯/刪除檔案和目錄、檢視 .npk 檔案的軟體包詳細資訊，以及將關鍵檔案儲存在 ''flash'' 目錄中以便重啟後保留。它支援最大 60KB 的檔案大小，並提供有關 RAM 磁碟行為、回寫快取和壓縮檔案儲存的警告。"
tags:
  - 'file-management'
  - 'routeros-features'
  - 'storage'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/files
captured_at: '2026-11-04T11:33:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

File 選單顯示路由器上的所有使用者空間檔案。可以建立新檔案或目錄、編輯檔案內容、刪除檔案或目錄。如果上傳了 RouterOS ".npk" 軟體包，檔案選單還會顯示軟體包特定的資訊，例如架構、構建日期和時間等。

:::warning
可以獲取和編輯最大 60KB 的檔案內容。要訪問更大檔案的內容，請參閱 [獲取檔案內容](./files.md#get-or-read-file-contents) 一節。
:::

```ros
[admin@MikroTik] > /file/print detail 
 0 name=wireless-7.16.1-arm.npk type=package size=1924.1KiB last-modified=2024-11-25 13:14:28 package-name="wireless" package-version="7.16.1" package-build-time=2024-10-10 14:03:32 
   package-architecture="arm" 

 1 name=routeros-7.16.1-arm.npk type=package size=11.1MiB last-modified=2024-11-25 13:14:34 package-name="system" package-version="7.16.1" package-build-time=2024-10-10 14:03:32 
   package-architecture="arm" 

 2 name=flash type=disk last-modified=2024-11-25 13:12:10 

 3 name=flash/skins type=directory last-modified=2024-11-25 13:10:52 

 4 name=flash/skins/newskin.json type=.json file size=0 last-modified=2024-11-25 13:10:52 

 5 name=flash/filename type=file size=0 last-modified=2024-11-25 13:11:58 

 6 name=flash/directory_name type=directory last-modified=2024-11-25 13:12:10 

```

:::danger
如果裝置的檔案列表中存在名為 **"flash"** 的目錄，那麼你希望在系統重啟/斷電重啟後保留的檔案必須儲存在該目錄中，因為該目錄之外的任何內容都儲存在 RAM 磁碟中，並會在重啟後丟失。這不包括 .npk 升級檔案，因為升級過程會在系統丟棄 RAM 驅動器內容之前應用這些檔案。

**警告：** 對於具有 NAND 快閃記憶體的多核裝置（例如 CCR 系列路由器、RB4011iGS），RouterOS 使用回寫機制，會將檔案更改快取到 RAM 記憶體中，而不是立即寫入快閃記憶體介質。只有在絕對必要時，檔案更改才會儲存到快閃記憶體中。寫入操作最多可延遲 40 秒。這有助於減少 CPU 週期，從而獲得更好的效能。但是，當裝置突然斷電時，這可能會導致檔案為空或長度為零，因為檔案未完全儲存到快閃記憶體中。

**警告：** 請注意，在某些情況下，RouterOS 可能會壓縮檔案以佔用更少的磁碟空間。在這種情況下，你在 **File** 選單中仍會看到原始檔案大小。但是，在 **Resource** 選單中，你可能會注意到可用空間比預期更多。

這是正常現象，因為計算 free-hdd-space 值時會使用壓縮後的檔案大小。
:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **contents** (*string*; Default: ) | 檔案的實際內容 |
| **creation-time** (*time*) **警告：** 直到 RouterOS 7.16  | 檔案建立的時間  |
| **last-modified** (*time*) | 檔案建立或最後修改的時間。在 RouterOS 7.16 中引入，用於替代 **creation-time**。  |
| **name** (*string*) | 檔名 |
| **package-architecture** (*string*) | 軟體包所針對的架構。僅適用於 RouterOS ".npk" 檔案 |
| **package-built-time** (*string*) | 軟體包構建的時間。僅適用於 RouterOS ".npk" 檔案 |
| **package-name** (*string*) | 可安裝軟體包的名稱。僅適用於 RouterOS ".npk" 檔案 |
| **package-version** (*string*) | 可安裝軟體包的版本。僅適用於 RouterOS ".npk" 檔案 |
| **size** (*integer*) | 檔案大小，以位元組為單位 |
| **type** (*string*) | 檔案型別。對於資料夾，檔案型別為 *directory* |

## 檔案操作 {#file-operations}

### 建立新檔案或目錄 {#create-new-file-or-directory}

要建立新檔案或目錄：

```ros
[admin@MikroTik] > /file/add name=/flash/filename type=file           
[admin@MikroTik] > file add name=/flash/directory_name type=directory 
```

### 獲取或讀取檔案內容 {#get-or-read-file-contents}

使用 *get* 命令，只能從不超過 60KB 的檔案中獲取檔案內容。要訪問更大檔案的內容，請使用 *read* 命令。結果以陣列形式返回。

例如：

```routeros
[admin@MikroTik] > :put [/file/get text.txt contents]
123456

[admin@MikroTik] > /file/read file=text.txt offset=2 chunk-size=3    
  data: 345
```

#### 選單特定屬性 {#menu-specific-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **chunk-size** (*integer [1..32768]*; Default: ) | 將從檔案中讀取的塊大小 |
| **offset** (*integer;*Default:) | 指定開始讀取檔案的偏移量 |

### 對檔案使用 head 或 tail {#head-or-tail-a-file}

使用 head 和 tail 函式，可以輸出檔案內容的前 n 行或後 n 行。

例如：

```routeros
/file/head test.txt n=3 numbered 
 1: 1
 2: 2
 3: 3
```

#### 選單特定屬性 {#menu-specific-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **n** (*integer [1..1000]*; Default: ) | 要列印的行數。 |
| **numbered** | 命令中出現該選項時，會在每行前面新增行號。 |

### 複製檔案或目錄 {#copy-a-file-or-directory}

使用 copy 命令可以克隆檔案或目錄。

例如：

```routeros
/file/copy test1.txt name=dir1/test1copy.txt
/file/copy dir1 name=dir2
/file/print 
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME                TYPE       SIZE  LAST-MODIFIED      
0 dir1                directory        2026-03-17 09:52:08
1 dir2                directory        2026-03-17 09:52:14
2 test1.txt           .txt file     0  2026-03-17 09:51:43
3 dir1/test1copy.txt  .txt file     0  2026-03-17 09:52:08
4 dir2/test1copy.txt  .txt file     0  2026-03-17 09:52:14
```
