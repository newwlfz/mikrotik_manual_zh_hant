---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/proxmox"
sidebar_position: 5
title: "CHR：Proxmox VE 安裝"
sidebar_label: "CHR：Proxmox VE 安裝"
description: "本頁提供了在 Proxmox VE 虛擬環境中部署 MikroTik Cloud Hosted Router (CHR) 的概述和詳細安裝步驟，涵蓋虛擬機器建立、映象處理和配置方法。"
tags:
  - 'proxmox'
  - 'chr'
  - 'kvm'
source: https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/proxmox
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

Cloud Hosted Router（CHR）是專為在 x86_64 虛擬化環境中執行而設計的 MikroTik RouterOS 版本。它提供完整的路由、防火牆、VPN 和管理功能，適用於本地和基於雲的虛擬基礎設施，例如 Proxmox VE。

Proxmox VE（KVM/QEMU）允許使用 raw 或 qcow2 磁碟映象靈活部署 CHR，並提供多種儲存後端和網路介面卡選項。

## 安裝步驟 {#installation-steps}

### 步驟 1：建立虛擬機器 {#step-1-create-a-virtual-machine}

- 在 Proxmox VE 中使用 Web 介面建立新 VM。
- 根據需要分配 CPU、記憶體和網路介面。
- 不要安裝作業系統（CHR 磁碟將手動掛載）。

### 步驟 2：下載並解壓 CHR 映象 {#step-2-download-and-extract-chr-image}

從 MikroTik 下載頁面 https://mikrotik.com/download 下載最新 CHR 映象到 Proxmox 主機：

```bash
wget https://download.mikrotik.com/routeros/7.21.4/chr-7.21.4.img.zip
```

:::warning
請將 URL 替換為 MikroTik [下載頁面](https://mikrotik.com/download) 上可用的最新 CHR 版本。
:::

解壓映象：

```bash
unzip chr-7.21.4.img.zip
```

這將生成一個用於安裝的 `.img` 檔案。

### 步驟 3：將映象移動到 VM 儲存 {#step-3-move-the-image-to-vm-storage}

Proxmox 預設本地儲存位置：

```bash
/var/lib/vz/images/<VM_ID>/
```

如有需要，建立目錄：

```bash
mkdir -p /var/lib/vz/images/<VM_ID>
```

移動映象：

```bash
mv chr-7.21.4.img /var/lib/vz/images/<VM_ID>/
```

### 步驟 4：將映象轉換為 QCOW2 {#step-4-convert-image-to-qcow2}

將 raw CHR 映象轉換為 qcow2 格式：

```bash
qemu-img convert -f raw -O qcow2 /var/lib/vz/images/<VM_ID>/chr-7.21.4.img /var/lib/vz/images/<VM_ID>/vm-<VM_ID>-disk-1.qcow2
```

### 步驟 5：將磁碟掛載到 VM {#step-5-attach-disk-to-vm}

VM 配置檔案位置：

```bash
/etc/pve/qemu-server/<VM_ID>.conf
```

透過 VM 配置檔案或 Proxmox Web 介面手動掛載磁碟。

:::tip
請先使用測試 VM 驗證配置語法是否正確。
:::

## 基於 GUI 的替代方法 {#alternative-gui-based-method}

1. 透過 Proxmox Web 介面建立基礎 VM。
2. 確保儲存設定為本地儲存。
3. 將 CHR 映象上傳到：`/var/lib/vz/images/<VM_ID>/`
4. 將映象轉換為 qcow2：

```bash
qemu-img convert -f raw -O qcow2 chr.img vm-<VM_ID>-disk-1.qcow2
```

1. 透過 Proxmox GUI 或 `.conf` 檔案掛載磁碟。

## 自動化安裝指令碼 {#automated-installation-script}

也可以在 Proxmox 主機上使用 Bash 指令碼部署 CHR。

**指令碼執行的操作：**

- 建立臨時目錄（/root/temp）。
- 下載 CHR 映象。
- 解壓並轉換該映象。
- 建立 VM 並掛載磁碟。

```bash
#!/bin/bash

version="nil"
vmID="nil"

echo "############## Start of Script ##############"

if [ ! -d /root/temp ]; then
    mkdir /root/temp
fi

read -p "Enter CHR version (e.g. 7.21.4): " version

cd /root/temp

wget https://download.mikrotik.com/routeros/$version/chr-$version.img.zip
unzip chr-$version.img.zip

read -p "Enter VM ID: " vmID

mkdir -p /var/lib/vz/images/$vmID

qemu-img convert -f raw -O qcow2 \
chr-$version.img \
/var/lib/vz/images/$vmID/vm-$vmID-disk-1.qcow2

qm create $vmID \
  --name chr-$version \
  --net0 virtio,bridge=vmbr0 \
  --bootdisk virtio0 \
  --ostype l26 \
  --memory 512 \
  --sockets 1 \
  --cores 1 \
  --virtio0 local:$vmID/vm-$vmID-disk-1.qcow2

echo "############## End of Script ##############"
```

### 實用提示 {#utility-tip}

修復指令碼中的 Windows 行尾符：

```bash
sed -i -e 's/\r$//' *.sh
```

## 支援的網路和磁碟介面 {#supported-network-and-disk-interfaces}

### Proxmox VE (KVM/QEMU) {#proxmox-ve-kvmqemu}

**網路介面卡：**

- Virtio（半虛擬化）
- E1000

**磁碟控制器：**

- IDE
- SATA
- Virtio（半虛擬化）
