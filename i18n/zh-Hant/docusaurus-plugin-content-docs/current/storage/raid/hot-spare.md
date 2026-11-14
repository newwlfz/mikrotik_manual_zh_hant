---
sidebar_key: "storage/raid/hot-spare"
sidebar_position: 1
title: "設定熱備盤"
sidebar_label: "設定熱備盤"
description: "本頁介紹如何在 RouterOS 中為 RAID 陣列配置熱備磁碟，透過為 RAID 配置分配備用磁碟，實現磁碟故障時的自動重建。"
tags:
  - 'raid'
  - 'storage'
  - 'backup'
source: https://manual.mikrotik.com/docs/storage/raid/hot-spare
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

可以為 RAID 陣列分配一塊熱備磁碟。如果發生磁碟故障，重建會立即在已分配的備用磁碟上開始。備用磁碟是陣列的成員，並在其上配置了 `raid-role=spare`。

新增具有所需磁碟數量的 RAID 陣列：

```ros
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

然後新增磁碟以及備用磁碟到 RAID。在本例中，我們將新增 `nvme5` 作為備用磁碟：

```ros
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4

/disk/set raid-master=raid5 raid-role=spare nvme5
```
