---
sidebar_key: "storage/btrfs/raid"
sidebar_position: 2
title: "Btrfs RAID"
sidebar_label: "Btrfs RAID"
description: "本頁提供在 RouterOS 中設定 Btrfs RAID 陣列的分步說明，涵蓋磁碟準備、格式化、新增裝置、資料均衡、擴充套件陣列、更換成員以及確保 RAID 配置檔案一致。"
tags:
  - 'btrfs'
  - 'storage'
  - 'raid'
source: https://manual.mikrotik.com/docs/storage/btrfs/raid
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](../index.md) 軟體包。
:::

Btrfs 檔案系統可以跨多個磁碟，並針對每種資料型別（`data`、`meta`、`system`）使用不同的*儲存配置檔案*。將單磁碟檔案系統轉換為 RAID1 或 RAID10 需要兩個步驟：先用 [`add-device`](../../cli-reference/disk/btrfs/filesystem/add-device.md) 新增磁碟，再用 [`balance-start`](../../cli-reference/disk/btrfs/filesystem/balance-start.md) 轉換配置檔案——整個過程無需解除安裝，也不會丟失資料。

## 雙磁碟 Btrfs-RAID（RAID1） {#two-disk-btrfs-raid-raid1}

如果你想僅用兩塊磁碟建立可靠的資料儲存方案（例如 NAS），可以按照以下步驟成功建立 Btrfs 的 RAID1 陣列：

1. 查詢要用於設定 Btrfs-RAID 的磁碟名稱。  

   ```routeros
   /disk/print
   ```

   :::warning
   在本示例中，使用的磁碟將被稱為 `<disk-name-1>` 和 `<disk-name-2>`，請務必將這些佔位符替換為實際的磁碟名稱！
   :::
2. 將你的其中一個磁碟格式化為 Btrfs，本例中為 `<disk-name-1>`。新建立的 Btrfs 檔案系統會自動標記為 `<disk-name-1>-fs`。  

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

3. 可以使用以下命令檢視 Btrfs 磁碟的當前狀態。  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

   :::info
   如果磁碟上存在已有的 RAID，並且為了簡化而想刪除任何過時的配置，可以使用 `/disk/format <disk-name-x> file-system=wipe-quick` 擦除磁碟。當 `/disk/btrfs/filesystem/print` 下存在不需要的條目時，這很有用。
   :::
4. 為簡化起見，為 Btrfs 驅動器新增一個標籤。  

   ```routeros
   /disk/btrfs/filesystem/set [find where devs=<disk-name-1>] label=BtrfsRAID
   ```

5. 向現有 Btrfs 磁碟新增一塊磁碟。這隻會將磁碟新增到檔案系統——新磁碟暫時不會接收任何資料。  

   ```routeros
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-2>
   ```

6. 啟動 Btrfs balance 程式，將檔案系統轉換為 RAID1。balance 會將每個 chunk 按新配置檔案重寫到兩塊磁碟上：  

   ```routeros
   /disk/btrfs/filesystem/balance-start [find where label=BtrfsRAID] data-profile=raid1 metadata-profile=raid1 system-profile=raid1
   ```

   進度會在 `/disk/btrfs/filesystem/print detail` 的 `balance-status` 下報告；完成狀態為 `done`。可使用 [`balance-cancel`](../../cli-reference/disk/btrfs/filesystem/balance-cancel.md) 取消正在執行的 balance。
7. **重要：** 再次確認磁碟的所有 Btrfs 配置檔案一致。在本例中，需要確保 `spaces` 列中的 `data`、`meta` 和 `system` 配置檔案均為 `raid1`。  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

    :::danger
    例如，如果在輸出中看到 `data,single:1`，則需要再次執行 `/disk/btrfs/filesystem/balance-start` 命令。
    :::

   :::info
期望狀態是輸出與下面類似，其中 `data`、`system` 和 `meta set to raid1` 的 Btrfs profile 設定為 raid1：

   ```routeros
   > /disk/btrfs/filesystem/print
   ...
   data,raid1:1.07GB disk1:1.07GB disk2:1.07GB, used:0%                                                                                                       
   system,raid1:33.6MB disk1:33.6MB disk2:33.6MB, used:0%                                                                                                     
   meta,raid1:1.07GB disk1:1.07GB disk2:1.07GB, used:0%    
   ```
   :::

   :::tip
   使用 [BtrfsRAIDCheck](#creating-btrfs-raid-check) 指令碼可提醒你 Btrfs 配置檔案不一致的情況！
   :::
8. 為第二塊磁碟設定 `mount-filesystem=no`，以防止檔案重複顯示。  

   ```routeros
   /disk/set <disk-name-2> mount-filesystem=no
   ```

   :::info
   Btrfs 具有一項特性，允許你掛載 Btrfs-RAID 中的任意成員，並且仍能訪問整個 Btrfs-RAID 陣列。該特性的缺點是，如果同一個陣列被掛載了兩次，那麼你的檔案也會出現兩次。為避免這種情況，你可以簡單地停用自動掛載其中一個 Btrfs-RAID 成員。
   :::
9. 為簡化起見，你還可以更改掛載點的名稱。  

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsRAID
   ```

10. 你新建的 Btrfs-RAID 陣列現在可以透過 `/BtrfsRAID/` 資料夾訪問。

有了 Btrfs-RAID 這樣可靠的儲存方案後，可以考慮按照以下建議指南為你的 RouterOS 裝置新增實用功能：

- 執行你自己的 [Containers](../../containers/index.md)
- [DLNA 媒體伺服器](../dlna.md)
- [SMB server](../smb.md)
- [NFS server](../nfs.md)

:::warning
當常規 [RAID](../raid/index.md) 與 Btrfs 檔案系統一起使用時，你的 RAID 陣列將無法從 Bitrot 中自我修復，常規 RAID 只能檢測 Bitrot。建議儘可能使用 Btrfs-RAID（即本節所述的配置）。
:::

## 四磁碟 Btrfs-RAID（RAID10） {#four-disk-btrfs-raid-raid10}

如果你想使用 Btrfs 建立具有冗餘且高容量的 RAID10 陣列，請執行以下命令：

1. 查詢要用於設定 Btrfs-RAID 的磁碟名稱。  

```routeros
/disk/print
```

   :::warning
   在本示例中，使用的磁碟將被稱為 `<disk-name-1>,``<disk-name-2>, <disk-name-3> 和 <disk-name-4>`，請務必將這些佔位符替換為實際的磁碟名稱！
   :::

1. 將其中一塊磁碟格式化為 Btrfs，此處為 `<disk-name-1>`：  

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

2. 可以使用以下命令檢視 Btrfs 磁碟的當前狀態：  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

   :::info
   如果磁碟上存在已有的 RAID，並且為了簡化而想刪除任何過時的配置，可以使用 `/disk/format <disk-name-x> file-system=wipe-quick` 擦除磁碟。當 `/disk/btrfs/filesystem/print` 下存在不需要的條目時，這很有用。
   :::
3. 為簡化起見，為 Btrfs 驅動器新增一個標籤：  

   ```routeros
   /disk/btrfs/filesystem/set [find where devs=<disk-name-1>] label=BtrfsRAID
   ```

4. 向現有 Btrfs 磁碟新增其他磁碟：  

   ```routeros
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-2>
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-3>
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-4>
   ```

5. 啟動 Btrfs balance 程式，將檔案系統轉換為 RAID10：  

   ```routeros
   /disk/btrfs/filesystem/balance-start [find where label=BtrfsRAID] data-profile=raid10 metadata-profile=raid1c4 system-profile=raid1c4
   ```

   :::info
   `data-profile`、`metadata-profile` 和 `system-profile` 有許多可能的配置。對於 RAID10 陣列，建議 `system-profile` 和 `metadata-profile` 都使用 `raid1c3` 或 `raid1c4`。raid1c4 配置檔案會在不同磁碟上儲存 4 份資料副本。這使資料具有更高的冗餘性，但會佔用更多磁碟空間。
   :::

   :::danger
   不支援 Btrfs RAID5 和 RAID6。如果需要此類 RAID 配置，請使用[常規 RAID](../raid/index.md)。請注意，將[常規 RAID](../raid/index.md) 與 Btrfs 一起使用時，你將無法獲得 bit-rot 保護。
   :::

   :::warning
   對於大多數用例，請將 `metadata-profile` 設定為與 `system-profile` 相同的值。避免為這兩個配置檔案使用不同的值。
   :::
6. 為其他磁碟設定 `mount-filesystem=no`，以防止檔案重複顯示：  

   ```routeros
   /disk/set <disk-name-2> mount-filesystem=no
   /disk/set <disk-name-3> mount-filesystem=no
   /disk/set <disk-name-4> mount-filesystem=no
   ```

7. 為簡化起見，你還可以更改掛載點的名稱：  

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsRAID
   ```

8. 你新建的 Btrfs-RAID 陣列現在可以透過 `/BtrfsRAID/` 資料夾訪問。

## 替換 Btrfs RAID 陣列中的磁碟 {#replacing-a-disk-in-a-btrfs-raid-array}

如果磁碟發生故障，或者你需要替換現有 Btrfs RAID 陣列中的磁碟，請按以下步驟操作：

1. 確保確定需要替換的正確磁碟。使用 `/disk/print detail` 和 `/disk/blink` 確定正確的磁碟。我們假設故障磁碟為 `disk2`。
2. 彈出故障磁碟：  

   ```routeros
   /disk/eject disk2
   ```

3. 物理移除故障磁碟。
4. 列印 Btrfs RAID 陣列的當前狀態：  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

5. 在命令輸出中查詢缺失磁碟的 `DEV-ID`：  

   ```routeros
   [admin@MikroTik] /disk> /disk/btrfs/filesystem/print
   Flags: I - MISSING-DEVS
   Columns: LABEL, DEV-IDS, DEVS, DEFAULT-SUBVOLUME, SPACES, BALANCE-STATUS, UUID, WRITE-ERRORS, READ-ERRORS, FLUSH-ERRORS, CORRUPTION-ERRORS, GENERATION-ERRORS
   #   LABEL      DEV-IDS  DEVS     DEFAULT-SUBVOLUME  SPACES                                     BALANCE-STATUS  UUID                                  W  R  F  C  G
   0 I BtrfsRAID        1  disk1    <FS_ROOT>          disk1:480GB, used:0%                       done            9246dfaa-be9f-4e08-a560-53cb8e82023b  0  0  0  0  0
                        2  missing                     data,raid1:1.07GB disk1:1.07GB, used:0%                                                          0  0  0  0  0
                                                        data,single:1.07GB, used:0%                                                                                   
                                                        system,raid1:33.6MB disk1:33.6MB, used:0%                                                                     
                                                        meta,raid1:1.07GB disk1:1.07GB, used:0%                                                                       
                                                        global-reserve:3.41MB, used:0%                                                                                

   ```

   :::info
   在本示例中，缺失磁碟的 `DEV-ID` 為 "2"。
   :::
6. 插入一塊新磁碟。
7. 確定新磁碟的名稱：  

   ```routeros
   /disk/print
   ```

   :::info
   在本示例中，新磁碟的名稱為 `disk3`
   :::
8. 執行以下命令以替換 Btrfs RAID 陣列中的磁碟：  

   ```routeros
   /disk/btrfs/filesystem/replace-device device-to-remove-id=2 device-to-add=disk3 BtrfsRAID
   ```

   :::warning
   請確保將 `device-to-remove-id` 正確設定為你之前確定的 `DEV-ID`！
   :::

   :::info
   [`replace-device`](../../cli-reference/disk/btrfs/filesystem/replace-device.md) 適用於缺失（已彈出）或未掛載的裝置。如果源磁碟正常且仍處於掛載狀態，請先解除安裝它（`/disk/set <disk> mount-filesystem=no`），否則命令會失敗並提示 `could not unmount <disk>`。透過 `replace-status` 跟蹤它；使用 [`replace-cancel`](../../cli-reference/disk/btrfs/filesystem/replace-cancel.md) 停止它。
   :::
9. 檢查替換狀態，並確保 `REPLACE-STATUS` 標記為 `done`。  

   ```routeros
   > /disk/btrfs/filesystem/print
   Columns: LABEL, DEV-IDS, DEVS, DEFAULT-SUBVOLUME, SPACES, BALANCE-STATUS, REPLACE-STATUS, UUID, WRITE-ERRORS, READ-ERRORS, FLUSH-ERRORS, CORRUPTION-ERRORS, GENERATION-ERRORS
   # LABEL   DEV-IDS  DEVS   DEFAULT-SUBVOLUME  SPACES                                                 BALANCE-STATUS  REPLACE-STATUS  UUID                                  WRITE-ERRORS  READ-ERRORS  F  C  G
   0 BtrfsRAID     1  disk1  <FS_ROOT>          disk1:480GB, used:9%                                   done            done            9246dfaa-be9f-4e08-a560-53cb8e82023b             0            0  0  0  0
                   2  disk3                     disk3:480GB, used:9%                                                                                                                    0  0  0  0  0
                                                 data,raid1:40.8GB disk1:40.8GB disk3:40.8GB, used:72%                                                                                                          
                                                 system,raid1:101MB disk1:101MB disk3:101MB, used:0%                                                                                                            
                                                 meta,raid1:3.22GB disk1:3.22GB disk3:3.22GB, used:1%                                                                                                           
                                                 global-reserve:30.7MB, used:0%                                                 
   ```

   :::info
   確保你的 Btrfs RAID 陣列的 `data`、`system` 或 `meta` 的 Btrfs 配置檔案不存在不一致的情況。所需的配置檔案取決於你的具體設定。對於 RAID1 設定，你很可能希望這些配置檔案保持一致，但在 RAID10 設定中這些值可以不同。在任何 RAID 設定中，`data`、`system` 或 `meta` 都不應出現 `single` 配置檔案。
   :::

## 擴充套件 Btrfs-RAID {#expanding-btrfs-raid}

Btrfs 是一種線上檔案系統，可以透過向 RAID 新增額外成員來輕鬆擴充套件。

### 向 RAID 新增額外成員 {#adding-additional-members-to-the-raid}

新增磁碟會同時增加容量和冗餘。例如，你可以將[第一節](#two-disk-btrfs-raid-raid1)中的雙磁碟 RAID1 陣列擴充套件為四磁碟 RAID10 陣列。整個過程中資料保持線上：

1. 將新磁碟新增到檔案系統。[`add-device`](../../cli-reference/disk/btrfs/filesystem/add-device.md) 會按每塊磁碟的完整大小注冊，但暫不向其中移動任何資料：  

   ```routeros
   /disk/btrfs/filesystem/add-device [find where label=BtrfsRAID] device=<disk-name-3>
   /disk/btrfs/filesystem/add-device [find where label=BtrfsRAID] device=<disk-name-4>
   ```

   ```routeros
   > /disk/btrfs/filesystem/print
   ...
   disk1:1.02TB, used:0%
   disk2:1.02TB, used:0%
   disk3:1.02TB, used:0%
   disk4:1.02TB, used:0%
   data,raid1:3.22GB disk1:3.22GB disk2:3.22GB, used:0%
   system,raid1:33.6MB disk1:33.6MB disk2:33.6MB, used:0%
   meta,raid1:1.07GB disk1:1.07GB disk2:1.07GB, used:0%
   ```

   所有資料塊仍位於前兩塊磁碟上。
2. 將 profile 轉換為 RAID10。balance 會將每個資料塊重寫到新 profile，並將資料分散到全部四塊磁碟上：  

   ```routeros
   /disk/btrfs/filesystem/balance-start [find where label=BtrfsRAID] data-profile=raid10 metadata-profile=raid1c4 system-profile=raid1c4
   ```

3. **重要：** 檢查 `spaces` 輸出中是否有使用先前 profile 的殘留資料塊。profile 轉換可能會在舊 profile 中留下一個資料塊：  

   ```routeros
   > /disk/btrfs/filesystem/print
   ...
   data,raid10:6.44GB disk1:6.44GB disk2:6.44GB disk3:6.44GB disk4:6.44GB, used:0%
   data,raid1:1.07GB disk3:1.07GB disk4:1.07GB, used:0%
   system,raid1c4:33.6MB disk1:33.6MB disk2:33.6MB disk3:33.6MB disk4:33.6MB, used:0%
   meta,raid1c4:1.07GB disk1:1.07GB disk2:1.07GB disk3:1.07GB disk4:1.07GB, used:0%
   ```

   :::danger
如果你注意到，例如，在輸出中 `data,raid1:1.07GB` 與 `data,raid10:...` 一起出現，那麼請再次執行 `/disk/btrfs/filesystem/balance-start` 命令，直到每個 `data`、`system` 和 `meta` chunk 都具有目標 profile。在此之前，該陣列對這些 chunk 不具備 RAID10 冗餘。
   :::

   期望狀態是每種資料型別只有一個 profile：  

   ```routeros
   > /disk/btrfs/filesystem/print
   ...
   data,raid10:2.15GB disk1:2.15GB disk2:2.15GB disk3:2.15GB disk4:2.15GB, used:0%
   system,raid1c4:33.6MB disk1:33.6MB disk2:33.6MB disk3:33.6MB disk4:33.6MB, used:0%
   meta,raid1c4:1.07GB disk1:1.07GB disk2:1.07GB disk3:1.07GB disk4:1.07GB, used:0%
   ```

4. 為新新增的磁碟設定 `mount-filesystem=no`，以防止檔案重複顯示：  

   ```routeros
   /disk/set <disk-name-3> mount-filesystem=no
   /disk/set <disk-name-4> mount-filesystem=no
   ```

一旦均衡完成，新配置檔案下的可用容量就會增加：由四塊等容量磁碟組成的 RAID10 陣列可容納的資料量是之前兩塊磁碟 RAID1 陣列的兩倍。您的檔案在整個過程中始終可訪問。

## 建立 Btrfs-RAID 檢查 {#creating-btrfs-raid-check}

監控 Btrfs-RAID 陣列的健康狀況對你來說極其重要。其中一種方法是使用以下指令碼作為工作示例：

```routeros
/system/scheduler
add interval=1w30s name=BraidBalanceStartCall on-event=BraidBalanceStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=01:00:00
add interval=1w30s name=BraidScrubStartCall on-event=BraidScrubStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=02:00:00
add interval=2m name=BraidBalanceStatusCheckCall on-event=BraidBalanceStatus policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=2m name=BraidScrubStatusCheckCall on-event=BraidScrubStatus policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=30s name=BraidHealthCheckCall on-event=BraidHealthCheck policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=2m name=BraidReplaceStatusCheckCall on-event=BraidReplaceStatus policy=ftp,read,write,policy,test,sniff start-time=startup

/system/script
add dont-require-permissions=no name=BraidScrubStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsscrubstatuscheck;\
    \nif (\$btrfsscrubstatuscheck != \"started\") do={\
    \n  :set \$btrfsscrubstatuscheck (\$btrfsscrubstatuscheck \"started\");\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ /disk/btrfs/filesystem/scrub-start \$i;\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    /log/info message=\"INFO: Btrfs scrub process started on  \$temp\";\
    \n    :delay 3; \
    \n  }\
    \n}\
    \n"
add dont-require-permissions=no name=BraidBalanceStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsbalancestatuscheck;\
    \nif (\$btrfsbalancestatuscheck != \"started\") do={\
    \n:set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"started\");\
    \n:local percentage;\
    \n:set \$percentage (\$percentage 50);\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ /disk/btrfs/filesystem/balance-start data-usage=\$percentage \$i;\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    /log/info message=\"INFO: Btrfs balance process started on  \$temp\";\
    \n    :delay 3; \
    \n  }\
    \n}"
add dont-require-permissions=no name=BraidBalanceStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsbalancestatuscheck;\
    \nif (\$btrfsbalancestatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=balance-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    if ( \$barray != \"done\" and \$btrfsbalancestatuscheck = \"started\") do={\
    \n        /log/info message=\"INFO: Btrfs current balance status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsbalancestatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs balancing already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt) do={\
    \n      /log/info message=\"INFO: Btrfs array balance status on  \$temp is \$barray \";\
    \n      :set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}"
add dont-require-permissions=no name=BraidScrubStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsscrubstatuscheck;\
    \nif (\$btrfsscrubstatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=scrub-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    if ( \$barray != \"done\" and \$btrfsscrubstatuscheck = \"started\") do={\
    \n      /log/info message=\"INFO: Btrfs current scrub status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsscrubstatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs scrubbing already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt ) do={\
    \n      /log/info message=\"INFO: Btrfs array scrub status on  \$temp is \$barray \";\
    \n      :set \$btrfsscrubstatuscheck (\$btrfsscrubstatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}"
add dont-require-permissions=no name=BraidReplaceStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsreplacestatuscheck;\
    \nif (\$btrfsreplacestatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=replace-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    :local multipleprofiles [ /disk/btrfs/filesystem/get value-name=spaces \$i; ]\
    \n    if ( \$barray ~ \"working\" and \$btrfsreplacestatuscheck = \"started\") do={\
    \n      /log/info message=\"INFO: Btrfs current replace status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray ~ \"done\" and \$btrfsreplacestatuscheck = \"started\" and \$multipleprofiles~\"single\" ) do={\
    \n      /log/info message=\"INFO: Braid balance after replace-device  started on  \$temp\";\
    \n         if (\$btrfsbalancestatuscheck!=\"started\") do={\
    \n             /disk/btrfs/filesystem/balance-start \$temp;\
    \n             :set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"started\");\
    \n         }\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsreplacestatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs replace already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt ) do={\
    \n      /log/info message=\"INFO: Btrfs array replace status on  \$temp is \$barray \";\
    \n      :set \$btrfsreplacestatuscheck (\$btrfsreplacestatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}\
    \n:set \$btrfsreplacestatuscheck (\$btrfsreplacestatuscheck \"started\");"
add dont-require-permissions=no name=BraidHealthCheck owner=admin policy=ftp,read,write,policy,test,sniff source="foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n:local sysadmin; \
    \n\
    \n:set  \$sysadmin \"<servername@domain.tld>\";\
    \n\
    \n:local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n:local haserror [/disk/btrfs/filesystem/get value-name=about \$i; ]\
    \n:local hasmissing [ /disk/btrfs/filesystem/get value-name=devs \$i; ]\
    \n:local hasmultiprofile [ /disk/btrfs/filesystem/get value-name=spaces \$i; ]\
    \n:local replacestatus [ /disk/btrfs/filesystem/get value-name=replace-status \$i; ]\
    \n:local multiplediskarray [:len [/disk/btrfs/filesystem/find where label=\$temp and dev-ids~\"2\"];]\
    \n\
    \n  if ( \$hasmissing~\"missing\" and ([:len \$replacestatus]=0)) do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found missing array member on \$temp\";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found missing array member\") body=(\"Btrfs array where found missing array member on \" .\$temp . \"   \");\
    \n   :delay 19; \
    \n  }\
    \n\
    \n  if ( \$multiplediskarray > 0 and \$hasmultiprofile~\"single\") do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found multiprofile on \$temp array. To start balance process, run  /disk/btrfs/filesystem/balance-start \$temp command \";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found multiprofile on \" .\$temp. \" array.\") body=(\"Btrfs array where found with multiprofile status on \" .\$temp . \"To start balance process, run once\
    \_ /disk/btrfs/filesystem/balance-start \" .\$temp. \" command \");\
    \n   :delay 19; \
    \n  }  \
    \n\
    \n  if (([:len \$haserror]) > 0 ) do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found errors on \$temp\";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found errors\") body=(\"Btrfs array where found errors on \" .\$temp . \"   \");\
    \n    :delay 20; \
    \n  }\
    \n}\
    \n"
```

你還需要在 RouterOS 裝置上調整電子郵件伺服器設定：

```routeros
/tool/e-mail
set from=<raidcheck@domain.tld> port=587 server=smtp.domain.com tls=starttls
```

:::warning
請確保按照電子郵件伺服器上的所需設定調整電子郵件設定。記得調整上方指令碼中的電子郵件地址。

:::
