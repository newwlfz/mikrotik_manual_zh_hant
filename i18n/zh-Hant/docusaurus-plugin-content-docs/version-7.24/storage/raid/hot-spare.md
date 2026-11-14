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
source: https://manual.mikrotik.com/docs/7.24/storage/raid/hot-spare
captured_at: '2026-11-04T11:33:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

可以為 RAID 陣列分配一塊熱備磁碟。如果發生磁碟故障，重建會立即在已分配的備用磁碟上開始。

新增具有所需磁碟數量的 RAID 陣列：

```ros
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

隨後，將磁碟以及備用磁碟新增到 RAID 中。在本例中，我們將把 NVMe5 新增為備用磁碟。

```ros
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4

/disk/set raid-master=raid5 raid-role=spare nvme5
```
