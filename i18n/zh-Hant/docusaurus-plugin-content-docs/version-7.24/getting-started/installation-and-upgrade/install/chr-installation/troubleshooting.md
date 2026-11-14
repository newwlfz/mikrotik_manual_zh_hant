---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/troubleshooting"
sidebar_position: 6
title: "CHR：故障排查"
sidebar_label: "CHR：故障排查"
description: "本頁介紹 MikroTik RouterOS CHR 的故障排除，涵蓋 Linux 網橋上的 IGMP snooping 問題、客戶機與外部世界之間與 VLAN 相關的資料流問題、虛擬機器管理程式中的 VLAN 標記要求，以及 VMware 客戶機自動化的限制。"
tags:
  - 'vlan'
  - 'igmp'
  - 'security-settings'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/install/chr-installation/troubleshooting
captured_at: '2026-11-04T11:28:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 在 Linux 上使用網橋 {#using-bridge-on-linux}

如果 Linux 網橋啟用了 IGMP snooping，並且你遇到 IPv6 流量問題，請停用此功能。IGMP snooping 會干擾 MLD 封包（多播），並阻止它們透過網橋。

```
echo -n 0 > /sys/class/net/vmbr0/bridge/multicast_snooping
```

### 來自客戶機的封包無法透過 {#packets-not-passing-from-guests}

**問題：** 在客戶機 CHR 上配置軟體介面（VLAN、EoIP、網橋等）後，路由器停止向外部世界傳遞資料。

**解決方案：** 檢查你的虛擬化管理系統 (VMS) 的安全設定。確認以下內容：

- 允許其他 MAC 地址透過
- 允許帶有 VLAN 標籤的封包透過

根據需要調整安全設定——例如，啟用 MAC 欺騙或允許特定的 MAC 地址範圍。對於 VLAN 介面，通常可以定義允許的 VLAN 標籤或 VLAN 標籤範圍。

### 在各種虛擬機器管理程式中的 CHR 上使用 VLAN {#using-vlans-on-chr-in-various-hypervisors}

CHR 不控制外部 VLAN 標記；它只處理從虛擬網路介面接收到的 VLAN 標籤。
在某些虛擬機器管理程式中，必須先在其管理程式側配置 VLAN 標記，然後才能在 CHR 虛擬機器內使用。

**實用文章：**

- Hyper-V VLAN 配置（Microsoft 官方文件）：
  - https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/configure-virtual-local-area-networks-for-hyper-v

- 使用 PowerShell 配置 Hyper-V VLAN 中繼：
  - https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmnetworkadaptervlan?view=windowsserver2025-ps

## VMware 整合說明 {#vmware-integration-notes}

CHR 不支援 VMware Tools 或任何客戶機代理整合。

客戶機級別的自動化（例如透過 VMware Tools、VIX 或 vSphere API 在 CHR 內執行指令碼）不可用。

僅支援電源管理和資源分配等基本虛擬機器管理程式功能。
