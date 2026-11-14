---
sidebar_key: "firewall-and-quality-of-service/queues/pcq-example"
sidebar_position: 2
title: "PCQ 示例"
sidebar_label: "PCQ 示例"
description: "Per Connection Queue (PCQ) 是 RouterOS 的一種佇列方法，用於在使用者之間均衡頻寬，並提供了使用 Queue Tree 和 Simple Queues 設定下載/上傳限制的示例。"
tags:
  - 'pcq'
  - 'queue-tree'
  - 'simple-queues'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/pcq-example
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

每連線佇列（PCQ）只需一個佇列，就能為網路上的每臺裝置提供各自的速度限制，而不是為每臺裝置各用一個佇列。PCQ 使用其分類器將流量劃分為子流，例如為每個目標地址劃分一個子流，並將每個子流限制為 `pcq-rate`。

## 限制 LAN 上的每臺裝置 {#limit-every-device-on-a-lan}

此示例將 LAN 192.168.88.0/24 上的每臺裝置限制為 10 Mbit/s 下載和 5 Mbit/s 上傳。

### 步驟 1：在 Queue Types 中新增 PCQ {#step-1-add-pcq-in-queue-types}

為下載和上傳各新增一個佇列型別。`pcq-classifier=dst-address` 為下載流量中的每臺裝置提供各自的子流，`src-address` 則為上傳流量提供各自的子流。`pcq-rate` 是每個子流（也就是每臺裝置）的限制，單位為位元每秒；`k` 和 `M` 字尾可用：

```ros
/queue/type/add name="PCQ_download" kind=pcq pcq-rate=10M pcq-classifier=dst-address
/queue/type/add name="PCQ_upload" kind=pcq pcq-rate=5M pcq-classifier=src-address
```

`pcq-limit` 不是速度：它是每個子流的佇列大小，單位為 KiB（預設 `50KiB`）。

### 步驟 2：部署 PCQ {#step-2-deploy-the-pcq}

#### Simple Queues 選項 {#simple-queues-option}

為整個 LAN 使用一個簡單佇列即可應用這兩種型別。`queue` 先採用上傳型別，再採用下載型別：

```ros
/queue/simple/add target=192.168.88.0/24 queue=PCQ_upload/PCQ_download
```

`/queue/simple/print stats` 會在 `pcq-queues` 中顯示該佇列有多少個子流（此處為裝置）。

#### Queue Tree 選項 {#queue-tree-option}

使用 packet-marks upload/download 標記所有封包（在此示例中，ether1-WAN 是連線到網際網路的公共介面，ether2-LAN 是用戶端所連線的本地介面）：

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether2-LAN new-packet-mark=client_upload
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether1-WAN new-packet-mark=client_download
```

然後，新增兩個佇列，一個用於下載，一個用於上傳：

```ros
/queue/tree/add parent=global queue=PCQ_download packet-mark=client_download
/queue/tree/add parent=global queue=PCQ_upload packet-mark=client_upload
```

:::warning
佇列不適用於 FastTracked 流量，並且預設配置會對已建立的連線進行 FastTrack。請確保防火牆不會對您想要限制的流量進行 FastTrack，例如在 `/ip/firewall/filter` 中停用 FastTrack 規則。
:::
