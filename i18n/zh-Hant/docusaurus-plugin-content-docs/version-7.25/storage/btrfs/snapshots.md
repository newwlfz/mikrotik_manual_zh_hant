---
sidebar_key: "storage/btrfs/snapshots"
sidebar_position: 3
title: "Btrfs 子卷與快照"
sidebar_label: "Btrfs 子卷與快照"
description: "本頁指導使用者在 RouterOS 中建立 Btrfs 子卷和快照，說明如何組織資料、格式化磁碟、設定諸如 Documents 和 Photos 之類的子卷，以及如何建立快照，從而在不重複資料的情況下實現高效備份。"
tags:
  - 'storage'
  - 'btrfs'
  - 'snapshots'
source: https://manual.mikrotik.com/docs/7.25/storage/btrfs/snapshots
captured_at: '2026-11-04T11:21:35+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](../index.md) 軟體包。
:::

## 建立子卷 {#creating-subvolumes}

建立子卷的主要好處是組織 Btrfs 主（根）子捲上的資料。可以將子卷視為具有分割區功能的資料夾，同時所有子卷之間仍然共享總磁碟空間。之後您可以將這些子卷用於更高階的任務，建議在擁有大量不同型別資料時建立子卷，尤其是需要頻繁備份的資料。請按照指南設定幾個示例子卷：

:::tip
子卷與快照配合使用時最為有用。請務必也檢視快照功能。

:::

1. 找到要用作 Btrfs 磁碟的磁碟名稱：  

   ```routeros
   /disk/print
   ```

   :::warning
   在此示例中，使用的磁碟將被稱為 `<disk-name-1>`，請確保將佔位符替換為實際的磁碟名稱！
   :::
2. 將磁碟格式化為 Btrfs，在此示例中為 `<disk-name-1>`：  

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

3. 為方便起見，為 Btrfs 磁碟新增標籤（格式化後預設會自動標記為 `<disk-name-1>-fs`）：  

   ```routeros
   /disk/btrfs/filesystem/set [find where devs=<disk-name-1>] label=BtrfsDisk
   ```

4. 為簡化操作，您也可以更改 Btrfs 磁碟掛載點：  

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsDisk
   ```

5. 在 `BtrfsDisk` 上建立一個名為 `Documents` 的新子卷：  

   ```routeros
   /disk/btrfs/subvolume/add name=Documents fs=BtrfsDisk
   ```

   :::info
   子卷也是快照。您可能會在各種選單中遇到這兩個名稱。簡單來說，快照是在特定時間建立的子卷，包含該時間點的資料。
   :::
6. 在 `BtrfsDisk` 上建立另一個名為 `Photos` 的子卷：  

   ```routeros
   /disk/btrfs/subvolume/add name=Photos fs=BtrfsDisk
   ```

7. 您可以檢視當前可用的子卷：  

   ```routeros
   /disk/btrfs/subvolume/print
   ```

8. 現在您可以透過 `/BtrfsDisk/Documents` 和 `/BtrfsDisk/Photos` 訪問這些子卷。

## 建立快照 {#creating-snapshots}

快照是一種節省空間的備份資料方式。透過建立快照，您可以儲存資料的當前狀態，之後可以訪問該狀態。

:::warning

快照不會建立資料的副本，它們儲存資料的當前狀態，同時允許您對當前資料進行更改。快照包含如何將當前資料恢復到建立快照時所呈現狀態的資訊。快照不會像完整備份那樣建立資料的多個副本。

:::

:::note

雖然您可以建立根子卷的快照，但建議為資料建立新的子卷，然後使用快照功能。這只是在管理大量快照時的一種偏好。

:::

1. 建立子卷（或使用根子卷，見上文）並將資料放入這些子卷中，例如：  

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos 
    3 BtrfsDisk/Documents/document1.txt
    4 BtrfsDisk/Photos/photo1.jpg
   ```

2. 在此示例中，我們建立了 `/BtrfsDisk/Documents` 和 `/BtrfsDisk/Photos/` 子卷，您可以透過以下命令檢視它們：  

   ```routeros
   /disk/btrfs/subvolume/print
   ```

3. 為了使快照更有條理，建立一個名為 `Snapshots` 的新子卷：  

   ```routeros
   /disk/btrfs/subvolume/add name=Snapshots fs=BtrfsDisk
   ```

4. 為 `Documents` 和 `Photos` 建立快照：  

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-22012025
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-22012025
   ```

5. 現在您應該擁有新的只讀子卷，其中包含您的檔案：  

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME      
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Photos/photo1.jpg
    6 BtrfsDisk/Snapshots/Documents-22012025
    7 BtrfsDisk/Snapshots/Photos-22012025
    8 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
    9 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   ```

6. 出於測試目的，您可以向子卷新增更多資料，您應該會注意到新新增的檔案不會出現在快照中，而只會出現在子卷中：  

   ```routeros
   [admin@infra1.mikrotikls.lv] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Documents/document2.txt
    6 BtrfsDisk/Photos/photo1.jpg
    7 BtrfsDisk/Photos/photo2.jpg 
    8 BtrfsDisk/Snapshots/Photos-22012025
    9 BtrfsDisk/Snapshots/Documents-22012025
   10 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
   11 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   ```

7. 現在您可以建立新的快照：  

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-23012025 
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-23012025 
   ```

8. 建立新快照後，每個子卷將擁有 2 個快照。一個包含較舊的檔案，另一個包含較舊和較新的檔案：  

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Documents/document2.txt
    6 BtrfsDisk/Photos/photo1.jpg
    7 BtrfsDisk/Photos/photo2.jpg
    8 BtrfsDisk/Snapshots/Photos-22012025
    9 BtrfsDisk/Snapshots/Documents-22012025
   10 BtrfsDisk/Snapshots/Documents-23012025
   11 BtrfsDisk/Snapshots/Photos-23012025
   12 BtrfsDisk/Snapshots/Documents-22012025/document1.txt 
   13 BtrfsDisk/Snapshots/Documents-23012025/document1.txt
   14 BtrfsDisk/Snapshots/Documents-23012025/document2.txt
   15 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   16 BtrfsDisk/Snapshots/Photos-23012025/photo1.jpg
   17 BtrfsDisk/Snapshots/Photos-23012025/photo2.jpg
   ```

   :::note

   多個快照不會為每個檔案建立多個副本，但如果某個檔案已被刪除且仍存在於快照中，那麼該已刪除檔案將佔用空間。如果某個檔案存在於多個快照中，那麼它只會佔用 1 個檔案的空間。

   :::
9. 如果您不再需要較舊的快照，可以將其刪除：  

   ```routeros
   /disk/btrfs/subvolume/remove [find where name=Documents-22012025]
   /disk/btrfs/subvolume/remove [find where name=Photos-22012025]
   ```

## 傳輸快照 {#transfer-your-snapshots}

Btrfs 允許您在兩臺使用 Btrfs 的裝置之間輕鬆傳送快照，雙方都使用 [`/disk/btrfs/transfer`](../../cli-reference/disk/btrfs/transfer.md)：傳送方使用 `send` 條目，接收方使用 `receive` 條目。在此示例中，我們將使用兩臺執行 Storage 軟體包的 RouterOS 裝置。包含需要備份的快照的 RouterOS 裝置將被稱為 `RouterA`，將接收備份的 RouterOS 裝置將被稱為 `RouterB`。

:::info

本指南僅展示如何在 RouterOS 裝置之間使用 Btrfs 傳輸的示例，但您也可以在 RouterOS 和 Linux 裝置之間傳輸快照。如果您需要此類功能，請務必查閱您的 Linux 發行版文件，瞭解如何在其上使用 Btrfs 傳輸。

:::

:::tip
本指南將使用同一臺 RouterOS 裝置上的 SSH 主機金鑰作為 SSH 使用者金鑰。如果你希望為 SSH 使用者使用自己的金鑰，那麼可以在 Linux 計算機上使用以下命令，稍後在 `/user/ssh-keys` 下匯入金鑰對：

```routeros
openssl genpkey -outform PEM -out btrfstransfer_key.pem -algorithm ED25519
openssl pkey -in btrfstransfer_key.pem -pubout -out btrfstransfer_key_pub.pem
```
:::

1. 可選：提高 SSH 伺服器的安全級別，在 `RouterA` 和 `RouterB` 上執行以下命令：  

   ```routeros
   /ip/ssh/set host-key-type=ed25519 strong-crypto=yes
   /ip/ssh/regenerate-host-key
   ```

   :::warning

   重新生成主機金鑰後，下次您嘗試使用 SSH 連線到 RouterOS 裝置時將出現錯誤訊息。您需要調整 SSH 用戶端的配置（通常在 `~/.ssh/known_hosts` 中）以信任新的主機金鑰。

   :::
2. 在 `RouterA` 上匯出 SSH 私鑰和公鑰：  

   ```routeros
   /ip/ssh/export-host-key key-file-prefix=admin
   ```

3. 在 `RouterA` 上為使用者 `admin` 匯入 SSH 私鑰：  

   ```routeros
   /user/ssh-keys/private/import private-key-file=admin_ed25519.pem user=admin
   ```

4. 將 SSH 公鑰從 `RouterA` 上傳到 `RouterB`：  

   ```routeros
   /file/sync/add local-path=admin_ed25519_pub.pem remote-address=RouterB user=admin mode=upload
   /file/sync/remove [find where local-path=admin_ed25519_pub.pem]
   ```

5. 在 `RouterB` 上建立一個新使用者，例如 `btrfstransfer`，併為其設定安全密碼：  

   ```routeros
   /user/add name=btrfstransfer group=write
   ```

   :::warning

   雖然密碼不會用於 Btrfs 傳輸功能，但您仍然需要使用安全密碼以防止未經授權訪問您的裝置。

   :::
6. 在 `RouterB` 上匯入上傳的 SSH 公鑰並將其設定為使用者 `btrfstransfer` 的金鑰：  

   ```routeros
   /user/ssh-keys/import public-key-file=admin_ed25519_pub.pem user=btrfstransfer
   ```

7. 在 `RouterA` 上設定型別 `send`：  

   ```routeros
   /disk/btrfs/transfer/add type=send fs=BtrfsDisk ssh-address=RouterB send-subvolumes=Documents-23012025 ssh-user=btrfstransfer ssh-receive-mount=BackupBtrfsDisk/Snapshots
   ```

   其中：  
   - `BtrfsDisk` 是在 `RouterA` 上透過 `/disk/btrfs/filesystem/print` 找到的 Btrfs 磁碟標籤。
   - `Documents-23012025` 是快照名稱（不是路徑）。
    - `btrfstransfer` 是 `RouterB` 上的 SSH 使用者。
   - `BackupBtrfsDisk` 是在 `RouterB` 上透過 `/disk/btrfs/filesystem/print` 找到的 Btrfs 磁碟標籤。
   - `Snapshots` 是 `BackupBtrfsDisk` 下用於存放快照的子卷。
8. 在 `RouterB` 上設定型別 `receive`：  

   ```routeros
   /disk/btrfs/transfer/add fs=BackupBtrfsDisk type=receive file=BackupBtrfsDisk/Snapshots
   ```

   其中：  
   - `BackupBtrfsDisk` 是在 `RouterB` 上透過 `/disk/btrfs/filesystem/print` 找到的 Btrfs 磁碟標籤
   - `BackupBtrfsDisk/Snapshots` 是 `Snapshots` 子卷的掛載路徑。
