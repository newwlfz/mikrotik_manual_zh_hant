---
sidebar_key: "storage/iscsi"
sidebar_position: 4
title: "iSCSI"
sidebar_label: "iSCSI"
description: "iSCSI 支援基於 IP 的儲存訪問，RouterOS 同時支援 target 和 initiator 模式，並提供 iSCSI 地址、IQN 識別符號以及用於用戶端和伺服器角色的可配置埠等屬性。"
tags:
  - 'iscsi'
  - 'storage'
source: https://manual.mikrotik.com/docs/7.24/storage/iscsi
captured_at: '2026-11-04T11:33:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

iSCSI 允許透過基於 IP 的網路訪問儲存。在發起端上，iSCSI 裝置將顯示為塊裝置。RouterOS 同時支援 target 和 initiator 模式。

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **iscsi-address** | iSCSI target 的 IP 地址。（主機裝置 IP） |
| **iscsi-export** | 在主機裝置上停用/啟用 iSCSI |
| **iscsi-iqn** | 用於命名 iSCSI target 的唯一識別符號。 |
| **iscsi-port** | iSCSI target 用於監聽來自發起端傳入連線的網路埠。iSCSI 流量的預設埠是 3260。 |
| **iscsi-server-iqn** | iSCSI 伺服器使用的唯一識別符號。預設情況下，IQN 的格式為 iqn.2000-02.com.mikrotik:*slot（從 7.21beta2 開始）* |
| **iscsi-server-port** | iSCSI 伺服器使用的網路埠。*（從 7.21beta2 開始）* |

## 配置示例 {#configuration-example}

主機

```ros
/disk
set pcie1-nvme1 iscsi-export=yes
```

用戶端

```ros
/disk
add type=iscsi iscsi-address=192.168.1.1 iscsi-iqn=iqn.2000-02.com.mikrotik:pcie1-nvme1
```
