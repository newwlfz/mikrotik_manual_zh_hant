---
sidebar_key: "storage/btrfs/maintenance"
sidebar_position: 1
title: "Btrfs 維護"
sidebar_label: "Btrfs 維護"
description: "本頁介紹 Btrfs 維護任務，包括定期 scrub 以檢測並糾正 RAID 陣列中的資料損壞、透過 balance 最佳化儲存空間使用，以及建立快照用於資料恢復。頁面提供了建議間隔、示例命令，以及有關儲存裝置健康狀況的警告。"
tags:
  - 'btrfs'
  - 'raid'
  - 'maintenance'
source: https://manual.mikrotik.com/docs/7.25/storage/btrfs/maintenance
captured_at: '2026-11-04T11:21:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

與其他功能豐富的檔案系統類似，Btrfs 需要定期維護。本頁介紹與 Btrfs 相關的日常任務。

## 定期 scrub {#periodic-scrubbing}

在 RAID 陣列中，你的資料儲存在多個磁碟上，或者多個磁碟包含如何重新組裝資料的資訊。沒有 RAID 時，磁碟在極少數情況下可能會損壞你資料中的幾個位元組，而你甚至可能不會注意到資料已損壞。使用 RAID 陣列時，當你讀取檔案，你的資料會與其他資料副本進行比較（或在組裝時校驗），並會提醒你資料已損壞。使用[常規 RAID](../raid/index.md) 時，例如在 RAID1 配置中，RAID 陣列無法判斷哪個檔案副本是正確的。它只會通知你檢測到了資料損壞。使用 Btrfs RAID，你不僅能檢測資料損壞，還能透過校驗和區分哪個檔案副本是正確的，並自動恢復它。

Scrub 是一個重新讀取整個 RAID 陣列的過程，在 Btrfs RAID 的情況下，會糾正任何資料損壞。雖然 Btrfs RAID 會在檔案讀取操作時糾正資料，例如當你想要從 RouterOS 裝置下載檔案時，但強烈**不**建議避免 scrub。在極少數情況下，例如在 RAID1 配置中，兩個磁碟都可能存在損壞的資料，而 Btrfs RAID 可能無法恢復資料。為避免此類情況並保護寶貴資料，請考慮定期執行 scrub。

:::warning

檢測到過多資料損壞通常表明儲存裝置正在故障。當你注意到許多資料損壞警告時，請考慮檢查儲存裝置。

:::

執行 scrub 的頻率間隔取決於每個使用場景。Scrub 是對儲存裝置的一項密集任務。它會重新讀取整個 RAID 陣列並執行額外檢查。在 scrub 期間，你可能會體驗到磁碟效能明顯下降，直到 scrub 完成。如果你擔心 scrub 期間的效能，請考慮降低 scrub 頻率。如果你更擔心資料完整性，請考慮提高 scrub 頻率。

- 摘要：用於檢測並糾正資料損壞
- 建議間隔：1 周
- [工作示例](./raid.md#creating-btrfs-raid-check)

示例命令：

```routeros
/disk/btrfs/filesystem/print
/disk/btrfs/filesystem/scrub-start 0
```

你也可以使用以下命令取消 scrub：

```routeros
/disk/btrfs/filesystem/scrub-cancel
```

## 定期 balance {#periodic-balance}

在 Btrfs 中，資料儲存在已分配的 chunk 中，這些 chunk 隨後允許以塊的形式儲存你的資料。隨著時間推移，由於各種資料活動，chunk 可能會部分填滿，並以次優方式分佈在許多 chunk 之間。平衡 Btrfs 檔案系統意味著重新排列這些 chunk 中的資料並恢復未分配空間。因此，你可以恢復丟失的可用空間以及 Btrfs 檔案系統的效能。這與其他檔案系統上的碎片整理操作有些類似。

平衡的一個重要引數是 `data-usage` 引數。這是一個過濾器，用於阻止平衡功能處理使用率高於某個百分比的 chunk。例如，`data-usage=50` 只會處理使用率為 50% 或更低的 chunk。你可以使用不同的值多次執行平衡命令，從而減少每次平衡操作所需的時間。平衡可能是一項密集任務，取決於你的可用空間以及自上次平衡操作以來資料的寫入方式，因此你可能會受益於使用不同的 `data-usage` 值分別執行平衡命令，以縮短因密集磁碟讀寫而導致效能下降的時間視窗。

如果你希望分別執行平衡命令，應使用 `data-usage` 值 25、50、75 和 90。不建議超過 90%。對大多數使用者而言，不需要分別執行平衡命令，每個間隔執行一次且 `data-usage` 為 50% 就足夠了。

- 摘要：用於恢復可用空間並提升效能。
- 建議間隔：每月兩次。
- 建議 `data-usage`：50。
- [工作示例](./raid.md#creating-btrfs-raid-check)。

示例命令：

```routeros
/disk/btrfs/filesystem/print
/disk/btrfs/filesystem/balance-start data-usage=50 0
```

你也可以使用以下命令取消 balance：

```routeros
/disk/btrfs/filesystem/balance-cancel
```

## 定期快照 {#periodic-snapshots}

快照可用於按設定間隔儲存檔案更改。當你有一個可靠的資料複製間隔時，快照最為有用，這樣你始終可以將資料恢復到先前狀態。下面你可以找到一個可直接使用的指令碼，用於建立定期快照：

```routeros
/system/scheduler
add interval=1d name=BraidSnapshotStartCall on-event=BraidSnapshotStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=23:15:00
add interval=1d name=BraidSnapshotCleanUpStartCall on-event=BraidSnapshotCleanUpStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=23:00:00
add interval=3m name=SystemBackupStartCall on-event=SystemBackupStart policy=ftp,read,write,policy,test,sniff start-time=startup

/system/script
add dont-require-permissions=no name=SystemBackupStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global systembackupstatuscheck;\
    \n:global systembackupdirectoryname; \
    \n:local sysadmin;\
    \n\
    \n:set \$sysadmin ( \$sysadmin \"servername@domain.tld\" );\
    \n:set \$systembackupdirectoryname (\$systembackupdirectoryname \"Braid17-20/@system-backup/\");\
    \n\
    \n if (\$systembackupstatuscheck != \"started\") do={\
    \n         :set \$systembackupstatuscheck (\$systembackupstatuscheck \"started\");\
    \n               :local datentime ([/system/clock/get date].\"-\".[/system/clock/get time]);\
    \n               :local servername ([/system/identity/get name]);\
    \n               /system/backup/save name=\"\$systembackupdirectoryname\$servername-\$datentime\";\
    \n\
    \n        :set \$systembackupstatuscheck (\$systembackupstatuscheck \"done\");\
    \n} else={\
    \n         /log/info message=\"ERROR: Cannot create  \$systembackupdirectoryname\$servername-\$datentime. Set manually :set systembackupstatuscheck (systembackupstatuscheck \\\"done\\\");\";\
    \n}\
    \n"
add dont-require-permissions=no name=BraidSnapshotStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfssnapshotstatuscheck;\
    \n:global snapshotdirectoryname; \
    \n:local maxusedspace;\
    \n:local sysadmin;\
    \n\
    \n:set \$maxusedspace ( \$maxusedspace 80 );\
    \n:set \$sysadmin ( \$sysadmin \"<servername@domain.tld>\" );\
    \n:set \$snapshotdirectoryname (\$snapshotdirectoryname \"@snapshots\");\
    \n\
    \n if (\$btrfssnapshotstatuscheck != \"started\") do={\
    \n         :set \$btrfssnapshotstatuscheck (\$btrfssnapshotstatuscheck \"started\");\
    \n         foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n           :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n           :local valueofusedspace [/disk/print count-only where use>=\$maxusedspace and fs-label=\$temp];\
    \n           if ( \$valueofusedspace=0) do={\
    \n            foreach j in=[/disk/btrfs/subvolume/find  where fs=\$temp and top-level!=\$snapshotdirectoryname and fullname!=\$snapshotdirectoryname ] do={\
    \n               :local parentvar [ /disk/btrfs/subvolume/get value-name=name \$j; ];\
    \n               :local datentime ([/system/clock/get date].\"-\".[/system/clock/get time]);\
    \n                  /disk/btrfs/subvolume/add read-only=yes fs=\"\$temp\" parent=\"\$parentvar\" name=\"\$snapshotdirectoryname/\$temp-\$parentvar-\$datentime\";\
    \n                   /log/info message=\"INFO: Braid snapshot created for  \$temp subvolume \$parentvar snapshotname  \$snapshotdirectoryname/\$temp-\$parentvar-\$datentime\";\
    \n                :delay 1;\
    \n            }\
    \n          } else={\
    \n                   /log/info message=\"ERROR: Snapshot was not created for safety reason.  Braid array \$temp used space exceeded \$maxusedspace %. Add more disks or cleanup storage.\"; \
    \n                   /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" ERROR: Braid snapshot was not created \") body=(\"Snapshot was not created for safety reason.  Braid array \" .\$temp. \" used space exceeded \" .\$max\
    usedspace. \" % Add more disks or cleanup storage. \" );\
    \n          }\
    \n\
    \n          :delay 3; \
    \n         }\
    \n        :set \$btrfssnapshotstatuscheck (\$btrfssnapshotstatuscheck \"done\");\
    \n}\
    \n"
add dont-require-permissions=no name=BraidSnapshotCleanUpStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfssnapshotcleanupstatuscheck;\
    \n:global snapshotdirectoryname; \
    \n:local maxsnapshotstokeep;\
    \n:local maxdaysoldsnapshotstokeep;\
    \n:local sysadmin;\
    \n\
    \n:set \$maxsnapshotstokeep ( \$maxsnapshotstokeep 10);\
    \n:set \$maxdaysoldsnapshotstokeep (\$maxdaysoldsnapshotstokeep \"10d\");\
    \n:set \$sysadmin ( \$sysadmin \"<servername@domain.tld>\" );\
    \n:set \$snapshotdirectoryname (\$snapshotdirectoryname \"@snapshots\");\
    \n\
    \n if (\$btrfssnapshotcleanupstatuscheck != \"started\") do={\
    \n         :set \$btrfssnapshotcleanupstatuscheck (\$btrfssnapshotcleanupstatuscheck \"started\");\
    \n         foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n           :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n           :local currenttimestamp; :set  \$currenttimestamp ( \$currenttimestamp [/system/clock/get date ] );\
    \n          :set  \$currenttimestamp ( \$currenttimestamp  -\$maxdaysoldsnapshotstokeep);\
    \n            foreach j in=[/disk/btrfs/subvolume/find  where fs=\$temp and top-level=\$snapshotdirectoryname ] do={\
    \n               :local parentname [ /disk/btrfs/subvolume/get value-name=name \$j;];\
    \n               :local parentsubvol [ /disk/btrfs/subvolume/get value-name=parent \$j; ];\
    \n               :local creationtimeofsnapshot; :set \$creationtimeofsnapshot (\$creationtimeofsnapshot [/disk/btrfs/subvolume/get value-name=creation-time \$j; ]);\
    \n               :local countparentsnapshots;  :set \$countparentsnapshots (\$countparentsnapshots [/disk/btrfs/subvolume/print count-only  where fs=\$temp and top-level=\$snapshotdirectoryname and parent=\$parentsubvol]);\
    \n               if ([:len \$parentsubvol]=0) do={\
    \n                   :local parentfullname [ /disk/btrfs/subvolume/get value-name=fullname \$j;];\
    \n                    /log/info message=\"INFO: SnapshotCleanup found snapshot of completely deleted subvolume. Location of snapshot \$temp/\$snapshotdirectoryname/\$parentname. This can only be removed manually.\";\
    \n               } else={\
    \n                if (\$currenttimestamp>=\$creationtimeofsnapshot or  \$countparentsnapshots>\$maxsnapshotstokeep ) do={\
    \n                   /log/info message=\"INFO: Braid snapshot  \$snapshotdirectoryname/\$parentname deleted. SnapshotCleanUp keeps  \$maxsnapshotstokeep snapshots or snapshots not older than \$maxdaysoldsnapshotstokeep days.\";\
    \n                  /disk/btrfs/subvolume/remove \$parentname;\
    \n                :delay 1;\
    \n               }\
    \n             }\
    \n            }\
    \n          :delay 3; \
    \n         }\
    \n        :set \$btrfssnapshotcleanupstatuscheck (\$btrfssnapshotcleanupstatuscheck \"done\");\
    \n}\
    \n"
```

## 可用空間 {#free-space}

在 Btrfs 中，由於資料以 chunk 方式儲存，確保有足夠的可用空間非常重要，這不僅是為了讓常規維護任務正常執行，也是為了檔案系統效能達到最佳。為確保你的 Btrfs 檔案系統正常工作，請考慮檢查 Btrfs 檔案系統上是否有足夠的可用空間。可用空間的理想值為 10%，但你不應讓 Btrfs 檔案系統的可用空間降至 5%。

- 摘要：不要讓 Btrfs 檔案系統被寫滿。
- 建議可用空間：5-10%。

## 示例命令 {#example-command}

```routeros
/disk/btrfs/filesystem/print
```

:::tip

如果你需要更多空間，請考慮將磁碟加入由一個或多個磁碟組成的 Btrfs RAID 陣列。

:::
