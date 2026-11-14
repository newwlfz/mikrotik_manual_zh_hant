---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/esxi"
sidebar_position: 2
title: "CHR：VMware ESXi 安裝"
sidebar_label: "CHR：VMware ESXi 安裝"
description: "本頁介紹在 VMware ESXi 上安裝與配置 MikroTik CHR 的方法，涵蓋受支援的網路介面（vmxnet3、E1000）與磁碟控制器（IDE、VMware Paravirtual SCSI），並說明如何透過調整 MTU 設定和重新配置介面來啟用巨型幀。"
tags:
  - 'vmware-esxi'
  - 'mtu'
  - 'jumbo-frames'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/install/chr-installation/esxi
captured_at: '2026-11-04T11:28:33+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 支援的網路和磁碟介面 {#supported-network-and-disk-interfaces}

### VMware ESXi {#vmware-esxi}

**網路介面卡：**

- vmxnet3
- E1000

**磁碟控制器：**

- IDE
- VMware Paravirtual SCSI
- LSI Logic SAS
- LSI Logic Parallel

#### ESXi {#esxi}

在將用於該 VM 的埠組或虛擬交換器上啟用混雜模式。

**ESXi 文件：**

- https://kb.vmware.com/kb/1004099

### 在 VMware ESXi 上執行 {#running-on-vmware-esxi}

#### 更改 MTU {#changing-mtu}

VMware ESXi 支援最高 9000 位元組的 MTU 值。要利用巨型幀，請調整 ESXi 安裝以允許更高的 MTU。

**重要：** 在 MTU 更改**之後**新增的虛擬乙太網介面將正確支援巨型幀。但是，在 MTU 更改**之前**新增的介面將限制為原始 MTU 值。如果你在更改 MTU 之前配置了介面，則必須將它們從虛擬客戶機中移除並重新新增。

**示例：** 新增到 ESXi 客戶機的兩個介面會根據新增時間顯示不同的 MTU 值：

```
[admin@chr-vm] > interface ethernet print 
Flags: X - disabled, R - running, S - slave 
 #    NAME           MTU MAC-ADDRESS       ARP       
 0 R  ether1        9000 00:0C:29:35:37:5C enabled   
 1 R  ether2        1500 00:0C:29:35:37:66 enabled
```
