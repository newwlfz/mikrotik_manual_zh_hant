---
sidebar_key: "storage/iscsi"
sidebar_position: 4
title: "iSCSI"
sidebar_label: "iSCSI"
description: "iSCSI 支援基於 IP 的儲存訪問，RouterOS 同時支援 target 和 initiator 模式，並提供 `iscsi-address`、IQN 識別符號以及用戶端和伺服器角色可配置埠等屬性。"
tags:
  - 'iscsi'
  - 'storage'
source: https://manual.mikrotik.com/docs/storage/iscsi
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

iSCSI 允許透過基於 IP 的網路訪問儲存。在發起端（用戶端）上，iSCSI 裝置會顯示為本地塊裝置。RouterOS 同時支援目標端和發起端模式：目標端匯出磁碟或檔案（在主機裝置上設定 `iscsi-export=yes`），發起端則透過網路將遠端目標掛載為新裝置。

iSCSI 伺服器預設監聽 TCP 埠 3260。伺服器預設呈現的 IQN 識別符號格式為 `iqn.2000-02.com.mikrotik:<slot>`。

## 配置示例 {#configuration-example}

主機：使用以下命令匯出磁碟：

```ros
/disk set pcie1-nvme1 iscsi-export=yes
```

用戶端：新增一個 `type=iscsi` 的裝置，並將其指向伺服器地址和 IQN：

```ros
/disk add type=iscsi iscsi-address=192.168.1.1 iscsi-iqn=iqn.2000-02.com.mikrotik:pcie1-nvme1
```

隨後，掛載的裝置會在 `/disk/print` 中顯示為普通塊裝置，並可在本地進行格式化和使用。
