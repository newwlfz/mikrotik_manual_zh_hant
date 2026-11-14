---
sidebar_key: "storage/raid/moving-array"
sidebar_position: 2
title: "將 RAID 陣列遷移到其他裝置"
sidebar_label: "將 RAID 陣列遷移到其他裝置"
description: "本頁說明如何將 RAID 5 陣列從舊裝置遷移到新裝置：先在新裝置上建立 RAID，再從舊裝置中彈出磁碟，並將其轉移到新裝置，RouterOS 會在新裝置上自動識別並掛載該陣列。"
source: https://manual.mikrotik.com/docs/7.25/storage/raid/moving-array
captured_at: '2026-11-04T11:21:40+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

可以將 RAID 陣列從一臺裝置遷移到另一臺裝置。

在本示例中，我們使用的是 RDS2216 上的 RAID 5 陣列，由 4 個成員組成。

首先，在“新”裝置上建立一個成員數量相同的 RAID 陣列，並分配成員槽位：

```ros
# 新设备
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

```ros
# 新设备 - 为（当前为空的）插槽分配角色
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4
```

在“舊”裝置上，彈出要遷移到“新”裝置的磁碟：

```ros
# 旧设备
/disk/eject nvme1
/disk/eject nvme2
/disk/eject nvme3
/disk/eject nvme4
```

從“舊”裝置上取下磁碟，並將它們插入“新”裝置中已分配的槽位。RouterOS 會自動檢測 RAID 超級塊並掛載該陣列，無需任何額外操作。
