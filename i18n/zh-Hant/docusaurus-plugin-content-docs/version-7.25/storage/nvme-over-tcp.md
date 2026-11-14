---
sidebar_key: "storage/nvme-over-tcp"
sidebar_position: 6
title: "NVMe over TCP"
sidebar_label: "NVMe over TCP"
description: "NVMe over TCP 支援發起端和目標端訪問網路附加的 NVMe 儲存，並可配置 IP 地址、埠和基於主機的訪問控制。示例展示瞭如何從 RouterOS 用戶端向伺服器掛載磁碟，包括 Linux 用戶端設定步驟。"
tags:
  - 'nvme'
  - 'storage'
  - 'tcp'
source: https://manual.mikrotik.com/docs/7.25/storage/nvme-over-tcp
captured_at: '2026-11-04T11:21:35+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

NVMe over TCP 允許在發起端（用戶端）側透過網路將儲存作為 NVMe 塊裝置訪問。在目標端（主機）側，該裝置可以是 HDD/SSD/NVMe 驅動器，甚至是 RAID 陣列。

NVMe over TCP 伺服器預設監聽 TCP 埠 4420。

## 示例 {#examples}

### 掛載磁碟 {#mount-a-disk}

在此示例中，一臺 RouterOS 裝置用作儲存伺服器（ **Host** ），另一臺 RouterOS 裝置需要透過網路掛載儲存裝置（ **Client** ）。

1. 在 **Host** 上使用以下命令：  

   ```ros
   /disk/set disk1 nvme-tcp-export=yes nvme-tcp-port=4420
   ```

2. 在 **Client** 上使用以下命令：  

   ```ros
   /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 nvme-tcp-name=disk1
   ```

3. 您的 **Client** 現在將看到一個實際上是透過 NVMe over TCP 在網路掛載的磁碟。

#### Linux 用戶端 {#linux-client}

使用以下命令在 Linux **Client** 上設定 NVMe over TCP。

1. 載入核心模組。  

    ```bash
    modprobe nvme_tcp
    ```

2. 發現現有的 NVMe over TCP 掛載。  

   ```bash
   nvme discover -t tcp -a 192.168.1.1 -s 4420
   ```

   ```routeros
   #OUTPUT:
   Discovery Log Number of Records 1, Generation counter 2
   =====Discovery Log Entry 0======
   trtype:  tcp
   adrfam:  ipv4
   subtype: nvme subsystem
   treq:    not specified, sq flow control disable supported
   portid:  4420
   trsvcid: 4420
   subnqn:  disk1
   traddr:  10.155.166.7
   sectype: none
   ```

3. 連線到 NVMe over TCP 掛載。  

   ```bash
   nvme connect -t tcp -a 192.168.1.1 -s 4420 -n disk1
   ```

4. 塊裝置現在應該可用了。  

   ```bash
   ls /dev/nvme*
   ```

    ```bash
    #OUTPUT:
    /dev/nvme0  /dev/nvme0n1  /dev/nvme-fabrics
    ```

5. 現在您可以像使用 Linux **Client** 上的任何其他塊裝置一樣使用已掛載的塊裝置。

如果您想斷開已掛載的塊裝置：

```bash
nvme disconnect -d /dev/nvme0
```

### 將檔案掛載為塊裝置 {#mount-a-file-as-a-block-device}

在此示例中，一臺 RouterOS 裝置用作儲存伺服器（ **Host** ），另一臺 RouterOS 裝置需要透過網路掛載儲存裝置（ **Client** ）。

:::warning

當您不想將整個磁碟分配給 **Client**，而是隻想將磁碟大小的一部分分配給 **Client** 時，這種設定很有用。掛載檔案而非磁碟的效能將低於使用 NVMe over TCP 掛載磁碟（或分割區）的效能。

:::

1. 在 **Host** 上使用以下命令建立一個將用作塊裝置的檔案：  

   ```routeros
   /disk/add type=file file-path=disk1/BIGFILE.img file-size=10G slot=blockdevice1
   /disk/set blockdevice1 nvme-tcp-export=yes 
   ```

2. 在 **Client** 上使用以下命令將檔案掛載為塊裝置：  

   ```routeros
   /disk/nvme-discover 192.168.1.1
   /disk/add nvme-tcp-address=192.168.1.1 nvme-tcp-name=blockdevice1 type=nvme-tcp
   /disk/format blockdevice1 file-system=ext4
   ```

3. 您的 **Client** 現在將看到一個名為 `blockdevice1` 的新磁碟，儘管在 **Server** 上該儲存裝置實際上是一個檔案。

:::tip

如果您想在 Linux **Client** 上掛載塊裝置，請參閱 [Linux 用戶端](#linux-client) 部分。

:::

### 掛載 RAID 陣列 {#mount-a-raid-array}

在此示例中，一臺 RouterOS 裝置用作儲存伺服器（ **Host** ），另一臺 RouterOS 裝置需要透過網路掛載儲存裝置（ **Client** ），同時還提供資料冗餘。

1. 在 **Host** 上設定 [RAID](./raid/index.md)，例如：  

   ```routeros
   /disk/add raid-device-count=8 raid-type=6 slot=RAID6_array type=raid
   /disk/set disk1 raid-master=RAID6_array raid-role=0
   /disk/set disk2 raid-master=RAID6_array raid-role=1
   /disk/set disk3 raid-master=RAID6_array raid-role=2 
   /disk/set disk4 raid-master=RAID6_array raid-role=3
   /disk/set disk5 raid-master=RAID6_array raid-role=4
   /disk/set disk6 raid-master=RAID6_array raid-role=5
   /disk/set disk7 raid-master=RAID6_array raid-role=6 
   /disk/set disk8 raid-master=RAID6_array raid-role=7
   /disk/set RAID6_array nvme-tcp-export=yes
   ```

2. 在 **Client** 上使用以下命令：

    ```ros
    /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 nvme-tcp-name=RAID6_array
    ```

3. 您的 **Client** 現在將看到一個磁碟，但它實際上是一個高度冗餘的 RAID 陣列。

:::tip

如果您想在 Linux **Client** 上掛載塊裝置，請參閱 [Linux 用戶端](#linux-client) 部分。

:::

:::danger

不要將來自不同 RouterOS 裝置的多個磁碟掛載到 Linux 用戶端上並將它們組成軟體 RAID 配置（例如 mdadm）。雖然這種配置確實提供了一定的冗餘，但您可能會遇到異常的延遲問題甚至超時。建議在 RouterOS 上建立 RAID 陣列，並將該 RAID 陣列作為塊裝置匯出到您的 Linux 用戶端。

:::
