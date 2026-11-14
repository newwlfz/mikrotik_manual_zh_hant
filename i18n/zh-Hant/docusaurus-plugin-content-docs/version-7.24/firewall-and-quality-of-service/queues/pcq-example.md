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
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/queues/pcq-example
captured_at: '2026-11-04T11:28:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

PCQ（Per Connection Queue，每連線佇列）是一種排隊規則，可以在少量管理開銷下為多個使用者動態均衡或整形流量。PCQ 場景可以分為三大類：為若干使用者提供相同頻寬、在使用者之間平均分配特定頻寬，以及在使用者之間平均分配未知頻寬。

## 為若干使用者提供相同頻寬 {#equal-bandwidth-for-a-number-of-users}

可以透過 Queue Tree 和 Simple Queues 使用 PCQ 型別，為若干使用者均衡頻寬[並設定最大限制]。我們將設定 64kbps 下載和 32kbps 上傳限制。

![](/img/13361e704ba849c3.webp)

### 步驟 1：在 Queue Types 中新增 PCQ {#step-1-add-pcq-in-queue-types}

新增兩個新條目——一個用於下載，一個用於上傳。`dst-address` 是使用者下載流量的分類器，`src-address` 用於上傳流量：

```ros
/queue/type/add name="PCQ_download" kind=pcq pcq-rate=64000 pcq-classifier=dst-address
/queue/type/add name="PCQ_upload" kind=pcq pcq-rate=32000 pcq-classifier=src-address
 
```

### 步驟 2：部署 PCQ {#step-2-deploy-the-pcq}

#### Queue Tree 選項 {#queue-tree-option}

使用 packet-marks 標記所有封包的上傳/下載：（假設 ether1-WAN 是連線 Internet 的公共介面，ether2-LAN 是用戶端連線的本地介面）：

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether2-LAN new-packet-mark=client_upload
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether1-WAN new-packet-mark=client_download
```

然後，需要兩條佇列規則，一條用於下載，一條用於上傳：

```ros
/queue/tree/add parent=global queue=PCQ_download packet-mark=client_download
/queue/tree/add parent=global queue=PCQ_upload packet-mark=client_upload
```

#### Simple Queues 選項 {#simple-queues-option}

或者，你也可以用一條命令完成：

```ros
/queue/simple/add target=192.168.0.0/24 queue=PCQ_upload/PCQ_download
```
